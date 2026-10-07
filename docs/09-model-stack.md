# Model stack and outside inspiration
**v0.1 · 7 Oct 2026 · research round (135 fetches, every repo verified on github.com today) + what we built from it the same day**

## 1. What we run (built 7 Oct)

| Piece | File | What it does | Status |
|---|---|---|---|
| Transparent xP | `scripts/xp_model.py` | team strength (actual goals + API xG/xGC, shrunk to league average) → fixture expected goals → P(clean sheet); per player: minutes model from starts and flags, xG/xA per 90 shrunk toward the position average below 270 minutes, DefCon as a Poisson rate vs threshold, bonus per start, cards; horizon with 0.84 decay; `ep_next` kept as the public baseline | v0, runs daily in the Action |
| Squad solver | `scripts/wc_solver.py` | MILP (pulp < 4 + HiGHS): 15-man squad under budget and FPL rules, best XI + captain per GW over the horizon, bench weight, minutes gate, locks/bans; `--baseline` scores the current 15 | v0, runs daily |
| Rival Radar | `scripts/fpl_pull.py` → `data/rivals.csv` | every rival's history and picks per GW: captain, vice, chip, transfers, hits, bench points, chips held | live from the next Action run |
| Grading table | `scripts/review_table.py` | our 15 with points, autosubs, captain vs field, league with rivals' captains/chips, every A-vs-B from `decisions.csv` with both scores | v0 |

First run (snapshot 6 Oct, GW6–10): no-wildcard baseline best XI ≈ 61 xP for GW6; the free wildcard draft ≈ 73. The three structures are in `data/xp/wc_drafts_gw06.md`. Weekly the review compares our xP with `ep_next` on absolute error; the loser gets fixed.

## 2. Free, verified building blocks we can add

| Name | What it adds | How we would use it |
|---|---|---|
| [FPL-Optimization-Tools](https://github.com/sertalpbilal/FPL-Optimization-Tools) (HiGHS multi-period solver; code also at [open-fpl-solver](https://github.com/solioanalytics/open-fpl-solver)) | the reference transfer planner: FT value, hit cost, horizon decay, chip weeks, locks/bans, booked transfers | feed it our xP CSV (`ID, Pos, Team, {gw}_Pts, {gw}_xMins`) when the weekly planning needs more than one move; our `wc_solver.py` is the one-shot subset |
| [AIrsenal](https://github.com/alan-turing-institute/AIrsenal) (Turing Institute; v2 Sep 2026, Python ≥ 3.12) | a complete second opinion: Dixon-Coles team model + player model + optimiser | run in the GitHub Action (needs live API), commit its prediction CSV, compare with ours monthly |
| [OpenFPL](https://github.com/daniegr/OpenFPL) · [paper](https://arxiv.org/abs/2508.09992) | position-specific XGBoost/RF ensembles; beats FPL Review's model on haulers in the paper | not a drop-in (needs Understat features); use its feature list to grow our xP |
| [FPL-Core-Insights](https://github.com/olbauday/FPL-Core-Insights) | per-GW player stats incl. CBIT and ClubElo, 2026/27 live, raw-fetchable | replace vaastav for weekly data; Elo as a team-strength prior |
| [penaltyblog](https://github.com/martineastwood/penaltyblog) | Dixon-Coles, Elo, implied odds | upgrade the team-strength step once we have ~10 matches per team (pip install needs a build step that failed in the sandbox today; fine in the Action) |
| [vaastav/Fantasy-Premier-League](https://github.com/vaastav/Fantasy-Premier-League) | history since 2016/17 | backtests only (weekly updates stopped) |

Not worth adding now: MCP servers for data we already snapshot ([fantasy-pl-mcp](https://github.com/rishijatia/fantasy-pl-mcp), [fpl-intelligence](https://github.com/dohyung1/x402-fpl-api)); their `rival_tracker` and `is_hit_worth_it` ideas are already in our scripts.

## 3. How people use Claude and other LLMs for FPL — what works, what fails

- **Works:** the LLM as orchestrator, rule enforcer and scribe over verified numbers (live API, a model's xP, a solver); rival analysis; explaining trade-offs; keeping the journal. The best Claude-Code analogue found ([fpl-copilot skill](https://raw.githubusercontent.com/sugarforever/01coder-agent-skills/main/skills/fpl-copilot/SKILL.md)) does exactly this: sync the API to a local DB, check freshness before answering, SQL, report.
- **Fails:** any number from memory (clubs, prices, injuries — the documented failure in every public experiment: [Scout Digital's ai-fpl study](https://www.scoutdigital.co.uk/case-study/ai-fpl/), City AM/T3 2023), minutes and rotation calls, calibrated probabilities, originality (consensus drift). Academic evidence agrees: in [KellyBench](https://arxiv.org/abs/2604.27865) LLM agents with EPL data and tools all lost money and a 2000s Dixon-Coles beat most of them; in [LLM-SoccerArena](https://arxiv.org/abs/2607.24573) web access improved Brier by only 0.023.
- **Graded in public is the standard:** [Onside AI](https://onsidearena.com/fpl-ai) publishes MAE 1.57 vs 1.86 for FPL's own `ep_next` over 25k predictions; [FPL Copilot](https://fplcopilot.com) replays every GW on xP with a captain hit-rate; [Hub AI](https://www.fantasyfootballhub.co.uk/team-reveals/hubai/team-reveal) (regression on Opta, not an LLM) finished top 0.5% in 2025/26 by following its own optimised transfers near the deadline.
- **Consequence for us:** rules 19–20 in `rules.md` — pull, never remember; grade every EXP; publish our xP against `ep_next` weekly.

## 4. Process practices adopted (sources)

1. Pre-registered expectation with a probability, scored later (Farnam Street decision journal; Brier scoring) → `decisions.csv`.
2. Grade process and outcome separately; luck in relative terms — "if everyone owns him, nobody got lucky" ([FPL Review season review](https://docs.fplreview.com/team-analysis/season-review/)) → the four cells in the review skill.
3. Hindsight-bias antidote: criteria before results, judge the logic ([Simon March, FFScout](https://www.fantasyfootballscout.co.uk/2021/05/20/hindsight-bias-and-how-not-to-look-back-in-anger-in-fpl)) → EXP written in LOCKED.
4. Decision-fatigue hygiene: short sessions, personal rules, a spine of keepers, sleep on it ([March, FFScout](https://www.fantasyfootballscout.co.uk/2020/12/29/how-to-avoid-decision-fatigue-ruining-your-fpl-transfers-and-captain-choices)) → two short chats, rule 14.
5. Don't chase last week's points, formation or captain ([FPL Theorist](https://www.fantasyfootballscout.co.uk/2022/07/14/the-three-types-of-chasing-last-weeks-points)) → bias tag `chasing-last-week`.
6. EV horizon discipline: differences < 0.5 over 12 GWs are noise; risk ∝ EO × EV ([FPL Review](https://docs.fplreview.com/the-model/projections/expected-value)) → solver decay, league-EO rule.
7. Mini-league play: study 4–5 rivals, time chips against their chip states, leaders take fewer risks, chasers more ([March on defending a lead](https://www.fantasyfootballscout.co.uk/2020/07/16/what-is-the-best-strategy-for-defending-a-fantasy-premier-league-mini-league-lead); [mini vs macro EO](https://www.fantasyfootballscout.co.uk/2022/02/04/mini-leagues-v-effective-ownership-does-mini-beat-macro-in-fpl)) → Rival Radar, rule 18.
8. Effective ownership: the most-captained player topped the contenders in only 5 of 29 GWs ([Az, FFScout](https://www.fantasyfootballscout.co.uk/2021/03/24/what-is-effective-ownership-and-why-is-it-so-widely-talked-about-in-fpl)) → captaincy is a real decision, not a mirror.
9. Chip sequencing: WC1 when data settles, FH on the cup blank, WC2 before the big double then BB, TC on a double premium; one conversation before pulling the button ([Lateriser GW32 2026](https://www.fantasyfootballscout.co.uk/2026/04/09/laterisers-fpl-gameweek-32-wildcard-team-reasoning)) → rule 17, chip-plan rewrite.
10. Blank/double forecasting from cup rounds ([Ben Crellin's calendar](https://www.fantasyfootballhub.co.uk/articles/crellin-calendar)) → Q2/Q3 inputs.
11. Pace benchmark: ~64 pts/GW ≈ top 10k; stability over dice-rolling (FFScout, Oct 2026) → honest rank bands at Q1.

## 5. Next model work (owner Claude, in order)
1. Validate v0 weekly: our xP vs `ep_next` MAE per GW in the review; keep whichever is closer as the prior.
2. Add FPL-Core-Insights per-GW stats and Elo to the team-strength step; replace the home factor constant with a fitted one at 10 matches.
3. Multi-period transfer planning with the sertalpbilal solver from GW8 (FT value, hits, chip weeks).
4. AIrsenal in the Action as the monthly second opinion.
5. Backtest the xP on 2025/26 (vaastav) before trusting any captaincy call that disagrees with EO.
