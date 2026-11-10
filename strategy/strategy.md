# Season Strategy — FPL 2026/27
**v3.0-ACTIVE · 10 Nov 2026 (Q2 review: §1 goals, §3 edge grades, §8 phases, §10 indicators) · supersedes v2.1 (15 Aug 2026)**
Six days before GW1. Q0 decisions taken 15 Aug: rank target, risk posture, conflict rule (changelog). Still open: rival names + team ID. Everything else is operative now. This revision applies the same treatment the protocol received: criticised, validated where possible, qualified where not, and fleshed out where v1.0 was thin.

**What changed from v1.0 and why (revision notes):**
1. Every edge now carries a **failure condition and early-warning indicator** — v1.0 stated edges as if they couldn't die. A strategy that can't be wrong isn't a strategy.
2. Every edge carries an **evidence status** — validated, mechanical, or assumption-to-be-measured. v1.0 mixed these silently.
3. Added the **objective-conflict rule** (§1) — v1.0 had two objectives and no rule for when they collide.
4. Added the **decision-inputs hierarchy** (§5) — v1.0 said "we won't out-model the market" but never said what we *do* use instead.
5. Added a **pre-mortem** (§9) and **KPI targets** (§10) — v1.0 had KPIs without pass/fail lines, which makes quarterly grading a mood.
6. Squad doctrine gained the captain pool, bench philosophy, cash buffer and team-value stance — the operational gaps a real week would have exposed immediately.

---

## 1. Objectives — and the rule for when they conflict

- **Primary: win the mini-league** (Fantasy Fellas, league 348280, ten managers). **The rival of service is whoever leads the league** (9 Nov: Jason, 27 ahead; Alex, 9 behind us, is watched for his open WC and FH). *(D-G1, D-G4, decided 9 Nov.)*
- **Secondary: an honest overall-rank band for GW38**, set once GW10 is final (the 15 Aug top-10k target is retired as a goal; it stays a stretch marker). OR 806k after GW10 came from one 123-point week, so the band is set from the season-plan, not extrapolated.
- **Tertiary: a complete decision log by GW38** proving which reasoning patterns earn points. Achieved by discipline alone; immune to variance; the compounding asset for season two and Project Beane.

**Conflict rule — decided 15 Aug: the league always wins.** Whenever league-EV and rank-EV genuinely diverge — mirror-vs-EV captaincy, blocking moves, chip timing against a rival — the league decision is taken, at any gameweek. Accepted consequence, stated plainly: the top-10k push runs at full aggression only where the league is not at stake; in direct-conflict weeks the league throttles it. Most weeks there is no conflict — good percentage play serves both — so the rule bites rarely but absolutely.

## 2. Premise — the game we are actually playing

Millions of managers, a decade-old ecosystem of projection services, and a market (ownership, prices, captaincy) that aggregates all of it. In year one we will not out-forecast that market. Two exploitable facts remain, and they are the whole strategy:

1. **The field donates points through unforced errors** — late transfers on tilt, unsaved teams, reactive chips, missed deadlines. These losses are voluntary; a system can decline to pay them.
2. **The field is predictably wrong in specific, nameable situations** — early-season overreaction, fatigue mispricing after a summer tournament, rule-change lag, and (in small leagues) emotional play. We position against those situations only, and stay with the crowd everywhere else.

A useful validated benchmark for how modest the bar is: simply matching the gameweek average every week lands a manager in roughly the top half by season's end. The edges below are designed to clear that floor structurally and then compound above it.

## 3. Theory of victory — six edges, each falsifiable

**Format per edge:** Claim → Mechanism → Operationalised by → Measured by → **Breaks when / early warning** → Evidence status.

### Q2 grades (10 Nov 2026, evidence in `docs/11-process-review-q2.md`)

| Edge | Grade after GW10 | Evidence | What changes |
|---|---|---|---|
| E1 Process floor | **Failed so far** | App differed from LOCKED in every week GW6-10; Free Hit fired instead of Wildcard (GW6); nothing executed in GW8 | Now the first priority: rules 4a and 4b, the T-48h and deadline+1h tasks, execution score as weekly indicator |
| E2 Patience arbitrage | **Not supported** | GW1-5 we were +11 on the overall average and 6th in the league; the early movers (Alex +84 in GW1-4) built the lead | Retired for this season (August is over); at the season review decide whether it returns in 2027/28 |
| E3 Deadline information | **Mixed** | Late information paid (same-day WC1 +22, BB1 +27) but a deadline was misread and three swaps went unwritten | Kept, bounded by rule 4a (deadline is line 1) and rule 17 (same-day chip checks) |
| E4 Calibration | **Working, slowly** | Brier 0.218 on 22 forecasts (coin flip 0.25); GW6 stayed ungraded for a month | Kept; EXP lines become ranges; the review reports Brier weekly |
| E5 Chip discipline | **Failed in set 1** | Three of three chips chosen on deadline day, one of them the wrong chip | Rewritten as rule 17 and chip plan v2; TC1 window rule |
| E6 Small-field game theory | **Supported** | The league, not the average, decided our rank (+21 on the average, 4th to 8th); the GW10 sword captain gained 28 on Haaland | Promoted to the main edge: rival of service = leader (rule 18), rival radar every week |
| **E7 Model-ranked decisions (new)** | **Supported** | xp_model beat FPL's ep_next on GW2-10 (MAE 2.23 vs 2.52); Claude's two captain calls against the model lost 12 and 14 | Rule 21 (model-default captain); transfers ranked by `one_transfer.py`; deviations logged and measured |
| **E8 Cheap nailed starters (new)** | **Supported** | 250 of 652 points came from players under £6m; Haaland incl. captaincy 138 | Squad doctrine §6 stays: nailed budget starters first, premiums second |

### E1 · Process floor — we don't beat ourselves
**Claim:** a meaningful share of the field's points-loss is self-inflicted; we structurally refuse those losses.
**Mechanism:** deadlines never missed, teams always saved, hits only on explicit 4-GW EV, chips only from written windows. Nuance the data forces on us: even elite managers take hits — top-10k finishers average around 10–11 per season — so the edge is not "no hits," it is **no bad hits**: every hit clears the EV bar or doesn't happen.
**Operationalised by:** T-90 check · Save rule · C1 hit bar · chip sleep rule · 10-minute week.
**Measured by:** deadline misses (target 0) · hit count and realised EV per hit · unsaved-team incidents (target 0).
**Breaks when:** it can't break as an edge, but it can be *insufficient* — process guarantees the floor, not the ceiling. Early warning that we're hiding behind it: beating the GW average while losing ground to the target band.
**Evidence status:** directionally validated (hit norms measured in the community); magnitude on ourselves self-measured from GW1.

### E2 · Patience arbitrage — August is for evidence, not conviction
**Claim:** with eight new-manager clubs and post-World-Cup fatigue, GW1–3 output is unusually noisy; the field will reprice on 90 minutes, and early re-pricers will on balance overpay.
**Mechanism:** we bank transfers, hold pre-planned structure, and buy minutes evidence rather than highlight reels. The three-week GW5–6 break plus WC1 window (GW4–6) is the designed reset point at maximum information.
**Operationalised by:** C1 standing rules (bank-first to 1 Sep; no premium at new-manager clubs without minutes evidence) · Q1 review 21–24 Sep.
**Measured by:** FTs used GW1–5 vs plan (≤3) · points of "held instead of chased" decisions, graded at Q1.
**Breaks when:** the obvious early picks simply work — new managers field their evident best XIs and early movers bank three weeks of returns while we sit in cash. **Early warning:** by GW3, the top-transferred-in players are collectively outscoring our equivalent held slots by a wide margin. **Response:** re-grade honestly at Q1 and convert — the edge is a hypothesis about *this* summer, not a religion.
**Evidence status:** assumption, specific to 26/27 conditions. The single most falsifiable edge we hold.

### E3 · Deadline information discipline
**Claim:** identical decisions are worth more made later; the field commits early and pays for it in lineup surprises.
**Mechanism:** decisions at maximum information — Session C after pressers, T-90 for news only, late-kickoff uncertainty explicitly priced into captaincy (a Monday captain is chosen blind).
**Operationalised by:** Session C timing · C2 early/late question · T-90.
**Measured by:** weekly delta = our captain's points vs the most-captained player's points (`field_captain` columns); target cumulative ≥ 0.
**Breaks when:** rarely as a mechanism, but its *value* shrinks in international-break weeks and midweek rounds when everyone has the same information window. No response needed — it just pays less some weeks.
**Evidence status:** mechanical — true by construction; payoff size self-measured.

### E4 · Calibration compounding — the log learns faster than we drift
**Claim:** by December we will know our two or three systematic biases, and correcting a named bias is worth more than any single transfer.
**Mechanism:** every major decision is logged with a stated expectation, then graded in a **process × outcome 2×2**: good process/good outcome (repeat), good process/bad outcome (variance — repeat anyway), bad process/good outcome (**luck — flag, do not repeat**), bad process/bad outcome (fix the process). We optimise the process row and explicitly refuse to learn from lucky outcomes.
**Operationalised by:** C6 stated expectation · A3 calibration check · quarterly grading.
**Measured by:** share of decisions graded "good process," trending up quarter over quarter · at least two named biases identified by Q2.
**Breaks when:** the log stops being honest — post-hoc rationalisation creeps into A3. **Early warning:** zero decisions graded "bad process" for three straight weeks (nobody is that good).
**Evidence status:** validated in forecasting practice generally; our implementation self-measured.

### E5 · Chip discipline — eight rank rockets, fired on schedule
**Claim:** chips fired from planned windows on written rationale outperform chips fired reactively after a bad week, and a large share of the field does the latter — especially with four chips expiring at the GW19 deadline (2 Jan).
**Mechanism:** windows pre-planned in chip-plan.md, weekly one-line check, overnight rule, no reactive fires. The expiry cliff is treated as a scheduling constraint from week one, not a December panic.
**Operationalised by:** C5 · chip-plan.md firing rule.
**Measured by:** each chip's points vs its no-chip baseline, logged in chip-plan.md · zero chips expired unused · zero unplanned fires.
**Breaks when:** rigidity — a genuinely superior unplanned window appears (injury-created double, fixture chaos) and we refuse it on principle. **Guard:** the plan may be amended *before* firing via the overnight rule; discipline means written-and-slept-on, not immovable.
**Evidence status:** assumption with strong community priors; our own baselines measured per fire.

### E6 · Small-field game theory — the mini-league is a different sport
**Claim:** against millions we play percentages; against a handful of named rivals we play people, and most small-league players never do.
**Mechanism:** weekly Rival Radar (their transfers, captains, chips). Ahead → shield: mirror the chasing rival's likely captain, deny variance, make *them* need luck. Behind → sword: differential captaincy first (cheapest leverage), structural differentials second. Rival archetypes noted at Q1 (optimizer / template-hugger / casual / maverick) because the counter differs: a casual is beaten by E1 alone; a maverick is beaten by shielding and waiting.
**Operationalised by:** A6 Rival Radar · C2 league rule · §7 triggers.
**Measured by:** gap to primary rival, weekly · league position at each review.
**Breaks when:** rivals are inactive (mirroring an inactive manager is meaningless — revert to pure percentage play) or the league is large enough (~15+) that it behaves like the global field. **Early warning:** rival transfer count near zero by GW5.
**Evidence status:** game-theoretically sound; depends entirely on rival behaviour — intel gathered from GW1.

## 4. Explicitly not our edge — with consequences

1. **Projection accuracy.** Consequence: we consume the market's consensus (§5) instead of fighting it; Beane earns a seat at the table only after beating baselines in backtest.
2. **Price-change surfing.** Consequence: team value is exhaust, never fuel — no player is held to protect TV, no player is bought for a rise; the only price-driven act allowed is *timing* an already-decided move.
3. **Differentials as identity.** Consequence: default squad is high-ownership; every deliberate differential must name which edge (E2 or E6) justifies it, in writing.

## 5. Decision-inputs hierarchy (year one)

When inputs disagree, higher beats lower:
1. **Minutes evidence** — confirmed lineups, presser quotes, pre-season/recent starts. Minutes dominate everything.
2. **Fixture context** — opponent's actual defensive/attacking form, venue, congestion.
3. **Market consensus as prior** — EO, most-captained, net transfers: the aggregated forecast of everyone else's models. We deviate from it only where an edge says so.
4. **Underlying per-90s** — xG/xA (Understat), DefCon rates: tie-breakers and regression checks, not headlines.
5. **Our own adjustments** — doctrine tilts (§6) and edge positions, always written down.
*Project Beane graduates into slot 3–4 only after beating the Marcel baseline and calibration tests in backtest (engine/RESEARCH.md).*

## 6. Squad doctrine 2026/27

1. **Two premiums in a flat market** (only Haaland £15.5m and Bruno £12.0m sit above £9.5m); overload the £6.0–8.5m value band. Re-test at Q1.
2. **Captain pool (new):** the armband rotates only within a pre-defined pool — Haaland (default), Bruno (home fixtures vs promoted sides per the official anchors). Off-pool captaincy = a sword move requiring a §7 trigger plus written rationale. Pool reviewed quarterly.
3. **BPS-shift tilt:** the bonus rewrite favours keepers, attacking full-backs and attackers and shaves elite centre-backs — price lists lag rule changes (the Gabriel £8.0m pass is this rule applied).
4. **DefCon midfielders as floor plays** (Stach/Caicedo archetype: 2-point floors at £5.5–6.0m).
5. **Stability weighting early:** Arsenal, Villa, Brentford, Everton, Leeds over-weighted until the eight new-manager clubs show minutes patterns.
6. **Fatigue asymmetry:** deep WC runners (Spain, Argentina, England, France) discounted GW1–3; fresh elites who barely played are the buy side (the Watkins position).
7. **Bench philosophy (new):** bench slots are insurance, priced accordingly — one playing £4.0–4.5m defender ordered first, a genuinely non-playing £4.0m keeper, and no bench player bought for upside we'd never start.
8. **Cash buffer (new):** keep ≥ £0.3–0.5m in the bank as injury flexibility; a fully-spent squad turns every injury into a hit.
9. **Window buffer:** until 1 Sep, 1–2 flexible slots + standing watch on post-launch entrants at near-zero ownership (António Silva is the live case).
10. **Differential budget (decided 15 Aug):** the 2–3 sword slots are sourced from our named edges — E2 fatigue/new-manager reads, E6 rival gaps, rule-change lag, post-launch entrants — never from boredom. A differential without a one-line thesis and an exit condition is not a position, it is a mood, and it doesn't make the squad.

## 7. Risk posture & triggers

**Default: calculated aggression — decided 15 Aug.** The XI carries **2–3 deliberate differentials at all times**, each with a written thesis and exit condition in the watchlist; off-pool captaincy is a legitimate rank tool (still requiring written rationale, rule 9). The qualifier matters: aggression is expressed in *positioning*, never in *churn*. The hit bar, sleep rules and bank-first discipline all stand — top-10k managers average ten-plus hits a season, but they are EV-positive hits; the elite game is more disciplined than the template game, not less. The league-first rule (§1) is the standing override on all of it. Triggers:

| Trigger | Condition | Response |
|---|---|---|
| League chase | > ~30 pts behind primary rival at a review checkpoint (default, adjustable) | Leverage escalates: differential captaincy first, structural differentials second; never a full rebuild |
| League protect | > ~50 pts ahead, or league genuinely at stake late | **League-first override in action:** mirror the chasing rival's likely captain, deny them variance — even at rank cost |
| Rank trajectory behind | Below the §10 checkpoint band at a review | Escalate: +1 differential slot, captaincy leverage weighted up |
| Rank trajectory ahead | Inside band while the league is tight | De-escalate toward shield until the league is secured, then resume |
| Edge abandonment | An edge's early-warning fires and survives one review | Delete or invert the edge, in the changelog, without sentimentality |
| Anti-tilt (standing) | Bottom-decile gameweek | No hit confirmed within 24h without a night's sleep |

## 8. Season phase map — with exit criteria

| Phase | GWs | Bias | Exit criteria (what "on track" means) |
|---|---|---|---|
| 1 Evidence | 1–5 | done | 310 pts, 6th in the league (see `docs/06`) |
| 2 Reset & structure | 6–10 | done | 652 pts, 2nd, 27 behind the leader; FH1, WC1, BB1 used |
| **3 Congestion & chip cliff** | **11–19** | Execution first; one transfer a week; TC1 in its best window; rotation vigilance at GW17–19 | No chip expires · execution score ≥ 90% (app = LOCKED with screenshot) · at least 2nd in the league at GW19 |
| 4 Winter rebuild | 20–26 | Set 2 opens; January entrants; build towards WC2 | WC2 only on a written rationale · gap to the leader ≤ 25 · blank/double calendar confirmed on premierleague.com |
| 5 Spring chip block | 27–33 | WC2 around GW31, FH2 on the big blank (see chip plan v2) | Every chip lands on a verified blank or double |
| 6 Endgame | 34–38 | League-first with full weight; BB2 and TC2 on the doubles | Every decision graded against the leader, not the field · all chips used |

Dates, deadlines and week types per gameweek: `strategy/season-plan.md`.

One line at the top of every GWxx chat names the phase.

## 9. Pre-mortem — it's May 2027 and we failed; what most likely happened?

1. **The log died in October.** No calibration, no E4, season two starts from zero. *Indicator:* a missing row. *Countermeasure:* unskippable-row rule; a missing row is a KPI failure by definition.
2. **Tilt spiral.** Three red weeks → hits stack → structure gone by November. *Indicator:* first rule-deviation note in the log. *Countermeasure:* anti-tilt rule + the deviation-must-be-written rule (§11.8) making panic expensive.
3. **E2 inverted and we doubled down.** Early movers profited; we held cash out of stubbornness past Q1. *Indicator:* the E2 early warning (§3) firing by GW3. *Countermeasure:* Q1 is a mandatory re-grade with delete authority (§7 edge abandonment).
4. **Captaincy bled invisibly.** Small weekly losses to the field captain compound to a rank-killing deficit. *Indicator:* cumulative captain-vs-field delta below −10 by GW6. *Countermeasure:* the delta is logged weekly and reverts us to pure shield when negative.
5. **A locked squad met an injury cluster.** Zero bank + zero flexibility = forced hits at the worst prices. *Countermeasure:* cash buffer + bench playability minimums (§6.7–6.8).
6. **The protocol got abandoned, not simplified.** *Countermeasure:* the two-consecutive-10-minute-weeks rule triggers simplification, and the 10-minute week is defined as legitimate.
7. **We chased 10k and lost the league to a template cousin.** The named tension of this strategy: aggression raises league variance against a small field that a solid template often beats. *Indicator:* league gap negative while overall rank climbs. *Countermeasure:* the league-first rule (§1) brakes the aggression wherever the league is genuinely at stake — by rule, not by mood.
8. **Differential addiction.** Sword slots multiplied without theses; being different became the identity §4.3 bans. *Indicator:* any differential in the XI with no written thesis. *Countermeasure:* the differential budget cap (§6.10) and standing rule 9.

## 10. KPI scoreboard (graded every quarterly review)

| KPI | Target | Source |
|---|---|---|
| Deadline misses / unsaved teams | 0 (any breach = system failure) | log |
| GW score vs GW average | ≥ average in ≥ 60% of GWs (validated top-half floor) | log |
| Overall rank trajectory | ~top 500k at Q1 · top 150k at Q2 · top 50k at Q3 · top 10k at GW38 (bands are posture-escalation gates, adjustable at reviews) | FPL |
| Differential performance | Sword slots collectively outscore their template equivalents over each quarter | log + watchlist theses |
| Gap to primary rival | Positive at Q2; league won at GW38 | Rival Radar |
| Captain vs most-captained (cumulative) | ≥ 0, earned through chosen leverage rather than mirroring — negative single weeks are expected and accepted | log columns |
| Hits | Each clears the 4-GW EV bar; realised EV ≥ 0 in aggregate | log |
| Bench points wasted | Bottom-quartile instinct check: reviewed, no fixed target year one | log |
| Chips | 0 expired unused · 0 unplanned fires · aggregate vs baseline > 0 | chip-plan |
| Decision quality (E4) | "Good process" share rising each quarter; ≥ 2 named biases by Q2 | A3 grading |
| Log completeness | 38/38 rows | repo |

### Weekly leading indicators (added Q2, D-G3; reported in every review)
| Indicator | Green / red | Baseline GW6-10 |
|---|---|---|
| Execution score (app = LOCKED, with screenshot) | >= 90% / < 70% | 0 of 5 weeks fully |
| Captain result vs sum of league captains | >= league mean / > 10 below | us 90, league 34-84 |
| Bench points, 4-week sum | <= league mean | us 36, league mean 43 |
| Brier of EXP lines excluding execution | <= 0.22 | 0.218 (n=22) |
| Days between written chip rationale and play | >= 1 | 0 in 3 of 3 |
| Gap to leader and to Alex | trend, no threshold | -27 and +9 (provisional) |

## 11. Standing discipline rules (consolidated)

1. Bank-first on transfers while the window is open (to 1 Sep); rolling is a decision, not a failure.
2. No premium at a new-manager club without minutes evidence.
3. Every Arsenal pick passes the neutral-club test.
4. Hits need explicit 4-GW EV clearly above 4 points; close calls are a no.
5. Chips fire only from written, slept-on rationale in chip-plan.md.
6. No hit within 24h of a red gameweek without a night's sleep.
7. The log row is written every week, including reduced weeks.
8. Deviation from any rule requires writing *why* before acting — rule-breaking is allowed but never free.
9. Off-pool captains require a named trigger plus written rationale.
10. Team value protects nothing and buys nothing; it only times moves already decided.

## 12. Governance

- **Scheduled revision:** every quarterly review (Q1 21–24 Sep · Q2 mid-Dec · Q3 early Mar · Q4 late Apr), each producing a changelog entry.
- **Unscheduled amendment:** allowed only on a written trigger event (edge early-warning fired, rule proven unworkable, rule-change by FPL), never on a bad weekend.
- **Authority:** Claude proposes, Erik decides; the changelog is the audit trail. Silence is not sign-off — **[ERIK]** items stay open until answered.

## Changelog

| Date | Version | Change |
|---|---|---|
| 2026-07-20 | template | Structure created |
| 2026-08-15 | v1.0-PROPOSAL | Theory of victory E1–E6, doctrine, triggers, phase map, KPIs |
| 2026-08-15 | v2.0-PROPOSAL | Per-edge failure modes + evidence status · objective-conflict rule · decision-inputs hierarchy · captain pool, bench, cash-buffer, TV doctrine · expanded trigger table · phase exit criteria · pre-mortem · KPI targets · governance. |
| 2026-08-15 | v2.1-ACTIVE | Q0 decisions encoded: rank target **top 10k** · default posture **calculated aggression** (2–3 differential budget, aggression in positioning not churn) · conflict rule **league always wins**. Trigger table and KPI bands recalibrated to the 10k trajectory; pre-mortem gains the aggression-vs-league tension and differential-addiction modes. Still open: rival names, team ID. |
| 2026-11-09 | v2.2 | Q2 review: §1 goals rewritten (league first, rival of service = leader, OR band instead of top 10k), §10 weekly leading indicators added. Phase exit criteria (D-G2, provisional A) and the rest of v3.0 follow in step C6. |
| 2026-11-10 | v3.0 | Q2 review closed: §3 edges graded (E1 and E5 failed, E2 retired, E6 promoted, E7 model-ranked decisions and E8 cheap nailed starters added), §8 phase map rewritten with the D-G2 exit criteria, links to season-plan and chip plan v2. Decided under Erik's standing delegation of 10 Nov. |
