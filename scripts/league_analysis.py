#!/usr/bin/env python3
"""League analysis GW1..last finished: captains, Triple Captain use and every transfer, per manager.

Inputs: data/history/picks/<entry>_<gw>.json and transfers_<entry>.json (scripts/fpl_history.py, run in
Actions), data/audit/player_gw.csv (per-GW player points and cumulative minutes, scripts/season_audit.py),
and the newest snapshot for names. Output: data/audit/captains.csv, transfers_league.csv, managers.csv.

Definitions (plain):
- Captain points = what the armband added in total (points x multiplier). If the captain did not play, the vice
  takes over (as in the game).
- Haaland benchmark = what the same armband would have given on Haaland that week (x the same multiplier).
- Best pick = the highest scorer in that manager's starting XI that week (hindsight, for scale only).
- A transfer is judged over the time the manager kept the new player (from that GW to the GW before he sold
  him again, or to the last finished GW): points of the player brought in minus points of the player sold,
  over exactly those GWs. Free Hit transfers are left out (the squad reverts after one week). Wildcard
  transfers are listed, but the out/in pairing on a Wildcard is the API's, not a real swap, so the manager
  totals (transfers, net, best, worst) count normal transfers only.
"""
import csv, glob, json, os, collections

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
H = os.path.join(ROOT, "data", "history")
SHORT = {"6756883": "Erik", "41757": "Alex", "6913443": "Jason", "888210": "Thomas", "8205933": "Richard",
         "2826110": "Billy", "6376934": "Kelvin", "2107617": "Lawrence", "2171229": "Robert", "1218083": "R.W."}
CHIP = {"wildcard": "WC", "freehit": "FH", "bboost": "BB", "3xc": "TC", "": ""}


def main():
    snap = json.load(open(sorted(glob.glob(os.path.join(ROOT, "data/snapshots/fpl_*.json")))[-1]))
    b = snap["bootstrap"]; team = {t["id"]: t["short_name"] for t in b["teams"]}
    name = {e["id"]: e["web_name"] for e in b["elements"]}
    club = {e["id"]: team[e["team"]] for e in b["elements"]}
    pts, cum = {}, {}
    for r in csv.DictReader(open(os.path.join(ROOT, "data/audit/player_gw.csv"))):
        k = (int(r["gw"]), int(r["element"])); pts[k] = int(r["event_points"]); cum[k] = int(r["minutes"] or 0)
    mins = lambda g, el: cum.get((g, el), 0) - cum.get((g - 1, el), 0)
    P = lambda g, el: pts.get((g, el), 0)
    haaland = [e["id"] for e in b["elements"] if e["web_name"] == "Haaland"][0]

    picks = {}
    for f in glob.glob(os.path.join(H, "picks", "*_*.json")):
        eid, gw = os.path.basename(f)[:-5].split("_"); picks[(eid, int(gw))] = json.load(open(f))
    entries = sorted({e for e, _ in picks}); gws = sorted({g for _, g in picks}); last = max(gws)

    caps = []
    for eid in entries:
        for g in gws:
            pk = picks.get((eid, g))
            if not pk: continue
            chip = CHIP.get(pk.get("active_chip") or "", pk.get("active_chip") or "")
            c = next(p for p in pk["picks"] if p["is_captain"]); v = next(p for p in pk["picks"] if p["is_vice_captain"])
            mult = 3 if chip == "TC" else 2
            who, note = c["element"], ""
            if mins(g, who) == 0 and mins(g, v["element"]) > 0:
                who, note = v["element"], "captain did not play, vice took over"
            xi = [p["element"] for p in pk["picks"] if p["position"] <= 11]
            best = max(xi, key=lambda el: P(g, el))
            caps.append(dict(gw=g, manager=SHORT.get(eid, eid), entry=eid, chip=chip, captain=name[who], club=club[who],
                             raw=P(g, who), mult=mult, captain_pts=P(g, who) * mult,
                             haaland_pts=P(g, haaland) * mult, vs_haaland=(P(g, who) - P(g, haaland)) * mult,
                             best_pick=name[best], best_pts=P(g, best) * mult, missed=(P(g, best) - P(g, who)) * mult,
                             tc_extra=P(g, who) if chip == "TC" else 0, note=note))

    trs = []
    for eid in entries:
        f = os.path.join(H, f"transfers_{eid}.json")
        if not os.path.exists(f): continue
        tl = sorted(json.load(open(f)), key=lambda t: t["time"])
        fh = {g for (e, g), pk in picks.items() if e == eid and pk.get("active_chip") == "freehit"}
        wc = {g for (e, g), pk in picks.items() if e == eid and pk.get("active_chip") == "wildcard"}
        hits = {g: pk["entry_history"]["event_transfers_cost"] for (e, g), pk in picks.items() if e == eid}
        n_in_gw = collections.Counter(t["event"] for t in tl)
        for i, t in enumerate(tl):
            g = t["event"]
            if g in fh or g > last: continue
            sold = next((u["event"] for u in tl[i + 1:] if u["element_out"] == t["element_in"] and u["event"] not in fh), None)
            end = (sold - 1) if sold else last
            span = list(range(g, end + 1))
            pi = sum(P(x, t["element_in"]) for x in span); po = sum(P(x, t["element_out"]) for x in span)
            hit_share = round(hits.get(g, 0) / n_in_gw[g], 1) if hits.get(g, 0) else 0
            trs.append(dict(manager=SHORT.get(eid, eid), entry=eid, gw=g, chip="WC" if g in wc else "",
                            out=name[t["element_out"]], out_club=club[t["element_out"]], out_price=t["element_out_cost"] / 10,
                            into=name[t["element_in"]], in_club=club[t["element_in"]], in_price=t["element_in_cost"] / 10,
                            weeks=len(span), kept_until=f"GW{end}" + (" (sold)" if sold else " (still in team)"),
                            pts_in=pi, pts_out=po, net=pi - po, hit=hit_share, net_after_hit=round(pi - po - hit_share, 1)))

    mgr = []
    for eid in entries:
        cs = [c for c in caps if c["entry"] == eid]; ts = [t for t in trs if t["entry"] == eid and not t["chip"]]
        n_wc = sum(1 for t in trs if t["entry"] == eid and t["chip"] == "WC")
        tc = [c for c in cs if c["chip"] == "TC"]
        mgr.append(dict(manager=SHORT.get(eid, eid), captain_total=sum(c["captain_pts"] for c in cs),
                        haaland_weeks=sum(c["captain"] == "Haaland" for c in cs), weeks=len(cs),
                        vs_always_haaland=sum(c["vs_haaland"] for c in cs), missed_vs_best=sum(c["missed"] for c in cs),
                        tc_gw=tc[0]["gw"] if tc else "", tc_captain=tc[0]["captain"] if tc else "",
                        tc_extra=tc[0]["tc_extra"] if tc else "",
                        transfers=len(ts), wc_transfers=n_wc, transfer_net=sum(t["net"] for t in ts),
                        hits=sum(picks[(eid, g)]["entry_history"]["event_transfers_cost"] for g in gws if (eid, g) in picks),
                        best_transfer=max(ts, key=lambda t: t["net"], default={}).get("into", ""),
                        best_net=max((t["net"] for t in ts), default=""),
                        worst_transfer=min(ts, key=lambda t: t["net"], default={}).get("into", ""),
                        worst_net=min((t["net"] for t in ts), default="")))
    out = os.path.join(ROOT, "data", "audit")
    for fn, rows in (("captains.csv", caps), ("transfers_league.csv", trs), ("managers.csv", mgr)):
        with open(os.path.join(out, fn), "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
        print(fn, len(rows))


if __name__ == "__main__":
    main()
