#!/usr/bin/env python3
"""Print the grading table for a finished gameweek from the repo snapshots — the review chat starts here.

Usage:
    python scripts/review_table.py            # the most recent finished GW in the newest snapshot
    python scripts/review_table.py --gw 5

Shows: our 15 with multiplier and GW points, autosubs, bench points, captain vs the field's
most-captained, the league table for that GW with each rival's captain/chip when available
(data/rivals.csv), and the players we named as alternatives in data/decisions.csv with their
points — so every A-vs-B call has both numbers on the table before anyone argues.
"""
import argparse
import csv
import glob
import json
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
POS = {1: "GK", 2: "DEF", 3: "MID", 4: "FWD"}


def snapshot_for(gw: int | None):
    """The last snapshot whose current event is `gw` (its elements' event_points are that GW's)."""
    files = sorted(glob.glob(os.path.join(ROOT, "data", "snapshots", "fpl_*.json")))
    chosen = None
    for f in files:
        s = json.load(open(f))
        cur = next((e["id"] for e in s["bootstrap"]["events"] if e["is_current"]), None)
        if gw is None or cur == gw:
            chosen = (f, s, cur)
    if not chosen:
        raise SystemExit(f"no snapshot with current GW {gw}")
    return chosen


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gw", type=int, default=None)
    a = ap.parse_args()
    f, s, gw = snapshot_for(a.gw)
    b = s["bootstrap"]; el = {e["id"]: e for e in b["elements"]}; teams = {t["id"]: t["short_name"] for t in b["teams"]}
    ev = next(e for e in b["events"] if e["id"] == gw)
    pk = s["picks"]; eh = pk["entry_history"]
    print(f"GW{gw} from {os.path.basename(f)} · finished={ev['finished']}")
    print(f"points {eh['points']} · average {ev['average_entry_score']} · highest {ev['highest_score']} · GW rank {eh['rank']:,} · OR {eh['overall_rank']:,} · bench {eh['points_on_bench']} · transfers {eh['event_transfers']} (hit {eh['event_transfers_cost']}) · chip {pk['active_chip']}")
    mc = el[ev["most_captained"]]
    cap = next(el[p["element"]] for p in pk["picks"] if p["is_captain"])
    print(f"captain {cap['web_name']} {cap['event_points']} vs field captain {mc['web_name']} {mc['event_points']} → delta {cap['event_points'] - mc['event_points']:+d}")
    print(f"{'#':>2} {'name':<14}{'team':<5}{'pos':<4}{'x':<3}{'pts':>4}  {'min':>4}  own%")
    for p in pk["picks"]:
        e = el[p["element"]]
        print(f"{p['position']:>2} {e['web_name']:<14}{teams[e['team']]:<5}{POS[e['element_type']]:<4}{p['multiplier']:<3}{e['event_points']:>4}  {e['minutes']:>4}  {e['selected_by_percent']}")
    if pk["automatic_subs"]:
        print("autosubs:", ", ".join(f"{el[x['element_in']]['web_name']} for {el[x['element_out']]['web_name']}" for x in pk["automatic_subs"]))
    print("\nleague:")
    rivals = {}
    rp = os.path.join(ROOT, "data", "rivals.csv")
    if os.path.exists(rp):
        for r in csv.DictReader(open(rp, encoding="utf-8")):
            if r["gw"] == str(gw):
                rivals[int(r["entry"])] = r
    for r in s["league"]["standings"]["results"]:
        rv = rivals.get(r["entry"], {})
        print(f"{r['rank']:>2} {r['entry_name'][:22]:<23}{r['total']:>4} ({r['event_total']:>3})  C {rv.get('captain', '?'):<12} chip {rv.get('chip', '?') or '-':<9} tr {rv.get('transfers', '?')} hit {rv.get('hit_points', '?')}")
    dp = os.path.join(ROOT, "data", "decisions.csv")
    if os.path.exists(dp):
        print("\ndecisions A vs B:")
        name_pts = {}
        for e in b["elements"]:
            name_pts.setdefault(e["web_name"], []).append((teams[e["team"]], e["event_points"]))
        for r in csv.DictReader(open(dp, encoding="utf-8")):
            if r["gw"] == str(gw):
                def pts(txt):
                    return "; ".join(f"{n} {name_pts[n]}" for n in [x.strip() for x in txt.replace('->', ',').replace('+', ',').split(',')] if n in name_pts)
                print(f"- {r['id']} {r['type']}: A={r['A']} [{pts(r['A'])}] · B={r['B']} [{pts(r['B'])}] · EXP {r['exp']} p={r['prob']}")


if __name__ == "__main__":
    main()
