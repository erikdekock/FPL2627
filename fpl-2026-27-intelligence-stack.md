# FPL 2026/27 — Intelligence Stack (Source Map)
**Version 1.0 · 20 July 2026 · companion to Project Scope v0.1**
Purpose: define exactly what we need to know — weekly and long-term — and the best place to get each piece. Research-verified July 2026.

---

## 0. How this stack works

Three horizons, three cadences:

| Horizon | Cadence | Core questions |
|---|---|---|
| **Season** | Pre-season + monthly | Squad philosophy, chip master plan, rank target, structural bets |
| **Rolling** | Weekly, 4–6 GW lookahead | Fixture swings, transfer paths, BGW/DGW radar, watchlist |
| **Gameweek** | Weekly execution | Transfers, captain, XI/bench, chip check |

Tiering of sources:
- **Tier 1 (core, every week):** official FPL + API · LiveFPL · Premier Injuries · BBC Sport FPL · Fantasy Football Scout · press-conference summaries
- **Tier 2 (situational):** Fantasy Football Hub (Crellin) · predicted-lineup sites · fpl.page · Understat/FBref · r/FantasyPL
- **Tier 3 (deep research / on demand):** FPL Review · GitHub datasets · podcasts/YouTube · academic/odds-based models

---

## 1. WEEKLY needs → where to find them

| # | What we need to learn | Primary source | Backup / cross-check | When (UK time; NL = +1h) |
|---|---|---|---|---|
| 1 | **Last GW review** — points vs average, rank move, bonus, what the field did | Official FPL app/API · LiveFPL (rank context, EO of what hurt/helped) | fpl.page "Gameweek Wrapped" | Mon–Tue |
| 2 | **Injuries & availability** — who's out, doubts, return dates | **Premier Injuries** (return-date table) · official FPL flags (API `status`/`news`) | BBC team-news article (updated live during pressers) | Rolling; firm by Fri |
| 3 | **Press conferences distilled** — what managers actually said | **Premier Fantasy Tools press-conference summaries** (free newsletter) | BBC Sport FPL team news · FFScout | Thu–Fri (pressers ~24–48h pre-match) |
| 4 | **Predicted lineups & rotation risk** | Fantasy Football Scout team news · **Fantasy Football Pundit** (start-% per player, uses leaks) | Fantasy Football Hub lineups · RotoWire | Fri (firm) · confirmed XIs ~60 min pre-KO |
| 5 | **Price changes tonight** — protect TV, time transfers | **LiveFPL price predictor** (livefpl.net/prices — widely regarded as the most accurate; FFScout embeds it) | FPLWatch | Predictor all day; changes ~01:30–02:30 |
| 6 | **Transfer market trends** — what the crowd is about to do | FPL API (`transfers_in/out_event`) · LiveFPL top transfers | r/FantasyPL daily threads (sentiment radar) | Tue–Fri |
| 7 | **Effective ownership & captaincy meta** — shield vs sword decisions | **LiveFPL** (top-10k EO, captains, chips, template combos) | Fix elite tracking | Thu–Sat pre-deadline |
| 8 | **Points projections (1–3 GW)** | FPL Review model (paid; the benchmark) — free era: our own read from stats + fixtures | Hub AI predictions · Fix algorithm | Pre-deadline |
| 9 | **Fixture difficulty, this GW + next 4–6** — attack/defence adjusted | Hub fixture analyser · Premier Fantasy Tools ticker | FPL API FDR (crude but instant) | Weekly |
| 10 | **Underlying stats** — xG, xA, xGI per 90, shots, chances; **DefCon counts** | Understat · FBref (free, authoritative) · official Scout DefCon articles | fpl.page (live DefCon tracking) · FFScout members stats | Post-GW + pre-transfer |
| 11 | **Set pieces & penalty takers** | FFScout set-piece takers list | Hub set-piece article | Check after any change/miss |
| 12 | **Captaincy shortlist** | LiveFPL EO + projections + BBC Friday content | The FPL Wire discussion | Fri–Sat |
| 13 | **Deadline safety net** | fpl.team free e-mail, 24h before every deadline (subscribe once) | Phone reminder from Notion Season Calendar | Automatic |

**The weekly information clock (typical Saturday-deadline GW):**
- **Nightly ~01:30–02:30 UK** — price changes execute; predictor verdict is reliable by ~22:00 the evening before.
- **Mon–Wed** — GW review, injury drip, transfer planning window (never transfer early without a price reason).
- **Thu** — BBC "team of the week" XI; first pressers; Hub/Scout team news updating.
- **Fri** — remaining pressers; BBC live FPL Q&A 15:30 UK; predicted lineups firm; **our gameweek chat happens Fri evening or Sat morning NL time**.
- **Sat** — deadline 90 min before first kickoff (12:30 UK KO → 11:00 UK / 12:00 NL deadline). Confirmed lineups only ~60 min before each KO — players in Sunday/Monday games carry extra lineup uncertainty at deadline; weight captaincy accordingly.
- **Note:** not every GW is Saturday-anchored — GW1 starts on a **Friday** and the season has five midweek rounds. The routine flexes to the deadline, not the weekday.

---

## 2. LONG-TERM needs → where to find them

| # | What we need to learn | Primary source | Notes |
|---|---|---|---|
| 1 | **Rules & game changes 26/27** | **premierleague.com / The Scout only** | Hard rule: no third-party site defines rules for us. Audit at launch. |
| 2 | **Initial squad ("first pick")** — prices, position classifications, new signings | FFScout "Ultimate pre-season guide" hub (price reveals position-by-position, Scout Reports on signings, Moving Target series, friendlies tracking) + FFScout predicted-price Draft tool (live now, machine-modelled prices) | Launch signals to watch: @OfficialFPL teasing prices on X; game site entering maintenance mode. |
| 3 | **Pre-season friendlies signals** — minutes, roles, fitness | Hub pre-season friendlies guide · FFScout pre-season coverage | Minutes in final 2 friendlies ≈ best GW1 lineup predictor. |
| 4 | **Season structure & BGW/DGW forecasting** | **Ben Crellin** (Fantasy Football Hub: planner + FPL calendar) | THE authority on blanks/doubles; becomes critical from ~December (cup rounds). |
| 5 | **Fixture swings across the season** | Hub fixture ticker · Premier Fantasy Tools season planner | Feed into Rolling-horizon transfer paths. |
| 6 | **Chip strategy theory & timing** | Hub chip strategy guide · FFScout chip articles · The FPL Wire (podcast debates) | Combine with Crellin's BGW/DGW map. |
| 7 | **Historical data & our own modelling** | **GitHub: vaastav/Fantasy-Premier-League** (GW-by-GW CSVs since 2016/17, Understat xG mapping, data dictionary) · **olbauday/FPL-Core-Insights** (2025/26 incl. match stats + team Elo) · FPL API | GitHub is reachable from Claude's sandbox → we can download CSVs and run pandas analysis ourselves (e.g., DefCon reliability, promoted-team value, price-vs-points curves). |
| 8 | **Projection-grade planning / solver** | **FPL Review** (projections + planner + solver; peer-reviewed comparisons treat its Massive Data Model as the commercial benchmark) | Paid. Candidate for the GW8 subscription decision. Open-source alternative exists (OpenFPL, academic). |
| 9 | **Elite manager behaviour** | LiveFPL top-10k templates & chip usage · Fix "move for move" elite tracking | Use as calibration, not gospel. |
| 10 | **Transfer window impact (until 1 Sep)** | FFScout Scout Reports / Moving Target · mainstream reliable journalism (BBC, The Athletic) | Window closes after GW2 — see Open Question #7. |
| 11 | **Strategy education & narrative** | Podcasts: **The FPL Wire** (Lateriser, Zophar, Pras — elite track records), Who Got The Assist?, FML FPL, Green Arrow (Hub) · YouTube: FFScout channel, Let's Talk FPL, FPL Harry · Newsletter: FPL Is Life (weekly digest of what FPL-internet is saying) | Pick 1–2, not all. Entertainment ≠ signal. |
| 12 | **Market-implied probabilities** — clean-sheet odds, goalscorer odds | Odds-based tools (e.g., Check The Chance) | Information input only — no betting (project guardrail). |

---

## 3. Source profiles (trust notes)

**Official FPL + API** — ground truth for prices, flags, ownership, deadlines. The API is free, public, no auth. Flags (75%/50%/25% doubt) are conservative and sometimes lag pressers — pressers beat flags.

**LiveFPL (Ragabolly)** — community-built, free core, now also apps. Best-in-class for: live rank, top-10k effective ownership, captaincy/chip meta, price predictions. FFScout itself embeds his price predictor. Trust: high; transparent about accuracy history.

**BBC Sport FPL** — big, free, editorially reliable. Four expert columnists (incl. Pras, Holly Shand), Thursday best-XI, Friday 15:30 live Q&A, and a continuously updated team-news + FPL-stats article during press conferences. Excellent zero-cost baseline.

**Fantasy Football Scout** — the long-established editorial heavyweight; fastest on launch news, price reveals, set-piece lists, team news. Free tier strong; members area adds stats/Rate My Team. Watch-out: annual memberships auto-renew.

**Fantasy Football Hub** — home of Ben Crellin (planner/calendar), Opta stats, AI predictions, expert reveals (incl. a former overall FPL champion, Jonas Sand Låbakk). Strongest bundle if we ever pay.

**Fantasy Football Fix** — algorithmic projections, price-change predictions, rotation planner, elite-manager tracking, browser extension. Popular with high-finishing managers.

**FPL Review** — projections + solver/planner; the model other models are measured against in published comparisons. Paid tiers for the best model. This is the "go pro" option if we want solver-grade multi-GW optimization.

**Premier Injuries** — dedicated injury table with expected return dates. The injury reference.

**Premier Fantasy Tools** — press-conference summaries in one readable page + free newsletter; also fixture ticker and season planner.

**Fantasy Football Pundit** — predicted lineups with per-player start probability, incorporating leaks. Good complement to FFScout's team news.

**fpl.page / FPL Focal (Oscar)** — live DefCon and bonus tracking, dashboards, launch-history articles. Community-trusted.

**Understat / FBref** — free, serious xG/xA and per-90 data. Our stats backbone when not paying for Opta access.

**GitHub datasets** — vaastav (canonical historical FPL dataset, 2016→now, with data dictionary and Understat ID mapping) and FPL-Core-Insights (modern extension with Elo + match stats). For our own sandbox analysis.

**r/FantasyPL** — largest open community; use for sentiment and catching things we missed, never as an authority.

**fpl.team** — free deadline-reminder email 24h before every deadline; predicted lineups powered by FPL Copilot.

---

## 4. What Claude pulls automatically in every gameweek chat

1. **FPL API** — bootstrap-static (prices, ownership, flags, form), fixtures, Erik's team via entry/{TEAM_ID}.
2. **LiveFPL prices page** — tonight's predicted rises/falls.
3. **Web search** — press-conference roundups (BBC / PFT / FFScout), predicted lineups, any breaking injury news.
4. **On demand** — GitHub CSVs into the sandbox for custom analysis (DefCon reliability, fixture-adjusted form, value curves).

Fallbacks: some sites rate-limit or paywall bots → search snippets + Erik's screenshots cover the gap. Optional future power-up: a community **FPL MCP server** exists that plugs the FPL API straight into Claude as tools (league spying, head-to-head analysis) — evaluate once the season is running.

---

## 5. Source hygiene rules (non-negotiable)

1. **Game rules only from premierleague.com.** Third parties get it wrong or invent things; AI-slop sites already publish fake 26/27 "rule changes."
2. **Two-source rule** for anything surprising (transfers, injuries, rule claims).
3. **Check the date** on every article — pre-season content ages in days.
4. **Pressers beat flags; confirmed lineups beat pressers.**
5. **Pre-season injury flags on lineup sites are noisy** — treat as prompts to verify, not facts.
6. **EO and crowd trends are inputs, never directives** — we use them to size risk, not to outsource decisions.
7. **Projection models are strongest 1–3 GWs out**; confidence decays beyond that. Multi-GW plans stay flexible.
8. **Odds are information; betting is out of scope.**

---

## 6. Open strategy questions (added to the backlog — beyond what was asked)

1. **World Cup fatigue mapping.** The season starts late precisely for post-WC recovery — but players from the deepest-running nations (finalists + semifinalists) still return latest. Before drafting: map every PL asset by WC exit round; expect early rotation/slow starts among deep-run players and value among early-exit/non-WC players.
2. **Post-Salah captaincy landscape.** Salah has left Liverpool — the single biggest EO/captaincy anchor of recent seasons is gone, and Pep has left City. Where does captaincy concentrate now? This decides our premium structure. Confirm destination/rumours at launch; watch Haaland's role under City's new manager.
3. **DefCon, year two.** We now have a full season of defensive-contribution data. Sandbox analysis: who hit thresholds most reliably per 90, and is the launch price list still mispricing them (cheap DefCon mids/CBs as bench-strength meta)?
4. **Position reclassifications at launch.** FPL sometimes reclassifies players (MID↔FWD, DEF↔MID). Screen the price list on day one — reclassifications are recurring sources of value.
5. **Promoted-team value.** Lampard's Coventry, Ipswich, Hull: historical hit-rate of promoted budget picks (defenders vs attackers) — a sandbox study before we auto-fill £4.0–4.5 slots.
6. **Eight new managers = role uncertainty.** Discipline rule: no premium commitment to a new-manager club until friendly/GW1–2 minutes evidence. Patience in GW1–4 is this season's structural edge.
7. **Transfer window closes 1 Sep (after GW2).** Two risks: buying someone who's sold/benched post-deadline-day, and missing late-arriving bargains who enter the game GW3+. Keep 1–2 squad slots flexible early.
8. **Deadline-day player-entry watch.** New signings get added to FPL with prices mid-season — monitor for instant-value entries.
9. **Mini-league meta vs overall rank.** Different games: when do we mirror rivals, when do we differentiate? LiveFPL league explorer / FPL Toolbox for rival tracking once leagues are set.
10. **Late-kickoff information asymmetry.** Assets playing Sunday/Monday are unconfirmed at deadline — a systematic captaincy/bench-order consideration, not a one-off.
11. **Midweek-round routine.** Five midweek rounds: compressed news cycle, pressers day-before, tighter chat scheduling. Season Calendar flags these.
12. **Paid-tool decision (GW8).** Candidates: FPL Review (solver/projections depth) vs Hub (Crellin + Opta + AI bundle) vs Fix (prices + elite tracking) vs FFScout membership (stats + community). Criterion: did the free stack demonstrably cost us points in GW1–8? Log misses in the Gameweek Log to make this evidence-based.

---

## 7. Immediate to-dos generated by this research

- [ ] Subscribe (free): fpl.team deadline email · Premier Fantasy Tools newsletter.
- [ ] Bookmark set for Erik's phone: livefpl.net · premierinjuries.com · BBC FPL page · FFScout pre-season hub.
- [ ] At launch: rules audit (Scope §3) + position-reclassification screen + price-list review.
- [ ] Sandbox studies to run pre-GW1: DefCon year-1 reliability · promoted-team pick history · WC-fatigue exposure map.
- [ ] Add §4 fetch list to the project instructions.
- [ ] Notion: file this doc under FPL HQ → "Intelligence Stack"; add the weekly clock to the Season Calendar page.

*Changelog: v1.0 — initial research pass, 20 July 2026. Revisit at launch and at GW8 (paid-tool decision).*
