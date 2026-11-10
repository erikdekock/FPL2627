#!/usr/bin/env python3
"""Build data/dashboard/weekscherm.json for the weekly dashboard (one JSON object, one key per dataset).

Inputs: newest data/snapshots file, newest data/xp/xp_gw*.csv + team_strength.csv, data/decisions.csv,
data/gameweek_log.csv, strategy/lessons.md, and the output of scripts/one_transfer.py (run here).
Everything is read from the repo; nothing from memory. Run: python3 scripts/dashboard_data.py
"""
import csv, glob, json, os, re, subprocess, sys, datetime as dt
from zoneinfo import ZoneInfo

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ME = "6756883"
SET1 = {"wildcard", "freehit", "bboost", "3xc"}
CHIP_NL = {"wildcard": "WC", "freehit": "FH", "bboost": "BB", "3xc": "TC"}
SHORT = {"6756883": "Erik", "41757": "Alex", "6913443": "Jason", "888210": "Thomas", "8205933": "Richard",
         "2826110": "Billy", "6376934": "Kelvin", "2107617": "Lawrence", "2171229": "Robert", "1218083": "R.W."}


def p(*a): return os.path.join(ROOT, *a)


def main():
    snapf = sorted(glob.glob(p("data/snapshots/fpl_*.json")))[-1]
    s = json.load(open(snapf))
    b = s["bootstrap"]
    els = {e["id"]: e for e in b["elements"]}
    team = {t["id"]: t["short_name"] for t in b["teams"]}
    cur = [e for e in b["events"] if e["is_current"]][0]
    nxt = [e for e in b["events"] if e["is_next"]][0]
    dl = dt.datetime.fromisoformat(nxt["deadline_time"].replace("Z", "+00:00"))
    uk, nl = dl.astimezone(ZoneInfo("Europe/London")), dl.astimezone(ZoneInfo("Europe/Amsterdam"))
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    mon = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    dstr = f"{days[nl.weekday()]} {nl.day} {mon[nl.month-1]}"
    locked_by = (nl - dt.timedelta(hours=3)).strftime("%H:%M")

    # ---------- league
    hist = {ME: s["history"]}
    for rid, rv in (s.get("rivals") or {}).items():
        hist[rid] = rv["history"]
    res = s["league"]["standings"]["results"]
    lead_total = max(r["total"] for r in res)
    league = []
    for r in res:
        eid = str(r["entry"]); h = hist.get(eid, {})
        used = {c["name"] for c in h.get("chips", []) if c["event"] <= 19}
        left = [CHIP_NL[c] for c in ["wildcard", "freehit", "bboost", "3xc"] if c not in used]
        cur_h = {c["event"]: c["total_points"] for c in h.get("current", [])}
        trend = [cur_h.get(g) for g in range(max(1, cur["id"] - 5), cur["id"] + 1)]
        league.append(dict(rank=r["rank"], manager=SHORT.get(eid, r["player_name"]), entry=eid,
                           total=r["total"], gw_points=r["event_total"], gap_leader=r["total"] - lead_total,
                           chips_left=" ".join(left) or "none", open_wc_fh=int(any(c in left for c in ["WC", "FH"])),
                           trend=" ".join(str(x) for x in trend if x is not None), me=int(eid == ME)))
    league.sort(key=lambda x: x["rank"])
    me = [x for x in league if x["me"]][0]
    leader = league[0] if not league[0]["me"] else league[1]
    alex = [x for x in league if x["entry"] == "41757"][0]

    # ---------- picks & ownership in the league (current GW picks)
    picks = {ME: s["picks"]["picks"]}
    for rid, rv in (s.get("rivals") or {}).items():
        if rv.get("picks") and "picks" in rv["picks"]:
            picks[rid] = rv["picks"]["picks"]
    own = {}
    for eid, pk in picks.items():
        if eid == ME: continue
        for q in pk: own[q["element"]] = own.get(q["element"], 0) + 1
    nriv = len(picks) - 1

    # ---------- xP + strength
    xpf = sorted(glob.glob(p("data/xp/xp_gw*.csv")))[-1]
    xp = {int(r["id"]): r for r in csv.DictReader(open(xpf))}
    gws = [int(c[5:]) for c in next(iter(xp.values())).keys() if re.fullmatch(r"xp_gw\d+", c)]
    ts = {r["team"]: r for r in csv.DictReader(open(p("data/xp/team_strength.csv")))}

    def diff(opp, home):
        t = ts.get(opp)
        if not t: return 3
        v = (float(t["att"]) + 1 / max(float(t["def"]), 0.3)) / 2 + (0 if home else 0.12)
        return 1 if v < 0.85 else 2 if v < 0.97 else 3 if v < 1.08 else 4 if v < 1.2 else 5

    fx = {}
    for f in s["fixtures"]:
        if f["event"] in gws:
            h, a = team[f["team_h"]], team[f["team_a"]]
            fx.setdefault((h, f["event"]), []).append((a, True))
            fx.setdefault((a, f["event"]), []).append((h, False))

    def fixcells(club):
        out = []
        for g in gws:
            lst = fx.get((club, g), [])
            if not lst: out.append(("BLANK", 0)); continue
            out.append(("+".join(f"{o}{'(H)' if hm else '(A)'}" for o, hm in lst), max(diff(o, hm) for o, hm in lst)))
        return out

    # ---------- minutes per GW from audit extract (cumulative minutes of the last snapshot per GW)
    pg = {}
    for r in csv.DictReader(open(p("data/audit/player_gw.csv"))):
        pg[(int(r["gw"]), int(r["element"]))] = int(r["minutes"] or 0)

    def mins(el, g):
        return pg.get((g, el), 0) - pg.get((g - 1, el), 0)

    POS = {1: "GK", 2: "DEF", 3: "MID", 4: "FWD"}
    teamrows = []
    for q in s["picks"]["picks"]:
        e = els[q["element"]]; x = xp.get(e["id"], {})
        cells = fixcells(team[e["team"]])
        row = dict(slot=q["position"], name=e["web_name"], club=team[e["team"]], pos=POS[e["element_type"]],
                   price=e["now_cost"] / 10, status={"a": "fit", "d": "doubt", "i": "injured", "s": "suspended", "u": "left club", "n": "unavailable"}.get(e["status"], e["status"]),
                   chance=e["chance_of_playing_next_round"], news=e["news"], tag=x.get("tag", ""),
                   min_last3=" ".join(str(mins(e["id"], g)) for g in range(cur["id"] - 2, cur["id"] + 1)),
                   pts=e["total_points"], form=float(e["form"]), xp_next=float(x.get(f"xp_gw{gws[0]}", 0)),
                   xp_6=float(x.get("xp_total", 0)), league_owners=own.get(e["id"], 0), sel=float(e["selected_by_percent"]),
                   bench=int(q["position"] > 11))
        for i, (txt, d) in enumerate(cells):
            row[f"f{i+1}"] = txt; row[f"d{i+1}"] = d
        teamrows.append(row)

    # ---------- captains (our 15, by next-GW xP)
    caps = sorted(teamrows, key=lambda r: -r["xp_next"])[:5]
    sword = me["gap_leader"] < -20
    captains = []
    for r in caps:
        e = [x for x in els.values() if x["web_name"] == r["name"] and team[x["team"]] == r["club"]][0]
        games = max(1, int(xp[e["id"]]["starts"] or 0))
        ppg = round(e["total_points"] / max(1, sum(1 for g in range(1, cur["id"] + 1) if mins(e["id"], g) > 0)), 2)
        captains.append(dict(name=r["name"], club=r["club"], fixture=r["f1"], xp=round(r["xp_next"], 2),
                             league_owners=r["league_owners"], of=nriv,
                             label="shield" if r["league_owners"] >= (nriv + 1) // 2 else "sword",
                             season_ppg=ppg, tc_margin=round(r["xp_next"] - ppg, 2)))

    # ---------- transfers via one_transfer.py
    out = subprocess.run([sys.executable, p("scripts/one_transfer.py"), "--xp", xpf, "--show", "8"],
                         capture_output=True, text=True, cwd=ROOT).stdout
    transfers = [dict(rank=0, move="Roll (save the transfer)", obj_delta=0.0, next_gw_delta=0.0, bank_after=None, note="baseline")]
    for line in out.splitlines():
        m = re.match(r"\s*([+-][\d.]+) obj \| ([+-][\d.]+) GW\d+ \| (.+?) \(sell £([\d.]+)\) -> (.+?) £([\d.]+) · own ([\d.]+)% · bank after £([\d.]+)", line)
        if m:
            transfers.append(dict(rank=len(transfers), move=f"{m[3]} → {m[5]}", obj_delta=float(m[1]),
                                  next_gw_delta=float(m[2]), bank_after=float(m[8]), note=f"sell £{m[4]}, buy £{m[6]}, owned by {m[7]}%"))

    # ---------- potential: best xP over the horizon, not in our 15
    mine = {q["element"] for q in s["picks"]["picks"]}
    pot = []
    for pid, x in xp.items():
        if pid in mine or x["tag"] not in ("nailed", "likely"): continue
        pot.append(dict(name=x["name"], club=x["team"], pos=x["pos"], price=float(x["price"]), xp_6=float(x["xp_total"]),
                        xp_per_m=float(x["xp_per_m"]), sel=float(x["own_pct"]), league_owners=own.get(pid, 0),
                        fixtures=x["fixtures"]))
    potential = sorted(pot, key=lambda r: -r["xp_6"])[:20]
    for i, r in enumerate(potential): r["rank"] = i + 1

    # ---------- fixture ticker
    fixtures = []
    for club in sorted(ts):
        row = dict(club=club, strength=round(float(ts[club]["att"]) - float(ts[club]["def"]), 2))
        for i, (txt, d) in enumerate(fixcells(club)):
            row[f"f{i+1}"] = txt; row[f"d{i+1}"] = d
        fixtures.append(row)

    # ---------- last week (current GW) per manager
    lastweek = []
    for eid, pk in picks.items():
        c = [q for q in pk if q["is_captain"]][0]; e = els[c["element"]]
        mrow = [x for x in league if x["entry"] == eid]
        lastweek.append(dict(manager=SHORT.get(eid, eid), points=mrow[0]["gw_points"] if mrow else None,
                             captain=e["web_name"], captain_pts=e["event_points"] * c["multiplier"], me=int(eid == ME)))
    lastweek.sort(key=lambda r: -(r["points"] or 0))

    decisions = []
    for r in csv.DictReader(open(p("data/decisions.csv"))):
        if int(r["gw"]) == cur["id"]:
            decisions.append(dict(id=r["id"], type=r["type"], A=r["A"], B=r["B"], outcome=r["outcome"][:160],
                                  process=r["process_grade"].split(" ")[0], result=r["outcome_grade"]))

    lessons = [l for l in open(p("strategy/lessons.md")).read().splitlines() if l.startswith("| 20")]
    last_lesson = lessons[-1].split("|")[3].strip() if lessons else ""

    # ---------- season curve
    log = list(csv.DictReader(open(p("data/gameweek_log.csv"))))
    evs = {e["id"]: e for e in b["events"]}
    season = []
    for c in s["history"]["current"]:
        g = c["event"]
        lp = [hist[e]["current"][g - 1]["points"] for e in hist if len(hist[e].get("current", [])) >= g]
        season.append(dict(gw=g, points=c["points"], field_avg=evs[g]["average_entry_score"],
                           league_avg=round(sum(lp) / len(lp), 1), overall_rank=c["overall_rank"]))

    # ---------- indicators (D-G3); values from the Q2 audit, refreshed by the review chat
    indicators = [
        dict(indicator="Execution: app = LOCKED", value="0 of 5 weeks", target="≥ 90%", state="red", basis="GW6–10"),
        dict(indicator="Captain vs league", value="90 vs avg 55", target="≥ league average", state="green", basis="GW6–10"),
        dict(indicator="Bench points (4 weeks)", value="36 vs avg 43", target="≤ league average", state="green", basis="GW6–9"),
        dict(indicator="Forecast Brier score", value="0.218", target="≤ 0.22", state="green", basis="22 forecasts"),
        dict(indicator="Chip rationale written ahead", value="0 of 3", target="≥ 1 day", state="red", basis="FH1, WC1, BB1"),
        dict(indicator="Gap to leader / Alex", value=f"{me['gap_leader']} / {me['total']-alex['total']:+d}", target="trend", state="info", basis=f"after GW{cur['id']}"),
    ]
    phase = [
        dict(criterion="TC1 played before the GW19 deadline", status="open", note="windows GW11 / GW16 / GW19 (D-S1)"),
        dict(criterion="Execution score ≥ 90%", status="open", note="measured from GW11 (rules 4a/4b)"),
        dict(criterion="At least P2 in the league at GW19", status="on track" if me["rank"] <= 2 else "behind", note=f"now P{me['rank']}"),
    ]

    sh = me["gap_leader"]
    headline = (f"{leader['manager']} leads by {abs(sh)}" if sh < 0 else f"We lead {leader['manager']} by {sh}") + \
               f"; he still has {leader['chips_left']}. Alex {me['total']-alex['total']:+d} with {alex['chips_left']}. Us: {me['chips_left']}."

    meta = [dict(gw=nxt["id"], deadline_uk=f"{uk:%a %d %b %H:%M} UK", deadline_nl=f"{dstr} {nl:%H:%M} NL",
                 deadline_utc=nxt["deadline_time"], locked_by=f"{locked_by} NL", phase="3 · Congestion & chip cliff" if nxt["id"] <= 19 else "",
                 chips_left=me["chips_left"], deadlines_to_gw19=max(0, 19 - nxt["id"] + 1),
                 bank=s["history"]["current"][-1]["bank"] / 10, total=me["total"], overall_rank=s["history"]["current"][-1]["overall_rank"],
                 league_rank=me["rank"], gap_leader=me["gap_leader"], posture="sword" if sword else "shield",
                 headline=headline, last_gw=cur["id"], last_points=s["history"]["current"][-1]["points"],
                 last_avg=cur["average_entry_score"], last_lesson=last_lesson,
                 snapshot=os.path.basename(snapf), xp_table=os.path.basename(xpf),
                 generated=dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%MZ"))]

    # ---------- league analysis (scripts/league_analysis.py)
    def rd(fn):
        f = p("data/audit", fn)
        return list(csv.DictReader(open(f))) if os.path.exists(f) else []
    captains_league = rd("captains.csv")
    for r in captains_league: r["key"] = f"{r['manager']} GW{r['gw']}"
    tc_used = [r for r in captains_league if r["chip"] == "TC"]
    transfers_league = sorted(rd("transfers_league.csv"), key=lambda r: (-int(r["gw"]), r["manager"]))
    for r in transfers_league: r["key"] = f"{r['manager']} GW{r['gw']} {r['out']}>{r['into']}"
    managers = sorted(rd("managers.csv"), key=lambda r: -int(r["captain_total"]))

    allout = dict(captains_league=captains_league, tc_used=tc_used, transfers_league=transfers_league, managers=managers, meta=meta, league=league, team=teamrows, captains=captains, transfers=transfers,
                  potential=potential, fixtures=fixtures, lastweek=lastweek, decisions=decisions,
                  season=season, indicators=indicators, phase=phase)
    os.makedirs(p("data/dashboard"), exist_ok=True)
    json.dump(allout, open(p("data/dashboard/weekscherm.json"), "w"), ensure_ascii=False, indent=1)
    print({k: len(v) for k, v in allout.items()})


if __name__ == "__main__":
    main()
