#!/usr/bin/env python3
"""Snapshot the FPL API into data/snapshots/ as one timestamped JSON.

Usage (local machine or Claude Code — NOT the claude.ai sandbox, which
cannot reach fantasy.premierleague.com; there Claude uses web_fetch instead):

    FPL_TEAM_ID=1234567 python scripts/fpl_pull.py

Stdlib only. Captures: bootstrap-static (players/prices/ownership/flags/
deadlines), fixtures, and — if FPL_TEAM_ID is set — the entry and current
Gameweek picks.
"""
import json
import os
import urllib.request
from datetime import datetime, timezone

BASE = "https://fantasy.premierleague.com/api"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "snapshots")


def get(path: str):
    req = urllib.request.Request(f"{BASE}/{path}", headers={"User-Agent": "fpl-hq/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def main() -> None:
    os.makedirs(OUT, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")
    snap = {"taken_utc": stamp, "bootstrap": get("bootstrap-static/"), "fixtures": get("fixtures/")}

    team_id = os.environ.get("FPL_TEAM_ID")
    if team_id:
        snap["entry"] = get(f"entry/{team_id}/")
        snap["transfers"] = get(f"entry/{team_id}/transfers/")
        snap["history"] = get(f"entry/{team_id}/history/")
        current = [e["id"] for e in snap["bootstrap"]["events"] if e.get("is_current")]
        if current:
            snap["picks"] = get(f"entry/{team_id}/event/{current[0]}/picks/")

    league_id = os.environ.get("FPL_LEAGUE_ID")
    if league_id:
        # standings + every rival entry id; rival picks are public after each deadline
        snap["league"] = get(f"leagues-classic/{league_id}/standings/")

    path = os.path.join(OUT, f"fpl_{stamp}.json")
    with open(path, "w") as f:
        json.dump(snap, f, separators=(",", ":"))
    print(f"saved {path} ({os.path.getsize(path) // 1024} KB)")


if __name__ == "__main__":
    main()
