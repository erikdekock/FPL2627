# Engine Research — Predictive Engines, Landscape & Steal List
**Version 1.0 · 20 July 2026 · feeds the Project Beane Charter (engine/KICKOFF.md)**
Mission of this doc: know everyone who has built something like this, take the quality that transfers, and add angles they don't have.

---

## 1. Landscape A — FPL-native engines

### Open source (we can read the code)

**OpenFPL — the academic benchmark-beater** · github.com/daniegr/OpenFPL · arXiv 2508.09992 (Groos, 2025)
Position-specific ensemble models trained purely on public FPL + Understat data (2020–21 to 2023–24), tested *prospectively* on 2024–25. Accuracy comparable to the leading commercial service overall — and **better on high-return players (the haulers that actually move rank)**. Works on 1/2/3-GW horizons. Key stealables: the feature construction from FPL+Understat, the outcome buckets (Zeros / Blanks ≤2 / Tickers 3–4 / Haulers ≥5), prospective (not just historical) evaluation, and the proof that public data suffices.

**AIrsenal — the Turing Institute's bot** · github.com/alan-turing-institute/AIrsenal
Full pipeline: SQLite schema (players, fixtures, results, predictions, transfer history) → Bayesian team-strength model (bpl-next, Dixon-Coles family) → player points prediction per fixture → transfer/lineup optimizer → can even execute transfers via the API. Updated for the 5-FT era. Key stealables: the database schema as architecture blueprint, Bayesian team-strength layer, clean fetch→predict→optimize→execute separation. Key lesson: **season 1 top 30%, season 2 bottom of their own mini-league (~5-millionth at GW9)** — written up honestly by the authors. Variance is brutal; models earn trust slowly.

**The Sertalp Çay solver ecosystem** · github.com/sertalpbilal/FPL-Optimization-Tools (+ open-fpl-solver, fpl_optimized; Solio Analytics)
Mixed-integer optimization for squad/lineup/captain/transfers over multi-GW horizons (pandas + sasoptpy + HiGHS/CBC). Free, documented, with a YouTube tutorial series that is effectively a course in FPL optimization (MILP, multi-objective, stochastic optimization, simulation, sensitivity analysis). Key stealables: **projections and optimization are separate layers** — the solver eats any projections CSV, so our numbers (or OpenFPL's) plug straight in later; the **decay objective** (~0.84 per future GW — near weeks weigh more); bench weights; randomized runs for sensitivity.

**Datasets:** vaastav/Fantasy-Premier-League (canonical GW-by-GW history since 2016/17, Understat mapping) · olbauday/FPL-Core-Insights (2025/26 + match stats + team Elo). Both pullable into our sandbox.

### Commercial (we can read the outputs and the claims)

**FPL Review** — the projection benchmark academic papers compare against; strengths: minutes modeling + expert/crowd input + odds-informed EV, with planner/solver on top. **Fantasy Football Hub / Fix** — Opta-fed projections bundled with content. **FPL Copilot / The Transfer Algorithm** — newer forecasters cited alongside them. Common thread: their real moat is **minutes forecasting and market/odds feeds**, not exotic math.

**Reading of the whole field:** everyone converges on the same pipeline — (1) team-strength model → (2) player event rates → (3) minutes model → (4) expected points → (5) optimizer. Quality differences live mostly in layers 2–3 and in discipline of evaluation. Our v1 copies the pipeline shape with the simplest defensible version of each layer.

---

## 2. Landscape B — adjacent fields, one transferable idea each

**Football match modeling — Dixon-Coles (1997).** Bivariate Poisson: attack + defence strength per team, home advantage, low-score correction (rho), time-decay on past matches. Still the foundation under most football betting models; gives per-fixture expected goals and scoreline probabilities → **clean-sheet probability and team-goals λ per fixture**, which is exactly what a fixture-adjusted FPL model needs. Our E3 fixture adjustment = Dixon-Coles-lite (or its outputs via bpl-next).

**DFS / game theory (DraftKings-world).** Their vocabulary maps 1:1 onto FPL: chalk = template, ownership = EO, leverage = being different where it's *paid*, cash games (protect floor) vs GPP tournaments (chase ceiling, score only matters relative to the field). Two imports: (a) **overall rank = massive-field GPP, the mini-league = small-field GPP** — different optimal risk in each, and rival-aware decisions in small fields; (b) **correlation stacking** — attacker + defender of the same team correlate (goals + CS), double-captaincy-week logic, and "leverage captaincy": low-EO captain picks are the cheapest way to buy variance when chasing.

**Sabermetrics / Moneyball.** Three imports: (a) the **Marcel lesson** — a dumb weighted multi-season average with regression to the mean is a shockingly strong baseline; any model we build must beat Marcel-for-FPL before it earns complexity; (b) **VORP → Points Above Replacement per £** — value is measured against the best *cheapest playable* option in the position, not against zero (this reframes budget picks and bench design); (c) market inefficiency thinking — the field's attention is the scarce resource; mispricing concentrates where attention doesn't go (DefCon year-2, reclassified players, post-BPS-rewrite defenders).

**Portfolio theory.** A squad is a portfolio: diversification vs concentration, covariance between holdings (three Arsenal players = one correlated bet), risk budget per line, and the **option value of the bench** (a playing 4.5 is insurance, not dead money). Chip timing = option exercise.

**Forecasting science (Tetlock).** Keep score on *ourselves*: log predictions (captain EV, transfer EV) and grade calibration over time. Ensembles beat single models; base rates beat narratives. Our Gameweek Log becomes a calibration dataset by ~GW10.

**Bayesian updating.** Small weekly samples + strong priors (AIrsenal's approach): start from historical rates, update gently. Protects us from 90-minutes-of-evidence overreaction in Aug/Sep — which is precisely when the field overreacts most.

---

## 3. The Steal List (ranked: value × effort), mapped to milestones

| # | Steal | From | Lands in |
|---|---|---|---|
| 1 | Pipeline shape: team model → event rates → minutes → xPts → optimizer | whole field | Architecture (E1) |
| 2 | Marcel-style baseline: weighted 3-season per-90 + regression; every later model must beat it | sabermetrics | E2 + backtest (E3) |
| 3 | **Points Above Replacement per £m** as the headline value metric | VORP | E2 |
| 4 | Outcome buckets Zeros/Blanks/Tickers/Haulers for evaluation + captaincy (P(haul), not just mean) | OpenFPL | E3, E5 |
| 5 | Dixon-Coles-lite team ratings with time-decay → CS prob + team-goals per fixture | Dixon-Coles / AIrsenal | E3 |
| 6 | Prospective evaluation discipline: backtest 25/26, then *live-test* Aug with predictions logged before matches | OpenFPL | E3 → season |
| 7 | Decay objective (~0.84/GW) + bench weights when weighing multi-GW plans | Sertalp | E4, weekly chats |
| 8 | Projections/optimizer separation — keep our CSV solver-compatible so Sertalp's solver is a free later upgrade | Sertalp | E4 (format), v2 (solver) |
| 9 | EO-leverage framing: shield vs sword per decision; mini-league as small-field GPP with rival tracking | DFS | E5 brief + strategy.md |
| 10 | Correlation awareness: same-team stacks & anti-stacks flagged in squad view | DFS/portfolio | E4, E5 |
| 11 | AIrsenal DB schema as data-model reference (incl. transfer/price history tables) | AIrsenal | E1 |
| 12 | Calibration self-scoring in the Gameweek Log (prediction vs outcome) | Tetlock | E5 → Q1 review |

---

## 4. Where we look further (our angles, not theirs)

1. **LLM-native minutes signal.** The commercial moat is minutes forecasting — built from human experts reading pressers. We have an LLM in the loop natively: every week Claude reads press conferences and team news and emits *structured* minutes priors (start probability + confidence + reason) that feed the model. Nobody in the open-source field does this systematically.
2. **Reasoning over numbers.** Engines output tables; our GW Brief outputs a decision argument — projections + EO leverage + league context + risk posture, reconciled in language. The integration is the product.
3. **Decision-quality loop.** We grade our own calibration weekly (steal #12) and adjust *process*, not just picks. Most managers — and most engines — never close this loop.
4. **Rival-aware mini-league play.** Small-field game theory (cover vs differentiate per rival) using LiveFPL league data. Engines optimize vs the global field; we also optimize vs Erik's actual opponents.
5. **Rules-shift arbitrage.** 26/27 changed BPS and kept DefCon with one season of data — models trained naively on 4 seasons will mis-weight exactly these. We explicitly model the rule deltas (also an OpenFPL-paper point: open methods adapt faster to rule changes).

## 5. Do-not-copy list

- **Deep learning in year one.** The literature's LSTM/CNN attempts don't reliably beat ensembles on this data volume; we're beginners — gradient-boosted or simpler wins.
- **Solver before validated projections.** Optimizing garbage yields confident garbage. Solver is v2.
- **Betting-odds scraping.** Legally/technically fragile; use odds qualitatively via public pages, not as a pipeline dependency.
- **Overfitting to shifting rules.** DefCon exists for one season; BPS just changed. Feature care > feature count.
- **Model worship.** Remember AIrsenal season 2. The engine advises; the process decides; variance humbles.

## 6. Resource shelf

Repos: daniegr/OpenFPL · alan-turing-institute/AIrsenal · sertalpbilal/FPL-Optimization-Tools (+ open-fpl-solver, fpl_optimized) · vaastav/Fantasy-Premier-League · olbauday/FPL-Core-Insights
Papers: Groos 2025 (arXiv 2508.09992, OpenFPL) · Dixon & Coles 1997 (JRSS-C) · the FPL-ML tail cited in OpenFPL's references (time-series, multi-stream, optimization theses)
Tutorials: Sertalp's FPL optimization YouTube series · dashee87's Dixon-Coles-in-Python walkthrough
Concept sources: DFS strategy literature on ownership/leverage/stacking (Stokastic, FantasyLabs) · Tetlock, *Superforecasting* · Michael Lewis, *Moneyball* (obviously)

## 7. Charter deltas (to apply in Engine 01)

1. E2 headline metric becomes **PAR/£** (Points Above Replacement per million) next to points-per-£m.
2. E3 = Marcel baseline + Dixon-Coles-lite fixture layer + backtest harness that scores **calibration and hauler-detection**, not just average error.
3. E4 output CSV formatted solver-compatible (player, GW, xPts) from day one.
4. E5 GW Brief adds two sections: *EO & leverage* (shield/sword call) and *minutes confidence* (LLM presser read, tagged with reasoning).
5. BACKLOG.md seeds: Sertalp solver integration · Monte Carlo rank simulation · OpenFPL model reuse/retrain · rival-tracker for the mini-league.

*Changelog: v1.0 — research pass 20 Jul 2026 (AIrsenal, OpenFPL, solver ecosystem, Dixon-Coles, DFS game theory, sabermetrics, portfolio/forecasting imports).*
