# Standing rules — read first in every chat
**v3.1 · 9 Nov 2026 · operational rules only; the theory lives in `strategy.md`. Changed only in a review chat, with a changelog line. Each rule names its origin.**

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
17. **Chips fire from a rationale written in `chip-plan.md` the day before**, with the baseline logged. **Same-day exception:** a chip may fire on deadline day only when three things are in the chat before activation: (1) value now vs the planned window, in model points; (2) for BB or FH, a minutes gate: every player involved is a predicted starter in two sources; (3) a screenshot of the confirm screen showing the chip's name. TC/BB cancellable before the deadline; WC/FH not. *(Origin: strategy E5; amended 9 Nov by D-S3 after FH1 was fired instead of WC1 in GW6 while same-day WC1 (+22) and BB1 (+27) paid.)*
18. **League beats overall rank in any conflict.** The rival of service is the league leader. More than 20 points behind the leader: sword posture (differential captaincy first, structural differentials second). Within 20 or ahead: shield (league-EO). Alex and the pack are watched weekly for open chips. *(Origin: strategy §1, §7; amended 9 Nov by D-G4 after the leader changed from Alex to Jason.)*

## Evidence
19. **Pull, never remember.** Prices, flags, ownership, squads, points come from the API or the snapshot, every time. `ep_next` is a baseline, never an input. xP and the solver are a prior to argue with, never the decision. *(Origin: every documented LLM-for-FPL failure is a number from memory.)*
20. **Decisions are graded process × outcome; luck is flagged and never repeated.** A lesson becomes a rule only when it recurs or a bias review promotes it. *(Origin: strategy E4.)*

## Changelog
| Date | Change |
|---|---|
| 2026-10-07 | v3.0 — first operational rule book, consolidated from `strategy.md` §11 and the Phase 1 retro (`docs/06`). |
| 2026-11-09 | v3.1 — rule 18 amended (rival of service = league leader, sword beyond 20 behind) by D-G4, agreed by Erik. Rules 4a, 4b and 17 follow in step F. |
| 2026-11-09 | v3.1 — rule 17 amended (same-day chip with value check, minutes gate and confirm-screen screenshot) by D-S3, agreed by Erik. |
