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

## Open, in order
1. Band 1, second star: Saka £9.6 (A) · none, money into band 2 (B) · Bruno £11.9 (dominated) · Palmer £9.7 (model says no, xGI/90 0.37).
2. Band 2 (£7.5–9.4), 2–3 slots incl. the João Pedro shield question (8/9 rivals).
3. Band 3 value core (£6.0–7.4).
4. Band 4 enablers (£5.0–5.9).
5. Band 5 budget / bench (£4.0–4.9), keeper pair.
6. Captain plan GW7–12 (which GWs off-pool, written before GW7) and 3–4 differentials with thesis + exit in `data/watchlist.csv`.

## Squad (fills as decisions land)
| Pos | Player | Club | £ | Tag (sources) | Rivals (of 9) | Role |
|---|---|---|---|---|---|---|
| FWD | Haaland | MCI | 15.6 | nailed (6/6 starts, 529 min; Maresca 13 Oct: no flags) | 9/9 | anchor, default captain |

Spent £15.6 · remaining £83.2 for 14 players (avg £5.94).
