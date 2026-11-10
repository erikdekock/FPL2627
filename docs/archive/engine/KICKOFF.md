# Kickoff Prompt — Project Beane (FPL Moneyball Engine)

> Paste everything below the line as the **first message of a new chat** inside the Claude project `FPL 2026/27`.
> Suggested chat name: `Engine 01 — Charter & MVP`. Repo home for this file: `engine/KICKOFF.md`.

---

Claude, today we start building **Project Beane**: my own FPL analytics and recommendation engine for the 2026/27 season. Moneyball, but for Fantasy Premier League — replace gut feeling with evidence, find what the market of millions of managers misprices, and buy points, not names.

## Context (established in earlier sessions — treat as fact)

- I run FPL 2026/27 as a structured project with Claude as co-manager. Single source of truth: the public GitHub repo `erikdekock/FPL2627` — readable without credentials; write-back uses a token held only in the Claude project instructions, never committed.
- Repo contains: `docs/` (project scope, intelligence stack, run-up plan to GW1), `strategy/` (strategy.md + chip-plan.md, quarterly review cadence), `data/` (gameweek_log.csv, watchlist.csv, snapshots/), `scripts/fpl_pull.py`, `CLAUDE.md` (working agreement).
- Cadence: one `GWxx` chat per gameweek following an 8-step protocol, plus quarterly `Strategy Qx` reviews. **The engine's job is to power steps 2–4 of the weekly chat:** data pull → analysis → transfer / captain / XI / chip recommendations.
- Season facts: GW1 deadline Fri 21 Aug, 18:30 UK / 19:30 NL (confirm at launch). Transfer window closes 1 Sep — after GW2. First-half chips expire at the GW19 deadline (2 Jan). The BPS is reworked this season (less DefCon overlap; better bonus prospects for GKs, full-backs and attackers). Scores are final at 09:00 UK the morning after each GW's last match.
- Free data sources available: official FPL API (bootstrap-static, fixtures, element-summary, entry picks) · vaastav/Fantasy-Premier-League on GitHub (GW-by-GW history since 2016/17, Understat xG mapping) · olbauday/FPL-Core-Insights (2025/26 incl. match stats + team Elo) · LiveFPL (prices/EO) · Understat/FBref. GitHub is reachable from the claude.ai sandbox; fantasy.premierleague.com is reachable there via web_fetch, and directly from Claude Code.

## Mission

Build an engine that, working by GW1 and improving all season:
1. **Ingests** fresh FPL data into the repo on a weekly rhythm (plus a one-time historical backfill).
2. **Computes** a small set of honest metrics: value (points per £m), form per 90, fixture-adjusted outlook, minutes security, DefCon value under the new BPS.
3. **Outputs a weekly GW Brief**: ranked transfer candidates, captain shortlist with reasoning, XI/bench check, and flags (price risk, rotation risk) — the evidence layer under every weekly decision.
4. **Can be backtested** against 2025/26, so we know whether to trust it before we follow it.

Two meta-goals, equally important:
- **I learn data analysis by building this.** I am a beginner. Teach me as we go — every session should make me measurably better at analysis AND at prompting Claude for data work.
- **Build it clean enough to share or sell later.** Documented, reproducible, no spaghetti. But commercialization decisions wait until the engine has proven itself on my own season.

## Honest calibration (hold me to this)

We will not out-model the established projection services in year one — and that's fine. Our edge is not the world's best model; it's the integration: my league context + your reasoning + our own transparent numbers + a disciplined weekly process, compounding over 38 gameweeks. Simple, explainable metrics beat a black box we don't understand — especially while I'm learning.

## Your role in this chat

Architect + hands-on builder + patient teacher. I am product owner and apprentice analyst. Pattern for every build step: (1) explain the concept in plain language, (2) we decide together, (3) you build it, (4) you walk me through the code well enough that I could modify it, (5) commit to the repo. Chat in Dutch; everything written to the repo in English.

## Guardrails (protect me from myself)

- MVP before elegance. One increment per session, each with a definition of done and a visible output (a table, a chart, a brief).
- The engine **augments** the weekly chats, never blocks them. If it isn't ready, the GW chat runs on API + judgment as designed.
- No paid data or tools in v1. No optimization solver until the basics are validated. If scope grows mid-session, park it in `engine/BACKLOG.md` instead of building it.
- Every model claim gets a baseline comparison: vs last season's actual points, vs template ownership, vs naive "pick the most expensive".

## What this first session must produce

1. **Engine Charter v0.1** → `engine/CHARTER.md`: mission, the exact weekly decisions supported, a sketched GW Brief format, and an explicit out-of-scope list.
2. **Scope ladder with dates**, pressure-tested against the run-up plan. Proposal to challenge:
   - **E1 — this week:** data pipeline v0 (API pull → clean tables in repo) + historical backfill of 25/26.
   - **E2 — by ~27 Jul:** core metrics v0 (points per £m, per-90 rates, minutes security, DefCon value under the new BPS).
   - **E3 — by ~3 Aug:** fixture adjustment + simple expected-points v0 + backtest harness on 25/26.
   - **E4 — by ~10 Aug:** initial-squad builder — ranked candidates per slot within £100m (feeds Draft v2/v3).
   - **E5 — by ~17 Aug:** GW Brief generator v1 → first real brief for GW1.
3. **Architecture sketch**: `engine/` folder layout, data flow, where code runs (Claude Code vs sandbox), file formats, run cadence.
4. **My learning curriculum**: ~8 concepts mapped onto E1–E5 (dataframes & joins · per-90 normalization · rolling form windows · fixture adjustment · a simple expected-points model · backtesting & baselines · visualizing a brief · prompting patterns for data analysis).
5. **Then start building E1 today.** Smallest real step: pull bootstrap-static, load it into a dataframe, show me the first honest value table, commit it.

## Decisions you need from me early (ask these, max five, then move)

1. Time budget: how many hours per week I invest in building + learning, pre-season and in-season.
2. GW Brief consumption: chat message, markdown in the repo, or both?
3. Initial-squad builder posture: pure value optimization, or value blended with my stated priors?
4. Learning depth: do I write code myself with your review, or read-and-understand yours?
5. Codename check: does **Project Beane** stay, or rename?

Start by reflecting the mission back to me in five lines so I can correct course, then ask your five questions, then propose Charter v0.1.
