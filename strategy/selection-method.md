# Selection method — how we pick players (v1.0, 23 Oct 2026)
**Origin: the WC1 build of 14–17 Oct 2026 (GW7: 70 pts vs avg 59, +22 on the old squad, OR 3.71M → 3.17M).** This is the method that produced the best week of the season. Every squad build (wildcard, free hit) and every transfer decision runs through it. Read it before any transfer or chip build.

## 1. The shape of a session
1. **Research first, selection together.** Claude pulls everything (API snapshot, xP model, solver, injuries, pressers, fixtures, Europe, rivals) and writes it to the brief *before* any name is chosen. Erik selects in chat, slot by slot.
2. **Increment by price band, in this order:** stars (£9.5+) → mid-premium (£7.5–9.4) → value core (£6.0–7.4) → enablers (£5.0–5.9) → budget/bench (£4.0–4.9). Each step narrows what is left; the running budget is stated after every decision ("spent £X for N, £Y left for M, avg £Z").
3. **One decision per message.** Claude gives A (recommendation, confidence) and B (named, costed); Erik decides; Claude writes the decision code (D-WC1, D-MID1, D-FORK, …) into `strategy/wcN-squad.md` with the one-line reasoning and commits the same turn.
4. **Comparison pages, not prose.** For every open slot Claude publishes a sortable page (HTML artifact, copies in `docs/outputs/gwNN/`) with ~10 candidates and the perspectives below as columns or rows, row winners highlighted, fixtures coloured by FPL difficulty. Erik reads the perspectives aloud and picks; Claude notes the pick and the perspectives that drove it.
5. **Challenge once.** When a pick contradicts the numbers or an earlier decision (Cherki = City exposure 2; Branthwaite correlated with Tarkowski), Claude says so once with the cost in xP, then writes it as a logged deviation if Erik keeps it.

## 2. The perspectives (columns on every comparison page)
| Perspective | What it answers | Source |
|---|---|---|
| **Expected points** (GW next, decayed 6-GW) | who scores from here | `xp_model.py --horizon 6` |
| **Points so far + per game + GW last** | who has actually delivered (the model shrinks thin samples; real output can be higher) | API |
| **Value per £** | xP divided by price | model |
| **Differential (rivals)** | how many of the 9 Fantasy Fellas own him; Alex owns him? (sword ≤ 1/9, template ≥ 5/9) | `data/rivals.csv`, rivals' picks |
| **Field ownership + transfers this week** | where the crowd is going | API |
| **Fixtures GW..GW+5** | opponent, home/away, FPL difficulty 2–5 coloured, Σ difficulty | API fixtures |
| **Captain weeks** | GWs where his xP is within 1.0 of Haaland's (off-pool armband options) | model |
| **Floor share** | % of xP from appearance + clean sheet + DefCon (weekly certainty) vs goals/assists (ceiling) | model components |
| **DefCon/90 vs threshold** | 10 for DEF, 12 for MID/FWD: above it = 2 pts most weeks | API |
| **xGI/90, xG vs goals** | under- or over-performance (Barry 3 G on 4.70 xG = due; João Pedro 5 G on 3.05 xG = running hot) | API |
| **Starts / minutes** | minutes gate (rule 8) | API + pressers |
| **Midweek load** | UCL Tue/Wed or UEL/UECL Thursday before the GW | competition calendars |
| **Set pieces** | pens / corners / FKs order | API |
| **Club limits** | max 3 per club; same-defence pairs are correlated | squad |

Filters that worked as their own pages: **"Second star"** (10 candidates for one premium slot), **"Differentials nobody owns"** (30+ pts, ≤ 1/9 rivals, < 21 % field), **"Under the radar"** (< 10 % field, ≤ 1/9 rivals, any position incl. strikers, with floor share), **head-to-head** (two names on every row), **pairs** (all mid+striker combinations scored by the solver on the *full* squad, with bank and club limits).

## 3. Rules the method enforces
- Minutes gate before ranking; nobody below *likely* starts, nobody below *50-50* is bought.
- A player with fewer starts than games at a UCL club with a rotating manager is **likely**, not nailed, even without a flag (lesson: Cherki 5/6 starts, 0 min in GW7).
- Max one asset from a club whose situation is the reason for doubt (D-WC1: City exposure = Haaland only); breaking it is a written deviation.
- Two players from one defence are one bet (Tarkowski + Barry: 2 pts together in GW7).
- Every differential gets a thesis + exit in `data/watchlist.csv` before LOCKED.
- Bank ≥ £0.3; fifteen players who play; three playing bench outfielders.

## 4. Erik's selection taste (observed, so Claude can frame options for it)
- Reads **points so far, form and expected points** first; value per £ second; fixtures third.
- Prefers "a sure shot" in the last slots (Ødegaard over Tavernier, Barry over Kostoulas) and conviction picks where he sees something the model does not (Vuskovic: right, 11 pts).
- Distrusts players who underdeliver on expectation (Saka) and backs form (Cherki, João Pedro). The model and Erik disagreed four times in GW7; Erik was right on Vuskovic and Muharemović, the model on Tavernier and Saka-class captaincy is still open.
- Wants the comparison as a table with colours and several perspectives, then talks through it.

## 5. Transfers in a normal week (1–2 FT)
Same method, smaller: (1) review all 15 on the perspectives (who is likely *not* to perform in the next 3 GWs), (2) name the one to ditch with the reason, (3) one comparison page of replacements within `selling price + bank`, scored by the solver on the full squad (+objective, +GW xP), (4) roll is always row zero. The script for (3) is `scripts/one_transfer.py` (each OUT × top-6 IN by position, solver delta).
