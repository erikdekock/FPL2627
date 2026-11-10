# Strategy Q2 · process review — programme and interim state
**v0.1 · Sun 8 Nov 2026 · living document: the status board is updated after every step, the audit (§6) is filled in step B. Owner Claude (project manager), decisions Erik. Chat `Strategy Q2 · process review`; kickoff in `docs/prompts/strategy-q2-process-review.md`.**

## 0. Why
GW10 was the best week of the season: 123 points, GW rank 37 of 11,260,358, OR 3,508,984 → 795,926 (provisional until lockdown Mon 9 Nov 09:00 UK), league P8 → P2 (−27 on Jason, +9 on Alex). The question of this review is not "what did we pick" but "which parts of the process produced that, which parts produced GW3 (36), GW8 (nothing executed) and GW9 (44), and what has to change so a 123-week becomes the standard output of the system, not an accident". Everything below is sized so that the whole programme lands before the **GW11 deadline, Sat 21 Nov 2026 11:00 GMT / 12:00 CET** (API `events[11].deadline_time` 2026-11-21T11:00:00Z). GW11 itself is decided in its own chat; nothing here decides GW11.

## 1. Inventory findings that shape the programme (read-back of 8 Nov, repo HEAD `8c48e2e`)
1. **The brain exists but is unevenly filled.** `rules.md` v3.0 unchanged since 7 Oct with four proposals open (4a, 4b, 17, 18); `lessons.md` 26 rows; `decisions.csv` 26 rows of which GW6 D1–D5 are still `open` (the GW06 review was never held); `gameweek_log.csv` GW1–5 backfilled on 7 Oct, GW10 provisional; `strategy.md` **v2.1 of 15 Aug, never revised** (Q1 review not held); `campaign-plan.md` v1.0 carries stale dates (GW19 cliff "Sat 2 Jan" — the API says Fri 1 Jan 2027 18:30 GMT); `selection-method.md` v1.0 is the one method that is documented from a week that worked.
2. **Models run daily, have never been measured.** `xp_model.py` v0 and `wc_solver.py` v0 run in the Action every day; the weekly xP-vs-`ep_next` comparison written into the review skill has never been done; the team-strength blend gave the league's best defence a full fixture discount (GW9, De Cuyper); the GW10 captain call was overridden with a finishing adjustment that is not in the model. 94 snapshots (23 Aug – 8 Nov) include a pre-deadline snapshot for every GW2–10, so a backtest is possible without external data.
3. **The two-chat week has run zero times as designed.** Reality since 7 Oct: one combined chat per gameweek (review of the last GW + decision for the next), 50 / 18 / 28 turns long; decisions taken on deadline morning or the evening before (GW6 Sat 09:20–11:50 UTC under the deadline, GW8 Fri afternoon and missed, GW9 Fri 21:30–00:07, GW10 Fri 06:23–06:37 with two "think again" loops); reviews never (GW6), in the next decide chat (GW7), nine and two days late (GW8, GW9), before lockdown (GW10); bias review at GW9 and Strategy Q1 not held. No chat from 18 Sep to 7 Oct.
4. **The automation was switched off after one run.** "FPL decide prep (Fri)" ran once (Fri 9 Oct, 21 min, wrote a correct GW06 prep into the brief); "FPL review prep (Tue)" never ran; both were disabled Tue 13 Oct 07:52 NL within ten seconds of a third task (bulk action, no chat records why). GW8 was then missed on a Friday that the prep task would have announced that morning. The 10 Oct chat proposed a deadline-relative "dispatcher" task, calendar entries, a default LOCKED, `model_log.csv` and `process_log.csv`; none of it was built. Google Calendar holds no FPL items.
5. **Project settings lag the repo.** The project instructions in the Claude project are the 7 Oct version; the 23 Oct draft (`docs/project-instructions.md`: deadline as line 1, selection method, handover docs, snapshot dispatch) was never pasted. The installed `fpl-strategy-review` skill is newer than its repo copy (handover step, "name the chip on the confirm screen", club-doubt rule).
6. **What the record says about the points.** Rule 10 (cheapest nailed scorer at the right club) and the GW7 selection method produced the two best weeks (70, 123); the sword captain under rule 18 produced +14 in GW10; plan-not-executed (GW4, GW7, GW8) and same-day chips (GW6, GW7, GW10) are the recurring process failures; Erik's conviction B beat Claude's A four times running (GW7 Vuskovic, GW9 De Cuyper, GW10 BB1, GW10 Barry) — the plan-anchoring hypothesis to test in §6.

## 2. The programme
Legend: **Erik decides** = a decision Erik takes in chat (one per message, A with reason / B / confidence); **Only Erik** = an action only Erik can perform (paste, save, approve, execute). Estimates are Claude working time; Erik's time is the decisions plus reading.

### A · Repair the brain first (facts, no strategy) — ~1 h, session 1
| # | Step | Produces | Erik |
|---|---|---|---|
| A1 | Grade GW6 D1–D5 from the API (chip +8 vs baseline; squad A free draft vs B over GW6–9; captain Mbeumo 16 vs Haaland 12, B executed; bench; GW ≥ 60 missed at 59) and close GW7 D2 (v1.0 vs free draft over GW7–10) | `data/decisions.csv` complete for GW6–10 | — |
| A2 | After Monday's lockdown check (scheduled task, Mon 9 Nov 11:30 NL): confirm GW10 row, brief §5–6, remove PROVISIONAL; log the GW12 bench as D2's counterfactual when GW12 is in | `data/gameweek_log.csv`, `briefs/GW10.md` | — |
| A3 | Correct stale facts: GW19 cliff date in `campaign-plan.md` §1.1/§1.3/§3 and `README.md`; phase notes in `make_deadlines.py` ("WC1 GW6 · TC1 GW7"); FBref status in `docs/02` | consistent dates everywhere | — |
| A4 | Sync `skills/` to the installed versions (interim; full rewrite in G) | repo = account | — |
| A5 | Paste the 23 Oct project instructions as an interim version (2 min; the final version comes in G2) — closes the "deadline as line 1" gap before any new chat | project settings | **Only Erik** (recommended now) |

### B · Audit GW1–10 — ~3 h, session 1 (deliverable: audit page + §6)
| # | Step | Produces | Erik |
|---|---|---|---|
| B1 | `scripts/season_audit.py`: per GW from the snapshots (pre-deadline and post-lockdown) and the API — points, average, GW rank, OR, league position, gap to Alex and to the leader, our captain vs the field's most-captained (delta, cumulative), bench points, autosub losses (0-minute starters), transfers and hits, chips with value vs baseline, LOCKED time vs deadline, executed vs LOCKED | `data/audit/season_gw.csv` + chart data | — |
| B2 | Points attribution per GW from picks × player event points (every GW1–10 is covered by a snapshot taken while that GW was current): premiums (≥ £9.5), captain surplus, club defence blocks, cheap nailed starters, mid-price mids, differentials (≤ 1/9 rivals), bench/chips; leaks: blanks from 0-minute starters, right-club-wrong-player vs teammates, execution gaps | `data/audit/attribution.csv`; GW10 vs the rest: structural or luck | — |
| B3 | Decision ledger: all 26 rows in the process × outcome 2×2; Brier of every EXP; A vs B by type (chip, captain, transfer, XI, bench, execution) — who won, by how much, where; explicit test of "Claude's A is plan-anchored and too cautious" (A-vs-B delta when B was Erik's call; how often A = "keep the plan"; template-ness of A vs B) | tables in §6 | — |
| B4 | Process audit per GW: which rules and steps were followed, skipped, or cost time without return; what demonstrably produced points (minutes gate catches, comparison pages, rule 10, rule 18) and what did not; time spent per chat from timestamps | §6 process table | — |
| B5 | Rivals: Fantasy Fellas top three per GW (captains, chips, transfers, hits), what they did that we missed or rightly avoided; top-10k template and chip timing (LiveFPL if fetchable, else API `most_selected`/`most_captained`/`chip_plays`) | §6 rival table | — |
| B6 | Publish the audit page (artifact: tables and charts) and §6; discuss the five most important findings | artifact + `docs/11` §6 | reads, reacts |

### C · Goals redefined — ~1 h with Erik, session 2 (4 decisions)
| # | Step | Produces | Erik |
|---|---|---|---|
| C1 | Evidence: where 652 pts / OR ~796k sit against the field's pace (points per GW needed for each rank band from here; the 10k target set in August against today's reality) | numbers for the decisions | — |
| C2 | **D-G1** End goal: win Fantasy Fellas (unchanged) + an honest OR band for GW38 | `strategy.md` §1 | **decides** |
| C3 | **D-G2** Sub-goals per phase (GW11–19, 20–26, 27–33, 34–38) with exit criteria | `strategy.md` §8 | **decides** |
| C4 | **D-G3** Weekly leading indicators with thresholds (captain delta vs league, bench points, transfer EV realised vs B, execution score, Brier, model MAE vs `ep_next`) and where they are logged | `strategy.md` §10, log columns | **decides** |
| C5 | **D-G4** Rival of record (Alex vs the leader, now Jason) and rule 18 rewritten on the current standings and chip positions (Jason WC/FH/BB vs our TC1; set 1 expires at the GW19 deadline, Fri 1 Jan 2027 18:30 GMT / 19:30 CET per the API) | `rules.md` 18 + changelog | **decides** |
| C6 | Write `strategy.md` v3.0 (§1, §7, §8, §10) with changelog; retire the E1–E6 edges that the audit grades inverted or insufficient | commit `Strategy Q2 review: goals` | — |

### D · Strategy per horizon, chips, season calendar — ~2 h, sessions 2 and 4
| # | Step | Produces | Erik |
|---|---|---|---|
| D1 | Short horizon: the fixed decision set of every decide chat and the information each decision needs (feeds F) | `strategy.md` §5 rewrite | — |
| D2 | Mid horizon (4–6 GW): fixture blocks GW11–19 per club with team strength, home/away, Europe load (UCL MD5 24/25 Nov, MD6 9/10 Dec; UEL/UECL Thursdays), rotation risk, price trend, FT banking plan | fixture map in the brief template | — |
| D3 | Long horizon: phase map with corrected dates, Christmas congestion (GW17 26 Dec, GW18 Tue 29 Dec, GW19 Fri 1 Jan, GW20 Tue 5 Jan), blanks and doubles verified against cup draws (web, sources), winter rebuild, set 2 | `campaign-plan.md` v2.0 | — |
| D4 | **D-S1** TC1: GW11 Haaland FUL (H) vs GW16 HUL (H) vs GW19 TOT (H), quantified with the captain model from E (distribution, ceiling, league-EO); **D-S2** chip plan v2 for set 2 and the interaction with Jason's chips; **D-S3** when a same-day chip is allowed (rule 17 amendment) | `chip-plan.md` v2 + changelog; `rules.md` 17 | **decides ×3** |
| D5 | Season calendar GW11–38: per GW the week type (roll · one-transfer · chip · WC/FH build · blank/double · midweek · post-break) and what we do; generated from the API deadlines so it follows TV moves | `strategy/season-plan.md` (+ `make_deadlines.py` writes the week type) | confirms |

### E · Models — ~5 h, session 3 (predictive, relevant, on time)
| # | Step | Produces | Erik |
|---|---|---|---|
| E1 | Backtest harness `scripts/backtest_xp.py`: for every GW2–10 run `xp_model.py` on the last pre-deadline snapshot, join actual points from the snapshot taken while the GW was current; MAE and bias overall, per position, per price band, for the top-20 by xP and for the top-5 captain candidates; clean-sheet calibration (predicted P(CS) vs actual); the same for `ep_next` and a naive form baseline | `data/model/calibration_gw02-10.csv`, §6 model table | — |
| E2 | Research with sources (web): how FPL Review, Hub AI, OpenFPL, AIrsenal and the sertalpbilal planner build minutes, finishing, team strength, captain and chip models; which building blocks are free and verifiable (Understat yes, FBref no; FPL-Core-Insights; API `element-summary`) | `docs/09` v0.2 | — |
| E3 | Candidate list with expected utility, cost and *when it runs* (daily snapshot · decide chat · chip/WC weeks only): shrunk G−xG finishing term · team-strength blend that stops discounting top defences · minutes model with Europe-Thursday and injury-return flags · captain model with distribution and ceiling (P(≥ 10), not only the mean) · league-EO-aware captain EV (expected gain vs each rival's likely captain) · chip-timing model (BB bench value and TC value per GW over the horizon) · multi-GW transfer planner with FT banking and hits · fixture ticker · price-change signal from daily `transfers_in/out_event` | ranked list in `docs/09` | reads |
| E4 | Build the top candidates by utility/cost, each tested on GW6–10 against v0; adopt only what measures better; wire into the Action (daily) and the decide chat (on demand) | scripts + `data/model/` + Action step | — |
| E5 | Everything not built becomes a numbered backlog; the review skill gains a weekly model line (our MAE vs `ep_next`) → `data/model_log.csv` | `docs/09` §5 backlog | — |
| E6 | Data layer: the snapshot prune step is a no-op in a fresh checkout (all 94 snapshots survive, 183 MB, ~2 MB/day); policy: keep every pre-deadline and post-lockdown snapshot, prune the rest after 14 days | `snapshot.yml` | — |

### F · The week system — ~2 h, session 4 (several decisions)
| # | Step | Produces | Erik |
|---|---|---|---|
| F1 | **D-W1** Week modes: roll · one-transfer · chip · WC/FH build · blank/double · midweek; per mode the steps, the models, the decisions, the time budget, and what must be LOCKED by when | `docs/12-week-system.md` | **decides** |
| F2 | Fixed agenda relative to the deadline (T−48 h prep · T−24 h decide after the pressers · T−3 h LOCKED and execution check · T+30 min API verification · lockdown + 2 h review prep · review within 48 h) and season moments (bias review every 4th review, quarterly review, chip windows T−7 d) | same document | confirms |
| F3 | **D-W2** Scheduled tasks redesigned as deadline-relative: one daily "FPL dispatcher" that reads the API, computes hours to the deadline and runs the right job (prep, decide brief with a default LOCKED, T−3 h check, verification, review prep, lockdown check) so Friday, Saturday and midweek deadlines all work; push notifications; alternative B: one-shot tasks per deadline | tasks live, first run observed | **decides**; **Only Erik** approves tasks and auto-approval |
| F4 | Google Calendar: per GW "decide", "execute + LOCKED check" and "review" entries from the API deadlines (UK + NL) | calendar GW11–38 | confirms |
| F5 | Default LOCKED safety net: if no decide chat has happened by T−24 h, the task writes a default (roll or forced transfer, flags handled, pool captain, bench order) that Erik can execute from his phone | in the dispatcher prompt | confirms |
| F6 | **D-W3…W6** Rules: 4a (deadline = line 1, LOCKED ≥ 3 h), 4b (every change after LOCKED = one line + screenshot), 17 (same-day chip only after value-vs-plan and minutes gate before activation), 18 (rival = leader); prune rules that never bit (audit decides which) | `rules.md` v4 + changelog | **decides, one per message** |

### G · Skills, project instructions, CLAUDE.md, lean repo — ~2 h, session 5
| # | Step | Produces | Erik |
|---|---|---|---|
| G1 | Rewrite `fpl-gw-decide`, `fpl-gw-review`, `fpl-strategy-review` for the new week system and models; propose a fourth skill if the chip/WC weeks need their own (`fpl-chip-week`); each proposed via the skills card, repo copies identical | cards + `skills/` | **Only Erik** saves the cards |
| G2 | `docs/project-instructions.md` v3 — the contract, pointing at the repo | text to paste | **Only Erik** pastes |
| G3 | `CLAUDE.md` v4 (week system, files, templates, commit messages) | commit | — |
| G4 | Lean repo: `docs/01–05`, `engine/`, the root duplicate of the intelligence stack → `docs/archive/`; README rewritten; the two project docs in the Claude project replaced by `docs/11` and the new instructions | commit | confirms |

### H · Close — 30 min, session 5
| # | Step | Produces | Erik |
|---|---|---|---|
| H1 | What changed in ten lines; what already applies in GW11; the kickoff for the GW11 decide chat; the date of the next review (bias review after GW13; Q3 early March) | last message + `docs/11` §7 | — |

## 3. Session plan (proposal — Erik sets the pace)
| Session | When | Steps | Output Erik sees |
|---|---|---|---|
| 1 | Sun 8 – Mon 9 Nov | A, B | audit page + five findings |
| 2 | Tue 10 Nov (GW10 numbers final after lockdown) | B6 discussion, C, D1–D3 | goals decided, strategy v3.0 |
| 3 | Wed 11 – Thu 12 Nov | E | calibration, built models, backlog |
| 4 | Fri 13 – Sat 14 Nov | D4–D5, F | chip plan v2, season calendar, week system, tasks and calendar live |
| 5 | Sun 15 – Mon 16 Nov | G, H | skills cards, instructions to paste, CLAUDE.md v4, kickoff GW11 |
| buffer | Tue 17 – Thu 19 Nov | first dispatcher run observed (T−48 h for GW11 = Thu 19 Nov 12:00 NL) | — |
| GW11 | Fri 20 Nov (after pressers) · deadline Sat 21 Nov 12:00 NL | GW11 decide chat on the new system | — |

## 4. What only Erik can do
1. Paste the project instructions (A5 interim, G2 final).
2. Save the three or four skill cards (G1).
3. Approve the scheduled tasks and switch them to automatic approval (F3); confirm the calendar entries (F4).
4. Take the decisions marked **decides**: D-G1…G4, D-S1…S3, D-W1…W6 — one per message.
5. Execute in the app and send the screenshot; a change after LOCKED is announced in one line (proposal 4b).

## 5. Definition of done (before the GW11 deadline)
Every step's output committed with `Strategy Q2 review: <part>` · audit reproducible by script · `strategy.md` v3.0, `rules.md` v4, `chip-plan.md` v2, `campaign-plan.md` v2.0, `strategy/season-plan.md`, `docs/12-week-system.md`, `docs/09` v0.2 with calibration · models adopted only with a backtest better than v0 · dispatcher task live with one observed run · calendar GW11–38 · skills saved and identical in the repo · project instructions pasted (Erik confirms) · GW11 kickoff written.

## 6. Audit GW1–10 (v0.2, 9 Nov 2026)
Data: `data/audit/{player_gw,picks_gw,entry_gw,rivals_gw}.csv`, built by `python3 scripts/season_audit.py extract|rivals` from the last snapshot of each GW. Page with charts: https://claude.ai/artifact/CsKNLhxkaVnTCRSbd8kHTM. **GW10 is provisional** (newest snapshot is mid-update: player points give 123, entry history 82); the lockdown check sets the final figure and the GW10 average.

### Findings
1. **Execution, not prediction, is the weak link.** Brier of the 22 forecast EXP lines 0.218 (coin flip 0.25). The 3 "executed as locked" lines: mean p 0.83, 0 of 3 true, Brier 0.70. In every GW6–10 the app differed from LOCKED. Net effect of the deviations was positive (GW6 -4, GW7 +3, GW8 -3, GW9 +8, GW10 +14) which hides the problem.
2. **The league is the yardstick, not the field average.** GW1–9: us +21 vs average (529 vs 508), P4 to P8. Seven of nine rivals scored +27 to +81 (Alex +78, Jason +81). Only Robert (-2) and R.W. (+19) are below us.
3. **Budget starters carry the points.** 652 pts GW1–10: players under £6 gave 250, Haaland incl. captain bonus 138, £6+ others 178+. GW10: budget 42, captain bonus 16 (Barry), Bench Boost 27.
4. **Plan-anchoring test: inconclusive.** 15 measurable A vs B contests: A won 9 (+63), B won 5 (+43), 1 tie. A won structural calls (WC +22, transfer +10, squad +8). B won 4 of 5 scored contests in GW9–10, all tactical (captain, XI, chip timing). Too small for a verdict; track from GW11.
5. **Bench points are not the leak.** GW6–9 bench 36 vs league mean 43 (16 to 63).

### Also graded in step A
GW6 D1–D5 and GW7 D2 closed from the API (commit 18539de). GW6: FH played instead of WC (wrong chip), captain swapped unwritten (-4), GW 59 vs average 58, model said 73.2 xP.

### Not yet done in B
B4 time per chat and B5 template/top-10k comparison; GW10 final after lockdown. Rival picks exist only for GW6–10 in snapshots (GW1–5: histories only).

## 8. Models — E1 backtest (v0.3, 10 Nov 2026)
Harness: `scripts/backtest_xp.py` (last snapshot before each deadline GW2-10, xp_model horizon 1, judged on every player with >= 2 expected points by any forecast; ~220-310 per GW). Output `data/model/backtest_gw.csv`, `backtest_pos.csv`.

| Forecast | MAE | Bias | Spearman rho | Top-10 actual | Top pick actual |
|---|---|---|---|---|---|
| xp_model v0 | 2.23 | -0.05 | 0.34 | 4.50 | 6.33 |
| FPL ep_next | 2.52 | +0.30 | 0.22 | 4.34 | 5.00 |
| Form (naive) | 2.67 | +0.50 | 0.18 | 3.74 | 3.44 |

Findings:
1. **The model beats ep_next and form on every metric**, in 8 of 9 GWs on MAE (GW2 is the exception, 5 games of evidence missing). No position bias worth fixing (all within ±0.2).
2. **Model top pick vs our captain A.** The model's highest-xP player was Mbeumo (GW6), Haaland (GW7-9) and Barry (GW10). Claude's captain A went against the model twice: Mbeumo in GW8 (model: Haaland; A lost 12) and Haaland in GW10 (model: Barry; A lost 14). Both times the B that won was the model's own pick. This is the concrete form of the plan-anchoring finding: **A was anchored to a captain story (sword in GW8, shield in GW10), not to the model.**
3. Rank correlation 0.34 is modest: single-GW points are noisy. The model is good for ranking options, not for promising a score (EXP lines should use ranges).
Next (E3/E4): finishing term (G - xG), defence-strength fix (GW9 De Cuyper), Europe/rotation minutes, captain distribution (ceiling, not only mean).

## 7. Closing summary
_To be written in step H._

## Changelog
| Date | Change |
|---|---|
| 2026-11-08 | v0.1 — programme written after the read-back; nothing decided yet. |
| 2026-11-09 | v0.2: step A1/A3 done, audit B1-B3 written (section 6), artifact published. |
| 2026-11-09 | **D-G1 decided (Erik): A.** Season goal = win league 348280; plus an honest OR band for GW38 set once GW10 is final. GW10 Monday snapshot confirms 123 pts, GW rank 37, OR 806,347 (still data_checked=false). |
| 2026-11-09 | **D-G2 provisional A (Erik said 'continue', no objection):** three exit criteria per phase. Phase 3: no chip expires, execution score >= 90% (app = LOCKED with screenshot), >= P2 in the league at GW19. Phase 4: WC2 on a written rationale, gap to leader <= 25. Phase 5-6: each chip on a verified blank/double, league beats OR. Thresholds are proposals, to be checked against the season-plan. Interim project instructions delivered to Erik in chat (A5). |
| 2026-11-09 | **D-G3 decided (Erik): A.** Six weekly leading indicators: execution score (green >= 90%, red < 70%), captain result vs league sum, bench points 4-week sum <= league mean, Brier of non-execution EXPs <= 0.22, days between written chip rationale and play (>= 1), gap to leader and to Alex (trend). Baselines GW6-10 in section 6. |
| 2026-11-09 | **D-G4 decided: A** (rival of service = leader; rule 18 v3.1). **D-S1 decided: A** (TC1 on a modelled window GW11/16/19, not auto-fired in GW11). |
| 2026-11-09 | **D-S3 decided: A** (rule 17 same-day exception with three checks). |
| 2026-11-09 | **D-W3 decided: A** (rules 4a and 4b added). |
| 2026-11-09 | **D-W2 decided: A (light version, Erik: 'not daily').** Two one-shot scheduled tasks per GW, created by the review chat from the API deadline: T-48h decide prep (push) and deadline+1h verification (push). Created for GW11: trig_018gVy6VnhGgrCxWzxNUsUgc (Thu 19 Nov 12:00 NL), trig_012PsKGZbtZHfMZ9P8dTuY14 (Sat 21 Nov 13:00 NL), both automatic approval. Fallback: Google Calendar 'beslischat openen' at T-24h for GW11-19, created 9 Nov from data/deadlines.csv. The review skill must create the next GW's two tasks (step G). |
| 2026-11-10 | v0.3: E1 backtest done (section 8); dashboard built (Weekly Board), league history cache, scouting reports Alex and R.W. |
| 2026-11-10 | **Standing delegation (Erik, 10 Nov):** 'go on without asking me for input; always do what works best for us; dynamic, content, quality, data-driven; consistency matters; as long as we win the league.' From here Claude takes the recommended option on process, model, dashboard and rule decisions and logs each one here. Still Erik's: transfers, captain, chips and anything irreversible in the game (decided in the GW chats). **D-M1: A** (rule 21, model-default captain). **D-DB4: A** (rival radar, execution block, TC planner on the Weekly Board). |
| 2026-11-10 | **D-S2 (delegated): chip plan v2 draft** for set 2 in chip-plan.md; `strategy/season-plan.md` v1.0 written (GW11-38, predicted blanks GW30/33, doubles GW32/35/36 from one source, to be confirmed on premierleague.com). Three skills proposed via cards (decide, review, strategy). |
