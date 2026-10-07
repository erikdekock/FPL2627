---
name: "fpl-gw-review"
description: "Use in Erik's FPL 26/27 project when a chat is named 'GWxx review' or a kickoff says 'review' (Tuesday after lockdown): grade last gameweek's decisions process x outcome from the API and the decide chat, write log, lessons, rules and the next kickoff."
---

# FPL — review the gameweek (chat `GWxx review`)

The learning half of the week. Scores are final at 09:00 UK the morning after the round's last match; never review before lockdown. Dutch in the chat, English in every file; you commit. The output of this chat is what the next decide chat starts from — if it is not written, the week did not teach anything.

## 1. Pull the truth (numbers first, scrolling never)
1. `git clone --depth 1 https://github.com/erikdekock/FPL2627 fpl && cd fpl`; read `briefs/GWxx.md` (the LOCKED block and the EXP lines), `data/decisions.csv` rows with status open, `strategy/rules.md`, `strategy/lessons.md`.
2. API via web fetch: `/api/entry/6756883/history/` (points, average, ranks, bank, value, transfers, hits, bench points) · `/api/entry/6756883/event/{gw}/picks/` (final picks, autosubs, multipliers) · `/api/bootstrap-static/` taken while the GW is still current (every player's `event_points` for the GW; `most_captained`, `average_entry_score`, `highest_score`, `chip_plays`) · `/api/leagues-classic/348280/standings/` · the nine rivals' `/api/entry/{id}/event/{gw}/picks/` and `/history/`. If the daily snapshot already holds a post-lockdown copy, use it: `python -I scripts/review_table.py --gw N` prints the grading table.
3. Read the decision script: search this project's `GWxx` chat for the decision passages (transfer, captain, XI, LOCKED) and compare what was said with what the API says was done. A mismatch is the first lesson.

## 2. Grade every decision (process x outcome)
For each row in `data/decisions.csv` for the GW:
- **Outcome:** points of A, points of B (the named alternative — both are in the API), delta, EXP hit or miss, and the probability that was stated (Brier contribution = (p − hit)²).
- **Process (G/B):** was the input hierarchy followed (minutes > fixtures > market > underlying > tilt), the minutes gate applied, the rule book followed, the deviation written before acting, two sources for the minutes claim?
- **Cell:** good/good → repeat · good/bad → variance, repeat anyway · bad/good → **luck, flag, do not repeat** · bad/bad → fix the process.
- **Bias tag** if one applies: minutes-optimism · right-club-wrong-player · chasing-last-week · field-EO-shield · unwritten-deadline-swap · plan-not-executed · dead-bench · other (name it).
Fill the row (outcome, delta, process_grade, outcome_grade, bias, reviewed_in). Then the weekly aggregates: our captain vs the field's most-captained (delta logged every week; cumulative in the log), bench points, autosub losses, transfer realised EV vs B, hits.

## 3. Rival Radar
One table: each rival's GW points, total, gap, captain, chip played, transfers and hits this GW, chips still held, OR. One line on the primary rival (Alex): what he did and what it means for shield/sword next week. Write it into the brief.

## 4. Write
- `data/gameweek_log.csv`: the row (gw, deadline_utc, transfers_out, transfers_in, hit_points, captain, vice, chip, gw_points, gw_average, gw_rank, overall_rank, team_value, bank, field_captain, field_captain_pts, lesson). Never edit past rows except factual corrections (note it in `lesson`).
- `data/decisions.csv`: graded rows.
- `strategy/lessons.md`: the lesson(s) of the week, dated, with evidence, status `seen-once` or `recurring`. A lesson that recurs is proposed as a rule.
- `strategy/rules.md`: change only when a lesson recurred or a bias review says so; add a changelog line with the date and the evidence. Never rewrite rules for phrasing.
- `strategy/chip-plan.md` log: if a chip was played, points vs the no-chip baseline (`python scripts/wc_solver.py --baseline` from the pre-deadline snapshot for a wildcard; the single-captain score for TC; the bench's points for BB).
- `briefs/GWxx.md` §review: the verdict in ten lines.
Commit `GWxx review: <lesson in five words>` and push.

## 5. Every fourth review (GW9, 13, 17, …) — the bias review
Aggregate `data/decisions.csv` by type: captain delta vs field (cumulative), transfer hit rate and realised EV vs B, minutes-optimism rate (how often "will start" was wrong), bench waste, differential performance vs template equivalents, hit EV, Brier score of all EXPs. Name or confirm two biases. Promote or retire rules. One dated changelog line in `strategy/strategy.md`. Compare our xP (`data/xp/`) with FPL's `ep_next` on MAE for the GW — note which was closer.

## 6. Hand over
1. In the chat (Dutch): the week in five lines, the verdict per decision in one line each, the one lesson, what changed in the rules (or "nothing").
2. `briefs/GW(xx+1).md` §0 "Carries in": max three items.
3. The **kickoff prompt** for the next decide chat, in a code block, ready to paste:
```
GW{n+1} · Fase {x} · deadline {dag} {datum} {UK-tijd} UK / {NL-tijd} NL · je bent de GW{n+1}-beslischat
Lees eerst: CLAUDE.md, strategy/rules.md, briefs/GW{n}.md, laatste 3 logrijen, watchlist, chip-plan.
Stand na GW{n}: {pt} pt · OR {or} · league P{pos} (−{gap} op Alex) · bank £{bank} · FT {ft} · chips: {chips}
Draagt over: {max 3}
Regel die deze week niet mag breken: {rule}
Read-back eerst: vat de stand in 5 regels samen en noem wat je niet kon vinden.
```
4. If a system change is wished for, list it as a proposal; it takes effect only when Erik confirms and it is written to the repo.

## Anti-patterns
- Reviewing from live scores before lockdown.
- Grading outcomes only ("it scored, so it was right"): the luck cell exists for a reason.
- A lesson that is a feeling ("be braver"); a lesson names a decision, the evidence and the rule it touches.
- Skipping the kickoff: the next chat then starts from zero, which is how Phase 1 was lost.
