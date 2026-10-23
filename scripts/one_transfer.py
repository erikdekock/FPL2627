#!/usr/bin/env python3
"""One-transfer finder: every OUT from the current 15 x the top-N affordable INs at that position,
each scored by wc_solver on the FULL squad (objective delta vs rolling, plus next-GW XI xP).

Usage: python scripts/one_transfer.py [--xp data/xp/xp_gwNN-MM.csv] [--top 6] [--show 20]
Selling price = purchase + half the profit (rounded down), from the transfers log; bank from history.
A tool to argue with, not a decision: the minutes gate and the perspectives in strategy/selection-method.md decide.
"""
import argparse, glob, json, os, sys
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wc_solver as w
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ap = argparse.ArgumentParser(); ap.add_argument("--xp"); ap.add_argument("--top", type=int, default=6); ap.add_argument("--show", type=int, default=20)
a = ap.parse_args()
snap = sorted(glob.glob(os.path.join(ROOT, "data/snapshots/fpl_*.json")))[-1]; s = json.load(open(snap))
xpf = a.xp or sorted(glob.glob(os.path.join(ROOT, "data/xp/xp_gw*.csv")))[-1]
rows, gws = w.load_xp(xpf); idx = {int(r["id"]): r for r in rows}
els = {e["id"]: e for e in s["bootstrap"]["elements"]}
cur = [p["element"] for p in s["picks"]["picks"]]
buy = {}
for t in sorted(s["transfers"], key=lambda t: t["time"]): buy[t["element_in"]] = t["element_in_cost"]
bank = s["history"]["current"][-1]["bank"] / 10
def sell(i):
    now = els[i]["now_cost"]; b = buy.get(i, now)
    return (b + (now - b) // 2 if now > b else now) / 10
def score(ids):
    sq, xi, cap, obj = w.solve(rows, gws, 999, "out", 0.1, 0.84, [], [], 15, fixed_ids=set(ids), label="t")
    g = gws[0]; return obj, sum(x[f"xp_gw{g}"] for x in xi[g]) + cap[g][f"xp_gw{g}"]
base_obj, base_g = score(cur)
print(f"{os.path.basename(snap)} · {os.path.basename(xpf)} · bank £{bank:.1f} · ROLL objective {base_obj:.1f}, GW{gws[0]} XI {base_g:.1f}")
teams = Counter(idx[i]["team"] for i in cur); res = []
for o in cur:
    budget = sell(o) + bank; pos = idx[o]["pos"]
    c = [r for r in rows if r["pos"] == pos and r["tag"] in ("nailed", "likely") and r["price"] <= budget + 1e-9 and int(r["id"]) not in cur
         and teams[r["team"]] - (idx[o]["team"] == r["team"]) < 3]
    for r in sorted(c, key=lambda r: -float(r["xp_decayed"]))[: a.top]:
        obj, g = score(set(cur) - {o} | {int(r["id"])})
        res.append((obj - base_obj, g - base_g, idx[o]["name"], sell(o), r["name"], r["team"], r["price"], r["own_pct"], budget - r["price"]))
for x in sorted(res, key=lambda x: -x[0])[: a.show]:
    print(f"{x[0]:+5.1f} obj | {x[1]:+4.1f} GW{gws[0]} | {x[2]} (sell £{x[3]}) -> {x[4]} {x[5]} £{x[6]} · own {x[7]}% · bank after £{x[8]:.1f}")
