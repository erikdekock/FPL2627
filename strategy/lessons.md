# Lessons — dated, with evidence
Status: `seen-once` · `recurring` · `rule` (promoted, see `rules.md`) · `retired`. The review chat appends; the bias review (every fourth review) promotes or retires.

| Date | GW | Lesson | Evidence | Status |
|---|---|---|---|---|
| 2026-08-21 | 1 | Presser-level verification before the deadline catches confirmed zeros (Porro not in squad). | Porro → Calafiori, 29 pts since | rule (8) |
| 2026-08-21 | 1 | An unwritten deadline swap is a mood, not a position. | Calvert-Lewin → Brobbey at the deadline; 24 vs 22 — luck, flagged | rule (5) |
| 2026-08-28 | 2 | In a 10-manager league the shield is league-EO, not field-EO. | Alex captained Bruno (46) vs our Haaland (26): −20 | rule (16) |
| 2026-08-28 | 2 | Executing before writing the deviation costs nothing until it does. | Watkins → João Pedro 17:32 deadline day, log after | rule (5) |
| 2026-09-04 | 3 | Predicted bench ≠ confirmed bench without a second signal. | Ndiaye sold, started 3/3; Elanga 1 pt then injured | rule (8) |
| 2026-09-04 | 3 | Holding TC below the bar is correct even when 1.79M fire it. | −9 vs field; good process | seen-once |
| 2026-09-08 | 3 | Right club, wrong player: the cheaper, less-owned starter at the same club outscored ours six times. | Stach 27/Bogle 42 · Collins 10/Janelt 28 · Elanga 18/Barnes 28 · Verbruggen 23/De Cuyper 38 · Keane 0/Tarkowski 43 · Egan 26/Tzolakis 34 | rule (10) |
| 2026-09-18 | 4 | A plan is not a transfer until the API shows it. | Collins→Bogle agreed Thu 10 Sep, never executed; Collins 0 min in the XI; Bogle 15 | rule (4) |
| 2026-09-18 | 4–5 | A bench that cannot play makes every flag a certain zero. | GW4: Collins + Elanga 0 min, Hughes 1; GW5: João Pedro 0 min, no sub; bench pts 1 in five GWs | rule (7, 9) |
| 2026-09-18 | 5 | A recommendation with 0-minute players in the XI must never reach Erik. | First GW5 XI had Senesi + Keane starting | rule (8) |
| 2026-10-07 | break | A review date in a document is not a meeting. | Q1 review 21–24 Sep not held; no chat 18 Sep → 7 Oct; WC built in three days instead of three weeks | rule (3) |
| 2026-10-07 | 1–5 | The protocol was abandoned, not simplified. | 82-minute three-session week never run; one long chat per GW | rule (3, 6) |
| 2026-10-23 | 6 | The wrong chip can be played with the right plan: name the chip on the confirm screen. | FH1 fired instead of WC1; squad reverted at GW7 | seen-once |
| 2026-10-23 | 7 | A LOCKED fix that is not re-screenshotted is not executed. | Three app differences from LOCKED in GW7 (+3 by luck) | recurring (rule 4) |
| 2026-10-23 | 7 | Two players from one defence share one result. | Tarkowski 0 + Barry 2 v Chelsea; flagged at build | seen-once |
| 2026-11-05 | 8 | The deadline is a fact from the API, not a weekday habit: a Friday deadline read as Saturday erased a whole plan. | GW8 deadline Fri 23 Oct 18:30 UK; nothing executed; +10 (Tavernier) and +5 (XI) lost, −12 (sword) avoided by accident | **recurring** → rule proposal (4a): line 1 of every decide chat = deadline from `events[].deadline_time` with hours to go; LOCKED ≥ 3 h before; execution confirmed by screenshot |
| 2026-11-05 | 8–9 | Plan-not-executed is now the dominant bias: three of the last five GWs (GW4, GW7, GW8). | decisions.csv rows 8/D1–D5 "not executed"; GW7 three app differences; GW4 Collins→Bogle never made | recurring (rule 4) |
| 2026-11-05 | 9 | A long-horizon buy is still a one-week bet when the squad needs the week: say which week the buy is for. | Isak (22.7 xP over 6 GWs, ARS(H) flagged as the weak week) 2 pts vs Jackson/Evanilson 9 (−7); the review asked for "a banger this week" | seen-once |
| 2026-11-05 | 9 | The league's best defence does not take a full fixture discount: team strength before FPL difficulty for benching decisions. | De Cuyper (4.0 xP) and Vuskovic (3.8) benched at MCI by A; Brighton CS at the Etihad, 9 + 6 pts; Erik's B took De Cuyper (+8) | seen-once → model calibration (`xp_model.py` CS weight for top-3 defences) |
| 2026-11-05 | 9 | Erik's conviction picks on Brighton defenders are 2 for 2 against the model. | Vuskovic GW7 (11, autosub), De Cuyper GW9 (9) | seen-once (watch for the bias cell: good/good twice is a pattern, not a rule yet) |
