# Phase 1 Retro — GW1–5: results, decisions, process
**v0.1 · Wed 7 Oct 2026 · written by Claude for Erik's review · companion to `docs/07-reset-plan-gw6.md`**

Sources: FPL API via repo snapshots (46 daily snapshots 23 Aug – 6 Oct; GW-final states taken from the last snapshot before each next deadline), live league standings and all nine rivals' `/history/` endpoints pulled 7 Oct 09:15 UTC, and the five gameweek chats (First selection, GW02, GW03, GW04, GW5) plus the Project Setup and Strategy-review chats. Where a chat and the API disagree, the API wins.

---

## 1. Scoreboard

| GW | Pts | Avg | Δ avg | GW rank | OR after | League pos | League GW rank | Captain (×2) | Field C | Bench pts | FTs |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 64 | 50 | +14 | 1.14M | 1.14M | 4 | 4/10 | Haaland 2 (4) | Haaland 2 | 0 | 0 |
| 2 | 92 | 81 | +11 | 2.82M | 1.44M | 4 | 5–6/10 | Haaland 13 (26) | Haaland 13 | 0 | 1 |
| 3 | 36 | 51 | −15 | 9.72M | 3.33M | 5 | 10/10 | Haaland 9 (18) | Haaland 9 | 1 | 1 |
| 4 | 68 | 69 | −1 | 5.57M | 3.72M | 6 | 8/10 | Haaland 9 (18) | Haaland 9 | 0 | 0 |
| 5 | 50 | 48 | +2 | 4.65M | 3.57M | 6 | 4/10 | Haaland 6 (12) | Haaland 6 | 0 | 2 |
| **Σ** | **310** | **299** | **+11** | | **3.57M** | **6/10** | | **78 (25% of total)** | Δ = 0 | **1** | **4, 0 hits** |

Team value 100.0 → 99.7 · bank £0.1 · chips used: none (all four first-half chips intact).

### KPI scoreboard vs `strategy.md` §10

| KPI | Target | Actual GW1–5 | Verdict |
|---|---|---|---|
| Deadline misses / unsaved teams | 0 | 0 missed deadlines; **1 planned transfer never executed (GW4)** | ❌ system failure by the KPI's own definition |
| GW score ≥ average | ≥ 60% of GWs | 3/5 (60%) | ⚠️ met on the line; GW3 bottom-decile |
| Overall rank trajectory | ~500k at Q1 | 3.57M | ❌ off by ~7× |
| Gap to primary rival | positive at Q2 | −69 to Alex (P1), −32 to P2 | ❌ "league chase" trigger (>30 behind) has fired |
| Captain vs most-captained (cum.) | ≥ 0 | 0 (mirrored every week) | ✅ mechanically; zero leverage attempted |
| Hits | each clears 4-GW EV | 0 hits | ✅ |
| Bench points wasted | reviewed | 1 point in 5 GWs — the league's lowest by far (rivals 30–80) | ⚠️ not efficiency: the bench never plays |
| Chips | 0 unplanned fires | 0 fired, 4 intact | ✅ the one edge actually realised |
| Decision quality (E4) | process share rising | **no graded decisions on record** | ❌ |
| Log completeness | 5/5 rows | **0/5** | ❌ pre-mortem #1 fired in week 1, not October |

---

## 2. The league: Fantasy Fellas after GW5

| Pos | Manager | Pts | Gap | OR | Chips used | FTs / hits | Bench pts | TV | Read |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Alex (Øde Toilette) | 379 | — | 90k | BB1 GW1 · TC1 GW3 | 5 / 1 | 45 | 101.3 | **Primary rival.** Optimizer: fires field-consensus chips early, captains situationally (Bruno GW2), TV +1.3. Holds WC1 + FH1. |
| 2 | Jason (TRAMAMPOLINE!) | 342 | −37 | 1.13M | none | 4 / 0 | 63 | 100.6 | Patient template; all four chips intact — the quiet threat for H2. |
| 3 | Thomas (Cala-fornication) | 336 | −43 | 1.47M | BB1 GW1 · WC1 GW4 | 3 / 0 | 51 | 100.9 | Two chips gone already; holds TC1 + FH1. |
| 4 | Richard (Buntingford Sensible) | 327 | −52 | 2.10M | none | 3 / 1 | 29 | 100.4 | 36 in GW1, 66 in GW5 — rising; all chips intact. |
| 5 | Billy (EZPeasy…) | 311 | −68 | 3.45M | WC1 GW5 | 3 / 0 | 37 | 100.2 | Just wildcarded. |
| **6** | **Erik (Brobbeytrap)** | **310** | **−69** | **3.57M** | **none** | **4 / 0** | **1** | **99.7** | |
| 7 | Kelvin (Heshy's Summer) | 303 | −76 | 4.21M | BB1 GW1 · TC1 GW3 | 4 / 0 | 61 | 99.8 | |
| 8 | Lawrence (Ecuadorian Derrière) | 297 | −82 | 4.77M | BB1 GW1 | 4 / 0 | 63 | 100.1 | P1 after GW1, falling. |
| 9 | Robert (CCW fc) | 275 | −104 | 6.67M | WC1 GW3 | 5 / 2 | 73 | 100.7 | |
| 10 | R.W. de Kock (Barfightlona) | 270 | −109 | 7.01M | TC1 GW3 · WC1 GW4 | 3 / 0 | 49 | 100.2 | Cousin; two chips gone. |

Erik's weekly score vs Alex: 64/69 · 92/112 · 36/50 · 68/104 · 50/48 — beaten in four of five weeks, by 20 or more twice (GW2 −20, GW4 −36).

**Chip map:** four managers (Thomas, Billy, Robert, R.W.) have already burned WC1; five have burned BB1 and/or TC1. Only Erik, Jason and Richard hold all four. That is the single real structural advantage Phase 1 produced, and the reset spends one of them.

---

## 3. Decision ledger — process × outcome

Grades: **GP/GO** good process & outcome (repeat) · **GP/BO** variance (repeat anyway) · **BP/GO** luck (flag, don't repeat) · **BP/BO** fix the process.

| # | GW | Decision | How it was made | Outcome | Grade | Lesson |
|---|---|---|---|---|---|---|
| 0a | 1 | Initial 15 incl. Steele (4.0 GK), Keane (5.0), Hughes (4.5) as "insurance" bench; Senesi (6.0) as Spurs starter | Deep multi-source verification of the XI; bench bought as insurance but **not** against the archetype-E rule "play actual minutes" (Keane behind Branthwaite, Hughes at congested Palace) | Keane 0 min, Hughes 29 min, Steele 0 min all season; Senesi 90 min then dropped by Spurs. **£19.0 (19% of budget) returned 5 points in five weeks** | BP/BO | A bench that cannot play is not insurance; it is a guaranteed zero behind every flag. Minimum: three playing outfield bench players. |
| 0b | 1 | Porro → Calafiori at T-1 day (Porro confirmed not in squad) | Presser-level check caught a confirmed zero | Calafiori 29 pts, 50% owned | GP/GO | Presser-level verification before the deadline works — keep it. |
| 0c | 1 | Calvert-Lewin → Brobbey at the deadline, outside the chat's analysis | Name pick (team name) without a written thesis | 24 vs 22 — a wash; Brobbey's 17 in GW5 is the season's top single score so far | BP/GO | Unwritten deadline swaps are exactly what the strategy bans. Luck, flagged. |
| 0d | 1 | Watkins held through the Al-Hilal saga (tripwire: official confirmation only) | Rule applied as written | Watkins 0 min → Davis autosub (2); Watkins left the league | GP/BO | Tripwire logic fine; the real error was buying an active transfer saga in a 15-player squad with no spare slot. |
| 1 | 2 | Watkins → João Pedro, executed 17:32 on deadline day, deviation written afterwards | Triggered (player sold abroad); Rule 1 (bank-first to 1 Sep) and Rule 8 (write before acting) both breached, logged post hoc | JP 33 pts, template anchor | GP-ish/GO | Triggered transfers are allowed in Phase 1; the sequence breach cost nothing here but was the first "we don't actually follow the written rule" data point. |
| 2 | 2 | Captain Haaland (13 → 26) with Bruno as VC (23) | Pool default, field-EO shield logic | Alex captained Bruno (46) and gained 20 in one week | GP/BO | In a 10-man league the shield is league-EO, not field-EO. Written down in GW2; never applied since. |
| 3 | 3 | Ndiaye → Elanga on "predicted bench" at City | Single source, no corroboration | Ndiaye started all three; Elanga 1 pt, then injured 6–8 weeks; sold again GW5 (FT burned twice) | BP/BO | Predicted bench ≠ confirmed bench without injury/quote/suspension. Written down in GW3. |
| 4 | 3 | TC held while 1.79M fired it on Haaland (9 pts) | Threshold not met (FPL xP 7.5) | −9 vs the field | GP/BO | Correct hold; do not relearn. |
| 5 | 3 | Senesi benched for Davis after 5/6 sources | Minutes evidence | Correct — but it moved the dead player to the bench instead of selling him | GP/GO | Benching a non-player fixes the week, not the squad. |
| 6 | 4 | **Collins → Bogle recommended and agreed; never executed** | Chat ended Thu 10 Sep with "confirm tonight"; no confirmation, no API check, T-90 missed a 25%-flagged starter | Collins 0 min in the XI, Elanga 0 min (Hughes autosub 1) → **effectively nine and a half men**; Bogle 15 that week | **BP/BO — the worst process failure of the block** | Plan ≠ executed unless the API says so. Every GW chat ends with a LOCKED message; Claude verifies post-deadline against `/transfers/` and `/picks/`. |
| 7 | 5 | Collins → Egan + Elanga → Gibbs-White, deadline day, two FTs | Model rebuilt mid-session after Erik caught fixture-weighting errors; first recommended XI contained Senesi + Keane (0 min) — corrected | Egan 1, Gibbs-White 2; EXP (GW + Wissa ≥ 10) failed | ⚠️ mixed | A recommendation with 0-minute players in the XI should never reach Erik. Minutes gate before ranking. |
| 8 | 5 | João Pedro (75% knee flag, Sunday) kept in the XI with no playing sub | Flag accepted, bench empty | JP 0 min, no autosub → ten men again | BP/BO | Flag + late kickoff + empty bench = structural zero. The bench rule (0a) is the fix. |
| 9 | 5 | Haaland (C) at home to Sunderland | Pool default | 6 pts; field identical | GP/BO | — |
| 10 | break | **Q1 review (21–24 Sep) not held; no WC squad built; no chat 18 Sep → 7 Oct** | — | The reset now happens in three days instead of three weeks | BP/— | The calendar in `campaign-plan.md` had this as "the set piece of the season". A dated review needs a dated chat. |

**Roads not taken, same decision points, as named in the chats:** Bogle over Collins in GW4 (+15); holding Ndiaye over buying Elanga (+4, two FTs saved); TC GW3 (+9). "Right club, wrong player" over five weeks: Verbruggen 23 vs De Cuyper 38 / Vušković 32 (BHA) · Stach 27 vs Bogle 42 (LEE) · Collins 10 vs Janelt 28 (BRE) · Elanga 18 vs Barnes 28 (NEW) · Keane 0 vs Tarkowski 43 (EVE) · Hughes 2 vs Mitchell 24 (CRY). Every scorer was cheaper and less owned. The bias is real and it is a selection bias, not a luck story.

---

## 4. Structural diagnosis — why 3.57M

**A. Dead money (the primary cause).** Four of fifteen never played: £19.0 bought 5 points. The squad was a 12-player squad with a 15-player budget from GW1, and became an 11-player squad in GW2 when Spurs dropped Senesi. Every injury flag thereafter was a certain zero (GW4 ×2, GW5 ×1). Rivals banked 30–80 bench points; we banked 1 — not because we were efficient but because there was nothing there.

**B. The execution loop was open.** Decisions were made in chat and assumed executed. GW4 proved they weren't. No chat ever closed with a verified state; two chats ended with questions to Erik that were never answered (GW04: transfer confirmation + Rival Radar; GW5: none of the "paste these" blocks were pasted).

**C. Nothing persisted.** `gameweek_log.csv` 0 rows (rows were drafted in GW02, GW03, GW04 and GW5 chats and never pasted), `watchlist.csv` empty, `chip-plan.md` still v0, `strategy.md` unchanged since 15 Aug, no Q1 changelog. Edge E4 (calibration compounding) therefore produced nothing, and every chat re-derived context from scratch. Root cause: the write token was revoked after setup and the "Erik pastes" fallback never fired once. *Resolved 7 Oct: this session has push access to the repo through Erik's GitHub connection; Claude writes the log itself from now on.*

**D. Selection bias — right club, wrong player.** Named in GW3, repeated in GW5 (Egan over Tzolakis/Ajayi at Hull). Pattern: we pick the *known name* at the right club rather than the *cheapest nailed scorer* there.

**E. Posture never materialised.** "Calculated aggression, 2–3 differentials with written theses": zero written theses, zero off-pool captains, zero league-EO captaincy decisions after the GW2 lesson. The aggression was all in the documents.

---

## 5. Way-of-work audit — protocol vs reality

| Protocol element (`docs/05`, `CLAUDE.md`) | What actually happened | Verdict |
|---|---|---|
| Three sessions/week (Review 22' · Scan 15' · Decide 45') + T-90 | One long chat per GW (GW5: deadline day only), no separate review sessions, T-90 missed a flagged starter in GW4 | ❌ never run as designed |
| Session A review after lockdown, process × outcome grading | Reviews happened inside the next GW chat, ungraded, unlogged | ❌ |
| Log row every week, EXP stated and graded | Drafted 4×, committed 0× | ❌ |
| Rival Radar weekly | Asked once (GW04) as a manual app check; never answered; rival data not in snapshots | ❌ (fixable: rival `/history/` and `/picks/` are reachable, proven 7 Oct) |
| Chip check one-liner | Present in most chats | ✅ |
| Hits need written EV | 0 hits | ✅ |
| Deviation written before acting | GW2 breached, GW1 deadline swap unwritten | ❌ |
| Data pull first | Done, but at enormous cost: snapshot filename scanning with 150 parallel curls, tarball downloads, broken `ep_next` discovered mid-session | ⚠️ plumbing ate the session; `git clone` of the public repo works in one command (proven 7 Oct) |
| Quarterly review Q1 21–24 Sep | Not held | ❌ |
| 150 KB of founding documents | Read at chat start, cost context every week, rarely acted on | ⚠️ over-specified for the capacity to run it |

**Net:** the strategy's own pre-mortem predicted this failure (#1 log dies, #5 locked squad meets injuries, #6 protocol abandoned not simplified). The diagnosis was in the document on 15 August; the countermeasures were never operated.

---

## 6. What to keep

- **All four chips intact** — fire WC1 now from a written rationale (`chip-plan.md`), keep TC1/BB1/FH1 scheduled, never reactive.
- **Zero hits, zero missed deadlines** — the E1 floor held where it was mechanical.
- **Presser-level verification before the deadline** (Porro catch) and **"predicted bench needs a second signal"** (Ndiaye lesson) — both proven.
- **The Hull read** (Tzolakis 34, Ajayi 27, Egan 26 at £4.1–4.7) was called correctly in GW3 — the squad just didn't act on it until GW5 and then bought the lowest scorer of the three.
- Erik's instinct caught two real model errors in GW5 (Bogle's fixture run, Tavernier's) — the human-in-the-loop step works; it needs a cleaner model to argue with.

---

## 7. Open questions the reset must answer (see `docs/07-reset-plan-gw6.md`)

1. **WC1 budget:** £99.7 at selling prices. Constraint: 15 players with real minutes, ≥ £0.3 bank, no "insurance" that cannot start.
2. **Haaland:** 39 pts (7.8 ppg) at £15.6 in a low-scoring season; City 5/5 on the pitch but guilty on the FFP charges (verdict 2 Oct, sanction pending, Maresca exit talk). Anchor, or spread the money? And is TC1 on Haaland H Ipswich (GW7) still the plan, or does TC move to a later, cleaner window?
3. **Bruno:** 31 pts, one haul, £11.9 — the second anchor has not been an anchor.
4. **Structure:** where the points actually are this season — Groß 47 (£5.9), Tarkowski 43, Bogle 42, Schade 39, De Cuyper 38, Tzolakis 34 — value band and defence, not premiums. How many premiums does a 15-playing-player squad afford?
5. **League position:** 69 behind Alex with 33 GWs left → the "league chase" trigger is live: captaincy leverage and 2–3 written differentials, inside a template core. Which differentials, and against whom (Alex holds WC1+FH1; Jason holds everything)?
6. **Repo & tooling:** log written by Claude via git (now possible) · rival `/history/` + `/picks/` into `fpl_pull.py` · post-deadline verification step · one-page protocol v3 replacing the 82-minute three-session week.
7. **Chip plan v1:** rewrite windows with the FFP uncertainty, the GW19 cliff (set-1 chips die at the GW19 deadline, Fri 1 Jan 2027 18:30 GMT per the live API — not Sat 2 Jan as the founding docs say) and BB1 needing 15 playable players.
