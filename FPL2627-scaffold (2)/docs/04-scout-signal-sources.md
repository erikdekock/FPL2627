# Scout Signal Sources
**Version 1.0 · 8 August 2026 · companion to engine/RESEARCH.md and docs/02-intelligence-stack.md**

Purpose: a vetted shortlist of people who evaluate **players and transfers as football decisions** — squad fit, role, tactical profile — weeks before the FPL crowd reprices them. This is the qualitative early-warning layer under the watchlist.

---

## 0. Why this layer exists (and its limit)

Standard FPL content is reactive: it prices players on last season's points and this week's form. Recruitment-minded analysts ask a different question — *is this a good signing, and what role will he actually play?* — which is a **leading indicator** of the two things FPL rewards most: minutes and role.

**The limit, stated honestly:** a well-scouted player is not automatically an FPL asset. Scouting quality and fantasy points diverge constantly — a brilliant ball-playing centre-back at a leaky club is a bad FPL pick. Every scout signal must pass a translation filter (§3) before it touches the watchlist. Use this layer for *hypothesis generation*, never for picks.

---

## 1. Primary source (Erik's find)

**Dougie Critchley** — European football for Sky Sports, formerly of Football Daily. YouTube: `@DougieCritchley` · X: `@DougieCritchley` (~51k followers). Analysis-led rather than rumour-led, with a strong continental-football lens — which is exactly where Premier League clubs shop.

**The worked example — António Silva to Bournemouth (31 Jul 2026):** signed from Benfica for a £21.4m fixed fee plus up to £4.3m in add-ons. Age 22, but 237 senior appearances for Benfica and 20 Portugal caps; Primeira Liga Defender of the Year in 2022/23. He is the direct replacement for Marcos Senesi (departed to Spurs), and Bournemouth specifically wanted a tall, defensively strong, ball-playing centre-back who prefers the left side — Senesi's exact slot. He arrived with one year left on his contract, having turned down a renewal.

**Why this is a textbook FPL signal:** the profile-for-profile replacement means the *role is pre-defined and nailed* — the single hardest thing to forecast in August. He also enters the game **after the 23 July launch**, so he was never in the initial price list and carries near-zero ownership. That is precisely the "deadline-day player-entry watch" item flagged as open question #8 in the Intelligence Stack. → Add to watchlist as **Monitor**; the DefCon question (does Marco Rose's Bournemouth sit deep enough for volume?) resolves in the first three gameweeks.

---

## 2. Additional sources (researched, ranked by usefulness to us)

**Tier 1 — highest signal-to-noise for our purpose**

| Source | Where | Why they're on the list |
|---|---|---|
| **Ben Mattinson** | X: `@Ben_Mattinson_` | The proof-of-concept for this whole layer. Built a following posting talent-ID threads, flagged Dean Huijsen and Cristhian Mosquera as ones to watch in May 2024 — both later moved to Real Madrid and Arsenal respectively — and was early on Tijjani Reijnders before his Man City move. Hired by Como 1907 as a first-team scout off the back of it. Caveat: now employed by a club, so output is thinner and more constrained. |
| **Liam Henshaw** | liamhenshaw.com | Data analyst and first-team scout at a football agency; writes openly about the actual tooling and method of recruitment analysis. Doubles as a teaching resource for Project Beane. |
| **The Transfers Podcast** | footballtransfers.substack.com | Duncan Castles interviews recruitment insiders — e.g. former Chelsea head of scouting Scott McLachlan on professionalising scouting, forecasting as the hardest skill, and Moneyball-style recruitment at Fulham. Structural insight into *how clubs decide*, which is upstream of every transfer. |

**Tier 2 — depth on demand**

| Source | Where | Use for |
|---|---|---|
| **Scouted Notebook** | scoutednotebook.com | Youth and emerging talent; the annual SCOUTED50 list flags breakout candidates. Subscription for full access. |
| **Total Football Analysis** | totalfootballanalysis.com | Match analysis, player profiles, recruitment pieces; free tier plus premium magazine. |
| **Spielverlagerung** | spielverlagerung.com | The deep tactical blog. For understanding a new manager's system — highly relevant with eight new Premier League bosses. |
| **Chris Gill podcast** | via 360scouting.com | Interviews with working scouts, analysts and coaches. Method over hot takes. |
| **360 Scouting** | 360scouting.com | Aggregator of the scouting ecosystem; useful for finding new sources as the season goes. |

---

## 3. The translation filter — scout signal → FPL action

A signal only reaches the watchlist if it survives all five:

1. **Minutes.** Does the analysis imply a nailed starting role, or potential? Potential is worthless to us before December.
2. **Position in FPL.** Which slot does the game assign him, and is that slot generous? (A defensive midfielder classified as MID with DefCon volume is worth more to us than to a real club.)
3. **Points mechanism.** Name the specific route to points: goals/assists, clean sheets, DefCon volume, saves, bonus. If we can't name it, there isn't one.
4. **Price and ownership.** Is he cheap enough to matter, and is the crowd still asleep? Mid-season entrants start at low ownership by definition.
5. **Team context.** Does the *team* generate the returns he needs? A great defender at a poor defensive side scores DefCon points but few clean sheets.

**Weekly ritual (add to the GWxx protocol, step 3):** one line — *"Scout radar: anything new worth monitoring?"* Anything that passes the filter goes into `data/watchlist.csv` as **Monitor** with a note naming the points mechanism. Nothing is ever bought on scout signal alone; it must also clear the normal minutes-and-form evidence bar.

---

## 4. ⚠️ Correction to the Intelligence Stack

**FBref lost its Opta data licence in January 2026** and no longer receives updated advanced statistics. Historical data remains usable for backtesting and research, but **it cannot be a current-season stats source** — which is how `docs/02-intelligence-stack.md` v1.0 listed it.

**Replacement plan:** Understat stays as the free xG backbone for current-season data (top five European leagues), with the official FPL API for FPL-specific stats and the Scout's DefCon coverage. Any guide still calling FBref the best free live resource is out of date. → Update the Intelligence Stack at the next quarterly review; verify Understat's own status at the same time.

*This correction was found through scout-source research, not FPL research — an early argument for keeping this layer.*

---

## 5. Backlog

- Confirm whether Ben Mattinson still posts publicly now that he's at Como; if not, find the successor account in that niche.
- Identify a dedicated Premier League *new-signings* tracker for the mid-season entry watch (FPL-specific).
- Consider an X list bundling these accounts for one weekly scan instead of five.
- Q1 review: has any scout signal produced actual points? Kill this layer if the answer is no by Christmas.

*Changelog: v1.0 — 8 Aug 2026. Sources researched and verified; Silva/Bournemouth example confirmed against Sky Sports reporting.*
