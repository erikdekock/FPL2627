# Weekly Operating Protocol — v2.1
**15 August 2026 · replaces v1.0 and v2.0 (same day) · repo home: `docs/05-weekly-operating-protocol.md`**
The complete weekly operating manual: strategy layer + decision layer + **app execution layer**. Every step timed, every step fed by named information, every in-game action mapped to the actual screen it happens on.

---

## Part 0 — Revision notes: what v1.0 got wrong

v2.0 exists because a critical re-read found real errors, not cosmetic ones. Logged here so the mistakes stay visible:

1. **The vice-captain claim was mechanically false.** v1.0 said a vice who plays *after* the captain "provides no protection if the captain is benched." Wrong: the vice-captaincy resolves at **Gameweek level** — if the captain plays 0 minutes in the GW, the vice's score is doubled regardless of kickoff order. Match order affects what you *know* at the deadline, not how the mechanic works. Corrected guidance: the vice must simply be a nailed starter; kickoff order is irrelevant to the mechanic.
2. **The Session A timing was impossible.** v1.0 scheduled Review at D-5. In consecutive Friday-deadline weeks (GW1→GW2: last match Monday night, lockdown Tuesday 09:00, next deadline Friday 18:30) there is no D-5 — the whole cycle fits in three days. v2.0 anchors Session A to **lockdown + first available moment**, not to a fixed D-day.
3. **The execution layer was missing entirely.** v1.0 described decisions as if executing them were trivial. In reality the app has one irreversible action (confirmed transfers), one classic failure point (unsaved team changes), and an asymmetric chip-cancellation rule. Those mechanics change *when* you should do things, so they belong in the protocol, not in footnotes.
4. **"Claude pulls automatically" overstated current infrastructure.** Automatic repo read/write requires the pushed repo + token in the project instructions — still unconfirmed. v2.0 marks every automation as *conditional on infra*; until then the protocol runs fully manual, which it is designed to do.

---

## Part I — Project state (the read-back, compressed)

| Layer | Status | Where |
|---|---|---|
| Scope, principles, season facts | ✅ Done | `docs/01` |
| Source map (13 weekly info needs) | ✅ Done, one correction pending (FBref → Understat) | `docs/02` |
| Run-up plan to GW1 | ✅ Done, in final week | `docs/03` |
| Scout signal layer + translation filter | ✅ Done | `docs/04` |
| Weekly protocol | ✅ This document | `docs/05` |
| Engine (Project Beane): kickoff prompt + research | ✅ Written, ⏸ not started | `engine/` |
| Repo pushed + token in project instructions | ❌ **Unconfirmed — blocks all automation** | — |
| Team registered, team ID captured, mini-league | ❌ Open | in-game |
| Strategy Q0 (rank target, risk posture) | ❌ Open | `strategy/strategy.md` |
| Final GW1 squad (draft v1 exists, 29 Jul) | ❌ Open — deadline Fri 21 Aug 18:30 UK / 19:30 NL | in-game |

---

## Part II — The week: three sessions + one check (~82 min total)

Deadlines are the anchor; weekdays are illustrative. GW1–3 deadlines: Fridays 18:30 UK (19:30 NL). Later rounds mostly Saturday late morning UK; five midweek rounds.

### Session A — REVIEW · at lockdown + first free moment · 22 min
*Lockdown = 09:00 UK the morning after the round's last match. Never review before it: Opta's post-match check can still move BPS and DefCon.*

A1 · **Score** (3'): points, GW average, GW rank, overall rank, TV, bank. One line.
A2 · **Attribute** (5'): split the result into *good decisions / bad decisions / variance* — name which is which before concluding anything. Which owned player returned, and was it foreseeable at the deadline? Which non-owned player hurt most — was he on the watchlist, and if yes, why did we pass?
A3 · **Calibrate** (5'): compare last week's *written expectation* with the outcome. Where were we confidently wrong? Is a pattern repeating?
A4 · **Squad health** (5'): flags picked up, minutes lost, set-piece/penalty changes, fixture turns → carry into Session B.
A5 · **Write** (2'): one row in `gameweek_log.csv` incl. the one-line lesson; watchlist updates.
A6 · **Rival Radar** (2'): Leagues & Cups → primary rivals' GW score, captain, transfers, chips played. One line into the log; feeds the C2 league rule. Against millions we play percentages; against five rivals we play the people.

### Session B — SCAN · ~D-2 · 15 min
*Estimating only. Nothing is decided, nothing is executed.*

B1 · **Availability** (4'): all 15 + shortlist. Flag percentages fresh or stale? Returning players = bench risk. European/cup midweek? Output: every player tagged **Nailed / Likely / 50-50 / Doubt** in the watchlist — Session C decisions must cite these tags, because minutes are the single biggest determinant of points.
B2 · **Fixtures, this GW + next 4** (4'): who enters a good/bad run; is any swing worth acting on *this* week; blank/double radar (from December).
B3 · **Prices** (3'): predicted rises/falls tonight. Price shifts a move's *timing*, never its *justification* (mechanics in Part IV).
B4 · **Options** (4'): 2–3 candidate moves, each costed, **"roll the FT" always a named candidate**. Which option keeps the most flexibility if something breaks?

### Session C — DECIDE · D-1 evening or D-0 · 45 min
*After the bulk of pressers. The only session where anything is committed. Every commitment: Propose → Challenge → Decide → Log.*

**C1 · Transfers (15')** — Challenge questions, answered out loud:
- Does this make sense in four weeks, or only this week?
- Evidence the incoming player is nailed — name it (minutes trend, presser quote, role). "Looks good" is not evidence.
- Am I reacting to one performance? What did I believe two weeks ago; what specifically changed?
- Hit: expected gain over 4 GWs clearly above 4 points? Close = no.
- What breaks if wrong — recoverable next week, or does it cost a wildcard?
- Standing rules: no premium at a new-manager club without minutes evidence · Arsenal picks pass the neutral-club test · bank-first while the window is open (to 1 Sep).
- Cost of doing nothing? Rolling to 2 FTs is often the highest-value move.
- **Anti-tilt:** after a bottom-decile gameweek, no hit is confirmed within 24 hours without a night's sleep. Chips already carry this rule; hits now do too.

**C2 · Captain + vice (10')**
- Shield week (match the field's EO) or sword week (differentiate)? What does the league position require *now*?
- Floor, not just ceiling — captaincy doubles blanks too.
- Fixture as good as it looks? Opponent's defensive form, not the badge.
- Early vs late kickoff: a Monday captain is chosen blind; price that in.
- Vice: nailed starter, full stop (order irrelevant — Part 0, note 1).
- If the differential captain fails and the template hauls: rank cost survivable?
- **League rule (E6):** ahead of the primary rival → mirror their likely captain unless our edge is clear (deny variance); behind per the strategy trigger → differential captaincy is the first leverage lever, before any transfer.

**C3 · XI + formation (8')**
- Any genuine doubt in the XI? A 75%-flag is usually a bench, not a gamble.
- Formation follows players, not the reverse. Valid shapes: 1 GK, 3–5 DEF, 2–5 MID, 1–3 FWD.
- Same-team stacking: three from one club = one correlated bet — deliberate or accidental?

**C4 · Bench order (4')**
- If exactly one starter misses, who do I *want* on? Order accordingly.
- Bench GK genuinely non-playing?
- (Bench Boost week: order irrelevant — all 15 score.)

**C5 · Chip check (3')** — one line, every week: does `chip-plan.md` say anything about this week, and has the planned reason actually materialised? Reactive chips banned; a chip proposal survives one night's sleep. Count: chips left vs GWs to the 2 Jan cliff.

**C6 · Commit + log (5')** — execute in-app (Part III), write the log row **including the explicit expectation** ("worth ~X points over 4 GWs") that Session A grades next week.

### T-90 — phone check · 90–120 min before deadline · 5 min
New info only; no rebuilding. (1) New injury/presser news since C? (2) Early confirmed lineups contradict anything? (3) Captain still starting? (4) Bench order still right? (5) If changed: **tap Save and see the confirmation**. Then stop.

---

## Part III — The app layer: where each step physically happens

**The map** (site + app share structure; nav from our own account screenshot): **Status** (dashboard: GW points, average, league summaries) · **Pick Team** · **Transfers** · **Points** · **Leagues & Cups** · **Fixtures** (with FDR) · **The Scout** (official articles, team news) · **Stats** (ownership, price changes, form) · Injuries · Help. New for 26/27, verified: the Pick Team, Transfers and Points pages are redesigned with extra viewing options for faster player comparison; an official **Price Change Predictor** appears in-game (live after the GW1 deadline); a skippable squad-building assistant on Squad Selection (browser only); Season History now shows career percentile rankings; leagues/ranks/H2H update live during matches with projected bonus from the 20th minute.

**One-time setup (this week, blocking):**
1. Register squad → confirm → pick team name (**AFC Kopstoot** — have a clean fallback ready; FPL filters names it dislikes) → pick favourite club → done.
2. **Capture the team ID**: open Points or Gameweek history — the URL reads `…/entry/1234567/…`; that number goes into the Claude project instructions and unlocks squad-state pulls via the API.
3. **Leagues & Cups → Create & Join**: create the mini-league *before the GW1 deadline* (scoring counts from the GW the league starts); send the invite code to the cousin. Auto-join links exist (`…/leagues/auto-join/{code}`).

**Session A in the app** (read-only): **Points** — points per player; tap a player's shirt for the event breakdown (bonus, DefCon, BPS detail). Check autosubs at the bottom of the page. **Leagues & Cups** — rival moves. Everything else lives in our own log, not the app.

**Session B in the app** (research, zero commits): **Transfers** page as a research tool — filters by position/club/price, sort by points/form/selected %; the redesigned comparison view replaces tab-hopping. **Stats** for ownership and transfer momentum; in-game price predictor from GW2. **Fixtures** for the FDR grid. ⚠️ House rule: on the Transfers page in Session B, *nothing is ever confirmed* — build shortlists, close the app.

**Session C in the app** (the only commits of the week):
- *Transfers:* Transfers → tap the outgoing player (marked out) → choose incoming from the filtered list → banner shows FTs used / hit cost → **Make Transfers** → confirmation screen: read it fully (FTs consumed, points deduction, bank after) → confirm. **Confirmed transfers are final — there is no undo, and the deadline does not reset them.** This is why execution lives in Session C only. Single exception (Part IV): a planned, >90%-certain move may be executed early in the week to beat a predicted price rise.
- *Wildcard / Free Hit:* activated on the Transfers page before confirming the batch. **Once confirmed with transfers, WC and FH cannot be cancelled.** Triple Captain and Bench Boost (activated on Pick Team) **can** be cancelled any time before the deadline. Sanity-check this asymmetry in-app at first chip use.
- *Captain & vice:* Pick Team → tap player → **Make Captain** / **Make Vice Captain**.
- *XI & bench:* Pick Team → tap player → **Substitute** → tap the swap partner. Formation adjusts automatically within valid shapes.
- *The Save trap:* captain, vice and substitutions **do not persist until "Save Your Team" is tapped and the confirmation appears.** The classic FPL self-inflicted wound is a captain change made, admired, and never saved. Every Pick Team visit ends with Save + visual confirm — including at T-90.

**During matches** (no actions): Points page runs live — league positions, overall rank and projected bonus (from 20') update in real time. Entertainment, not input. Nothing is final until lockdown at 09:00 next morning; Session A waits.

---

## Part IV — Mechanics that change decisions (validated)

- **Autosubs** resolve at Gameweek end, in bench order, only for starters with 0 minutes, and only if a legal formation results; GK swaps only with GK. Design the bench for the *likely* failure, not the nightmare.
- **Vice-captaincy** transfers only if the captain plays 0 minutes in the whole GW; kickoff order irrelevant.
- **Transfers are final once confirmed**; team-sheet changes (captain, XI, bench) are editable until deadline *if saved*.
- **Prices** move overnight (~01:30–02:30 UK), ±£0.1m on net transfers; you keep 50% of profit on selling. Locked until the GW1 deadline. Trade-off rule: information beats £0.1m, except for a planned move already decided on evidence — then beat the rise.
- **Chips:** one per GW · no FH in GW1 · FH in GW19 blocks FH in GW20 · first set dies at the GW19 deadline (13:30 GMT, 2 Jan) · WC/FH irreversible once confirmed, TC/BB cancellable pre-deadline.
- **Lockdown 09:00 UK next morning:** full-time scores are provisional (Opta review moves BPS/DefCon). Never grade a week early.
- **11 position reclassifications** this season — the launch audit screens them; reclassified players are recurring value.
- **Deadline:** 90 minutes before the round's first kickoff; no grace period. Whatever was last *saved* is what plays.

## Part V — Information map (per step)

| Step | Needs | Source | When |
|---|---|---|---|
| A1–A2 | Final points, bonus, DefCon, autosubs | FPL Points page / API — post-lockdown | ≥09:00 UK next day |
| A3 | Last week's written rationale | `gameweek_log.csv` | instant |
| B1 | Injuries, flags, returns | Premier Injuries · FPL flags | firm by D-1 |
| B2 | Fixtures + FDR next 4–6 | FPL Fixtures / API · tickers | weekly |
| B3 | Price predictions | LiveFPL prices · in-game predictor (from GW2) | nightly |
| B4 | Per-90s, xG | Understat (**not FBref** — Opta licence lost Jan 2026) | post-lockdown |
| C1 | Transfer trends, ownership | FPL Stats / API · LiveFPL | D-1 |
| C1–C3 | Pressers, predicted lineups | BBC live team news · PFT · FF Pundit · FFScout | D-2 → D-0 |
| C2 | Top-10k EO, captaincy meta | LiveFPL | D-1 |
| C5 | Chip windows | `strategy/chip-plan.md` | weekly |
| Scout radar | Signings, role changes | Critchley · Mattinson · Transfers Podcast (filter in `docs/04`) | 1 line/week |

*Automation status: API pulls and repo write-backs activate only once the repo is pushed and the token sits in the project instructions. Until then every row above is a manual check — the protocol is built to survive that.*

## Part VI — Special cases

- **Friday deadlines (GW1–3):** B → Wednesday, C → Thursday evening; accept a lower presser count rather than deciding at 18:00 Friday in a rush.
- **Midweek rounds (×5):** B+C merge into one 30' block the evening before; do the open Session A briefly anyway.
- **GW1 specifically (this week):** no Session A. C = Thursday 20 Aug evening (first pressers) + T-90 Friday ~17:45 NL. Squad final except captain/bench by Thursday night.
- **Post-break (GW6):** mini pre-season — weight recent evidence lower; the field overreacts, we don't.
- **Travel weeks (if any arise):** C moves earlier; two local-time alarms; T-90 non-negotiable.
- **Blanks/doubles (from Dec):** extra B-step — verify who actually has a fixture, and how many.

## Part VII — The 10-minute week (legitimate, not failure)

1. Flags on the 15 → bench/replace anyone out (3') · 2. Roll the FT unless someone's unavailable (1') · 3. Captain the highest-owned premium at home (2') · 4. Bench order (2') · 5. Save + confirm; log "reduced week, rolled FT" (2').

## Part VIII — Written every week, no exceptions

`gameweek_log.csv` (one row incl. lesson + stated expectation **+ the most-captained player and his points** — the weekly E3 benchmark) · `watchlist.csv` (status changes + minutes tags) · `chip-plan.md` (only on window shifts/fires) · commit `GWxx: <moves|roll>, C:<captain>`. **The log row is unskippable, including 10-minute weeks.** Two consecutive 10-minute weeks trigger a simplification review at the next session — the answer to overload is a lighter protocol, never a dead one. By ~GW10 this log is a calibration dataset about our own judgement — the one asset no subscription sells.

*Changelog: v2.0 — 15 Aug 2026. Corrected vice mechanic and Review timing; added execution layer (transfer finality, Save trap, chip asymmetry, team-ID capture, 26/27 UI changes); marked automation conditional on infra; tightened throughout.*
*Changelog: v2.1 — 15 Aug 2026, perspective round. Added A6 Rival Radar and the C2 league rule (opponent perspective, strategy E6); minutes tags in B1 (points-engine perspective); anti-tilt hit rule in C1 (operator perspective); unskippable log row + field-captain benchmark columns (measurement + pre-mortem perspectives). Each amendment traces to an edge in `strategy/strategy.md`. Next revision: after GW3, with three real weeks of friction behind it.*
