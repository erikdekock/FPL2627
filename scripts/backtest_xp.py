#!/usr/bin/env python3
"""Backtest the xP model on finished gameweeks, against FPL's ep_next and a naive form baseline.

For each GW N (2..last finished): take the last snapshot taken before N's deadline, run
scripts/xp_model.py on it with horizon 1, and compare its xP for GW N with the points players
actually scored in GW N (data/audit/player_gw.csv). Same for ep_next (FPL's own forecast in that
snapshot) and 'form' (the API's points-per-game of the last 30 days).

Players judged: everyone with at least 2 expected points by any of the three forecasts (the ones a
manager would consider). Metrics: MAE (average miss in points), bias (forecast minus actual; positive
= too optimistic), Spearman rank correlation, and the actual points of each forecast's top-10 and
top captain pick. Output: data/model/backtest_gw.csv (per GW x forecast) and backtest_pos.csv.
"""
import csv, glob, json, os, subprocess, sys, tempfile, datetime as dt
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def spearman(a, b):
    def rank(v):
        o = sorted(range(len(v)), key=lambda i: v[i]); r = [0.0] * len(v); i = 0
        while i < len(o):
            j = i
            while j + 1 < len(o) and v[o[j + 1]] == v[o[i]]: j += 1
            for k in range(i, j + 1): r[o[k]] = (i + j) / 2
            i = j + 1
        return r
    ra, rb = rank(a), rank(b); n = len(a); ma, mb = sum(ra) / n, sum(rb) / n
    cov = sum((x - ma) * (y - mb) for x, y in zip(ra, rb))
    va = sum((x - ma) ** 2 for x in ra) ** .5; vb = sum((y - mb) ** 2 for y in rb) ** .5
    return cov / (va * vb) if va and vb else 0


def main():
    dl = {int(r["gw"]): dt.datetime.fromisoformat(r["deadline_utc"].replace("Z", "+00:00"))
          for r in csv.DictReader(open(os.path.join(ROOT, "data/deadlines.csv")))}
    act = {}
    for r in csv.DictReader(open(os.path.join(ROOT, "data/audit/player_gw.csv"))):
        if r["finished"] == "True": act[(int(r["gw"]), int(r["element"]))] = int(r["event_points"])
    done = sorted({g for g, _ in act})
    snaps = sorted(glob.glob(os.path.join(ROOT, "data/snapshots/fpl_*.json")))
    stamp = lambda f: dt.datetime.strptime(os.path.basename(f)[4:21], "%Y-%m-%dT%H%M%S").replace(tzinfo=dt.timezone.utc)
    out_gw, out_pos = [], []
    for g in done:
        if g < 2: continue
        pre = [f for f in snaps if stamp(f) < dl[g]]
        if not pre: continue
        snap = pre[-1]; s = json.load(open(snap))
        if not any(e["is_next"] and e["id"] == g for e in s["bootstrap"]["events"]): continue
        tmp = tempfile.mkdtemp()
        subprocess.run([sys.executable, os.path.join(ROOT, "scripts/xp_model.py"), "--snapshot", snap, "--horizon", "1", "--out", tmp],
                       check=True, capture_output=True)
        xp = {int(r["id"]): r for r in csv.DictReader(open(glob.glob(os.path.join(tmp, "xp_gw*.csv"))[0]))}
        form = {e["id"]: float(e["form"]) for e in s["bootstrap"]["elements"]}
        rows = []
        for pid, r in xp.items():
            if (g, pid) not in act: continue
            f = {"model": float(r[f"xp_gw{g}"]), "ep_next": float(r["ep_next"] or 0), "form": form.get(pid, 0)}
            if max(f.values()) < 2: continue
            rows.append((pid, r["pos"], act[(g, pid)], f))
        for k in ("model", "ep_next", "form"):
            pred = [x[3][k] for x in rows]; real = [x[2] for x in rows]
            top = sorted(rows, key=lambda x: -x[3][k])[:10]
            out_gw.append(dict(gw=g, forecast=k, n=len(rows), snapshot=os.path.basename(snap),
                               mae=round(sum(abs(p - a) for p, a in zip(pred, real)) / len(rows), 3),
                               bias=round(sum(p - a for p, a in zip(pred, real)) / len(rows), 3),
                               spearman=round(spearman(pred, real), 3),
                               top10_actual=round(sum(x[2] for x in top) / 10, 2),
                               top_pick=xp[top[0][0]]["name"], top_pick_actual=top[0][2]))
            for pos in ("GK", "DEF", "MID", "FWD"):
                sub = [x for x in rows if x[1] == pos]
                if not sub: continue
                out_pos.append(dict(gw=g, forecast=k, pos=pos, n=len(sub),
                                    mae=round(sum(abs(x[3][k] - x[2]) for x in sub) / len(sub), 3),
                                    bias=round(sum(x[3][k] - x[2] for x in sub) / len(sub), 3)))
        if not os.environ.get('BT_NOWRITE'): print(g, os.path.basename(snap), len(rows))
    for fn, rows in ((("backtest_gw.csv", out_gw), ("backtest_pos.csv", out_pos)) if not os.environ.get("BT_NOWRITE") else ()):
        with open(os.path.join(ROOT, "data/model", fn), "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    # summary
    import collections
    agg = collections.defaultdict(list)
    for r in out_gw: agg[r["forecast"]].append(r)
    for k, rs in agg.items():
        n = len(rs)
        print(f"{k:8} GWs {n} · MAE {sum(r['mae'] for r in rs)/n:.2f} · bias {sum(r['bias'] for r in rs)/n:+.2f} · "
              f"rho {sum(r['spearman'] for r in rs)/n:.2f} · top10 avg {sum(r['top10_actual'] for r in rs)/n:.2f} · "
              f"top pick avg {sum(r['top_pick_actual'] for r in rs)/n:.2f}")


if __name__ == "__main__":
    main()
