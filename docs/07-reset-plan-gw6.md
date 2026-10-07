# Reset Plan — WC1 at GW6
**v0.1 · Wed 7 Oct 2026 11:30 NL · owner: Claude (project manager), decisions: Erik · living document — updated after every step**

**Deadline GW6: Sat 10 Oct 2026, 11:00 BST = 12:00 NL** (first kickoff Arsenal–Leeds 13:30 NL). Lockdown GW6: Tue 13 Oct 09:00 UK (Monday game Coventry–Newcastle). Next: GW7 deadline Sat 17 Oct 11:00 BST / 12:00 NL.

**Phase:** 2 Reset & Structure (GW6–10). We enter it with the Q1 review unheld and the WC squad unbuilt, so the reset runs in three days instead of three weeks. The plan below is sized for that.

**Rules in force for this reset:** chips fire only from written, slept-on rationale (WC rationale written Thu, confirmed Fri, fired Fri evening or Sat morning) · no player in the 15 without minutes evidence · every differential has a one-line thesis + exit condition in `data/watchlist.csv` before the deadline · plan ≠ executed until the API confirms it · league beats overall rank in any conflict.

---

## Status board

| # | Step | When (NL) | Owner | Status | Output |
|---|---|---|---|---|---|
| 0 | Inventory & diagnosis | Wed 7 Oct | Claude | ✅ done | `docs/06-retro-phase1-gw1-5.md`, log rows GW1–5 backfilled, this plan |
| 1 | Way of work v3 — decide the operating changes | Wed 7 Oct (today) | Erik decides D1–D2 | 🟡 proposal written | `docs/08-operating-system-v3.md` (the learning loop; project-instructions text in §7.1); `CLAUDE.md` rewrite follows acceptance |
| 2 | Chip plan v1 — WC1 rationale written, TC1/BB1/FH1 re-windowed | Thu 8 Oct morning | Claude drafts, Erik reads | 🔲 | `strategy/chip-plan.md` v1 with log entry |
| 3 | Strategy amendments v2.2 (not a full rewrite) | Thu 8 Oct morning | Claude drafts, Erik decides D3–D5 | 🔲 | `strategy/strategy.md` changelog entry |
| 4 | WC squad build v0.1 — three structures, candidate pool with minutes evidence | Thu 8 Oct afternoon | Claude | 🔲 | `strategy/wc1-squad.md` v0.1 + watchlist theses |
| 5 | Erik's review of v0.1 → v0.2 | Thu 8 Oct evening | Erik | 🔲 | feedback in chat |
| 6 | Pressers, injuries from the break, predicted XIs, Rival Radar → squad v1.0, captain/vice, XI, bench | Fri 9 Oct 14:00–18:00 | Claude | 🔲 | `strategy/wc1-squad.md` v1.0 |
| 7 | Sleep rule + final go | Fri 9 Oct evening | Erik decides D6 | 🔲 | "GO" in chat |
| 8 | Execute in app: Wildcard → 15 → C/VC → bench → Save → screenshot | Sat 10 Oct 09:30–11:15 (hard stop 11:45) | Erik; Claude checks screenshot | 🔲 | saved team confirmed |
| 9 | Post-deadline verification against the API; GW6 log row (pre-result) | Sat 10 Oct 12:05 | Claude | 🔲 | commit `GW06: WC1, C:<name>` |
| 10 | GW6 review after lockdown; WC1 graded vs baseline; TC1 decision for GW7 | Tue 13 Oct | Claude + Erik | 🔲 | log row complete, chip-plan log |

---

## Step detail

### Step 1 — Way of work v3 (today, 20 min)
Why first: the squad build runs on these rules, and the retro shows the old protocol was never run. Proposed changes (each a yes/no for Erik):

- **Claude writes the repo.** This session has push access through Erik's GitHub connection. Log rows, watchlist, chip-plan log and docs are committed by Claude at the end of every GW chat. The "paste this" fallback is retired (it fired 0 times in 5 weeks).
- **LOCKED close-out.** Every GW chat ends with one message: transfers (as executed), chip, captain/vice, XI, bench order, bank, EXP. If that message does not exist, nothing was decided. After each deadline Claude verifies the actual state from `/entry/6756883/event/{gw}/picks/` and `/transfers/` and writes it into the log — the GW4 failure cannot recur silently.
- **Minutes gate before ranking.** No player reaches a recommendation, the 15, or the XI without minutes evidence (started last match or confirmed by presser/predicted XIs). A flagged starter with no playing substitute is a transfer or a bench decision, never a hope.
- **Bench rule.** Three playing outfield bench players at all times; the GK pair may include one true non-player. Budget consequence accepted.
- **One-page protocol** replaces the 82-minute three-session week: **Review** (Tue/Wed after lockdown, 15 min: grade EXP, one lesson, log row committed) · **Decide** (Thu or Fri, 30–45 min: data pull by `git clone` + API via web fetch, transfer A/B, captain, XI, chip line, EXP, LOCKED) · **T-90** (5 min, flags and captain only). `docs/05` is archived, not deleted.
- **Rival Radar automated.** `fpl_pull.py` gains the nine rivals' `/history/` and `/event/{gw}/picks/` (reachable, proven 7 Oct). Rival of record: **Alex** (primary), Jason and Thomas (chasing pack).
- **Chat hygiene.** One chat per GW named `GWxx`, opened Tuesday, closed with LOCKED. Reviews and quarterly work get their own named chat (`Strategy Qx`), dated in the calendar — the unheld Q1 review is the proof that a date in a document is not a meeting.

### Step 2 — Chip plan v1 (Thu morning)
- **WC1 → GW6 (recommendation A, confidence high).** Rationale to be written in `chip-plan.md`: 19% dead money, two long-term injuries sold already, a bench that cannot play, four weeks of new-manager evidence, and the GW6–12 fixture map. Alternative B (defer to GW7 for one more week of post-break evidence) costs a week of dead money and buys information everyone else already has — not recommended.
- **TC1.** Original plan GW7, Haaland H Ipswich (Ipswich 11 conceded, 0 clean sheets). Still statistically the best single fixture in H1 for a £15.6 player — but Haaland is at 7.8 ppg and City's FFP sanction is pending. Options to write up: (a) GW7 as planned if Haaland is in the WC squad and fit; (b) hold for GW11 (H Fulham) / GW16 (H Hull) with more information on the sanction; (c) TC on Bruno H vs a promoted side instead. Decision at Step 10, not now — TC is cancellable, WC is not.
- **BB1** window GW8–12 stands, conditional on 15 playable players (which the WC must deliver). **FH1** burn GW17–18 stands. All set-1 chips expire at the GW19 deadline — **Fri 1 Jan 2027 18:30 GMT per the live API** (the founding docs say Sat 2 Jan 13:30; the API wins, to be re-verified).

### Step 3 — Strategy v2.2 (Thu morning)
A dated changelog entry, not a rewrite: dead-money rule (§6.7 bench philosophy replaced), the league-chase trigger declared live (−69 to Alex), captain-pool review under City uncertainty, "cheapest nailed scorer at the right club" as the countermeasure to the named bias, log ownership moved to Claude. Full Q1-style review of the six edges is scheduled as its own chat after GW6 (`Strategy Q1`, w/c 12 Oct).

### Step 4 — WC squad build v0.1 (Thu afternoon)
Inputs: Thursday's snapshot (GitHub Action ~12:00 NL) + live bootstrap via web fetch · fixtures GW6–12 · Understat xG/xA (not FBref) · international-break minutes (who played four matches) · ownership/EO for template vs differential decisions · rivals' GW5 squads.
Budget: **£99.7** (team value at selling prices incl. £0.1 bank — verify in the app under Wildcard before building).
Deliverable: three structures costed to the pound, each with 15 playing players and ≥ £0.3 bank —
- **A. Two anchors** (Haaland + Bruno) with a value spine;
- **B. One anchor** (Haaland) and the money spread into the £5.5–8.5 band where the points are (Groß, Schade, De Cuyper, Bogle, Tarkowski, Tzolakis class);
- **C. No Haaland** — on the table because Erik asked for it; graded honestly against A/B on captaincy EV and league-EO (Haaland is 73.9% owned and the field's captain every week, so dropping him is a sword move that needs a written thesis).
Plus 2–3 differential candidates with thesis + exit, and the GW6 captain question (Haaland away at Liverpool, Sunday 16:30 BST, vs Bruno home to Spurs, Saturday 17:30 BST).

### Step 6 — Friday: information at maximum
Thursday/Friday pressers (Maresca, Slot, Arteta, Carrick, De Zerbi, Frank, Farke, Hull), Premier Injuries, BBC, FFScout predicted XIs, international-return status for every candidate · Rival Radar (Alex's GW5 picks and chip status; Billy and Thomas just wildcarded — their squads show the local template) · final squad v1.0, captain/vice (vice = nailed starter, kickoff order irrelevant), XI, bench order.

### Step 8 — Saturday execution
Erik, in the app, in this order: **Transfers → Play Wildcard → confirm** (irreversible) → make all changes → confirm transfers → **Pick Team** → captain/vice → bench order → **Save Your Team** → wait for the saved confirmation → screenshot to Claude. Claude checks every name, C/VC, bench order and bank against v1.0 before 11:45 NL. Nothing new after 11:45. Saturday lineups (12:30 BST kickoff) come after the deadline for everyone.
If Erik cannot be at the app Saturday morning: execute Friday 21:00–23:00 NL after the pressers; prices do not matter under a Wildcard.

### Step 9 — Verification
Claude pulls the GW6 picks and transfers at 12:05 NL and writes the pre-result log row: transfers out/in (all), chip `wildcard`, captain, vice, bank, TV, EXP. Commit `GW06: WC1, C:<captain>`. Any mismatch with v1.0 is logged as a lesson, not fixed (it cannot be).

---

## Decisions for Erik

| # | Decision | Options | Claude's rec | Needed by |
|---|---|---|---|---|
| D1 | Claude writes the repo directly (log, watchlist, chip-plan, docs, snapshot script) | yes / no | yes — the alternative produced zero rows | today |
| D2 | Protocol v3 one-pager replaces the three-session protocol | yes / keep v2.1 | yes | today |
| D3 | WC1 fires in GW6 | A: GW6 · B: GW7 | A, high confidence | Fri evening (written Thu) |
| D4 | Haaland in the WC squad | keep / sell | to be argued in Step 4 with numbers; default keep (captaincy EO) | Fri |
| D5 | Differential budget for the WC squad | 2 / 3 slots | 2, each with thesis + exit | Fri |
| D6 | Final GO on squad v1.0 | go / change | — | Fri evening |
| D7 | Saturday execution window | Sat 09:30–11:15 NL / Fri evening | Sat morning if available | Thu |
| D8 | Rival of record | Alex (primary), Jason + Thomas (pack) | as stated | Thu |

## Definition of done (Sat 10 Oct 12:00 NL)
Wildcard active · 15 players, all with minutes evidence · ≥ £0.3 bank · captain + nailed vice · bench order set · "Your team has been saved" seen · screenshot checked by Claude · API-verified at 12:05 · log row committed · chip-plan log entry written · 2–3 watchlist theses committed.

## Risks
| Risk | Mitigation |
|---|---|
| Late injury news from the international break on Saturday morning | three playing bench players; T-90 scan at 10:30 NL; execution window ends 11:45 |
| Erik unavailable Saturday morning | Friday-evening execution (prices irrelevant under WC) |
| Haaland captain blind at Anfield (Sunday) | captain decision EO-aware on Friday; vice nailed; TC untouched |
| Data plumbing eats the session again | `git clone` of the repo (one command) + API via web fetch — both proven today |
| Reset becomes a 3-hour chat with no LOCKED message | Step 7 is a one-word decision; Step 8 is a checklist; both are time-boxed |
| City sanction lands mid-build | FPL points unaffected by a points deduction; squad built with ≤ 2 City players unless the numbers say otherwise |
