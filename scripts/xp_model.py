#!/usr/bin/env python3
"""xP model v0 — transparent expected points per player per gameweek, from the FPL API only.

Usage:
    python scripts/xp_model.py                       # latest snapshot, next 5 GWs
    python scripts/xp_model.py --horizon 6 --snapshot data/snapshots/fpl_2026-10-06T163833Z.json

Writes data/xp/xp_gw{first}-{last}.csv with one row per player: price, position, team,
minutes tag, p_start, xMins, per-GW xP, horizon total (decayed) and FPL's own ep_next as the
baseline we grade ourselves against.

Why every number comes from where it comes from (plain language, so Erik can argue with it):

  Team strength. For each team, attack = how many goals it creates per game, defence = how many
  it concedes per game. We blend three readings: actual goals (noisy after 5 games), expected
  goals from the API (sum of the players' xG; the keeper's expected_goals_conceded as the team
  xGC), and FPL's own strength ratings as a prior that stops five matches from deciding everything.
  A fixture's expected goals = attacker's attack x defender's defence / league average, times a
  home factor. From that: P(clean sheet) = exp(-lambda), and the expected "goals conceded" penalty.

  Player minutes. p_start = starts / games played, adjusted by the FPL availability flag
  (chance_of_playing_next_round) and status. Minutes when starting = minutes / starts.
  A player below 'likely' is flagged, and the solver never picks 'doubt' or 'out'.

  Player points per fixture = appearance + goals + assists + clean sheet - goals conceded
  + saves + DefCon + bonus - cards. Goals and assists use the player's season xG/xA per 90,
  scaled by his expected minutes and by how good the fixture is for his team (fixture expected
  goals / team's season average). DefCon uses defensive_contribution per 90 as a Poisson rate
  against the position threshold (10 for defenders, 12 for others). Bonus is his season bonus
  per start. Nothing is estimated from memory; everything is a field in the snapshot.

  Horizon total = sum over the next N gameweeks with a decay (0.84 per week, the FPL Review /
  sertalpbilal convention) so this week matters more than week five.

Known limits (v0): no opponent-specific adjustment for individual players, no penalty-taker
bonus beyond what xG already contains, no injury-return modelling, bonus not fixture-adjusted,
double gameweeks summed naively, 5 matches of evidence. Compare against ep_next every week;
the review grades which one was closer.
"""
from __future__ import annotations

import argparse
import csv
import glob
import json
import math
import os
from collections import defaultdict

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
POS = {1: "GK", 2: "DEF", 3: "MID", 4: "FWD"}
GOAL_PTS = {1: 10, 2: 6, 3: 5, 4: 4}
CS_PTS = {1: 4, 2: 4, 3: 1, 4: 0}
DEFCON_THRESHOLD = {1: 10, 2: 10, 3: 12, 4: 12}
DECAY = 0.84
HOME_FACTOR = 1.12  # ~home teams score 12% more; league-wide constant, fitted roughly


def latest_snapshot() -> str:
    files = sorted(glob.glob(os.path.join(ROOT, "data", "snapshots", "fpl_*.json")))
    if not files:
        raise SystemExit("no snapshots in data/snapshots")
    return files[-1]


def poisson_cdf(k: int, lam: float) -> float:
    return sum(math.exp(-lam) * lam**i / math.factorial(i) for i in range(k + 1))


def expected_conceded_penalty(lam: float) -> float:
    """E[floor(goals/2)] for Poisson goals — the -1 per 2 conceded rule, in expectation."""
    e, p_acc = 0.0, 0.0
    for g in range(0, 12):
        p = math.exp(-lam) * lam**g / math.factorial(g)
        e += p * (g // 2)
        p_acc += p
    return e


def team_strengths(bootstrap: dict, fixtures: list) -> dict:
    """Blend actual goals, API xG/xGC and FPL strength ratings into attack/defence per team."""
    teams = {t["id"]: t for t in bootstrap["teams"]}
    gf, ga, played = defaultdict(float), defaultdict(float), defaultdict(int)
    for f in fixtures:
        if not f["finished"]:
            continue
        h, a = f["team_h"], f["team_a"]
        gf[h] += f["team_h_score"]; ga[h] += f["team_a_score"]; played[h] += 1
        gf[a] += f["team_a_score"]; ga[a] += f["team_h_score"]; played[a] += 1
    # API xG: team xG = sum of players' expected_goals; team xGC = first-choice keeper's xGC
    xg, xgc = defaultdict(float), {}
    for e in bootstrap["elements"]:
        xg[e["team"]] += float(e["expected_goals"])
        if e["element_type"] == 1:
            prev = xgc.get(e["team"], (0, 0.0))
            if e["minutes"] > prev[0]:
                xgc[e["team"]] = (e["minutes"], float(e["expected_goals_conceded"]))
    n_teams = len(teams)
    league_gpg = sum(gf.values()) / max(1, sum(played.values()))  # goals per team per game
    # FPL strength ratings as prior (scale ~1000-1400): normalise to multiplicative factors
    att_prior = {t: ((teams[t]["strength_attack_home"] or 0) + (teams[t]["strength_attack_away"] or 0)) / 2 for t in teams}
    def_prior = {t: ((teams[t]["strength_defence_home"] or 0) + (teams[t]["strength_defence_away"] or 0)) / 2 for t in teams}
    att_mean = sum(att_prior.values()) / n_teams
    def_mean = sum(def_prior.values()) / n_teams
    if att_mean == 0 or def_mean == 0:
        # FPL has not published strength ratings this season: prior = league average for everyone
        att_prior = {t: 1.0 for t in teams}; def_prior = {t: 1.0 for t in teams}
        att_mean = def_mean = 1.0
    out = {}
    for t in teams:
        p = max(1, played[t])
        actual_att = gf[t] / p / league_gpg
        actual_def = ga[t] / p / league_gpg
        x_att = xg[t] / p / league_gpg if xg[t] else actual_att
        x_def = xgc[t][1] / p / league_gpg if t in xgc else actual_def
        prior_att = att_prior[t] / att_mean
        prior_def = def_mean / def_prior[t]  # higher defence rating -> concede less
        # weights: evidence grows with games played; at 5 games the prior still carries a third
        w_ev = min(0.67, p / 7.5)
        att = w_ev * (0.5 * actual_att + 0.5 * x_att) + (1 - w_ev) * prior_att
        dfc = w_ev * (0.5 * actual_def + 0.5 * x_def) + (1 - w_ev) * prior_def
        out[t] = {"att": att, "def": dfc, "played": p, "gf": gf[t], "ga": ga[t]}
    return out, league_gpg


def fixture_lambdas(fixtures: list, strengths: dict, league_gpg: float, gws: list[int]) -> dict:
    """Per team per GW: list of (opponent, venue, lambda_for, lambda_against)."""
    per_team = defaultdict(lambda: defaultdict(list))
    for f in fixtures:
        if f["event"] not in gws:
            continue
        h, a = f["team_h"], f["team_a"]
        lam_h = strengths[h]["att"] * strengths[a]["def"] * league_gpg * HOME_FACTOR
        lam_a = strengths[a]["att"] * strengths[h]["def"] * league_gpg / HOME_FACTOR
        per_team[h][f["event"]].append((a, "H", lam_h, lam_a))
        per_team[a][f["event"]].append((h, "A", lam_a, lam_h))
    return per_team


def minutes_model(e: dict, games_played: int) -> tuple[float, float, str]:
    """Return (p_play, expected minutes if he plays, tag)."""
    status = e["status"]
    if status in ("i", "s", "u", "n") or e.get("removed"):
        return 0.0, 0.0, "out", 0.0
    starts = e["starts"]
    gp = max(1, games_played)
    p_start = min(1.0, starts / gp)
    mins_per_start = e["minutes"] / starts if starts else 0.0
    # sub appearances: minutes that did not come from starts, ~15 min per sub appearance
    p_sub = 0.0
    if e["minutes"] > 0 and starts < gp:
        sub_minutes = max(0.0, e["minutes"] - starts * mins_per_start)
        p_sub = min(1.0 - p_start, 0.5, sub_minutes / (gp * 15.0))
    chance = e.get("chance_of_playing_next_round")
    if chance is not None:
        p_start *= chance / 100.0
        p_sub *= chance / 100.0
    if chance is not None and chance <= 25:
        tag = "out"
    elif chance is not None and chance <= 50:
        tag = "doubt"
    elif p_start >= 0.8 and (chance is None or chance >= 75):
        tag = "nailed" if (chance is None or chance == 100) else "likely"
    elif p_start >= 0.6:
        tag = "likely"
    elif p_start >= 0.4:
        tag = "50-50"
    else:
        tag = "doubt" if p_start > 0 or p_sub > 0 else "out"
    p_play = min(1.0, p_start + p_sub)
    xmins = p_start * mins_per_start + p_sub * 20
    return p_play, xmins, tag, p_start


def position_averages(elements: list) -> dict:
    """Minutes-weighted per-90 rates per position (players with 180+ minutes): the shrinkage target."""
    acc = defaultdict(lambda: defaultdict(float))
    for e in elements:
        if e["minutes"] < 180:
            continue
        pos, m = e["element_type"], e["minutes"]
        for k in ("expected_goals_per_90", "expected_assists_per_90", "defensive_contribution_per_90", "saves_per_90"):
            acc[pos][k] += float(e.get(k) or 0.0) * m
        acc[pos]["bonus_per_start"] += (e["bonus"] / max(1, e["starts"])) * m
        acc[pos]["minutes"] += m
    return {pos: {k: v / max(1.0, d["minutes"]) for k, v in d.items() if k != "minutes"} for pos, d in acc.items()}


def player_fixture_xp(e: dict, lam_for: float, lam_against: float, p_play: float, p_start: float, xmins_total: float,
                      team_avg_lambda: float, games_played: int, pos_avg: dict | None = None) -> dict:
    pos = e["element_type"]
    # shrink thin samples toward the position average: full trust from 270 minutes
    w = min(1.0, e["minutes"] / 270.0)
    avg = (pos_avg or {}).get(pos, {})
    def rate(key, player_value):
        return w * player_value + (1 - w) * float(avg.get(key, player_value))
    mins = max(0.0, min(90.0, xmins_total))
    share = mins / 90.0
    p60 = p_start * (1.0 if (e["minutes"] / max(1, e["starts"]) if e["starts"] else 0) >= 60 else 0.6)
    appearance = p_play * 1.0 + p60 * 1.0  # 1 for playing, +1 for 60+
    fix = lam_for / team_avg_lambda if team_avg_lambda else 1.0
    xg90 = rate("expected_goals_per_90", float(e["expected_goals_per_90"]))
    xa90 = rate("expected_assists_per_90", float(e["expected_assists_per_90"]))
    goals = xg90 * share * fix * GOAL_PTS[pos]
    assists = xa90 * share * fix * 3
    p_cs = math.exp(-lam_against)
    cs = p60 * p_cs * CS_PTS[pos]
    conceded = -p60 * expected_conceded_penalty(lam_against) if pos in (1, 2) else 0.0
    saves = p_play * rate("saves_per_90", float(e["saves_per_90"])) * share / 3.0 if pos == 1 else 0.0
    dc90 = rate("defensive_contribution_per_90", float(e.get("defensive_contribution_per_90") or 0.0))
    dc_rate = dc90 * share
    p_defcon = 1 - poisson_cdf(DEFCON_THRESHOLD[pos] - 1, dc_rate) if dc_rate > 0 else 0.0
    defcon = p_play * p_defcon * 2
    bonus_rate = rate("bonus_per_start", e["bonus"] / max(1, e["starts"])) if e["starts"] else float(avg.get("bonus_per_start", 0.0)) * 0.5
    bonus = p_start * bonus_rate * (0.8 + 0.4 * fix) / 1.2
    cards = -p_play * (e["yellow_cards"] / max(1, games_played))
    total = appearance + goals + assists + cs + conceded + saves + defcon + bonus + cards
    return {"xp": total, "app": appearance, "goals": goals, "assists": assists, "cs": cs, "conceded": conceded,
            "saves": saves, "defcon": defcon, "bonus": bonus, "cards": cards, "p_cs": p_cs}


def run(snapshot: str, horizon: int, out_dir: str) -> str:
    s = json.load(open(snapshot))
    b, fixtures = s["bootstrap"], s["fixtures"]
    teams = {t["id"]: t for t in b["teams"]}
    next_gw = next(ev["id"] for ev in b["events"] if ev["is_next"])
    gws = list(range(next_gw, next_gw + horizon))
    strengths, league_gpg = team_strengths(b, fixtures)
    lambdas = fixture_lambdas(fixtures, strengths, league_gpg, gws)
    games_played = {t: strengths[t]["played"] for t in teams}
    team_avg_lambda = {t: strengths[t]["att"] * league_gpg for t in teams}
    pos_avg = position_averages(b["elements"])

    rows = []
    for e in b["elements"]:
        t = e["team"]
        gp = games_played[t]
        p_play, xmins, tag, p_start = minutes_model(e, gp)
        per_gw, parts = {}, defaultdict(float)
        for gw in gws:
            xp_gw = 0.0
            for (opp, venue, lam_for, lam_against) in lambdas[t].get(gw, []):
                r = player_fixture_xp(e, lam_for, lam_against, p_play, p_start, xmins, team_avg_lambda[t], gp, pos_avg)
                xp_gw += r["xp"]
                for k, v in r.items():
                    if k != "p_cs":
                        parts[k] += v
            per_gw[gw] = round(xp_gw, 2)
        total_decayed = sum(per_gw[gw] * DECAY ** i for i, gw in enumerate(gws))
        fixtures_str = " ".join(f"{teams[opp]['short_name']}({venue})" for gw in gws for (opp, venue, _, _) in lambdas[t].get(gw, [])) or "-"
        rows.append({
            "id": e["id"], "name": e["web_name"], "team": teams[t]["short_name"], "pos": POS[e["element_type"]],
            "price": e["now_cost"] / 10, "status": e["status"], "chance": e.get("chance_of_playing_next_round"),
            "news": e["news"][:60], "own_pct": e["selected_by_percent"], "pts_so_far": e["total_points"],
            "starts": e["starts"], "minutes": e["minutes"], "tag": tag, "p_start": round(p_start, 2),
            "xmins": round(xmins, 0), "ep_next": e["ep_next"], "fixtures": fixtures_str,
            **{f"xp_gw{gw}": per_gw[gw] for gw in gws},
            "xp_total": round(sum(per_gw.values()), 2), "xp_decayed": round(total_decayed, 2),
            "xp_per_m": round(total_decayed / (e["now_cost"] / 10), 2),
            **{f"c_{k}": round(v, 2) for k, v in parts.items()},
        })
    rows.sort(key=lambda r: -r["xp_decayed"])
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, f"xp_gw{gws[0]:02d}-{gws[-1]:02d}.csv")
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    # team strength table for the brief
    with open(os.path.join(out_dir, "team_strength.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["team", "att", "def", "played", "gf", "ga"])
        for t in sorted(strengths, key=lambda x: -strengths[x]["att"]):
            st = strengths[t]
            w.writerow([teams[t]["short_name"], round(st["att"], 2), round(st["def"], 2), st["played"], int(st["gf"]), int(st["ga"])])
    print(f"snapshot {os.path.basename(snapshot)} · GWs {gws[0]}-{gws[-1]} · {len(rows)} players -> {out}")
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--snapshot", default=None)
    ap.add_argument("--horizon", type=int, default=5)
    ap.add_argument("--out", default=os.path.join(ROOT, "data", "xp"))
    a = ap.parse_args()
    run(a.snapshot or latest_snapshot(), a.horizon, a.out)
