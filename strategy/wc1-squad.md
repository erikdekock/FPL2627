# WC1 squad — GW7 (deadline Sat 17 Oct 2026 11:00 BST / 12:00 CEST)
**v0.1 · Wed 14 Oct 2026 · build in progress, band by band in chat; v1.0 freezes Friday after the pressers (minutes gate, two sources per player).** Research: `briefs/GW07.md`, pool `data/xp/wc_candidates_gw07.md`, solver `data/xp/wc_drafts_gw07.md`. Budget: est. £99.1 (to be confirmed from the app), bank floor £0.3 → £98.8 to spend.

> The GW6 version of this file (the squad that was executed on the Free Hit, not the Wildcard) is preserved in git history (commit 6ed6587 and earlier). The GW7 build starts from the same evidence base one week on.

## Decisions taken (Erik decides; A/B and reasoning in the chat and in `briefs/GW07.md` §7)
| # | Decision | Taken | Reasoning in one line | Confidence |
|---|---|---|---|---|
| D-WC1 | Haaland in or out, given the City verdict | **In** (14 Oct 15:59) | In-season off-pitch sanctions have not moved on-pitch output historically (Everton 23/24, Forest 24, Chelsea 22, Juventus 22/23); the sanction timeline is years; City won at Anfield after the verdict and lead 18/18, 16–5; Haaland 45 pts, 0.91 xGI/90, 9/9 rivals; the solver costs his absence at −8 objective plus −2 to −3 xP/GW on the armband. The "City trouble" thesis is expressed as **City exposure = Haaland only**. | high (0.8) |

**Exit conditions for Haaland (watchlist row to follow):** two of three matches under 60 minutes without an injury · a confirmed January exit · Maresca leaves · City lose 3 of 5.

### Second-star midfielder — Erik's shortlist (14 Oct 16:39, from the comparison page `Second star midfielder`)
Erik read the five perspectives (xP, differential, value per £, fixtures, points so far) and shortlisted **Mbeumo, Groß, Cherki, Gibbs-White, Rogers**. Saka (top on xP, 2/9 rivals) was not shortlisted; Bruno and Palmer dropped. Consequence: the shortlist has no £9.5+ midfielder, so the build is **structure B (no second star, money spread over the £6.0–8.0 band)**; solver cost of that vs Saka: −3.3 xP over GW7–12 (287.5 vs 290.8), −0.2 in GW7.

| Rank | Player | £ | xP 7–12 | Captain weeks (≥ Haaland −1) | Rivals | xP/£ | Pts (ppg) | Σ diff | Load | Reading |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Mbeumo MUN | 7.9 | 23.9 | GW8, 9, 10, 12 | 0/9 | 3.03 | 33 (5.5) | 20 | UCL | top four on every perspective; the only sword with a captain ceiling |
| 2 | Groß BHA | 6.0 | 22.7 | GW10, 12 | 7/9 (Alex) | 3.78 | 53 (8.8) | 19 | UECL Thu | best value and best raw scorer; template, so shield not sword; Brighton Thursday rotation, Mitoma/Minteh out to 24 Oct |
| 3 | Gibbs-White NFO | 8.0 | 21.6 | GW10, 12 | 1/9 | 2.70 | 30 (5.0) | 20 | none | real differential, no Europe; 2 pts in GW6, −102k transfers out; ARS(H) first |
| 4 | Cherki MCI | 7.9 | 19.5 | — | 1/9 | 2.47 | 44 (7.3) | 18 | UCL | best per start (5 starts, 392 min: the model prices the minutes risk); City exposure would be 2 against D-WC1; +340k transfers in this week |
| 5 | Rogers CHE | 7.9 | 18.9 | — | 6/9 (Alex) | 2.39 | 38 (6.3) | 18 | none | easiest run and fresh, but lowest xP of the five and template: no sword value |

Model note: Cherki's and Rogers' xP sit below their points because the model shrinks 5–6 starts toward the position average; their real output so far is higher than the table says. That is an argument for the top two of them in band 2, not against the ranking.

| # | Decision | Taken | Reasoning in one line | Confidence |
|---|---|---|---|---|
| D-MID1 | Mbeumo + Groß in | **In** (14 Oct 16:39) | Mbeumo: top four on all five perspectives, 0/9 rivals, four captain weeks. Groß: best value and raw scorer; template (7/9) so he is the shield pick in midfield. They are complements, not alternatives. | high |
| D-MID2 | Third attacking mid: Gibbs-White or Cherki | **Cherki** (14 Oct 16:43) | Erik's call on form (44 pts in 5 starts, 7.3 ppg, 1/9 rivals, lightest fixtures Σ18). **Written deviation (rule 5) from D-WC1:** City exposure becomes 2 (Haaland + Cherki). Claude's objection, stated once: it contradicts the "City trouble" thesis and the model prices his minutes (392 of 540) at 19.5. Thesis for the watchlist: City's creator at 0.69 xGI/90 behind Haaland; **exit:** benched twice in three without injury, or any sanction news that changes City's XI. | medium (0.55) |

Running total after D-MID2: Haaland 15.6 + Mbeumo 7.9 + Groß 6.0 + Cherki 7.9 = **£37.4** · £61.4 left for 11 (2 GK, 5 DEF, 2 MID, 2 FWD), avg £5.58 · bank floor £0.3 → £61.1 to spend.

### Differentials — Erik's reading of the page `Differentials nobody owns` (14 Oct 16:54)
Fourteen players with 30+ pts, ≤ 1 of 9 rivals, < 21 % field. The league's differentials sit in defence: Tarkowski 46 (0/9), Bogle 43 (1/9), Vuskovic 40 (0/9), Justin 32 (0/9, 1.6 % field), Trafford 30 (0/9). Attacking options Semenyo (City exposure 3) and Cunha (United exposure 2) were not taken.

| # | Decision | Taken | Reasoning in one line | Confidence |
|---|---|---|---|---|
| D-DEF1 | Tarkowski + Vuskovic in | **In** (14 Oct 16:54) | Tarkowski: top-scoring defender in the game and 0/9 rivals, DefCon 11.3/90, 22.1 xP — the biggest anomaly on the page. Vuskovic: Erik's conviction pick ("talented, I see it happening around him"): 40 pts, nailed CB at the best defence in the league (5 conceded in 6), Struijk suspended GW7, 0/9 rivals, 4.6 % field. Model caveat stated: Vuskovic's xP (18.6) is the lowest of the five defenders the solver wants and it benches him in four of six GWs — he is a conviction differential and needs his thesis + exit in `watchlist.csv`. | Tarkowski high · Vuskovic medium |
| D-DEF2 (provisional) | Bogle £4.7 as defender 3 | provisional, confirm in band 5 | Best value on both pages (4.51 xP/£, 43 pts); both solver runs with the six locks include him, plus Thomas (COV, £4.0) and De Cuyper (BHA, £5.1, 5/9 rivals). FFScout Bijol note is the Friday check. | medium-high |
| D-GK (provisional) | Trafford £5.0 + Tzolakis £4.7 | provisional, confirm in band 5 | Both solver runs; 0/9 and 2/9 rivals; rotate by fixture (rule 7 allows it); Butland and Rodon out help both. | medium-high |

Running total after D-DEF1: £37.4 + Tarkowski 6.2 + Vuskovic 5.1 = **£48.7** · £50.1 left for 9 (2 GK, 3 DEF, 2 MID, 2 FWD), avg £5.57; with Bogle, Trafford and Tzolakis provisionally in: **£63.1**, £35.7 left for 6 (2 DEF, 2 MID, 2 FWD), avg £5.95.

| # | Decision | Taken | Reasoning in one line | Confidence |
|---|---|---|---|---|
| D-FORK | Saka or João Pedro | **João Pedro** (14 Oct 17:15) | Erik: João Pedro wins the first four rows (points 45, 9.0 ppg, 12 in GW6, form) and the rest is close; "Saka underperforms when expectations are high". Claude's advice was Saka (0.65) for the second captain option; the shield reading (8/9 rivals) is accepted as the league logic. Structure (ii): no £9.5+ midfielder; Tavernier + Ødegaard class fill the last two midfield slots. Caveat on record: João Pedro has 5 goals on 2.77 xG. | medium (0.5) |
| D-DEF3 (leaning) | De Cuyper £5.1 | Erik "very interested" (17:15), not yet confirmed | Best defender in the model (22.7 xP), 53 pts, 5/9 rivals; would make Brighton three (Groß, Vuskovic, De Cuyper) = club maximum. | — |

Running total after D-FORK: £48.7 + João Pedro 7.8 = **£56.5** decided; incl. provisional Bogle, Trafford, Tzolakis **£70.9**; £27.9 left for 5 (2 DEF, 2 MID, 1 FWD), avg £5.58 — or £22.8 for 4 if De Cuyper confirms.

Solver with the six locked (budget £98.8), the fork that was left: **(i) Saka** £9.6 + E.Le Fée 5.7 + Barry + Emersonn, De Cuyper + Thomas + Bogle, Trafford + Tzolakis → objective 288.1, GW7 XI 71.5; **(ii) no Saka:** Tavernier 6.1 + Ødegaard 6.8 + Barry + João Pedro 7.8, same defence and keepers → 285.8, GW7 XI 71.5. Same GW7, −2.3 over six weeks for (ii); (ii) buys the 8/9 shield striker and loses the second captain option.

Solver with the four locked (budget £98.8): it still buys **Saka** as the fifth midfielder (objective 289.1, GW7 XI 72.2) with Tavernier, a £4.0–6.2 defence (De Cuyper, Tarkowski, Thomas, Bogle, Justin), Trafford/Tzolakis, Barry + Emersonn. With João Pedro also locked: 287.6, Tarkowski drops to Davis. So the second star is back on the table by budget, not by the shortlist.

## Open, in order
1. ~~The fork~~ → João Pedro taken.
2. Under-the-radar slots (page `Under the radar`, 17 names incl. strikers): one midfielder and the third forward from Barry / Emersonn / Kostoulas / Evanilson / Gonzalo, and the midfield pair from Tavernier / Dewsbury-Hall / Janelt / Le Fée / Stach / Gomez class.
3. Defenders 4 and 5: De Cuyper £5.1 (leaning) + Thomas £4.0 / Justin £4.5 / Muharemović £5.0 / Branthwaite £5.5.
4. Confirm the provisional names (Bogle, Trafford, Tzolakis); bench order; captain plan; watchlist rows.
4. Band 4 enablers (£5.0–5.9).
5. Band 5 budget / bench (£4.0–4.9), keeper pair.
6. Captain plan GW7–12 (which GWs off-pool, written before GW7) and 3–4 differentials with thesis + exit in `data/watchlist.csv`.

## Squad (fills as decisions land)
| Pos | Player | Club | £ | Tag (sources) | Rivals (of 9) | Role |
|---|---|---|---|---|---|---|
| FWD | Haaland | MCI | 15.6 | nailed (6/6 starts, 529 min; Maresca 13 Oct: no flags) | 9/9 | anchor, default captain |
| MID | Mbeumo | MUN | 7.9 | nailed (6/6, 540 min; no flag) | 0/9 | sword, off-pool captain GW8/9/10/12 |
| MID | Groß | BHA | 6.0 | nailed (6/6, 540 min; UECL Thursday rotation to watch) | 7/9 | shield, value |
| MID | Cherki | MCI | 7.9 | nailed by flag, 5/6 starts (392 min) — presser check Friday | 1/9 | form pick; City exposure 2 (deviation logged) |
| FWD | João Pedro | CHE | 7.8 | nailed (5/6, 431 min; 100 % after the knee flag) | 8/9 | shield striker |
| DEF | Tarkowski | EVE | 6.2 | nailed (6/6, 540 min; no flag) | 0/9 | differential, DefCon floor |
| DEF | Vuskovic | BHA | 5.1 | nailed (6/6, 527 min; Struijk suspended GW7) | 0/9 | conviction differential |
| DEF | Bogle (provisional) | LEE | 4.7 | nailed (6/6, 450 min; Bijol note) | 1/9 | value, confirm Friday |
| GK | Trafford (provisional) | LEE | 5.0 | nailed (6/6; Rodon out) | 0/9 | GK1 by fixture |
| GK | Tzolakis (provisional) | HUL | 4.7 | nailed (6/6; Butland out to Dec) | 2/9 | GK2 by fixture |

Spent £56.5 decided (£70.9 incl. provisional) · remaining £27.9 for 5 players (2 DEF, 2 MID, 1 FWD).
