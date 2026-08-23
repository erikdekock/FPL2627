# FPL 2026/27

Public repo (`erikdekock/FPL2627`) — readable by Claude in any chat without credentials. **Never commit tokens or login details here.** Single source of truth for Erik's Fantasy Premier League 2026/27 campaign, co-managed with Claude. In-game team name: **Brobbeytrap**. Everything in this repo is English-only.

## Scope in one paragraph

Win the mini-league(s) and hit the season rank target by running FPL as a process, not a mood: a data-informed weekly decision cycle (transfers, captain, XI, chip check), a quarterly strategy review, and a versioned memory of every decision and its reasoning. This repo stores the strategy, the data, and the logs; Claude chats do the thinking; the FPL site executes.

## Operating rhythm

| Cadence | Chat | Reads | Writes |
|---|---|---|---|
| **Weekly** (per Gameweek) | `GWxx` chat in the Claude project | strategy.md, chip-plan.md, gameweek_log.csv, live FPL API | new row in gameweek_log.csv, watchlist updates, squad snapshot |
| **Quarterly** (4×/season + pre-season) | `Strategy Qx` chat | full repo + season evidence | revised strategy.md (with changelog), revised chip-plan.md |

Quarterly reviews are pinned to the season's natural breaks — see `strategy/strategy.md` for the dates.

## Repo map

```
docs/       Founding documents (scope, intelligence stack, run-up plan) — stable
strategy/   strategy.md (living, quarterly) · chip-plan.md (living)
data/       gameweek_log.csv · watchlist.csv · snapshots/ (FPL API dumps)
scripts/    fpl_pull.py (API snapshot; run locally / Claude Code)
```

## Ground rules

1. Game rules come from premierleague.com only.
2. Every gameweek decision gets one row + one lesson in the log. No row, no learning.
3. Hits (-4) and chips require a written rationale before firing.
4. Arsenal-bias guardrail: every Arsenal pick must survive the "what if he played for Villa?" test.
5. Strategy changes happen in quarterly reviews (or on genuine shocks), not on a bad Saturday.

## Key season facts (2026/27)

- GW1 deadline: **Fri 21 Aug 2026, 18:30 BST / 19:30 NL** (confirm at launch). GW1 runs Fri–Mon.
- Transfer window closes **Tue 1 Sep 23:00 UK** — after GW2.
- Three-week break between GW5 and GW6 (21 Sep – 6 Oct, merged international window).
- Chips: two sets of WC/FH/TC/BB. First set expires at the **GW19 deadline, 13:30 GMT Sat 2 Jan 2027**. One chip per GW. No Free Hit in GW1.
- Scores lock at 09:00 UK the day after each GW's final match — review after lockdown, not at full time.
