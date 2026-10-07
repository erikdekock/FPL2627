#!/usr/bin/env python3
"""Snapshot the FPL API into data/snapshots/ as one timestamped JSON, and keep data/rivals.csv current.

Usage (GitHub Actions daily, or any machine that can reach fantasy.premierleague.com —
the claude.ai shell cannot; there Claude reads these snapshots and uses web fetch for live calls):

    FPL_TEAM_ID=6756883 FPL_LEAGUE_ID=348280 python scripts/fpl_pull.py

Stdlib only. Captures: bootstrap-static (players/prices/ownership/flags/deadlines), fixtures,
and — with FPL_TEAM_ID — the entry, its transfers, history and current-GW picks; with
FPL_LEAGUE_ID — the league standings plus, for every entry in the league, its history (chips,
hits, bench points, OR) and its current-GW picks (public after each deadline). From that it
appends one row per rival per gameweek to data/rivals.csv (captain, vice, chip, transfers, hits,
points) — the Rival Radar that the review chat reads.
"""
import csv
import json
import os
import urllib.request
from datetime import datetime, timezone

BASE = "https://fantasy.premierleague.com/api"
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
OUT = os.path.join(DATA, "snapshots")
RIVALS_CSV = os.path.join(DATA, "rivals.csv")
RIVAL_FIELDS = ["gw", "entry", "entry_name", "player_name", "gw_points", "total_points", "league_rank",
                "overall_rank", "captain", "vice", "chip", "transfers", "hit_points", "bench_points",
                "team_value", "bank", "chips_used", "snapshot"]


def get(path: str):
    req = urllib.request.Request(f"{BASE}/{path}", headers={"User-Agent": "fpl-hq/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def rivals_rows(snap: dict, gw: int, stamp: str) -> list[dict]:
    el = {e["id"]: e["web_name"] for e in snap["bootstrap"]["elements"]}
    rows = []
    for r in snap["league"]["standings"]["results"]:
        eid = r["entry"]
        hist = snap["rivals"].get(str(eid), {}).get("history", {})
        picks = snap["rivals"].get(str(eid), {}).get("picks", {})
        cur = next((h for h in hist.get("current", []) if h["event"] == gw), {})
        cap = next((el[p["element"]] for p in picks.get("picks", []) if p["is_captain"]), "")
        vice = next((el[p["element"]] for p in picks.get("picks", []) if p["is_vice_captain"]), "")
        rows.append({
            "gw": gw, "entry": eid, "entry_name": r["entry_name"], "player_name": r["player_name"],
            "gw_points": r["event_total"], "total_points": r["total"], "league_rank": r["rank"],
            "overall_rank": cur.get("overall_rank", ""), "captain": cap, "vice": vice,
            "chip": picks.get("active_chip") or "", "transfers": cur.get("event_transfers", ""),
            "hit_points": cur.get("event_transfers_cost", ""), "bench_points": cur.get("points_on_bench", ""),
            "team_value": cur.get("value", ""), "bank": cur.get("bank", ""),
            "chips_used": "+".join(f"{c['name']}@{c['event']}" for c in hist.get("chips", [])),
            "snapshot": stamp,
        })
    return rows


def upsert_rivals(rows: list[dict]) -> None:
    existing = []
    if os.path.exists(RIVALS_CSV):
        existing = list(csv.DictReader(open(RIVALS_CSV, encoding="utf-8")))
    keep = [r for r in existing if not any(r["gw"] == str(n["gw"]) and r["entry"] == str(n["entry"]) for n in rows)]
    keep.extend(rows)
    keep.sort(key=lambda r: (int(r["gw"]), int(r["league_rank"])))
    with open(RIVALS_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=RIVAL_FIELDS)
        w.writeheader(); w.writerows(keep)


def main() -> None:
    os.makedirs(OUT, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")
    snap = {"taken_utc": stamp, "bootstrap": get("bootstrap-static/"), "fixtures": get("fixtures/")}
    current = [e["id"] for e in snap["bootstrap"]["events"] if e.get("is_current")]
    gw = current[0] if current else None

    team_id = os.environ.get("FPL_TEAM_ID")
    if team_id:
        snap["entry"] = get(f"entry/{team_id}/")
        snap["transfers"] = get(f"entry/{team_id}/transfers/")
        snap["history"] = get(f"entry/{team_id}/history/")
        if gw:
            snap["picks"] = get(f"entry/{team_id}/event/{gw}/picks/")

    league_id = os.environ.get("FPL_LEAGUE_ID")
    if league_id:
        snap["league"] = get(f"leagues-classic/{league_id}/standings/")
        snap["rivals"] = {}
        for r in snap["league"]["standings"]["results"]:
            eid = r["entry"]
            try:
                entry = {"history": get(f"entry/{eid}/history/")}
                if gw:
                    entry["picks"] = get(f"entry/{eid}/event/{gw}/picks/")
                snap["rivals"][str(eid)] = entry
            except Exception as ex:  # one rival failing must not kill the snapshot
                snap["rivals"][str(eid)] = {"error": str(ex)}
        if gw:
            upsert_rivals(rivals_rows(snap, gw, stamp))

    path = os.path.join(OUT, f"fpl_{stamp}.json")
    with open(path, "w") as f:
        json.dump(snap, f, separators=(",", ":"))
    print(f"saved {path} ({os.path.getsize(path) // 1024} KB) · GW {gw} · rivals {len(snap.get('rivals', {}))}")


if __name__ == "__main__":
    main()
