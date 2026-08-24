#!/usr/bin/env python3
"""Generate a human-readable deadline calendar from the newest snapshot.

Writes data/deadlines.csv and strategy/season-calendar.md.
Run by the daily workflow, so the calendar always reflects the FPL API —
deadlines shift when TV picks move kickoffs, and this keeps up automatically.
"""
import csv, glob, json, os
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UK, NL = ZoneInfo("Europe/London"), ZoneInfo("Europe/Amsterdam")

PHASES = [
    (1, 5, "1 Evidence", "Bank FTs, verify minutes, observe rivals"),
    (6, 10, "2 Reset & Structure", "WC1 GW6 · TC1 GW7 · BB1 GW8-12"),
    (11, 19, "3 Congestion & chip cliff", "FH1 burn GW17-18 · all set-1 chips die at GW19"),
    (20, 26, "4 Winter rebuild", "January entrants · WC2"),
    (27, 33, "5 Spring block", "FH2/BB2/TC2 on blanks & doubles"),
    (34, 38, "6 Endgame", "League above all"),
]

def phase(gw):
    for lo, hi, name, note in PHASES:
        if lo <= gw <= hi:
            return name, note
    return "?", ""

def main():
    snaps = sorted(glob.glob(os.path.join(ROOT, "data", "snapshots", "fpl_*.json")))
    if not snaps:
        print("no snapshot found")
        return
    with open(snaps[-1]) as f:
        events = json.load(f)["bootstrap"]["events"]

    rows = []
    for e in events:
        dt = datetime.fromisoformat(e["deadline_time"].replace("Z", "+00:00"))
        rows.append({
            "gw": e["id"],
            "deadline_utc": e["deadline_time"],
            "deadline_uk": dt.astimezone(UK).strftime("%a %d %b %Y %H:%M %Z"),
            "deadline_nl": dt.astimezone(NL).strftime("%a %d %b %Y %H:%M %Z"),
            "phase": phase(e["id"])[0],
            "finished": e.get("finished", False),
        })

    os.makedirs(os.path.join(ROOT, "data"), exist_ok=True)
    with open(os.path.join(ROOT, "data", "deadlines.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    now = datetime.now(timezone.utc)
    nxt = next((r for r in rows if not r["finished"]
                and datetime.fromisoformat(r["deadline_utc"].replace("Z", "+00:00")) > now), None)

    md = ["# Season Calendar — FPL 2026/27", "",
          f"Auto-generated from the FPL API on {now:%Y-%m-%d %H:%M} UTC. Do not edit by hand — "
          "`scripts/make_deadlines.py` rewrites this file daily, so it follows the API when TV picks move kickoffs.", ""]
    if nxt:
        md += [f"**Next deadline — GW{nxt['gw']}: {nxt['deadline_nl']}** (UK: {nxt['deadline_uk']})", ""]
    md += ["Deadlines are 90 minutes before each round's first kickoff. No grace period.", ""]

    for lo, hi, name, note in PHASES:
        md += [f"## Phase {name} — GW{lo}–{hi}", f"*{note}*", "",
               "| GW | Deadline (NL) | Deadline (UK) | Status |", "|---|---|---|---|"]
        for r in rows:
            if lo <= r["gw"] <= hi:
                status = "✅ done" if r["finished"] else ("▶️ current" if r is nxt else "")
                md += [f"| {r['gw']} | {r['deadline_nl']} | {r['deadline_uk']} | {status} |"]
        md += [""]

    md += ["## Fixed season markers", "",
           "- Transfer window closes: **Tue 1 Sep 2026, 23:00 UK** (after GW2)",
           "- Three-week international break: **21 Sep – 6 Oct** (between GW5 and GW6)",
           "- International breaks: 9–17 Nov · 22–30 Mar",
           "- **Chip cliff: GW19 deadline — unused first-set chips expire**",
           "- January window opens 1 Jan · UCL final 26 May (four days before GW38)",
           "- Quarterly reviews: Q1 21–24 Sep · Q2 14–18 Dec · Q3 8–12 Mar · Q4 26–30 Apr", ""]

    os.makedirs(os.path.join(ROOT, "strategy"), exist_ok=True)
    with open(os.path.join(ROOT, "strategy", "season-calendar.md"), "w") as f:
        f.write("\n".join(md))
    print(f"wrote {len(rows)} deadlines; next = GW{nxt['gw'] if nxt else '-'}")

if __name__ == "__main__":
    main()
