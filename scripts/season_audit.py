#!/usr/bin/env python3
"""Season audit, stage 1: extract per-GW facts from the committed snapshots.

For every GW N the LAST snapshot whose bootstrap marks N as current is used
(GW1-9: finished=True; the newest GW may still be provisional). That snapshot
holds the final event_points of every player AND the picks/history of every
tracked entry for GW N. Nothing here comes from memory or the network.

Outputs (data/audit/):
  player_gw.csv  one row per (gw, player): event_points + cumulative stats
  picks_gw.csv   one row per (gw, entry, pick): element, multiplier, captain flags
  entry_gw.csv   one row per (gw, entry): points, bench, transfers, cost, chip, ranks
Usage: python3 scripts/season_audit.py extract
"""
import csv, glob, json, os, sys, collections

SNAP = "data/snapshots/fpl_*.json"
OUT = "data/audit"
CUM = ["minutes", "starts", "goals_scored", "assists", "clean_sheets", "goals_conceded",
       "bonus", "bps", "saves", "yellow_cards", "red_cards", "own_goals",
       "expected_goals", "expected_assists", "expected_goals_conceded",
       "defensive_contribution", "total_points"]


def last_snapshot_per_gw():
    best = {}
    for f in sorted(glob.glob(SNAP)):
        d = json.load(open(f))
        ev = [e for e in d["bootstrap"]["events"] if e["is_current"]]
        if not ev:
            continue
        best[ev[0]["id"]] = (f, d, ev[0]["finished"])
    return best


def extract():
    os.makedirs(OUT, exist_ok=True)
    best = last_snapshot_per_gw()
    prows, krows, erows = [], [], []
    for gw, (f, d, fin) in sorted(best.items()):
        b = d["bootstrap"]
        team = {t["id"]: t["short_name"] for t in b["teams"]}
        for e in b["elements"]:
            row = dict(gw=gw, element=e["id"], name=e["web_name"], team=team[e["team"]],
                       pos=e["element_type"], price=e["now_cost"] / 10,
                       event_points=e["event_points"], sel=e["selected_by_percent"],
                       snap=os.path.basename(f), finished=fin)
            for c in CUM:
                row[c] = e.get(c)
            prows.append(row)
        ents = {"6756883": (d["picks"], d["history"])}
        for rid, rv in (d.get("rivals") or {}).items():
            if rid not in ents:
                ents[rid] = (rv.get("picks"), rv.get("history"))
        for eid, (pk, hist) in ents.items():
            if not pk or "picks" not in pk:
                continue
            eh = pk.get("entry_history", {})
            erows.append(dict(gw=gw, entry=eid, chip=pk.get("active_chip") or "", **{
                k: eh.get(k) for k in ["points", "total_points", "rank", "overall_rank", "bank",
                                        "value", "event_transfers", "event_transfers_cost",
                                        "points_on_bench"]}, snap=os.path.basename(f)))
            for p in pk["picks"]:
                krows.append(dict(gw=gw, entry=eid, pos=p["position"], element=p["element"],
                                  mult=p["multiplier"], cap=int(p["is_captain"]),
                                  vc=int(p["is_vice_captain"])))
    for name, rows in (("player_gw", prows), ("picks_gw", krows), ("entry_gw", erows)):
        with open(f"{OUT}/{name}.csv", "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
            w.writeheader(); w.writerows(rows)
        print(name, len(rows))


if __name__ == "__main__":
    if sys.argv[1:] == ["extract"]:
        extract()
    else:
        print(__doc__)


# ---------------------------------------------------------------- stage 2
def latest():
    fs = sorted(glob.glob(SNAP))
    return json.load(open(fs[-1])), fs[-1]


def rivals_gw():
    """One row per (entry, gw) from the newest snapshot's histories (GW1..now)."""
    d, f = latest()
    names = {str(r["entry"]): (r["player_name"], r["entry_name"])
             for r in d["league"]["standings"]["results"]}
    rows = []
    ents = dict(d.get("rivals") or {})
    ents.setdefault("6756883", {"history": d["history"]})
    for eid, rv in ents.items():
        h = rv.get("history") or {}
        chips = {c["event"]: c["name"] for c in h.get("chips", [])}
        for c in h.get("current", []):
            rows.append(dict(entry=eid, manager=names.get(eid, ("?", "?"))[0], gw=c["event"],
                             points=c["points"], total=c["total_points"], rank=c["rank"],
                             overall_rank=c["overall_rank"], bench=c["points_on_bench"],
                             transfers=c["event_transfers"], hit=c["event_transfers_cost"],
                             value=c["value"], bank=c["bank"], chip=chips.get(c["event"], "")))
    with open(f"{OUT}/rivals_gw.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(sorted(rows, key=lambda r: (r["gw"], r["entry"])))
    print("rivals_gw", len(rows), os.path.basename(f))


if __name__ == "__main__" and sys.argv[1:] == ["rivals"]:
    rivals_gw()
