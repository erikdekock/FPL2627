# Kickoff prompt — "Strategy Q2 · process review" (written 8 Nov 2026, after GW10)

Open a new chat in the FPL 26/27 project named **Strategy Q2 · process review** and paste everything inside the block.

```
Strategy Q2 · process review · je bent de strategie- en procesreview-chat (geen GW-beslischat)

WAAROM DEZE CHAT
GW10 was onze beste week ooit: 123 punten, GW-rank 37 van 11,27 miljoen, OR 3.508.984 → ~796k (top 31% → top 7%), league P8 → P2 (−27 op Jason, +9 op Alex). Ik wil dat dit de standaard wordt, geen toeval. Deze chat onderzoekt ons hele proces van GW1 t/m GW10 – wat werkte, wat niet, waarom – en ontwerpt hoe we het vanaf nu beter doen: doelen, strategie per horizon, chips, modellen, het weekritme, de skills, de projectinstellingen. Diep onderzoek, eerlijk, met bewijs. GW11 (deadline za 21 nov 11:00 UK / 12:00 NL) draait in een andere chat; neem daar geen beslissingen over, maar alles wat je hier oplevert moet vóór die deadline bruikbaar zijn.

WERKAFSPRAKEN
- Chat in het Nederlands, elk bestand in het Engels. Jij schrijft en commit; ik plak nooit.
- Gebruik de skill fpl-strategy-review als raamwerk en breid hem uit waar deze opdracht verder gaat.
- Nooit een getal uit je geheugen: alles uit de repo, de FPL-API (web fetch, of de snapshot-workflow via gh workflow dispatch als web fetch verouderde cache geeft), of een bron met URL.
- Jij stelt voor, ik beslis. Eén beslissing per bericht; per voorstel: aanbeveling A met reden, alternatief B, vertrouwen. Regels, skills en projectinstellingen veranderen pas na mijn akkoord, met een changelog-regel.
- Wees kritisch op jezelf. Claude's eigen fouten zijn onderdeel van het onderzoek (zie de GW10-lessen: plan-anchoring, ad-hoc modelcorrecties op de deadline-ochtend).

STAP 0 · INVENTARIS EN READ-BACK
1. git clone --depth 1 https://github.com/erikdekock/FPL2627 (koppel met push-toegang). Lees alles wat telt: CLAUDE.md, README, docs/01–10 + docs/project-instructions.md, engine/, strategy/* (strategy, campaign-plan, chip-plan, rules, lessons, selection-method, season-calendar, wc1-squad), skills/*/SKILL.md, scripts/* (lees xp_model.py, one_transfer.py, wc_solver.py, review_table.py echt door), data/gameweek_log.csv, data/decisions.csv (alle rijen), data/watchlist.csv, data/rivals.csv, briefs/GW06–GW11, docs/outputs/gw07.
2. Projectdocs (Projects-tool: project_info, claude/selection-method.md, claude/handover-gw07-wildcard.md) en het projectgeheugen.
3. De eerdere chats in dit project: zoek ze op met conversation_search / recent_chats (GW-beslischats, reviews, WC-build, de GW10-chat). Begrijp hoe een week écht verliep: hoe lang, hoeveel berichten, waar beslissingen vielen, wat er niet in de repo terechtkwam.
4. De geplande taken (list_triggers): "FPL decide prep (Fri)" en "FPL review prep (Tue)" staan sinds 13 okt UIT. Zoek uit waarom en of dat pijn heeft gedaan.
5. Read-back: regel 1 = volgende deadline uit de API (UK + NL, dagen te gaan), dan de stand in 5 regels, dan in 5 regels hoe het systeem nu in elkaar zit (bestanden, skills, taken, chats), en wat je niet kon vinden.

STAP 1 · AUDIT GW1–10 (wat is er gebeurd en waarom)
Met cijfers uit de API en de repo, per gameweek en opgeteld:
- Punten vs gemiddelde, GW-rank, OR-verloop, league-gap per week; captain vs field-captain (cumulatief), bankpunten, autosub-verliezen, transfers en gerealiseerde EV vs B, hits, chips met hun waarde vs de baseline, deadlines gemist of half uitgevoerd.
- Puntenattributie: waar kwamen onze punten vandaan (premiums, captain, goedkope vaste spelers, verdedigingsblokken per club, differentials, bank/chips) – en waar lekten ze (blanks, verkeerde speler bij de goede club, gemiste uitvoering)? Vergelijk GW10 met de rest: wat was structureel, wat was geluk?
- Beslissingen: alle rijen van decisions.csv in de vier vakken (proces × uitkomst). Brier-score van alle EXP's. A (Claude) vs B (Erik) – hoe vaak won wie, met hoeveel, bij welk type beslissing? Test expliciet de hypothese "Claude's A is plan-geankerd en te voorzichtig".
- Proces: welke regels en stappen werden gevolgd, welke overgeslagen, welke kostten tijd zonder rendement, welke leverden aantoonbaar punten op? Wat was productief, wat contraproductief voor onze doelen?
- Rivalen: hoe scoren de top van Fantasy Fellas en het top-10k-template; welke keuzes maakten zij die wij misten of terecht vermeden?
Lever een audit-pagina (artifact, met tabellen en grafieken) en docs/11-process-review-q2.md.

STAP 2 · DOELEN OPNIEUW DEFINIËREN
- Herzie strategy.md §1 en §10: einddoel (Fantasy Fellas winnen? OR-doel?), subdoelen per fase, en meetbare leidende indicatoren per week (bijv. captain-delta vs league, bankpunten, transfer-EV, uitvoeringsscore, Brier) met drempels.
- Rivaal-van-dienst: Alex of de leider (nu Jason)? Herzie regel 18 (shield/sword) op de huidige stand en chip-posities: Jason heeft WC, FH en BB, wij alleen TC1 (set 1 vervalt bij de GW19-deadline, vr 1 jan 18:30 UK – verifieer in de API).

STAP 3 · STRATEGIE PER HORIZON
- Kort (deze GW): wat beslissen we elke week en op welke informatie.
- Middellang (4–6 GW): fixture-blokken, moeilijkheid, thuis/uit, team-sterkte, Europa-belasting (do/zo), rotatie, prijsontwikkeling, FT-banking.
- Lang (seizoen): de fasekaart in campaign-plan.md, de kerstcongestie, blanks en doubles (verifieer wat bekend is), de winterherbouw, set 2.
- Chips: herzie het chipplan voor TC1 (GW11 Haaland FUL thuis – houden of verplaatsen?), set 2 (WC2, FH2, BB2, TC2), en de interactie met Jasons chips. Wanneer is een chip op de dag zelf toegestaan (GW10 BB werkte, GW6 FH ging mis)?
- Lever een seizoenskalender GW11–38: per GW wat het type week is en wat we dan doen.

STAP 4 · MODELLEN (voorspellend, maar relevant en op het juiste moment)
- Kalibreer xp_model.py op GW6–10: MAE en bias per positie, per prijsklasse, voor captains; vergelijk met FPL ep_next. Waar zit het model systematisch naast?
- Onderzoek (web, met bronnen) hoe sterke FPL-modellen en -tools werken (openbare methoden, open-source projecten, academisch werk) en welke bouwstenen gratis en verifieerbaar zijn (docs/09-model-stack.md is het startpunt; geen FBref, Understat wel).
- Kandidaten om te bouwen of aan te passen, elk met verwacht nut en kosten: afwerkingsterm (gekrompen G−xG), thuis/uit- en tegenstandersterkte, minutenmodel (rotatie, Europa, terugkeer uit blessure), captain-model met verdeling en plafond i.p.v. alleen gemiddelde, league-EO-bewuste captain-EV (verwachte winst op rivalen), chip-timingmodel (BB/TC-waarde per GW), multi-GW transferplanner met FT-banking en hits, fixture-ticker, prijsveranderings-signaal.
- Bepaal per model wanneer het draait en welke beslissing het voedt (urgentie en relevantie): wat in de dagelijkse snapshot, wat in de decide-chat, wat alleen bij chips/WC.
- Bouw wat binnen deze chat haalbaar is en test het met een backtest op GW6–10; de rest als genummerde backlog.

STAP 5 · HET WEEKSYSTEEM (een stappenplan dat we elke week uitvoeren)
- Ontwerp het weekritme opnieuw met modi: rol-week, één-transfer-week, chip-week, WC/FH-build, blank/double-week. Per modus: welke stappen, welke modellen, welke beslissingen, tijdsbudget, wat er LOCKED moet staan en wanneer.
- Een vaste agenda per week (prep-taak, decide, uitvoering + screenshot, API-verificatie, review na lockdown) en per seizoensmoment (bias-review elke 4e review, kwartaalreview, chip-vensters).
- Herontwerp of heractiveer de geplande taken (prep en review) zodat elke chat begint met de getallen klaar; ook de post-deadline-verificatie en de lockdown-check.
- Regels: werk de openstaande voorstellen uit en leg ze aan mij voor: 4a (deadline-regel 1, LOCKED ≥ 3 u), 4b (elke wijziging na LOCKED = één regel + screenshot), 17 (chip op de dag zelf alleen na waarde-vs-plan en minutencheck vóór activatie), 18 (rivaal = leider). Schrap regels die niets opleveren.

STAP 6 · SKILLS, PROJECTINSTELLINGEN, CLAUDE.md
- Herschrijf waar nodig fpl-gw-decide, fpl-gw-review en fpl-strategy-review (en stel eventueel een nieuwe skill voor, bijv. voor chip-weken of de seizoenskalender). Lees elke huidige SKILL.md eerst en stel volledige nieuwe versies voor via propose_skills; houd de repo-kopie in skills/ gelijk.
- Stel een nieuwe versie voor van de projectinstructies (docs/project-instructions.md) en van CLAUDE.md, en zeg precies wat ik in de projectinstellingen moet aanpassen.
- Houd de repo slank: wat twee reviews niet gelezen is, naar docs/archive/.

OPLEVERING EN VOLGORDE
1. Read-back (stap 0) → wacht op mijn akkoord.
2. Audit (stap 1) als artifact + docs/11 → bespreek de 5 belangrijkste bevindingen.
3. Doelen en strategie (stap 2–3) → beslissingen één voor één.
4. Modellen (stap 4): kalibratie, gebouwde verbeteringen met backtest, backlog.
5. Weeksysteem, regels, skills, instellingen (stap 5–6) als voorstellen → mijn akkoord → schrijven en committen (strategy/*.md met changelog, rules.md, skills via propose_skills, geplande taken).
6. Afsluiting: wat er veranderd is in 10 regels, wat in GW11 al geldt, de kickoff voor de GW11-beslischat (als die nog niet gestart is) en de datum van de volgende review.
Commit als "Strategy Q2 review: <onderdeel>". Werk liever in meerdere sessies grondig dan in één keer oppervlakkig; zet een tussenstand in de repo (docs/11) zodat een vervolgchat kan doorgaan.
```
