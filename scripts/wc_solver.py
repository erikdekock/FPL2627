#!/usr/bin/env python3
"""Wildcard / squad solver v0 — a small MILP (pulp + HiGHS) over the xP table from xp_model.py.

Usage:
    python scripts/wc_solver.py                                  # 15-man wildcard squad, budget from the snapshot
    python scripts/wc_solver.py --budget 99.4 --ban Haaland      # structure C: no Haaland
    python scripts/wc_solver.py --lock Haaland --lock B.Fernandes
    python scripts/wc_solver.py --baseline                       # best XI from the CURRENT 15 (the no-wildcard baseline)

What it maximises: sum over the horizon of decayed (0.84^k) expected points of the best XI
per gameweek + captain doubled + a small weight for bench points (autosub insurance). It obeys
the FPL rules (2 GK, 5 DEF, 5 MID, 3 FWD, max 3 per club, legal formations) and our own rules:
nobody tagged 'doubt' or 'out' can be bought (the minutes gate), optional minimum bank, locks
and bans. It is a tool for arguing, not a decision: the decide chat reads the result next to
presser news, predicted XIs and league-EO, and writes A/B with theses.

Caveats: v0 xP is five matches of evidence; the solver will happily stack one team's cheap
defenders because their fixtures look soft — that is a feature to interrogate, not obey.
"""
from __future__ import annotations

import argparse
import csv
import glob
import json
import os

import pulp

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
POS_SLOTS = {"GK": 2, "DEF": 5, "MID": 5, "FWD": 3}
FORMATION = {"GK": (1, 1), "DEF": (3, 5), "MID": (2, 5), "FWD": (1, 3)}
TAG_RANK = {"nailed": 4, "likely": 3, "50-50": 2, "doubt": 1, "out": 0}


def latest(pattern: str) -> str:
    files = sorted(glob.glob(pattern))
    if not files:
        raise SystemExit(f"nothing matches {pattern}")
    return files[-1]


def load_xp(path: str):
    rows = list(csv.DictReader(open(path)))
    gws = sorted(int(k[5:]) for k in rows[0] if k.startswith("xp_gw"))
    for r in rows:
        r["price"] = float(r["price"])
        for gw in gws:
            r[f"xp_gw{gw}"] = float(r[f"xp_gw{gw}"])
    return rows, gws


def current_squad_ids(snapshot: str) -> tuple[set[int], float]:
    s = json.load(open(snapshot))
    ids = {p["element"] for p in s["picks"]["picks"]}
    value = s["picks"]["entry_history"]["value"] / 10  # team value incl. bank, selling prices
    return ids, value


def solve(rows, gws, budget, min_tag, bench_weight, decay, locks, bans, max_team, fixed_ids=None, label="wildcard"):
    cand = [r for r in rows if TAG_RANK[r["tag"]] >= TAG_RANK[min_tag] and r["name"] not in bans]
    if fixed_ids is not None:
        cand = [r for r in rows if int(r["id"]) in fixed_ids]
    idx = {int(r["id"]): r for r in cand}
    prob = pulp.LpProblem(label, pulp.LpMaximize)
    x = {i: pulp.LpVariable(f"x_{i}", cat="Binary") for i in idx}
    y = {(i, g): pulp.LpVariable(f"y_{i}_{g}", cat="Binary") for i in idx for g in gws}
    c = {(i, g): pulp.LpVariable(f"c_{i}_{g}", cat="Binary") for i in idx for g in gws}
    w = {g: decay ** k for k, g in enumerate(gws)}
    prob += pulp.lpSum(
        w[g] * (idx[i][f"xp_gw{g}"] * (y[i, g] + c[i, g]) + bench_weight * idx[i][f"xp_gw{g}"] * (x[i] - y[i, g]))
        for i in idx for g in gws
    )
    prob += pulp.lpSum(x.values()) == 15
    for pos, n in POS_SLOTS.items():
        prob += pulp.lpSum(x[i] for i in idx if idx[i]["pos"] == pos) == n
    prob += pulp.lpSum(idx[i]["price"] * x[i] for i in idx) <= budget
    for team in {r["team"] for r in cand}:
        prob += pulp.lpSum(x[i] for i in idx if idx[i]["team"] == team) <= max_team
    for g in gws:
        prob += pulp.lpSum(y[i, g] for i in idx) == 11
        prob += pulp.lpSum(c[i, g] for i in idx) == 1
        for pos, (lo, hi) in FORMATION.items():
            prob += pulp.lpSum(y[i, g] for i in idx if idx[i]["pos"] == pos) >= lo
            prob += pulp.lpSum(y[i, g] for i in idx if idx[i]["pos"] == pos) <= hi
        for i in idx:
            prob += y[i, g] <= x[i]
            prob += c[i, g] <= y[i, g]
    for name in locks:
        ids = [i for i in idx if idx[i]["name"] == name]
        if not ids:
            raise SystemExit(f"lock not in candidate pool (tag below {min_tag}?): {name}")
        prob += pulp.lpSum(x[i] for i in ids) >= 1
    if fixed_ids is not None:
        for i in idx:
            prob += x[i] == 1
    prob.solve(pulp.HiGHS(msg=False))
    squad = [idx[i] for i in idx if x[i].value() > 0.5]
    xi = {g: [idx[i] for i in idx if y[i, g].value() > 0.5] for g in gws}
    cap = {g: next(idx[i] for i in idx if c[i, g].value() > 0.5) for g in gws}
    obj = pulp.value(prob.objective)
    return squad, xi, cap, obj


def report(squad, xi, cap, gws, budget, title):
    order = {"GK": 0, "DEF": 1, "MID": 2, "FWD": 3}
    squad = sorted(squad, key=lambda r: (order[r["pos"]], -r[f"xp_gw{gws[0]}"]))
    cost = sum(r["price"] for r in squad)
    print(f"\n=== {title} · cost £{cost:.1f} of £{budget:.1f} (bank £{budget - cost:.1f}) ===")
    print(f"{'pos':<4}{'name':<14}{'team':<5}{'£':<6}{'tag':<7}{'own%':>6}" + "".join(f"{'gw'+str(g):>7}" for g in gws) + f"{'dec':>7}")
    for r in squad:
        print(f"{r['pos']:<4}{r['name']:<14}{r['team']:<5}{r['price']:<6}{r['tag']:<7}{r['own_pct']:>6}" + "".join(f"{r[f'xp_gw{g}']:>7.2f}" for g in gws) + f"{float(r['xp_decayed']):>7.2f}")
    for g in gws:
        xi_g = sorted(xi[g], key=lambda r: order[r["pos"]])
        pts = sum(r[f"xp_gw{g}"] for r in xi_g) + cap[g][f"xp_gw{g}"]
        bench = [r for r in squad if r not in xi_g]
        form = "-".join(str(sum(1 for r in xi_g if r["pos"] == p)) for p in ("DEF", "MID", "FWD"))
        print(f"GW{g}: XI xP {pts:.1f} ({form}) · C {cap[g]['name']} · bench " + ", ".join(r['name'] for r in sorted(bench, key=lambda r: (r['pos'] != 'GK', -r[f'xp_gw{g}']))))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--xp", default=None, help="xp csv from xp_model.py (default: latest in data/xp)")
    ap.add_argument("--snapshot", default=None)
    ap.add_argument("--budget", type=float, default=None, help="default: team value from snapshot minus --min-bank")
    ap.add_argument("--min-bank", type=float, default=0.3)
    ap.add_argument("--min-tag", default="likely", choices=list(TAG_RANK))
    ap.add_argument("--bench-weight", type=float, default=0.1)
    ap.add_argument("--decay", type=float, default=0.84)
    ap.add_argument("--max-team", type=int, default=3)
    ap.add_argument("--lock", action="append", default=[])
    ap.add_argument("--ban", action="append", default=[])
    ap.add_argument("--baseline", action="store_true", help="best XI from the current 15, no transfers")
    ap.add_argument("--horizon", type=int, default=None, help="use only the first N gameweeks of the xp table")
    a = ap.parse_args()

    xp_path = a.xp or latest(os.path.join(ROOT, "data", "xp", "xp_gw*.csv"))
    snapshot = a.snapshot or latest(os.path.join(ROOT, "data", "snapshots", "fpl_*.json"))
    rows, gws = load_xp(xp_path)
    if a.horizon:
        gws = gws[: a.horizon]
    current_ids, team_value = current_squad_ids(snapshot)
    budget = a.budget if a.budget is not None else round(team_value - a.min_bank, 1)
    print(f"xp table {os.path.basename(xp_path)} · snapshot {os.path.basename(snapshot)} · horizon GW{gws[0]}-{gws[-1]} · team value £{team_value:.1f}")

    if a.baseline:
        squad, xi, cap, obj = solve(rows, gws, 999, "out", a.bench_weight, a.decay, [], [], 15, fixed_ids=current_ids, label="baseline")
        report(squad, xi, cap, gws, team_value, "BASELINE: current 15, best XI per GW")
    else:
        squad, xi, cap, obj = solve(rows, gws, budget, a.min_tag, a.bench_weight, a.decay, a.lock, a.ban, a.max_team)
        title = "WILDCARD draft" + (f" · lock {a.lock}" if a.lock else "") + (f" · ban {a.ban}" if a.ban else "") + f" · min tag {a.min_tag}"
        report(squad, xi, cap, gws, budget, title)
        print(f"objective (decayed horizon xP incl. captain, bench x{a.bench_weight}): {obj:.1f}")
