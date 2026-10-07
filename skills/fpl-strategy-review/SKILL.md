---
name: "fpl-strategy-review"
description: "Use in Erik's FPL 26/27 project for 'Strategy Qx' chats, wildcard or free-hit builds and chip-plan rewrites: grade the six edges, cost squad structures with the solver, re-window chips, amend strategy with a changelog."
---

# FPL — strategy review, squad build, chip plan (chat `Strategy Qx` or `WCx build`)

Slower work than the weekly chats, done between gameweeks. Dutch in the chat, English in the files; Claude proposes, Erik decides; every change is a dated changelog line, never a silent rewrite.

## A. Quarterly review (Q1 w/c 12 Oct · Q2 mid-Dec · Q3 early Mar · Q4 late Apr)
1. Clone the repo; read `strategy/strategy.md` whole, `campaign-plan.md`, `chip-plan.md`, `rules.md`, `lessons.md`, every `briefs/`, `data/gameweek_log.csv`, `data/decisions.csv`, the last retro in `docs/`.
2. Season evidence from the API: rank trajectory, points vs average per GW, league table and every rival's chips/hits/transfers/OR, template drift (ownership of our 15 vs the field), the scoring environment (average GW score, top scorers by price band).
3. **Grade each edge E1–E6** on its own "measured by" and "breaks when" lines: validated / insufficient / inverted / untested. An edge whose early warning fired and survived one review is deleted or inverted in the changelog, without sentimentality.
4. **KPI scoreboard** (§10 of strategy.md) filled in with numbers. Re-set the rank bands honestly if the season has moved them; the league target never moves.
5. **Rival archetypes** (optimizer / template-hugger / casual / maverick) from `data/rivals.csv`, and the rival of record for the next quarter.
6. **Bias verdict** from `decisions.csv`: the two named biases and the rule that counters each.
7. Write: `strategy.md` changelog entry (version bump), `rules.md` changes, `campaign-plan.md` calendar corrections, commit `Strategy Qx review`.

## B. Wildcard / Free Hit squad build
1. Fresh data: newest snapshot + live API; `python scripts/xp_model.py --horizon 5` (6 for a wildcard before a fixture swing); `python scripts/wc_solver.py --baseline` for the no-chip baseline, then the structures: free draft, `--lock` the anchors, `--ban` an anchor, `--min-tag nailed` for a risk-off version. Save the outputs to `data/xp/wc_drafts_gwNN.md`.
2. **Rules that bind the build:** 15 players with real minutes (bench = three playing outfield players; one non-playing keeper allowed) · bank ≥ £0.3 · 2–3 differentials, each with a written thesis + exit in `watchlist.csv` · "cheapest nailed scorer at the right club" beats the known name · every Arsenal pick passes the neutral-club test · no premium at a new-manager club without minutes evidence (Haaland excepted in writing) · at most three from one club and, unless the numbers insist, at most two from Man City while the FFP sanction is pending.
3. **Cost each structure to the pound** and argue it in words: where the points are this season by price band, captaincy ceiling and league-EO (dropping the field's captain is a sword move with a written thesis), fixture runs GW..GW+6, rotation risk (European clubs, Thursday–Sunday), international-break minutes.
4. Presser day: re-tag minutes from two sources per player; remove anyone below *likely*; rerun the solver with the new tags; freeze v1.0 in `strategy/wcN-squad.md` with the thesis per differential and the captain/vice for the first GW.
5. Chip rule: the rationale is written in `chip-plan.md` **the day before** the fire; the file's log table gets the baseline (best XI xP of the old 15) so the review can grade the chip.
6. Hand the LOCKED-ready squad to the decide chat (or run the decide steps here if it is deadline week).

## C. Chip plan rewrite
Inputs: chips held (ours and every rival's), the GW19 cliff for set 1 (verify the date in `bootstrap-static` events), Ben Crellin's blank/double map once cup rounds are drawn, the scoring environment, each candidate's fixture and minutes outlook. For each chip: window (GW range), trigger that fires it, the baseline to grade it against, the rival-state consideration (if the chasing rival holds the same chip for the same week, ours is shield; if he has burned his, ours is sword). Table + a dated changelog line. Reactive fires are banned; a proposal sleeps one night.

## Anti-patterns
- A review that produces prose without a changelog line.
- A squad built from names instead of minutes tags and xP, or a solver draft accepted without the argument.
- Chip windows copied from last season's calendar; the fixture list and cup draws decide.
- Rank targets left at 10k when the evidence says 500k: unreachable targets stop steering.
