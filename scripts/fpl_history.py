#!/usr/bin/env python3
"""Cache every league entry's transfers and per-GW picks (GW1..last finished) under data/history/.

Picks of a finished GW never change, so each file is fetched once; transfers are refreshed every run.
Runs in GitHub Actions (the API is not reachable from the chat sandbox). Output:
  data/history/transfers_<entry>.json   full transfer list of the entry
  data/history/picks/<entry>_<gw>.json  picks, automatic_subs, active_chip, entry_history of that GW
"""
import json, os, time, urllib.request

API = "https://fantasy.premierleague.com/api/"
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "data", "history")
LEAGUE = os.environ.get("FPL_LEAGUE_ID", "348280")


def get(path):
    for i in range(4):
        try:
            req = urllib.request.Request(API + path, headers={"User-Agent": "fpl2627-history/1.0"})
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except Exception:
            time.sleep(2 + 3 * i)
    raise RuntimeError(path)


def main():
    os.makedirs(os.path.join(OUT, "picks"), exist_ok=True)
    boot = get("bootstrap-static/")
    done = [e["id"] for e in boot["events"] if e["finished"]]
    league = get(f"leagues-classic/{LEAGUE}/standings/")
    n = 0
    for r in league["standings"]["results"]:
        eid = r["entry"]
        json.dump(get(f"entry/{eid}/transfers/"), open(os.path.join(OUT, f"transfers_{eid}.json"), "w"))
        for gw in done:
            f = os.path.join(OUT, "picks", f"{eid}_{gw}.json")
            if os.path.exists(f):
                continue
            json.dump(get(f"entry/{eid}/event/{gw}/picks/"), open(f, "w")); n += 1
            time.sleep(0.3)
    print(f"entries {len(league['standings']['results'])} · finished GWs {len(done)} · new pick files {n}")


if __name__ == "__main__":
    main()
