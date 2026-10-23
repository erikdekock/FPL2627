# Chip Master Plan — FPL 2026/27

## Confirmed rules (official, 20 Jul 2026)

Two sets of four chips (Wildcard, Free Hit, Triple Captain, Bench Boost) — 8 total. First set **expires at the GW19 deadline — API `events[19].deadline_time` 2027-01-01T18:30:00Z = Fri 1 Jan 2027 18:30 GMT / 19:30 CET (corrected 10 Oct 2026; earlier text said Sat 2 Jan)**; no carry-over. One chip per Gameweek. Free Hit cannot be played in GW1; FH1 in GW19 blocks FH2 in GW20.

## Windows (v0 — provisional, to be set in Q0 and revised quarterly)

| Chip | Half | Planned window | Status | Rationale |
|---|---|---|---|---|
| Bench Boost 1 | H1 | ~~GW1~~ → **GW8–12, post-WC1** | Open (re-windowed 14 Oct) | Needs the fifteen playing players the wildcard delivers; on the GW7–12 grid GW10 and GW12 are the softest full-squad weeks, but the Thursday–Sunday clubs (BHA, BOU, CRY, SUN) rotate in exactly those weeks — decide on predicted XIs, not on the grid |
| Wildcard 1 | H1 | GW4–6 → **GW7** | **LOCKED for GW7 (Sat 17 Oct 10:10 NL)** — rationale in the log, 14 Oct; API verification after the 11:00 BST deadline | GW6 was played on FH1 by mistake (see log); the pre-chip 15 returns at the GW7 deadline with the same dead money, so the structural reset moves one week. Window GW4–6 planned since 20 Jul; the reason has not changed, only the gameweek |
| Triple Captain 1 | H1 | ~~GW7 (Haaland H Ipswich)~~ → **GW11 (Haaland H Fulham, Sat 21 Nov) · GW16 (H Hull) · GW19 (H Spurs, last legal week)** | Re-windowed 14 Oct | One chip per gameweek: TC1 cannot ride on the GW7 wildcard. Alex burned TC1 in GW3, so ours is a sword chip he cannot answer; fire from a written rationale the day before, baseline = Haaland's single-captain xP |
| Free Hit 1 | H1 | ~~Hold for fixture-hell GW3–19~~ | **Spent GW6 (10 Oct 2026)** — see log | Activated instead of WC1; no FH insurance left in set 1 |
| Wildcard 2 | H2 | Jan–Feb, to set up the spring block | Open | Shape around BGW/DGW map (Crellin) |
| Bench Boost 2 | H2 | Biggest DGW | Open | Classic |
| Triple Captain 2 | H2 | Premium DGW | Open | Classic |
| Free Hit 2 | H2 | Biggest BGW | Open | Classic |

## Firing rule

No chip fires without a written rationale in this file *before* the deadline. Reactive chip use is banned; a chip proposal mid-week goes through one night's sleep.

## Log

| Date | Chip | GW | Rationale (short) | Outcome (pts vs baseline) |
|---|---|---|---|---|
| 2026-10-10 | ~~WC1~~ **FH1 (executed)** | 6 | Written as the WC1 rationale: squad broken: Brobbey out (hamstring, ~25 Oct), Steele/Senesi/Hughes/Keane 0 xMins = £24.7 dead money, two 10-man GWs already (GW4, GW5), João Pedro on a flag with no playing cover. Window GW4–6 planned since 20 Jul; reset plan written 7 Oct (`docs/07`); solver free draft 73.2 xP vs no-chip baseline 58.0 (+15/GW through GW10); fifteen players with real minutes, bank £0.3. **Rule 17 deviation (rule 5):** rationale written on deadline day, not the day before — the Thu/Fri decide chat did not happen (process failure, logged as a lesson); the decision itself is the planned one, not reactive. Squad: `strategy/wc1-squad.md`. **Correction 14 Oct:** the API (`history.chips`) shows `freehit` activated 09:41 UTC on 10 Oct — the Free Hit was played, not the Wildcard. One-week squad; the pre-chip 15 returned at the GW7 deadline. FH1 is spent; WC1 is still held. | Baseline: best XI from the old 15 = 58.0 xP pre-match; actual pre-chip best XI 51 pts. **Outcome: 59 vs 51 = +8** (GW6 average 58). Graded in the GW06 review as "chip fired, wrong chip" |
| 2026-10-14 | WC1 | 7 | Same structural case, one week later and worse: the Free Hit squad reverts, so GW7 without a chip is Verbruggen, Steele · Davis, Egan, Calafiori, Senesi, Keane · B.Fernandes, Szoboszlai (50 % flag), Gibbs-White, Stach, Hughes · Haaland, João Pedro, Brobbey (out) — four non-players and a flagged starter, bank £0.1 (rules 7, 9, 11 breached by the squad itself). Snapshot 14 Oct 13:30 UTC, `xp_model.py --horizon 6`: no-chip best XI GW7 = **53.7 xP** (Senesi in the XI), free wildcard draft 72.0 xP GW7, objective 290.8 vs 222.7 over GW7–12 ≈ +15–18 xP/GW. League −75 to Alex (rule 18): the wildcard is where the 3–4 structural differentials and the off-pool captain plan get built, not a template copy. Written Wed 14 Oct for a Sat 17 Oct deadline (rule 17 satisfied on timing). **Deviation to log if confirmed:** Erik reports activating the chip on 14 Oct before this line was written (rule 5) — not reactive, the window was planned, but the order was wrong again. Squad: `strategy/wc1-squad.md` v1.0 after Friday's pressers. | Baseline: pre-chip 15 best XI GW7 = 53.7 xP (C Haaland). Outcome: TBD in GW07 review |
| 2026-10-23 | — | — | **Re-window (no fire).** TC1 loss in GW7 recorded: Haaland 13 at home to Ipswich, the original TC week, blocked by WC1 (one chip per GW) because WC1 slipped from GW6 after FH1 was played by mistake. TC1 → GW11 (Haaland v FUL H). BB1 → GW10, built by the GW9 transfers (bench xP 12.9 now, 19.4 after Cherki → Tavernier + Janelt → Iwobi); fallback GW12. Layered planning: every transfer in GW9–10 is also judged on what it does to the BB bench. | — |
