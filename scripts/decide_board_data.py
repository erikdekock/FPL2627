#!/usr/bin/env python3
"""Export the data for the interactive GW decide board (Transfers + Selection + Captain + Chip).

Usage: python scripts/decide_board_data.py [--xp data/xp/xp_gwNN-MM.csv] [--out data/dashboard/decide_gwNN.json]

Squad, sell prices (FPL 50% profit rule, as in one_transfer.py), bank, league standings, rivals'
latest picks and chips, and a candidate pool (tag nailed/likely, top 45 per position by decayed xP,
plus every rival-owned player) with per-GW xP over the file's horizon, fixtures with FDR,
underlying stats, set-piece orders, minutes and ownership. The page does the arithmetic
(best XI by formation enumeration, captain, decay, swaps) client-side.
"""
import argparse, csv, glob, json, os
from collections import Counter

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
RIVALS = {"6913443": "Jason", "41757": "Alex", "888210": "Thomas", "8205933": "Richard", "2826110": "Billy",
          "6376934": "Kelvin", "2107617": "Lawrence", "2171229": "Robert", "1218083": "R.W."}
CHIPS = {"wildcard": "WC", "freehit": "FH", "bboost": "BB", "3xc": "TC"}

ap = argparse.ArgumentParser(); ap.add_argument("--xp"); ap.add_argument("--out"); a = ap.parse_args()
snapf = sorted(glob.glob(os.path.join(ROOT, "data/snapshots/fpl_*.json")))[-1]; s = json.load(open(snapf))
xpf = a.xp or sorted(glob.glob(os.path.join(ROOT, "data/xp/xp_gw*.csv")), key=os.path.getmtime)[-1]
rows = list(csv.DictReader(open(xpf)))
gws = sorted(int(k[5:]) for k in rows[0] if k.startswith("xp_gw"))
xp = {int(r["id"]): r for r in rows}
b = s["bootstrap"]; els = {e["id"]: e for e in b["elements"]}; T = {t["id"]: t["short_name"] for t in b["teams"]}
nxt = next(e for e in b["events"] if e["is_next"])

# fixtures per team per GW (list, doubles allowed)
fx = {}
for f in s["fixtures"]:
    if f["event"] in gws:
        fx.setdefault(f["team_h"], {}).setdefault(f["event"], []).append([T[f["team_a"]], "H", f["team_h_difficulty"]])
        fx.setdefault(f["team_a"], {}).setdefault(f["event"], []).append([T[f["team_h"]], "A", f["team_a_difficulty"]])

ko = {}
for f in s["fixtures"]:
    if f["event"] == gws[0]:
        for t in (f["team_h"], f["team_a"]): ko.setdefault(t, f["kickoff_time"])
cur = [p["element"] for p in s["picks"]["picks"]]
buy = {}
for t in sorted(s["transfers"], key=lambda t: t["time"]): buy[t["element_in"]] = t["element_in_cost"]
def sell(i):
    now = els[i]["now_cost"]; bb = buy.get(i, now)
    return (bb + (now - bb) // 2 if now > bb else now) / 10

own = Counter(); cap = Counter(); rivals = []
for rid, name in RIVALS.items():
    r = s["rivals"].get(rid)
    if not r: continue
    pk = r["picks"]; ids = [p["element"] for p in pk["picks"]]
    for i in ids: own[i] += 1
    c = next((p["element"] for p in pk["picks"] if p["is_captain"]), None)
    if c: cap[c] += 1
    used = [CHIPS.get(c["name"], c["name"]) for c in r["history"]["chips"] if c["event"] <= 19]
    rivals.append({"id": rid, "name": name, "squad": ids, "xi": [p["element"] for p in pk["picks"] if p["position"] <= 11],
                   "captain": c, "chips_left": [x for x in ["WC", "FH", "TC", "BB"] if x not in used],
                   "bank": pk["entry_history"]["bank"] / 10})

pool = set(cur) | set(own)
for pos in ("GK", "DEF", "MID", "FWD"):
    c = [r for r in rows if r["pos"] == pos and r["tag"] in ("nailed", "likely")]
    c.sort(key=lambda r: -float(r["xp_decayed"]))
    pool |= {int(r["id"]) for r in c[:45]}

def f2(x):
    try: return round(float(x), 2)
    except (TypeError, ValueError): return 0.0
players = []
for i in sorted(pool):
    if i not in xp: continue
    r, e = xp[i], els[i]
    players.append({
        "id": i, "n": r["name"], "t": r["team"], "p": r["pos"], "c": float(r["price"]),
        "sell": sell(i) if i in cur else None, "own": i in cur,
        "xp": [f2(r[f"xp_gw{g}"]) for g in gws],
        "fx": [fx.get(e["team"], {}).get(g, []) for g in gws],
        "tag": r["tag"], "pst": f2(r["p_start"]), "xm": f2(r["xmins"]), "st": e["status"], "news": e["news"],
        "pts": e["total_points"], "last": e["event_points"], "form": f2(e["form"]), "mins": e["minutes"], "starts": e["starts"],
        "g": e["goals_scored"], "xg": f2(e["expected_goals"]), "a": e["assists"], "xa": f2(e["expected_assists"]),
        "xgi90": f2(e["expected_goal_involvements_per_90"]), "dc90": f2(e.get("defensive_contribution_per_90")),
        "cs": e["clean_sheets"], "ict": f2(e["ict_index"]), "inf": f2(e["influence"]), "cre": f2(e["creativity"]), "thr": f2(e["threat"]),
        "pen": e["penalties_order"], "cor": e["corners_and_indirect_freekicks_order"], "dfk": e["direct_freekicks_order"],
        "sel": f2(e["selected_by_percent"]), "lg": own[i], "lgc": cap[i], "dprice": e["cost_change_event"] / 10,
        "tin": e["transfers_in_event"], "tout": e["transfers_out_event"], "ep": f2(e["ep_next"]),
    })

st = [{"rank": x["rank"], "name": x["player_name"], "team": x["entry_name"], "id": x["entry"], "gw": x["event_total"], "total": x["total"]}
      for x in s["league"]["standings"]["results"]]
h = s["history"]["current"][-1]
used = [CHIPS.get(c["name"], c["name"]) for c in s["history"]["chips"] if c["event"] <= 19]
out = {
    "meta": {"snapshot": os.path.basename(snapf), "taken_utc": s.get("taken_utc"), "xp_file": os.path.basename(xpf), "gws": gws,
             "gw": nxt["id"], "deadline_utc": nxt["deadline_time"], "bank": h["bank"] / 10, "value": h["value"] / 10,
             "points": h["total_points"], "overall_rank": h["overall_rank"], "last_gw_points": h["points"], "ft": 1,
             "chips_left": [x for x in ["WC", "FH", "TC", "BB"] if x not in used],
             "tc_expires": "GW19 deadline, Fri 1 Jan 2027 18:30 GMT"},
    "kickoff": {T[t]: k for t, k in ko.items()},
    "squad": cur, "players": players, "standings": st, "rivals": rivals,
}
dst = a.out or os.path.join(ROOT, "data", "dashboard", f"decide_gw{nxt['id']:02d}.json")
os.makedirs(os.path.dirname(dst), exist_ok=True)
json.dump(out, open(dst, "w"), separators=(",", ":"), ensure_ascii=False)
print(f"{dst}: {len(players)} players, GWs {gws[0]}-{gws[-1]}, snapshot {os.path.basename(snapf)}")
