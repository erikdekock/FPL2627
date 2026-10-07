# Operating System v3 — the learning loop
**v0.1 PROPOSAL · Wed 7 Oct 2026 · Claude proposes, Erik decides · replaces `docs/05-weekly-operating-protocol.md` (archived, not deleted) once accepted**

The question this answers: how does this project become a strategic advisor that actually learns — week after week — instead of a set of documents that describe one? The retro (`docs/06`) showed the shape of the failure: the thinking happened in chats, nothing survived the chat, and the next chat started from zero. Everything below follows from one principle, borrowed from the pattern that already works in Erik's other projects (`studio-handover`, `ri-week-close`):

> **Chats are stateless. The repo is the brain. A chat that does not write to the repo did not happen.**

---

## 1. What "self-learning" means here, concretely

A system learns when it (1) states what it expects before it acts, (2) measures what happened, (3) compares the two, (4) names the pattern in its errors, and (5) changes its own rules — and then (6) *reads those rules* before the next decision. We built (1) once (EXP lines in chats), never did (2)–(5), and (6) was impossible because nothing was written.

The loop, as data:

| Step | Artifact (repo) | Written by | When |
|---|---|---|---|
| 1 Expect | `data/decisions.csv` — one row per decision with alternative B and a falsifiable EXP + probability | Decide chat | before the deadline |
| 2 Measure | FPL API (ours, rivals, every player's GW points) | Review chat | after lockdown |
| 3 Compare | `decisions.csv` outcome columns: points A vs points B (the counterfactual), EXP hit/miss, process grade, outcome grade | Review chat | Tue |
| 4 Name | `strategy/lessons.md` — dated lesson, evidence, status (seen once / recurring / rule / retired) | Review chat | Tue |
| 5 Change | `strategy/rules.md` — numbered standing rules with origin; changed only in a review chat with a changelog line | Review chat (monthly bias review promotes/retires) | Tue, monthly, quarterly |
| 6 Read | the kickoff prompt tells the next chat to read `rules.md` first and read back the state | Decide chat | Thu/Fri |

The counterfactual is the engine. Because every recommendation is written as **A with B as the named alternative**, the realised points of A *and* B are both in the API the following week. Over 30 gameweeks that produces the one dataset no subscription sells: how good our A-vs-B calls are, by decision type, and where they are systematically wrong. "Right club, wrong player" became visible only because somebody compared Stach to Bogle; the system should do that comparison every week, for every decision, by default.

---

## 2. The week — two short chats, not one long one

**Recommendation A (confidence medium-high): two chats per gameweek.** `GWxx` decides; `GWxx review` learns. The retro shows that when review and decision share a chat, the review is what gets skipped under deadline pressure — four reviews were drafted, zero were finished.
**Alternative B:** one chat per GW with the review as act one. Cheaper in chat count, and it is what we had.

### Chat 1 — `GWxx review` · Tuesday (or the first free 20 minutes after lockdown) · 15–25 min
Opens with the kickoff written by the previous review. Steps, in order:
1. **Pull the truth.** `git clone` the repo (one command, proven); API: our `/history/`, `/event/{gw}/picks/` incl. autosubs, `/transfers/`; league standings; the nine rivals' `/event/{gw}/picks/` and `/history/` (chips, hits). Every owned and rejected player's GW points.
2. **Read the script.** Search the project's `GWxx` chat and read the decision passages (the tools can read past chats in this project — used for the retro). Compare what was *said* with what the API says was *done*. Any mismatch is a lesson before anything else.
3. **Grade every row** in `decisions.csv` for that GW: EXP hit/miss, points A vs B, process grade (was the input hierarchy followed, was the minutes gate applied, was the rule book followed), outcome grade. Four cells: good/good repeat · good/bad variance · bad/good **luck — flag** · bad/bad fix.
4. **Rival Radar.** Rivals' transfers, captains, chips, hits; league-EO of our key assets; gap to Alex. One table in the brief.
5. **Write** the log row (`gameweek_log.csv`), the graded decisions, the lesson(s) (`lessons.md`), and — only if a lesson recurred or a monthly review says so — a rule change (`rules.md` + changelog). Commit `GWxx review: <lesson in five words>`.
6. **Hand over.** Write `briefs/GW(xx+1).md` §0 "Carries in" and the **kickoff prompt** for the next decide chat (Dutch, code block, ready to paste, with a read-back instruction). Close.

Every fourth review (GW9, 13, 17, …) is also the **bias review**: aggregate `decisions.csv` by type — captain delta vs field, transfer realised EV vs B, minutes-optimism rate (how often "will start" was wrong), bench waste, differential performance vs template equivalents, hit EV. Name or confirm two biases; promote or retire rules; one changelog line in `strategy.md`.

### Chat 2 — `GWxx` · Thursday or Friday, after the pressers · 30–45 min
Opens with the kickoff prompt from the review. **First reply is a read-back**: the state in five lines (points, rank, league gap, bank/FT, chips, open items) plus anything it cannot find — before any analysis. Then:
1. **Data at maximum information.** Snapshot + live API; flags; Premier Injuries; press-conference summaries (Premier Fantasy Tools / BBC); predicted XIs (FFScout + one independent source); LiveFPL/API ownership and transfer trends; fixtures GW+1..+5; Understat for tie-breaks. Never one source for a minutes claim.
2. **Minutes gate.** Every one of our 15 and every candidate gets a tag: nailed / likely / 50-50 / doubt / out, with the source. Nobody below "likely" reaches the XI; nobody below "50-50" reaches the 15. A flagged starter with no playing substitute is a transfer or a bench decision, never a hope.
3. **The five decisions**, each as A (with reasoning and a confidence level) and B (named, costed), each with an EXP:
   - Transfer: roll is always a named candidate; hits need 4-GW EV clearly above 4; the archetype and the thesis/exit for any differential go into `watchlist.csv` the same turn.
   - Captain + vice: EO-aware (field for rank, **league-EO for the league**: who of the nine owns him, who captains him); late-kickoff discount; vice = nailed starter.
   - XI + formation; bench order (autosubs resolve in bench order at GW end).
   - Chip line: what `chip-plan.md` says about this week; what has materialised; chips left vs GWs to the cliff.
   - Rival angle: ahead → shield (mirror the chaser's captain); behind → sword (differential captaincy first). One line.
4. **LOCKED.** One message, fixed shape: transfers as to be executed, chip, captain/vice, XI, bench order, bank after, and the EXP block. Erik executes in the app and sends a screenshot; Claude checks it name by name. No LOCKED message = no decision was made.
5. **Verify** after the deadline: Claude reads `/event/{gw}/picks/` and `/transfers/` and appends the actual state to the brief. Commit `GWxx: <moves|roll>, C:<captain>`.

### The 10-minute week (legitimate)
Flags on the 15 → bench/replace → roll unless somebody is out → captain the pool default → bench order → Save → LOCKED → log row "reduced week". The log row and LOCKED are never skipped; everything else is.

---

## 3. What we bank, where, and how it is retrieved

| File | Holds | Rule |
|---|---|---|
| `data/gameweek_log.csv` | one row per GW: moves, hit, C/VC, chip, points, average, ranks, TV, bank, field captain + his points, lesson | unskippable; never edited except factual corrections |
| `data/decisions.csv` *(new)* | one row per decision: gw, type, A, B, inputs used, EXP, probability, outcome, points A, points B, delta, process grade, outcome grade, bias tag, reviewed-in | the calibration dataset; the review chat fills the outcome columns |
| `briefs/GWxx.md` *(new)* | the decision brief: carries-in, data timestamp, Rival Radar table, the five decisions with A/B/EXP, LOCKED block, post-deadline verification, review verdict | one page; the only thing the next chat needs besides the CSVs |
| `data/watchlist.csv` | every differential and candidate with archetype, thesis, exit condition, minutes tag, date | a differential without a row is not allowed in the XI |
| `strategy/rules.md` *(new)* | the numbered standing rules (operational, one line each, with origin) | read first in every chat; changed only in review chats with a changelog line |
| `strategy/lessons.md` *(new)* | dated lessons with evidence and status | a lesson becomes a rule when it recurs or a bias review promotes it |
| `strategy/strategy.md`, `campaign-plan.md`, `chip-plan.md` | the theory, the calendar, the chip windows | quarterly; chip-plan gets a log line on every fire |
| `data/rivals.csv` *(new, automated)* | per GW per rival: points, captain, chip, transfers, hits, OR | written by `fpl_pull.py` daily + review chat |
| `data/snapshots/` | daily API dump via GitHub Action | unchanged; add rival `/history/` and `/picks/` |

**Retrieval at the start of any chat:** `git clone --depth 1` (seconds), then read `rules.md`, the last three log rows, the previous brief, the open watchlist, `chip-plan.md`. Project memory (Claude's own) holds preferences and conventions, never game data. Past chats are searchable from inside the project and are used by the review chat to read the decision script; they are never the system of record.

**Who writes:** Claude writes every file above and commits (push access through Erik's GitHub connection, proven 7 Oct; if a session lacks it, the chat's last message carries the exact rows and Erik pastes — the fallback that must fire the same day, not "later"). Erik never maintains files by hand.

---

## 4. Information: where we look, and the honest limits

The source map in `docs/02` is good and stays. What changes is the operating rule: **every weekly brief names its sources and their timestamps**, and a minutes claim needs two independent sources or an official flag.

| Need | Primary (works from here) | Notes |
|---|---|---|
| Our team, rivals, prices, ownership, flags, points | FPL API via web fetch (`bootstrap-static`, `fixtures`, `entry/{id}/…`, `leagues-classic/{id}/standings`, `element-summary/{id}`) | Reachable from the chat via web fetch; not from the shell. Daily snapshot in the repo as backup. `ep_next` is broken this season — never a decision input. |
| Injuries, return dates | Premier Injuries · official flags | Flags lag pressers by hours. |
| What managers said | Premier Fantasy Tools press-conference summaries · BBC team news | Thursday/Friday; Monday-game clubs after our deadline. |
| Predicted XIs | Fantasy Football Scout team news + one independent (RotoWire / Fantasy Football Pundit) | Predicted bench ≠ confirmed bench without injury, quote or suspension. |
| Ownership, EO, captaincy meta, price predictions | LiveFPL (partly JavaScript — fetch may fail; then the API's `selected_by_percent` and `transfers_in_event`) | League-EO is computed by us from the nine rivals' picks — nobody else has it. |
| Projections as a prior | one free xP model as benchmark (candidate: FPL Copilot; FPL Review if we ever pay) | A prior, never the decision; our own read is logged next to it so the review can compare. |
| Underlying stats | Understat (xG/xA); official Scout DefCon pieces | Not FBref. |
| Fixture swings, blanks/doubles | Hub ticker, Ben Crellin for BGW/DGW | Crellin from December onwards. |
| Scout radar (differentials) | Critchley, Mattinson, Transfers Podcast → five-question filter (`docs/04`) | Feeds `watchlist.csv` only; never a direct buy. |
| Elite behaviour | LiveFPL top-10k template and chip timing | Calibration, not gospel. |

Rules of evidence: minutes beat fixtures beat market consensus beat underlying numbers beat our own tilt (`strategy.md` §5). Surprising claims verified twice. No betting content.

---

## 5. The decisions, and what each one rests on

| Decision | Cadence | Rests on (in order) | Guardrails |
|---|---|---|---|
| Squad structure (premiums, formation, bench shape) | WC/FH chats, monthly check | where the points are this season by price band · 15 playing players · bank ≥ £0.3 | dead-money cap: no more than one non-playing player (the second GK) |
| Transfer (A / B / roll) | weekly | triggered (injury, minutes loss) vs speculative · 4-GW horizon · archetype named · realised-EV history of our past transfers | hits need written EV > 4; no hit within 24h of a red week; deviation written before acting |
| Captain + vice | weekly | pool (Haaland default, Bruno home vs promoted) · fixture · league-EO · kickoff timing | off-pool = sword move with written trigger; vice nailed |
| XI + bench order | weekly | minutes tags · fixtures · autosub mechanics | nobody below "likely" starts |
| Chip | per plan | `chip-plan.md` window + written rationale + one night's sleep | never reactive; TC/BB cancellable, WC/FH not |
| Rule changes | review chats only | `decisions.csv` aggregates | changelog line, dated |

How a disagreement is handled: Erik decides; the override is logged as its own decision row ("Erik override", with both EXPs). Over a season that row set tells us whether the instinct or the model is better where they differ — which is exactly what Erik started this project to learn.

---

## 6. Staying ahead: against the field and against nine people

Against the field we do not out-forecast anyone; we **decline the field's errors** (process floor) and **time chips from plan**. Against nine named rivals the game is different and most of them do not play it:

1. **Chip asymmetry — the live edge.** We hold all four first-half chips; six rivals have burned one or two. Every chip we fire from a written window on a planned week is worth more than theirs fired after a bad weekend.
2. **Rival Radar, automated.** Rival picks are public after each deadline. `fpl_pull.py` captures them daily; the review brief shows their captains, chips, hits and transfers; the decide chat uses **league-EO** for captaincy: when Alex and Thomas both own and captain Haaland, captaining Haaland protects nothing against them and leverage must come from elsewhere.
3. **Positioning, not churn.** Two or three written differentials from the scout radar and the "cheapest nailed scorer at the right club" rule — the one bias we have already measured.
4. **The calibration dataset.** By GW15 we will know our captain delta, our transfer hit rate and our minutes optimism in numbers. Nobody else in the league keeps that; it is the compounding asset for the second half, when chips 5–8 and the blank/double block decide the league.
5. **Shield when ahead, sword when behind — by rule.** Today: 69 behind → sword posture is active (differential captaincy first, structural differentials second), inside a template core, until the gap is inside 30.

---

## 7. What changes in the project itself

### 7.1 Project instructions (Erik pastes; Claude cannot edit them)
Shrink to the contract and point at the repo. Proposed text:

```
ROLE: FPL co-manager & analyst for Erik, 2026/27. Direct, evidence-based: recommendation A with
reasoning + named alternative B, confidence flagged. Challenge rage moves once; Erik decides.
Chat in Dutch; every file in English.

TEAM: Brobbeytrap · team 6756883 · league 348280 (Fantasy Fellas). Rival of record: Alex (41757);
pack: Jason (6913443), Thomas (888210).

FIRST ACTION IN EVERY CHAT: git clone --depth 1 https://github.com/erikdekock/FPL2627 and read
CLAUDE.md, strategy/rules.md, the last three rows of data/gameweek_log.csv, the latest
briefs/GWxx.md, data/watchlist.csv, strategy/chip-plan.md. Then read the state back in five lines
before any analysis. Never trust memory for prices, flags, ownership or the squad: pull the API.

CHATS: "GWxx" = decide (Thu/Fri, ends with LOCKED + EXP block, verified against the API after the
deadline). "GWxx review" = learn (Tue, grades every decision process x outcome, writes log,
decisions, lessons, rules, the next kickoff). "Strategy Qx" = quarterly. Nothing counts unless it
is committed to the repo; Claude commits.

HARD RULES: the numbered rules in strategy/rules.md; deadline = 90 min before first kickoff,
state UK and NL time; confirmed transfers are final; chips only from written, slept-on rationale;
first chip set expires at the GW19 deadline (verify date in the API).
```

### 7.2 `CLAUDE.md` in the repo
Becomes the operating contract: the two-chat rhythm, file ownership, commit messages, the read-back, the LOCKED template, the EXP format, the verification step. (`docs/05` archived as `docs/archive/05-…`.)

### 7.3 Skills (installed by Erik as a plugin `fpl-2627`; drafted in `skills/` in the repo, as in the studio)
| Skill | Triggers | Owns |
|---|---|---|
| `fpl-gw-review` | "GWxx review", a kickoff that says review, Tuesday after lockdown | the review steps, the grading rubric, the counterfactual query, the log/decisions/lessons writes, the kickoff template |
| `fpl-gw-decide` | "GWxx", a kickoff that says decide | the data pull (API URLs, snapshot, sources), minutes gate, the five decisions, the LOCKED and EXP templates, the verification step |
| `fpl-strategy-review` | "Strategy Qx", every fourth review | the bias review aggregates, the edge grading, chip-plan rewrite, changelog discipline |
Skills carry the *how*; `rules.md` carries the *what*; the kickoff carries the *state*. Lessons that would have saved a round go into the skill that owns them (studio rule, same here).

### 7.4 Tooling (Claude builds, small)
- `scripts/fpl_pull.py`: add the nine rivals' `/history/` and `/event/{gw}/picks/`, our `/transfers/` per GW, and write `data/rivals.csv`.
- `scripts/review.py`: given a GW, print the grading table (our picks with points, autosubs, every decision's A and B points, rivals' captains and chips) so the review chat starts from numbers, not from scrolling.
- `scripts/kickoff.py`: prints the kickoff prompt skeleton from the repo state (deadline UK/NL, phase, chips left, FTs, bank, open watchlist, last lesson).

---

## 8. Templates

**EXP (in LOCKED, one line per decision):** `EXP-T1 Gibbs-White ≥ 6 pts GW6–7 (p=0.6) · EXP-C Haaland ≥ field captain (p=0.5) · EXP-X no autosub loss (p=0.9) · EXP-GW ≥ 55 vs expected average ~50 (p=0.6)`

**LOCKED (last message of a decide chat):**
```
LOCKED GW07 · deadline Sat 17 Oct 11:00 BST / 12:00 NL · chip: none
OUT → IN: … (FT, hit 0)   bank after: £0.4
C: … · VC: …
XI (3-4-3): GK · DEF … · MID … · FWD …
Bench: 1. … 2. … 3. … · GK …
EXP: …
Verify after deadline: picks + transfers from the API → appended to briefs/GW07.md
```

**Kickoff (written by the review chat, Dutch, pasted by Erik):**
```
GW08 · Fase 2 · deadline vr 23 okt 18:30 UK / 19:30 NL · je bent de GW08-beslischat
Lees eerst: CLAUDE.md, strategy/rules.md, briefs/GW07.md, laatste 3 logrijen, watchlist, chip-plan.
Stand na GW7: … pt · OR … · league P… (−… op Alex) · bank £… · FT … · chips: …
Draagt over: … (max 3)
Regel die deze week niet mag breken: …
Read-back eerst: vat de stand in 5 regels samen en noem wat je niet kon vinden.
```

---

## 9. KPIs for the operating system itself (graded at every bias review)
Log rows 100% · decisions graded within 48h of lockdown 100% · LOCKED present every GW · post-deadline verification every GW · kickoff written every week · a lesson per week · rule changes only via review chats · time per week ≤ 75 min (review ≤ 25, decide ≤ 45, T-90 5) · two consecutive 10-minute weeks trigger simplification, never silence.

---

## 10. Open questions Erik did not ask, and should
1. **Beane.** The engine was designed before the operating loop existed. Proposal: park Beane until the loop has run four clean weeks; `decisions.csv` is its training signal, and it only earns a seat when it beats the written A/B record.
2. **Model choice per chat.** Judgment chats (decide, review, strategy) on the strongest model; data-only runs can be cheaper. Erik does this in the studio already.
3. **Time budget.** The old protocol was 82 minutes and was never run; the new one is ≤ 75 and is designed around two short, named chats. If that still slips, the 10-minute week is the floor, not silence.
4. **When Erik is away.** A reduced-week rule exists; a "no chat this week" rule does not. Proposal: if no decide chat happened by T-24h, Claude's review chat of the previous week already wrote a default LOCKED (roll, pool captain, flags handled) that Erik executes from his phone.
5. **The second league (1492621).** Not in the snapshot script; add it or declare it out of scope.
6. **What counts as a win in May.** League first, always; but the rank bands were set for a 10k season and are now a 3.5M season. Re-set them at the Q1 review (w/c 12 Oct) honestly, or they stop steering anything.

---

## Adoption path
Week 1 (this week): WC1 reset runs on the new rules by hand (minutes gate, LOCKED, verification, log, decisions rows). Week 2 (GW7): `rules.md`, `lessons.md`, `decisions.csv`, `briefs/` exist; first `GW06 review` chat is run from this document. Week 3: the three skills are drafted in `skills/` and installed; `fpl_pull.py` captures rivals. GW9: first bias review. Q1 review chat w/c 12 Oct re-sets the rank bands and grades the six edges.
