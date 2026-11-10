# Handover — from the GW7 wildcard chat to the chat `GW08` (GW8 review + GW9 decide)
**Written Fri 23 Oct 2026 21:00 NL. Closes the chat that built WC1 (14–17 Oct), decided GW8 (23 Oct) and reviewed GW7.** Read this, `strategy/selection-method.md`, `CLAUDE.md` and `strategy/rules.md` before anything else.

## 0. Where we are (API, snapshot 2026-10-23T18:42Z)
- **GW8 is live** (deadline passed Fri 23 Oct 18:30 BST). Saved team = the GW7 team: no transfer (1 FT rolled), C Haaland, VC Groß, XI 3-4-3 Trafford · Tarkowski, De Cuyper, Muharemović · Groß, Mbeumo, Cherki, Ødegaard · Barry, Haaland, João Pedro · bench Tzolakis, Vuskovic, Janelt (suspended GW8), Bogle.
- **Next deadline: GW9, Sat 31 Oct 2026 11:00 GMT / 12:00 CET** (clocks go back Sun 25 Oct; API `events[9].deadline_time` 2026-10-31T11:00:00Z).
- **2 free transfers for GW9**, bank £0.4, TV £99.1. Chips left in set 1: **BB1, TC1** (WC1 GW7, FH1 GW6). Set 1 expires at the GW19 deadline (Fri 1 Jan 2027 18:30 GMT).
- After GW7: 439 pts · OR 3,168,399 · league P7/10, **−78 to Alex** (517). Jason 485, Richard 463, Billy 461, Kelvin 459, Thomas 454.

## 1. GW7 in one table (the best week of the season)
70 pts vs avg 59 · GW rank 2.28M · OR 3.71M → 3.17M · wildcard +22 on the old squad's best XI (48).

| Player | £ | xP GW7 | Pts GW7 | Verdict | Why (and could we have known?) |
|---|---|---|---|---|---|
| Haaland (C) | 15.7 | 7.6 | 13 (×2) | ✅ sure shot | D-WC1: kept despite the City verdict; the sanction timeline is years, his minutes and xGI (0.91/90) were never in doubt. All 9 rivals also captained him, so it closed nothing in the league. |
| Vuskovic | 5.1 | 5.1 | 11 (autosub) | ✅ conviction pick | Erik's call ("talented, I see it happening around him"); the model had him the lowest defender. Best defence in the league, Struijk out. Came on for Cherki. |
| Mbeumo | 7.9 | 5.1 | 8 | ✅ | Top four on every perspective, 0/9 rivals. The sword asset. |
| De Cuyper | 5.3 | 6.4 | 6 | ✅ | Best defender in the model, 59 pts season; a Brighton defence (5 CS) that is the league's best. |
| Groß | 6.2 | 6.2 | 5 | ✓ | Shield (7/9 rivals), 58 pts season. Did his job. |
| Muharemović | 5.0 | 4.6 | 5 | ✓ | Rule 10 pick (nailed, Rodon out, DefCon 10.4/90). Erik played him over Bogle against LOCKED: +3, luck. |
| Ødegaard | 6.8 | 5.0 | 3 | ❌ under | 1.60 xA and **0 assists** this season: the chances are created, the finishing is not his. Variance more than a wrong pick; Tavernier (the alternative) scored 10. |
| Tzolakis | 4.7 | 4.6 | 3 (bench) | – | |
| João Pedro | 7.9 | 4.4 | 2 | ❌ under | **5 goals on 3.05 xG**: he was running hot, the model said 4.4 and was right. Flagged at the Saka fork ("one runs hot, the other is owed"). Chosen as the 8/9 shield, which is what he is: a miss costs us nothing against the league. |
| Barry | 5.7 | 6.3 | 2 | ❌ under | Opposite of João Pedro: **3 goals on 4.70 xG** — the chances keep coming, the goals are owed. Everton v Chelsea, same result as Tarkowski. Keep. |
| Bogle | 4.7 | 5.2 | 2 (bench) | – | Benched by Erik against LOCKED. |
| Tarkowski | 6.2 | 5.6 | 0 | ❌ | Chelsea scored; no CS, no DefCon. One bad week for a 46-pt defender. **Correlated with Barry** (one defence, one result) — flagged when Branthwaite was rejected. |
| Cherki | 8.0 | 5.3 | 0 (benched) | ❌ **the wrong call** | Rested v Ipswich (Maresca rotated five), subbed at HT v PSG, scored v AEK. **Could we have known? Partly, yes:** 5 of 6 starts and 392 of 540 min were in the data; UCL Tue + early Saturday; FFScout on Saturday called his place "far from secure"; and he broke our own D-WC1 rule (City exposure = 1). What we could not know is *which* game Maresca would rest him in. Lesson in `selection-method.md` §3: fewer starts than games at a rotating UCL club = *likely*, not nailed. |
| Janelt | 5.0 | 4.1 | −1 (bench) | ❌ variance | Red card; suspended GW8, back for GW9. |

**What made the week (keep doing):** the band-by-band build, the perspective pages, the solver as a prior to argue with, the minutes gate, Erik's conviction picks where he sees what the model does not.
**What cost us (fix):** (1) breaking our own club-exposure rule (Cherki); (2) correlated defenders (Everton pair); (3) execution — GW7 app ≠ LOCKED in three places, GW8 app ≠ LOCKED on every line because the deadline was misread (Friday 18:30, not Saturday). The next chat states the deadline from the API in its first line and delivers LOCKED ≥ 3 h before it.

## 2. GW9 decision prep (the next chat runs it after GW8's results)
**Goal: one transfer (two are available), ditch the player least likely to be relevant, buy the one most likely to score.**
Pre-GW8 solver (`scripts/one_transfer.py`, `data/xp/one_transfer_pre_gw09.txt`, GW9–13):
1. **Cherki → Tavernier (BOU £6.2): +5.0 xP over GW9–13, +1.9 in GW9, bank after £2.1.** Same verdict as on 23 Oct. Tavernier: 42 pts, set pieces, 1/9 rivals. Cherki out = City exposure back to 1.
2. Ødegaard → Tavernier +3.2 · Groß → Tavernier +2.8 (worse than 1).
3. Second FT: Janelt → Iwobi (FUL £5.4) +2.2 · Muharemović → Thomas (COV £4.0) +1.9 · or **roll** (2 FT is the cap-friendly default; rule 14: roll is always a named candidate).
Re-run after GW8 with `python scripts/xp_model.py --horizon 6 && python scripts/one_transfer.py`, then a perspective page for the ditch candidates and the replacements (method §5).

**Squad review for GW9 (to redo with GW8 data):** keep Haaland, Mbeumo, Groß, De Cuyper, Vuskovic, Muharemović, Bogle, Trafford, Tzolakis, Tarkowski, Barry (xG owed), Ødegaard (xA owed), João Pedro (shield, 8/9). Ditch: **Cherki** (minutes + rule). Watch: Janelt (back GW9, bench 3).

**Captain GW9:** Haaland vs Mbeumo was a tie on xP in GW8 and the GW8 sword was not executed. The next chat writes the GW9–12 captain plan before it picks (rule 16): which week is the off-pool week and why.

**Chips — the layered view (Erik, 23 Oct): chip weeks are built by the transfers before them, not found afterwards.**
- **TC1 in GW7 was a real loss of 13 points** (Haaland 13 v Ipswich at home, the original TC week). It could not ride on the wildcard (one chip per GW). In expectation the wildcard was still right (+16 xP vs ~+7.6 for TC; actual +22 vs +13); the loss comes from GW6, where the Free Hit was played instead of the Wildcard — had WC1 fired in GW6 as planned, TC1 was free for GW7. Lesson: a chip mistake costs the next chip window too.
- **TC1 → GW11** (Haaland v Fulham at home, Sat 21 Nov, after the break; FPL difficulty 2). Alternatives: GW16 (Hull H), GW19 (Spurs H).
- **BB1 — target GW10 (Fri 6 Nov deadline), built by the GW9 transfers.** Model bench xP (four bench players, GW9–13): current 15 → GW10 12.9 · after Cherki → Tavernier → 14.3 · after Cherki → Tavernier **and** Janelt → Iwobi → **19.4** (GW12 18.7). Caveat: the model scores the suspended Janelt at 0 for every GW (he is back for GW9), so the Iwobi gain is overstated by roughly his 3–4 xP a week. Layer: if the GW9 chat uses both FTs, GW10 becomes the BB week; if it rolls one, GW12 is the fallback. Check before firing: all four bench players nailed, no Thursday-Europe club among them that week (Brighton, Bournemouth, Palace, Sunderland play UECL/UEL the Thursday before GW10), rationale written the night before.
## 3. Open items for the next chat
1. **GW8 review** after lockdown (Tue 27 Oct 09:00 GMT): grade the GW8 rows in `data/decisions.csv` (status "not executed"), log row 8.
2. Bias review at GW9 (every fourth review): two named biases so far — *plan-not-executed* (GW4, GW7, GW8) and *club-exposure deviation* (Cherki).
3. Q1 strategy review is overdue (`strategy.md` still v2.1): run it as `Strategy Q1` after GW9.

## 4. Where everything lives
`strategy/selection-method.md` (the method) · `strategy/wc1-squad.md` (every build decision with its reasoning) · `briefs/GW07.md`, `briefs/GW08.md` · `data/decisions.csv` (graded GW7, open GW8) · `data/watchlist.csv` (thesis + exit per player) · `docs/outputs/gw07/*.html` (the six comparison pages: second star, differentials, under the radar, Saka v João Pedro, last two slots, pairs) · `scripts/one_transfer.py`.

## Kickoff prompt for the next chat (name it `GW08`)
```
GW08 · Fase 2 · je bent de GW08-chat: eerst de GW08-review (na lockdown di 27 okt 09:00 UK), daarna de GW09-beslissing · deadline GW09 za 31 okt 11:00 UK / 12:00 NL (check in de API)
Lees eerst, in deze volgorde: docs/10-handover-gw07-wildcard.md (de overdracht: stand, spelersoordeel GW7, transferprep GW9, chiplagen), strategy/selection-method.md (hoe we kiezen: per prijsband, vergelijkingspagina's met perspectieven), CLAUDE.md, strategy/rules.md, briefs/GW08.md (LOCKED én verificatie: app ≠ LOCKED), laatste 3 logrijen, data/watchlist.csv, strategy/chip-plan.md.
Stand na GW7: 439 pt · OR 3,168,399 · league P7 (−78 op Alex) · bank £0.4 · FT 2 voor GW9 · chips: BB1, TC1
Draagt over: 1) Cherki → Tavernier ligt er al twee weken, opnieuw toetsen met scripts/one_transfer.py en een vergelijkingspagina; 2) tweede FT bouwt richting Bench Boost GW10 (gelaagd denken: welke transfer maakt de bank sterk); 3) captain-plan GW9–12 op papier vóór de keuze, TC1 → GW11.
Regel die deze week niet mag breken: regel 4, plan ≠ uitgevoerd tot de API het bevestigt; LOCKED ≥ 3 uur vóór de deadline, tweede screenshot na elke correctie.
Read-back eerst: regel 1 = de deadline uit de API (UK + NL, uren te gaan), dan de stand in 5 regels en wat je niet kon vinden.
```
