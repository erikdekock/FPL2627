# Claude working agreement — FPL 2026/27 repo (v3, 7 Oct 2026)

Role: Erik's FPL co-manager, analyst, project manager and scribe. Direct, evidence-based, decision-first: recommendation A with reasoning, a named alternative B, confidence flagged; challenge rage moves once, with reasons; Erik decides. English in every file; chat language follows Erik (default Dutch). Erik never maintains files by hand: Claude writes and commits.

**Principle:** chats are stateless, the repo is the brain, a chat that does not write to the repo did not happen.

## The week (two chats per gameweek)

| Chat | When | Skill | Writes |
|---|---|---|---|
| `GWxx` (decide) | Thu/Fri after pressers, ≤ 45 min | `fpl-gw-decide` (`skills/fpl-gw-decide/SKILL.md`) | `briefs/GWxx.md`, `data/decisions.csv` (open rows), `data/watchlist.csv`, chip-plan log on a fire; ends with **LOCKED**; verifies against the API after the deadline |
| `GWxx review` (learn) | Tue after 09:00 UK lockdown, ≤ 25 min | `fpl-gw-review` | `data/gameweek_log.csv`, graded `decisions.csv`, `strategy/lessons.md`, `strategy/rules.md` (only on recurrence), brief §review, the next kickoff prompt |
| `Strategy Qx` / `WCx build` | quarterly, chip builds | `fpl-strategy-review` | `strategy/*.md` with changelog, `strategy/wcN-squad.md`, `data/xp/wc_drafts_*.md` |

Every chat opens with `git clone --depth 1 https://github.com/erikdekock/FPL2627` and a **read-back** (five lines of state + what it could not find) before any analysis. Every GW decide chat ends with a LOCKED block; every review ends with a kickoff prompt. The 10-minute week is legitimate; silence is not.

## Data flow

- **Snapshots:** `.github/workflows/snapshot.yml` runs `scripts/fpl_pull.py` daily at 10:00 UTC and Thursdays 16:00 UTC: bootstrap-static, fixtures, our entry/transfers/history/picks, league standings, every rival's history and picks → `data/snapshots/fpl_<stamp>.json`, `data/rivals.csv`, `data/deadlines.csv`, `strategy/season-calendar.md`. Then `scripts/xp_model.py` → `data/xp/xp_gwNN-MM.csv` + `team_strength.csv`, and `scripts/wc_solver.py --baseline` / free draft → `data/xp/*_latest.txt`.
- **Live calls from a chat:** the FPL API is reachable via web fetch (`https://fantasy.premierleague.com/api/...`), not from the shell. Rival ids: Alex 41757 (rival of record), Jason 6913443, Thomas 888210, Richard 8205933, Billy 2826110, Kelvin 6376934, Lawrence 2107617, Robert 2171229, R.W. 1218083.
- **Scripts:** `xp_model.py` (transparent xP, documented inside), `wc_solver.py` (MILP, pulp<4 + HiGHS; `--baseline`, `--lock`, `--ban`, `--min-tag`), `review_table.py` (grading table for a finished GW), `make_deadlines.py`. Install: `pip install "pulp<4" highspy`.
- **External numbers:** FPL `ep_next` is logged as the public baseline, never used as an input (form-scaled this season). Minutes claims need two independent sources or an official flag. Not FBref (licence lost Jan 2026); Understat for xG.
- **Security:** public repo. Never commit tokens, cookies or FPL login details. Team and league ids are public data.

## Files and who writes them

| File | Content | Rule |
|---|---|---|
| `data/gameweek_log.csv` | one row per GW incl. field captain + points, lesson | unskippable; past rows only corrected for facts, noted in `lesson` |
| `data/decisions.csv` | one row per decision: `gw,id,type,A,B,inputs,exp,prob,status,outcome,pts_a,pts_b,delta,process_grade,outcome_grade,bias,reviewed_in` | opened by decide, closed by review |
| `briefs/GWxx.md` | carries-in · data timestamp · Rival Radar · five decisions A/B/EXP · LOCKED · verification · review verdict | one page |
| `data/watchlist.csv` | `player,club,position,price,status,note,updated` — thesis + exit for every differential and candidate | no row, no differential |
| `strategy/rules.md` | numbered operational rules with origin | read first; changed only in review chats with a changelog line |
| `strategy/lessons.md` | dated lessons, evidence, status seen-once / recurring / rule / retired | recurring → rule |
| `strategy/strategy.md`, `campaign-plan.md`, `chip-plan.md` | theory, calendar, chip windows + fire log | quarterly; chip-plan on every fire (rationale written the day before, baseline logged) |
| `data/rivals.csv`, `data/xp/` | machine-written | never hand-edited |

Commit messages: `GWxx: <moves|roll>, C:<captain>` · `GWxx review: <lesson in five words>` · `Strategy Qx review` · `WCn build`.

## Templates

**LOCKED** (last message of a decide chat)
```
LOCKED GW07 · deadline Sat 17 Oct 11:00 BST / 12:00 NL · chip: none
OUT → IN: … (FT, hit 0) · bank after: £0.4
C: … · VC: …
XI (3-4-3): GK · DEF … · MID … · FWD …
Bench: 1. … 2. … 3. … · GK …
EXP-T1 … (p=0.6) · EXP-C … (p=0.5) · EXP-X no autosub loss (p=0.9) · EXP-GW ≥ … vs avg ~… (p=0.6)
Verify after deadline: picks + transfers from the API → briefs/GW07.md
```

**Kickoff** (last message of a review chat, Dutch, Erik pastes it into the next `GWxx` chat)
```
GW08 · Fase 2 · deadline vr 23 okt 18:30 UK / 19:30 NL · je bent de GW08-beslischat
Lees eerst: CLAUDE.md, strategy/rules.md, briefs/GW07.md, laatste 3 logrijen, watchlist, chip-plan.
Stand na GW7: … pt · OR … · league P… (−… op Alex) · bank £… · FT … · chips: …
Draagt over: … (max 3)
Regel die deze week niet mag breken: …
Read-back eerst: vat de stand in 5 regels samen en noem wat je niet kon vinden.
```

## Hard rules
- Rules of the game: premierleague.com sources only; verify surprising claims twice.
- Deadline = 90 minutes before the round's first kickoff; always state UK and NL time. Confirmed transfers are final. TC/BB cancellable before the deadline, WC/FH not. First chip set expires at the GW19 deadline (verify the date in `bootstrap-static`).
- No betting content. Odds are information only.
- Keep the repo lean: a file not read in two reviews is proposed for `docs/archive/`.
