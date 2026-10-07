# Standing rules — read first in every chat
**v3.0 · 7 Oct 2026 · operational rules only; the theory lives in `strategy.md`. Changed only in a review chat, with a changelog line. Each rule names its origin.**

## Process
1. **Read-back before analysis.** Every chat opens with the repo state in five lines plus what it could not find. *(Origin: Phase 1 — every chat re-derived context from zero.)*
2. **Nothing counts until it is committed.** Claude writes and commits log, decisions, brief, lessons; Erik never pastes. *(Origin: 0 of 5 log rows in Phase 1.)*
3. **LOCKED closes a decide chat; a kickoff closes a review chat.** No LOCKED = no decision; no kickoff = the next week starts blind. *(Origin: GW04 chat ended with open questions; the transfer was never made.)*
4. **Plan ≠ executed until the API confirms it.** After every deadline Claude reads picks and transfers and writes the actual state into the brief. *(Origin: GW4 Collins→Bogle, 15 points.)*
5. **Deviation is written before acting.** Rule-breaking is allowed, never free. *(Origin: GW2 Watkins→João Pedro executed first, written after.)*
6. **The log row and the EXP are unskippable**, including 10-minute weeks. *(Origin: strategy pre-mortem #1.)*

## Squad
7. **Fifteen players with real minutes.** Bench = three playing outfield players; the second keeper may be a true non-player. *(Origin: £19.0 for 5 points, GW1–5; two ten-man gameweeks.)*
8. **Minutes gate.** Tag everyone nailed / likely / 50-50 / doubt / out with the source. Nobody below *likely* starts; nobody below *50-50* is bought. A minutes claim needs two independent sources or an official flag; predicted bench is not confirmed bench without injury, quote or suspension. *(Origin: Ndiaye GW3, Senesi GW2.)*
9. **A flagged starter with no playing substitute is a transfer or a bench decision**, never a hope. *(Origin: Collins GW4, João Pedro GW5.)*
10. **Cheapest nailed scorer at the right club** beats the known name there. *(Origin: Stach/Bogle, Collins/Janelt, Elanga/Barnes, Verbruggen/De Cuyper, Keane/Tarkowski, Egan/Tzolakis.)*
11. **Bank ≥ £0.3.** A fully spent squad turns every injury into a hit. *(Origin: strategy §6.8; bank £0.1 at GW5.)*
12. **Every differential has a thesis and an exit condition in `data/watchlist.csv`** before it plays. Two or three at a time, never more. *(Origin: strategy §6.10; zero written theses in Phase 1.)*
13. **Every Arsenal pick passes the neutral-club test.** No premium at a new-manager club without minutes evidence (Haaland is the written exception). *(Origin: strategy §11.)*

## Transfers, captains, chips
14. **Roll is always a named candidate.** Hits need written 4-GW EV clearly above 4; close calls are a no; no hit within 24h of a red gameweek. *(Origin: strategy §11.4, §11.6.)*
15. **Team value times moves, never justifies them.** *(Origin: strategy §11.10.)*
16. **Captain from the pool** (Haaland default, Bruno home vs promoted) unless a written trigger says sword. **League-EO decides shield vs sword**, not field-EO; the vice is a nailed starter. *(Origin: GW2, −20 to Alex.)*
17. **Chips fire only from a rationale written in `chip-plan.md` the day before**, with the baseline logged; never reactive. TC/BB cancellable before the deadline; WC/FH not. *(Origin: strategy E5; chip set 1 expires at the GW19 deadline — verify the date in the API.)*
18. **League beats overall rank in any conflict.** Behind the rival of record by more than 30: sword posture (differential captaincy first, structural differentials second). *(Origin: strategy §1, §7; −69 to Alex after GW5.)*

## Evidence
19. **Pull, never remember.** Prices, flags, ownership, squads, points come from the API or the snapshot, every time. `ep_next` is a baseline, never an input. xP and the solver are a prior to argue with, never the decision. *(Origin: every documented LLM-for-FPL failure is a number from memory.)*
20. **Decisions are graded process × outcome; luck is flagged and never repeated.** A lesson becomes a rule only when it recurs or a bias review promotes it. *(Origin: strategy E4.)*

## Changelog
| Date | Change |
|---|---|
| 2026-10-07 | v3.0 — first operational rule book, consolidated from `strategy.md` §11 and the Phase 1 retro (`docs/06`). |
