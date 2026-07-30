# Kid Engagement Demand Taxonomy

Date: 2026-07-29

Action: `KAL-RES-005`

Frozen repository base:
`6bccf7635980e4200fbdc5655c7f7cb2ce36dd40`

## Decision

This bounded query and SERP review found no evidence that `Make`, `Create`,
`Explore`, and `Go Deeper` are established parent-facing taxonomy standards.
It did not comprehensively audit industry taxonomies or test parent
comprehension. The labels remain useful internal engagement dimensions, but
the current evidence does not support using them as the site's primary labels.

The smallest concrete editorial candidate supported by this research is one
umbrella plus four browse categories:

1. **Activities**: the site umbrella and age-led chooser.
2. **Games**: a browse category for physical, family, card, board, and other
   clearly qualified games.
3. **Arts & Crafts**: a browse category for art and object-making with a
   concrete materials-and-steps
   model.
4. **Science & Building**: a browse category for experiments, STEM,
   engineering, construction, and tinkering.
5. **Outdoor & Nature**: a browse category for outdoor play, nature
   activities, and scavenger hunts.

This is an architecture recommendation, not an implementation. Do not change
navigation or create pages in this transaction.

Use age, location, time, setup, cost, mess, energy, player count, adult role,
and screen-free status as routes or filters. Keep pretend play, storytelling,
music, sensory play, and substantial projects as activity types or interest
lenses until a larger coherent search and content model is supported. Treat
local outings and product recommendations as separate future systems:

- local outings need location, freshness, and business-data maintenance;
- kits, books, subscriptions, toys, and board-game buying need access,
  firsthand use, current facts, original evidence, and disclosure.

## Why The Labels Change

The old five-lane model mixed different concepts:

- `Make` and `Create` overlap in ordinary and editorial meaning, and the
  current research does not supply a reliable parent-facing boundary.
- `Explore` could mean nature, a museum, local places, or simply browsing.
- `Go Deeper` describes duration or depth, not what the child will do.
- `Games` is a more concrete candidate than `Play`, but the broad search phrase
  `games for kids` is heavily ambiguous with online games.

The new recommendation separates the parent-facing choice from the internal
editorial model. KAL can still use agency, imagination, experimentation,
exploration, and depth when evaluating an activity. Those dimensions do not
need to become navigation labels.

## Evidence Boundaries

- The exact register is
  `data/kid-engagement-taxonomy-keywords-2026-07-29.csv`.
- Semrush US intent, volume, KD, and CPC are July 2026 `TOOL_ESTIMATE`
  evidence collected through the logged-in Keyword Overview bulk interface.
- All 96 rows were explicitly refreshed on 2026-07-29 and showed `Now`.
- Public search results and inspected pages are `SOURCE_BACKED` research
  inputs within the limitations below.
- Parent-job personas are `RESEARCH_HYPOTHESIS`.
- Taxonomy, page ownership, and sequencing are `EDITORIAL_JUDGMENT`.
- The 2026-07-29 public-safe GSC snapshot is `MEASURED`.
- Complete current GSC query rows and numeric cross-query SERP overlap remain
  `UNKNOWN`.
- Close keyword variants overlap and are not summed into a market-size claim.
- A zero estimate remains zero; an unavailable estimate remains `n/a`.
- No parent test, child quote, engagement result, learning result, safety
  outcome, original visual, or firsthand product use is inferred.

## Current GSC Context

The newest validated snapshot was collected 2026-07-29 with finalized data
through 2026-07-27:

- 72 impressions;
- 0 clicks;
- average position 29.28;
- 61 sitemap URLs discovered;
- 7 of 7 priority URLs indexed.

It is performance-identical to the 2026-07-28 snapshot. The ramp article still
has 24 impressions at average position 16.58. The unchanged snapshot does not
select a taxonomy or implementation. Complete query rows remain unavailable.

## Keyword Method

The exact universe was frozen before collection: 12 queries in each of eight
groups.

| Group | Question tested |
|---|---|
| umbrella | Do parents use broad activity or age-led language? |
| situation-constraint | Are indoor, rainy-day, home, prep, and similar terms categories or filters? |
| games | Is Games a coherent parent-facing lane, and where is it ambiguous? |
| arts-crafts | Do concrete art and craft terms support a distinct content type? |
| science-building | Does the current STEM/building wedge have a recognizable demand model? |
| pretend-story-music | Do imagination-led terms support one primary label? |
| explore-outings | Are nature discovery and local places one architecture? |
| projects-kits | Is depth a category, or does it split into project and commercial product jobs? |

### Register summary

| Group | Rows | Numeric | `n/a` | Zero | At least 100 | At least 1,000 | Median numeric volume | Median KD |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Umbrella | 12 | 12 | 0 | 0 | 11 | 10 | 3,900 | 26 |
| Situation/constraint | 12 | 12 | 0 | 2 | 8 | 3 | 325 | 21.5 |
| Games | 12 | 12 | 0 | 0 | 10 | 8 | 4,400 | 20.5 |
| Arts/crafts | 12 | 12 | 0 | 0 | 11 | 8 | 1,600 | 30.5 |
| Science/building | 12 | 11 | 1 | 0 | 9 | 5 | 390 | 19 |
| Pretend/story/music | 12 | 12 | 0 | 1 | 4 | 1 | 35 | 20 |
| Explore/outings | 12 | 12 | 0 | 2 | 9 | 5 | 320 | 20.5 |
| Projects/kits | 12 | 12 | 0 | 2 | 10 | 4 | 590 | 21.5 |
| **Total** | **96** | **95** | **1** | **7** | **72** | **44** | **590** | **22.5** |

These counts describe the frozen research set, not the total market. The set
was intentionally balanced across hypotheses, so group medians are directional
comparisons rather than weighted demand shares.

### High-signal exact terms

| Query | Intent | US volume | KD | Taxonomy implication |
|---|---|---:|---:|---|
| `kids activities` | Commercial | 550,000 | 47 | Strong umbrella, but broad and mixed with local/digital models |
| `rainy day activities for kids` | Informational | 60,500 | 22 | Important situation route, not a content type |
| `things to do with kids near me` | Transactional | 60,500 | 17 | Local product, not a nature category |
| `games for kids` | Mixed | 40,500 | 91 | Large but strongly ambiguous with online games |
| `kids activities near me` | Transactional | 40,500 | 27 | Local finder intent |
| `things to do with kids` | Informational | 18,100 | 21 | Broad chooser language |
| `crafts for kids` | Informational | 14,800 | 48 | Distinct materials-and-steps content type |
| `science experiments for kids` | Informational | 14,800 | 46 | Distinct experiment content type |
| `arts and crafts for kids` | Mixed | 12,100 | 43 | Recognizable parent label |
| `family games` | Commercial | 9,900 | 10 | Useful label, but product/free-play intent can mix |
| `activities for kids` | Informational | 9,900 | 44 | Umbrella chooser |
| `board games for kids` | Mixed | 8,100 | 21 | Product evidence gate |
| `card games for kids` | Informational | 4,400 | 14 | Qualified no-purchase Games opportunity |
| `science kits for kids` | Mixed | 4,400 | 25 | Commercial evidence gate |
| `nature scavenger hunt` | Informational | 2,900 | 24 | Concrete Outdoor & Nature page model |
| `stem activities for kids` | Informational | 2,900 | 41 | Supports current science/STEM ownership |
| `music games for kids` | Informational | 1,900 | 46 | A specific game subtype, not proof of one imagination category |
| `activities for 4 year olds` | Informational | 1,300 | 25 | Age remains a primary route |
| `crafts for 4 year olds` | Mixed | 1,000 | 33 | Age can refine a concrete category |

Important negative evidence:

- `no prep activities for kids` and `low prep activities for kids` returned
  zero estimates, but prep burden still recurs as a parent decision field.
- `pretend play activities`, `imaginative play ideas`, and
  `dramatic play activities` each returned 20.
- `long term projects for kids` and `weekend projects for kids` returned zero.
- `tinkering activities for kids` returned `n/a`, not zero.

This does not mean those experiences lack value. It means their exact labels
do not currently justify top-level search architecture.

## Representative SERP Samples

Twelve exact queries were sampled through OpenAI web search on 2026-07-29 in
English. The provider did not expose a fixed country, device, requested depth,
complete ordered organic set, or Google-specific features. Some responses
pooled results when queries were submitted together. The retained URLs below
are reproducible examples of the returned page models, not claimed Google
positions or complete top results.

Numeric URL/domain overlap is therefore `UNKNOWN`.

| Query | Retained representative URLs | Observed page model | Confidence |
|---|---|---|---|
| `kids activities` | `https://missscout.com/`<br>`https://www.littleactivity.com/activities`<br>`https://indyschild.com/70-things-to-do-with-kids-now-that-were-all-stuck-at-home/` | Local finder, filterable library, broad publisher list | Medium for mixed intent; low for rank |
| `indoor activities for kids` | `https://www.nhs.uk/healthier-families/activities/indoor-activities-for-kids/`<br>`https://www.bbcgoodfood.com/howto/guide/indoor-activities-kids`<br>`https://www.goodhousekeeping.com/life/g31445865/indoor-activities-for-kids/` | Institution and major-publisher roundups | High for broad situation model; low for rank |
| `games for kids` | `https://kidsonline.com/`<br>`https://glazegames.com/best/games-for-kids`<br>`https://kalszone.com/` | Browser and digital games | High that broad wording is digitally ambiguous |
| `crafts for kids` | `https://www.madeformums.com/school-and-family/easy-crafts-for-kids/`<br>`https://www.classpop.com/magazine/crafts-for-kids`<br>`https://www.moma.org/d/pdfs/W1siZiIsIjIwMTkvMDcvMTAvZmkwb2lobWJ6X0FydF9NYWtpbmdfd2l0aF9Nb01BX1BSRVZJRVcucGRmIl1d/Art%20Making%20with%20MoMA%20PREVIEW.pdf?sha=25b830ad6cabed2b` | Materials, steps, finished object, age/occasion variants | High for distinct content type; low for rank |
| `science experiments for kids` | `https://www.goodhousekeeping.com/life/hobbies-and-activities/g32176446/science-experiments-for-kids/`<br>`https://curiodyssey.org/learn-explore/science-experiments-for-kids/`<br>`https://www.pbs.org/parents/simple-science-activities` | Experiment libraries with setup and explanation | High for distinct content type; low for rank |
| `pretend play activities` | `https://www.healthychildren.org/English/family-life/power-of-play/Pages/pretend-play-ways-children-can-exercise-their-imagination.aspx?form=HealthyChildren`<br>`https://www.brighthorizons.com/article/children/pretend-play-learning-opportunities`<br>`https://extension.psu.edu/programs/betterkidcare/content-areas/environment-curriculum/activities/all-activities/lets-pretend-activities` | Development/expert guidance with example prompts | Medium for guidance intent; low for rank |
| `nature activities for kids` | `https://www.rhs.org.uk/education-learning/children-young-people/family-activities/10-nature-activities`<br>`https://kids.nationalgeographic.com/nature/article/get-outside`<br>`https://www.scouts.org.uk/activities/nature-hunt/` | Outdoor activity lists and runnable nature hunts | High for Outdoor & Nature model; low for rank |
| `projects for kids` | `https://projects.raspberrypi.org/`<br>`https://bestprojectideas.com/wp-content/uploads/2024/12/Kids-Project-Ideas.pdf`<br>`https://education.nsw.gov.au/content/dam/main-education/en/home/parents-and-carers/school-holidays/going-to-the-zoo-these-school-holidays/Activities_to_Try.pdf` | Coding, broad project lists, and mixed activity resources | High that unqualified `projects` is ambiguous |
| `card games for kids` | `https://cardrulesplus.com/lists/easy-card-games-for-kids/`<br>`https://solitaired.com/card-games-for-kids`<br>`https://gamerules.com/card-games/kids-card-games/` | Standard-deck rules mixed with commercial card games | High for qualified Games model; low for rank |
| `nature scavenger hunt` | `https://www.scouts.org.uk/activities/nature-hunt/`<br>`https://www.blm.gov/sites/blm.gov/files/Learn_CCSC_Nature-Learning-Downloads_Nature-Scavenger-Hunt.pdf`<br>`https://www.orcity.org/DocumentCenter/View/18436/Nature-Scavenger-Hunt---Childrens` | Runnable hunt and printable/checklist utility | High for a concrete Outdoor & Nature subtype |
| `science kits for kids` | `https://sciencebasedkids.com/compare/best-science-kits-for-kids/`<br>`https://time.com/4066213/kids-children-technology-sets/`<br>`https://www.techlearning.com/features/10-of-the-best-tools-to-teach-stem` | Product comparison and buying guidance | High for commercial/evidence-heavy model |
| `activities for 4 year olds` | `https://www.nemours.org/reading-brightstart/at-home-activities/4-year-olds.html`<br>`https://www.cdc.gov/act-early/milestones/4-years.html`<br>`https://extension.psu.edu/programs/betterkidcare/early-care/tip-pages/all/fun-with-four-year-olds` | Age-led activities and developmental guidance | High for age route; low for rank |

## Ranking-Page Inspection

Twenty-three pages were opened or directly inspected. The Stanford family card
games PDF appeared in results but failed to fetch, so it is not counted below.

| # | Page | Type | Useful pattern | KAL implication or limitation |
|---:|---|---|---|---|
| 1 | [NHS indoor activities](https://www.nhs.uk/healthier-families/activities/indoor-activities-for-kids/) | Public health | Active indoor ideas | Situation-led breadth; authority advantage |
| 2 | [BBC Good Food indoor activities](https://www.bbcgoodfood.com/howto/guide/indoor-activities-kids) | Major publisher | Scannable broad list | Indoor is a route spanning multiple types |
| 3 | [Good Housekeeping indoor activities](https://www.goodhousekeeping.com/life/g31445865/indoor-activities-for-kids/) | Major publisher | Deep roundup | Generic short list would be weak |
| 4 | [MadeForMums crafts](https://www.madeformums.com/school-and-family/easy-crafts-for-kids/) | Parenting publisher | Concrete objects, supplies, age range | Supports Arts & Crafts as a recognizable type |
| 5 | [Good Housekeeping science](https://www.goodhousekeeping.com/life/hobbies-and-activities/g32176446/science-experiments-for-kids/) | Major publisher | Experiments organized by concept | Science is a coherent activity model |
| 6 | [CuriOdyssey science](https://curiodyssey.org/learn-explore/science-experiments-for-kids/) | Science institution | Hands-on experiment library | Source/explanation trust matters |
| 7 | [PBS simple science](https://www.pbs.org/parents/simple-science-activities) | Public media | Activity-plus-reading context | KAL can compete on execution, not authority claims |
| 8 | [HealthyChildren pretend play](https://www.healthychildren.org/English/family-life/power-of-play/Pages/pretend-play-ways-children-can-exercise-their-imagination.aspx?form=HealthyChildren) | Professional guidance | Prompts and developmental context | SERP leans guidance; KAL must not copy outcome claims |
| 9 | [Bright Horizons pretend play](https://www.brighthorizons.com/article/children/pretend-play-learning-opportunities) | Childcare provider | Example scenarios | Pretend is useful but not one strong nav cluster |
| 10 | [RHS nature activities](https://www.rhs.org.uk/education-learning/children-young-people/family-activities/10-nature-activities) | Horticultural institution | Runnable nature activities | Supports Outdoor & Nature |
| 11 | [National Geographic Kids outdoors](https://kids.nationalgeographic.com/nature/article/get-outside) | Major publisher | Seasonal outdoor prompts | Nature/outdoor is a recognizable interest |
| 12 | [Scouts nature hunt](https://www.scouts.org.uk/activities/nature-hunt/) | Youth organization | One runnable hunt | Strong utility pattern for scavenger hunts |
| 13 | [BLM nature scavenger hunt](https://www.blm.gov/sites/blm.gov/files/Learn_CCSC_Nature-Learning-Downloads_Nature-Scavenger-Hunt.pdf) | Government printable | Portable checklist | Printable utility is distinct from local listings |
| 14 | [CardRules+ kids card games](https://cardrulesplus.com/lists/easy-card-games-for-kids/) | Rules specialist | Age, players, difficulty, rules | Useful field model; claims require verification |
| 15 | [Solitaired card games](https://solitaired.com/card-games-for-kids) | Game/rules publisher | Broad rules list | Mixes physical and online play |
| 16 | [Game Rules card games](https://gamerules.com/card-games/kids-card-games/) | Rules specialist | Game-by-game instructions | Confirms rule accuracy and variant choice matter |
| 17 | [MadeForMums card games](https://www.madeformums.com/school-and-family/best-card-games-for-kids-uk/) | Commerce publisher | Age labels and product choices | Commercial cards differ from standard-deck utility |
| 18 | [Nemours age-four activities](https://www.nemours.org/reading-brightstart/at-home-activities/4-year-olds.html) | Health/education institution | Age-led activity library | Supports age as a primary route |
| 19 | [CDC age-four milestones](https://www.cdc.gov/act-early/milestones/4-years.html) | Government guidance | Choice and age context | Reference only; KAL cannot imply screening expertise |
| 20 | [Raspberry Pi projects](https://projects.raspberrypi.org/) | Technology nonprofit | Filterable substantial projects | Shows `projects for kids` can mean coding |
| 21 | [ScienceBasedKids science kits](https://sciencebasedkids.com/compare/best-science-kits-for-kids/) | Affiliate comparison | Age/interest matrix | Page says both "age-tested" and "0 products evaluated"; low-trust example, not a factual source |
| 22 | [LittleActivity library](https://www.littleactivity.com/activities) | Activity platform | Age, subject, difficulty, duration filters | Demonstrates utility model; page claims were not independently verified |
| 23 | [Miss Scout](https://missscout.com/) | Local activity finder | Location, age, category, booking | Local outings require a different product and freshness system |

## Parent-Job Hypotheses

These are review lenses, not fictional testimonials or parent-test evidence.

| Persona hypothesis | Job | Evidence trail | Needed decision fields |
|---|---|---|---|
| Start-now parent | Find one feasible thing for the current indoor, rainy, or at-home moment | Situation estimates; NHS, BBC, Good Housekeeping | time, setup, materials, mess, adult role |
| Age-fit parent | Avoid ideas that are too easy, hard, language-heavy, or fiddly | Age estimates; Nemours, CDC, current KAL age pages | age/readiness, reading, fine-motor load, rescue |
| Play-together parent | Pick a physical family/card game, not a browser game | Broad Games SERP; card-rule pages; `family games` and card terms | players, ages, rules, competitiveness, minutes |
| Creative-result parent | Make a recognizable object or artwork with available supplies | Arts/crafts estimates; MadeForMums | finished result, materials, cutting, mess, drying time |
| Curiosity parent | Start a visible experiment or building challenge and understand what changes | Science/STEM estimates; GH, PBS, CuriOdyssey | question, setup, one-variable test, explanation |
| Outdoor-discovery parent | Turn a walk, backyard, or park visit into an activity | Nature/scavenger estimates; RHS, Scouts, BLM | location, duration, portability, collect/observe boundary |
| Shortcut buyer | Choose a kit, book, box, or game that fits the child | Kit/subscription/board terms; product pages | access, firsthand use, current facts, disclosure |

## Current KAL Ownership

Repository inventory was collected on 2026-07-29 with `rg --files site`,
grouped by path, and reconciled with all 16 rows in
`data/seo_keyword_targets.csv`. The inventory contains 64 HTML files: 5 under
`site/ages/`, 14 under `site/collections/`, and 37 under `site/cards/`.
Negative statements below mean no dedicated path or SEO target was present in
that inventory; they do not claim that no individual card contains a related
idea.

| Demand area | Exact local-path evidence | Decision |
|---|---|---|
| Broad/age activities | `site/index.html`<br>`site/cards.html`<br>`site/ages/activities-for-3-year-olds-at-home.html`<br>`site/ages/activities-for-4-year-olds-at-home.html`<br>`site/ages/activities-for-5-year-olds-at-home.html`<br>`site/ages/activities-for-6-year-olds-at-home.html`<br>Four matching age targets in `data/seo_keyword_targets.csv` | Preserve. `Activities` is the umbrella; do not add another broad kids-activities URL without an ownership audit. |
| Indoor/rainy/prep constraints | `site/collections/indoor-activities-for-preschoolers.html`, `rainy-day-activities-for-preschoolers.html`, `no-prep-activities-for-preschoolers.html`, `no-cut-preschool-activities.html`, and `independent-activities-for-preschoolers.html`; matching targets exist for all except no-cut | Treat as routes/filters and consolidation candidates, not top-level categories. |
| Games | `site/cards/duplo-games.html`; no family-game or card-game hub/path appears in the 64-file inventory or 16-row target register | Distinct adjacent lane only when qualified. `KAL-RES-004` remains the next research action. |
| Arts & Crafts | Craft-like cards include `site/cards/paper-chain-test.html`, `tube-sculpture.html`, and `paper-roll-play.html`; no arts/crafts hub or target appears in the inventory/register | Strong future research candidate; do not create a page yet. |
| Science & Building | `site/ages/stem-activities-for-4-year-olds.html`<br>`site/collections/stem-activities-for-preschoolers.html`<br>`site/collections/science-experiments-for-4-year-olds.html`<br>`site/collections/engineering-activities-for-4-year-olds.html`<br>`site/collections/building-activities-for-4-year-olds.html`<br>`site/collections/original-stem-activities-for-4-year-olds.html`<br>`site/articles/cardboard-box-car-ramp-preschoolers.html` | Existing evidence wedge and clearest current category ownership. Audit overlap before expansion. |
| Pretend/story/music/sensory | Related individual cards include `site/cards/blanket-river.html`, `sound-shaker-match.html`, and `color-mixing-cups.html`; no dedicated pretend/story/music/sensory hub or SEO target appears in the inventory/register | Keep as tags/activity types for now. |
| Outdoor & Nature | No outdoor/nature/scavenger path or SEO target appears in the inventory/register | Valid future research lane; do not merge with local outings. |
| Local outings | No place/location/finder path or SEO target appears in the inventory/register; the static repo has no freshness workflow for venue data | Separate future product; not currently ready. |
| Projects/kits/resources | No kit/book/subscription/product-comparison path or SEO target appears in the inventory/register | Keep project depth as a format; hold product guidance behind the separate firsthand-product evidence gate. |

## Taxonomy Recommendation

### Parent-facing structure candidate

| Label | Role | Search/content boundary | Current readiness |
|---|---|---|---|
| Activities | Site umbrella and age-led chooser | Broad hands-on ideas; route by age and moment | Existing |
| Games | Concrete content type | Qualify physical/family/card/board; avoid targeting broad digital-ambiguous wording alone | Research next |
| Arts & Crafts | Concrete content type | Art/craft output with supplies and steps | Research after Games |
| Science & Building | Concrete content type | Experiments, STEM, engineering, construction | Existing wedge |
| Outdoor & Nature | Concrete content type | Outdoor play, nature observation, scavenger hunts | Future research |

### Routes and filters

- age and readiness;
- at home, indoors, outdoors, backyard, or travel;
- available time and setup;
- materials, cost, mess, and cutting;
- energy level and available space;
- number of players and mixed-age fit;
- adult involvement and independent-play potential;
- screen-free status;
- interest hook such as vehicles, animals, water, music, stories, or sensory
  play.

These dimensions can appear in page titles or dedicated pages only when later
SERP and ownership evidence supports distinct intent. They are not an
automatic URL factory.

### Internal lenses, not navigation

- experimentation;
- imagination;
- agency;
- challenge;
- exploration;
- replayability;
- project depth.

KAL should still use these to judge whether an idea is interesting and useful.
They do not need to be explained to parents as a taxonomy.

## Label-By-Label Verdict

- **Make:** reject as a standalone parent-facing category. It overlaps Arts &
  Crafts and Science & Building.
- **Create:** reject as a standalone parent-facing category. It is broader and
  less precise than Arts & Crafts, storytelling, or music.
- **Explore:** reject as a primary label. Use Outdoor & Nature for activity
  content; handle local outings separately.
- **Go Deeper:** reject as a primary label. Use project depth or sustained
  engagement as a format/filter.
- **Play:** rename to Games for parent-facing use, but qualify individual
  search targets because broad `games for kids` is digital-heavy.

## Sequencing

1. Keep `KAL-RES-004` as the next research-only action: validate 5 to 7
   standard-deck games, reconcile rule variants, and test the required chooser
   fields. Do not create the page in that action.
2. After Games, run a separate Arts & Crafts decision pack focused on ages
   3-6, concrete craft outcomes, material/mess/cutting constraints, current KAL
   card overlap, and the evidence needed for original utility.
3. Defer Outdoor & Nature until those two adjacent lanes are understood.
4. Do not build local outings without a location/freshness operating model.
5. Do not build kit, subscription, book, toy, or board-game buying guidance
   without actual access and the existing product-evidence gate.
6. If the user accepts this recommendation, register a separate strategy
   adoption action to replace the abstract labels in canonical docs. A later,
   separately scoped implementation action would decide whether navigation
   should change.

## Unresolved Evidence

- Complete current GSC queries: `UNKNOWN`.
- Comparable complete Google top-result sets and numeric overlap: `UNKNOWN`.
- Actual parent comprehension of the proposed labels: `UNKNOWN`.
- Current KAL engagement or preference data: `UNKNOWN`.
- Parent-tested Games, Arts & Crafts, or Outdoor & Nature evidence: `UNKNOWN`.
- Firsthand product evidence for kits, books, subscriptions, toys, or board
  games: unavailable.
- Whether five parent-facing categories are better than four at KAL's current
  content depth: requires later usability and inventory review.

## Transaction Outcome

Research conclusion: the concrete candidate is strong enough to take to a
separate strategy-adoption decision, not to claim measured parent
comprehension. Keep the live site and current canonical strategy unchanged
until that separate action is authorized and reviewed.

Next eligible action: `KAL-RES-004`.
