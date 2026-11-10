# Weekscherm refresh (dashboard https://claude.ai/artifact/T76mFS5AcKuPGoGPCGrdTA)

Run by the T-48h prep task and by every review chat.

1. `git pull` (the history workflow caches all picks and transfers in data/history/), then
   `python3 scripts/season_audit.py extract && python3 scripts/league_analysis.py && python3 scripts/xp_model.py --horizon 6 && python3 scripts/dashboard_data.py`
   (writes `data/dashboard/weekscherm.json`; needs `pip install "pulp<4" highspy`).
2. Upload it: Artifact tool, `url` = the dashboard, `asset: true`, `file_path` = data/dashboard/weekscherm.json. Note the returned `/_blob/<id>`.
3. ArtifactData `batch` of `update` on `datasets/<id>` for the 22 ids
   meta, league, team, captains, transfers, potential, fixtures, lastweek, decisions, season, indicators, phase,
   captains_league, tc_used, transfers_league, managers,
   radar, radar_sum, tc_plan, execution, gaprows, catchup (read each dataset for its version first):
   `{"source": {"url": "/_blob/<id>"}, "updated": {"at": <UTC now>, "by": "Claude (scripts/dashboard_data.py)"}, "edit": {"via": "claude", "at": <UTC now>}}`
   (read each document first for its version; pass it as if_version).
4. Delete the previous blob (Artifact `delete` with `path` = old id) only after step 3 succeeded.
5. The indicators rows are filled from the latest review; update them in `scripts/dashboard_data.py` when the review computes new values.
The page itself (`files/index.html`, source in `docs/dashboard/index.html`) is not touched by a refresh.
