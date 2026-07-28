# Age-4 Activity Cluster Decision Pack

Status: review-clean (`PASS_WITH_P3`)

Action: `KAL-RES-001`

Prepared: 2026-07-28

Frozen base: `f693cb02ac623d9c97ed5a371c9b8bfd8c650749`

Scope: age-4 at-home, age-4 STEM, preschool STEM, engineering, cardboard-ramp,
no-cut, original-test-pack, and supporting-card roles

Publication state: research-only; no `site/**`, generator, indexing, external
account, parent-test claim, or deployment mutation

## Decision

Promote one existing-page improvement:
`site/articles/cardboard-box-car-ramp-preschoolers.html`.

Do not create a new page.

The bounded next implementation should make the ramp guide a clearer
build-then-test page for a parent who wants something usable now:

1. retain the no-cut cardboard-plus-books answer and troubleshooting;
2. add one compact, source-backed "change one thing" test route for height,
   car, or surface;
3. distinguish editorial estimates from measured experience, removing or
   relabeling unsupported setup/play-duration and "parent-tested" language;
4. keep the article as the primary ramp build/troubleshooting page and route
   deeper observation work to Ramp Detective in the original test pack;
5. add no parent/child observation, tested-status, engagement, safety-outcome,
   or original-photo claim.

This is not a CTR rewrite. The page has no clicks and complete current GSC query
rows are unavailable. It is an evidence-integrity and parent-utility
improvement supported by page-level discovery, prior query evidence, current
SERP patterns, and the current page audit.

## Evidence Classification

| Evidence | Collected/freshness | Class and use | Limitation |
|---|---|---|---|
| Public-safe GSC snapshots | 2026-07-27 and 2026-07-28, data through 2026-07-25 and 2026-07-26 | `MEASURED`; aggregate, page, crawl, and priority-index context | Complete query, country, and device rows are intentionally omitted. |
| Historical GSC query rows | 2026-07-09 | `MEASURED`; directional evidence that `cardboard ramp` and `how to make a ramp with cardboard` surfaced | Stale, incomplete low-volume sample; not current query ownership. |
| Historical Semrush rows | 2026-07-09 US database | `TOOL_ESTIMATE`; stale corroboration only | Not refreshed; no paid/API use was authorized for this action. |
| Current OpenAI web search | 2026-07-28 | `SOURCE_BACKED` research input for surfaced page types and recurring jobs | Underlying provider, market enforcement, device, full organic depth, and completeness are not exposed. |
| Current ranking pages | Inspected 2026-07-28 | `SOURCE_BACKED`; page-pattern and content-gap analysis | Not proof of rankings, demand, KAL testing, or safety outcomes. |
| Parent/community questions | Surfaced 2026-07-28 | `RESEARCH_HYPOTHESIS` input for parent jobs | Qualitative and self-selected; not demand or firsthand KAL evidence. |
| Current KAL pages | Repository at frozen base | `SOURCE_BACKED` for what the product currently says; audit conclusions are `EDITORIAL_JUDGMENT` | Public behavior was not changed in this transaction. |
| Validated parent-test intake | Unavailable | `UNKNOWN` | The user's earlier report that two activities looked good is not a validated intake. |
| Original ramp photo or diagram | Unavailable | `UNKNOWN` | The current image is not treated as evidence of a real KAL session. |
| Current keyword volume, KD, CPC | Unavailable | `UNKNOWN` | No values are inferred or treated as zero. |

## Fresh GSC Context

Both snapshots passed `node tools/gsc-snapshot.mjs --validate-existing`; all 11
checked-in public JSON snapshots validated.

| Metric | 2026-07-27 snapshot | 2026-07-28 snapshot | Interpretation |
|---|---:|---:|---|
| Finalized data through | 2026-07-25 | 2026-07-26 | Rolling windows differ by one day. |
| Impressions | 61 | 72 | Changed monitoring context, not query evidence. |
| Clicks | 0 | 0 | No CTR experiment is supported. |
| Average position | 28.84 | 29.28 | Aggregate movement is not action-selecting. |
| Priority indexed | 7/7 | 7/7 | No indexing intervention is needed. |
| Discovered sitemap pages | 61 | 61 | Stable. |

Relevant page rows:

| Page | 2026-07-27 impressions / position | 2026-07-28 impressions / position | Index/crawl context |
|---|---|---|---|
| Cardboard ramp article | 17 / 19.76 | 24 / 16.58 | Priority URL indexed; last crawl 2026-07-25. |
| Age-4 at-home hub | 8 / 52.25 | 10 / 57.7 | Priority URL indexed; last crawl 2026-07-22. |
| Age-4 STEM hub | 1 / 45 | 1 / 45 | Priority URL indexed. |
| Preschool STEM hub | 5 / 38.6 | 5 / 38.6 | Priority URL indexed. |
| Engineering age-4 page | 5 / 21.4 | 5 / 21.4 | Page row present; not separately inspected in the priority set. |
| No-cut preschool page | 5 / 27 | 5 / 27 | Priority URL indexed. |
| Cardboard ramp card | 1 / 46 | 1 / 46 | Page row present; current inspection state is `UNKNOWN`. |
| Original age-4 STEM pack | no public page row | no public page row | Priority URL indexed; query/performance detail is `UNKNOWN`. |

The ramp movement is the strongest visible page signal. It does not prove the
current query mix, parent satisfaction, or the value of a title/meta rewrite.

## Query Universe

No close variants are summed. Historical tool values are retained only where
the exact phrase appeared in the 2026-07-09 research artifact.

| Theme | Exact query | Source/market/date | Volume | KD | Intent | Likely job | Limitation |
|---|---|---|---:|---:|---|---|---|
| Age/context | `activities for 4 year olds at home` | OpenAI web search, intended US/English, 2026-07-28; historical Semrush US 2026-07-09 | 50 stale | 17 stale | broad ideas | Find age-fit choices without leaving home. | Current metrics `UNKNOWN`; broad roundup SERP. |
| Age/context | `home activities for 4 year olds` | Historical GSC/Semrush US, 2026-07-09 | 90 stale | 21 stale | broad ideas | Get a realistic home-day activity. | Current metrics and complete query evidence `UNKNOWN`. |
| STEM/age | `stem activities for 4 year olds` | OpenAI web search 2026-07-28; historical Semrush US 2026-07-09 | 30 stale | 6 stale | category/ideas | Choose a hands-on age-4 STEM activity. | Current SERP is mixed and current metrics are `UNKNOWN`. |
| STEM/age | `stem activities for 4 year olds at home` | OpenAI web search, 2026-07-28 | `UNKNOWN` | `UNKNOWN` | category/ideas | Find a short household-material STEM test. | Exact-age results are sparse. |
| STEM/preschool | `stem activities for preschoolers` | Historical Semrush US, 2026-07-09 | 1300 stale | 11 stale | category/ideas | Browse preschool STEM options. | Large stale estimate; no current query row. |
| Engineering | `engineering activities for preschoolers at home` | OpenAI web search, 2026-07-28 | `UNKNOWN` | `UNKNOWN` | category/ideas | Find build-test-redesign activities. | Mixed educator/home results. |
| Engineering | `engineering activities for 4 year olds` | Checked-in keyword target, observed 2026-06-26 | `UNKNOWN` | `UNKNOWN` | category/ideas | Find an age-specific building challenge. | Current SERP sample not retained. |
| Ramp/build | `how to make a ramp with cardboard` | OpenAI web search 2026-07-28; historical GSC/Semrush US 2026-07-09 | 50 stale | 17-18 stale | how-to | Build a simple ramp with materials already at home. | Search mixes preschool, RC, craft, and general ramp intent. |
| Ramp/build | `cardboard ramp` | Historical GSC/Semrush US, 2026-07-09 | 210 stale | 21 stale | ambiguous how-to | Find a cardboard ramp design. | Broad intent includes RC, pets, access, and other non-preschool uses. |
| Ramp/preschool | `cardboard ramp toy cars preschool` | OpenAI web search, 2026-07-28 | `UNKNOWN` | `UNKNOWN` | activity/how-to | Set up a preschool toy-car ramp and know what to test. | Stronger age/activity alignment; no current volume. |
| Ramp/experiment | `preschool toy car ramp experiment` | OpenAI web search, 2026-07-28 | `UNKNOWN` | `UNKNOWN` | experiment | Turn ramp play into one visible test. | Results skew educator/curriculum. |
| Ramp/experiment | `toy car ramp friction experiment preschool` | OpenAI web search, 2026-07-28 | `UNKNOWN` | `UNKNOWN` | experiment | Compare surfaces without a long lesson. | Results skew educator/curriculum. |
| Ramp/rescue | `toy car ramp keeps falling preschool` | OpenAI web search, 2026-07-28 | `UNKNOWN` | `UNKNOWN` | troubleshooting | Stabilize or simplify a failed setup. | Search result set was noisy; demand is not established. |
| Constraint | `no cut preschool activities` | OpenAI web search, 2026-07-28 | `UNKNOWN` | `UNKNOWN` | constraint-led ideas | Avoid scissors and adult craft preparation. | Surfaced results mix no-prep and scissor-skill intent. |
| Constraint | `no prep activities for preschoolers` | OpenAI web search, 2026-07-28; checked-in target observed 2026-06-26 | `UNKNOWN` | `UNKNOWN` | constraint-led ideas | Start without a preparation session. | No comparable complete SERP retained. |
| Constraint | `low mess activities for 4 year olds` | OpenAI web search, 2026-07-28 | `UNKNOWN` | `UNKNOWN` | constraint-led ideas | Protect time and cleanup capacity. | Community-heavy, no current metrics. |
| Constraint | `indoor activities for 4 year olds at home` | OpenAI web search, 2026-07-28; checked-in target observed 2026-06-26 | `UNKNOWN` | `UNKNOWN` | context-led ideas | Fill an indoor stretch with realistic choices. | Broad, competitive roundup intent. |

## SERP Samples And Overlap

### Capture limits shared by all samples

- Search provider/product: OpenAI web search
- Provider database/snapshot date: not exposed
- Pack capture timestamp: 2026-07-28T18:28:18Z
- Per-query timestamp: not exposed
- Country/market: US intended; actual search geolocation not exposed
- Locale/language: English query and response; exact locale not exposed
- Device: `UNKNOWN`
- Requested organic depth: `UNKNOWN`
- Retained organic rows: first five surfaced web results recorded below
- Complete at requested depth: no
- Errors, omissions, SERP features, ads, AI summaries, PAA, video modules, and
  unretained rows: not exposed
- Rank meaning: surfaced order only; not verified organic rank

Because these sets are incomplete and provider details are not fully exposed,
exact-URL and domain overlap counts and Jaccard values are `UNKNOWN`.

### Sample A: `activities for 4 year olds at home`

User job: choose age-fit activities from a broad set.

| Surfaced order | Exact URL | Domain | Page/result type | Notes |
|---:|---|---|---|---|
| 1 | https://www.nemours.org/reading-brightstart/at-home-activities/4-year-olds.html | nemours.org | authority age hub | Literacy/learning taxonomy and strong institutional trust. |
| 2 | https://www.junglefun.co.uk/fun-activities-for-4-year-olds-at-home/ | junglefun.co.uk | commercial roundup | Current large list with low-mess framing. |
| 3 | https://www.weekend.com/post/activities-for-4-year-olds | weekend.com | editorial roundup | Claims real-family testing; broad list. |
| 4 | https://www.twinkl.co.uk/blog/home-learning-activities-for-4-year-olds | twinkl.co.uk | education/product roundup | School-readiness taxonomy and product ecosystem. |
| 5 | https://www.cdc.gov/act-early/milestones/4-years.html | cdc.gov | official age guidance | Not an activity roundup; authority result around age expectations. |

Pattern: breadth and authority dominate. KAL should remain a useful routing hub,
not try to win by adding more generic list items.

### Sample B: `STEM activities for 4 year olds at home`

User job: find an age-fit, hands-on STEM activity at home.

| Surfaced order | Exact URL | Domain | Page/result type | Notes |
|---:|---|---|---|---|
| 1 | https://learner.outschool.com/articles/stem-activities-for-kids-at-home | outschool.com | broad STEM-by-age guide | Current, strong framing around open questions and iteration. |
| 2 | https://www.junglefun.co.uk/fun-activities-for-4-year-olds-at-home/ | junglefun.co.uk | broad age roundup | Not STEM-specific. |
| 3 | https://www.twinkl.com/blog/home-learning-activities-for-4-year-olds | twinkl.com | education roundup | Not STEM-specific. |
| 4 | https://www.education.sa.gov.au/students/curriculum-and-learning/stem-learning/explore-stem-home | education.sa.gov.au | government STEM guide | Authority and inquiry prompts; broad ages. |
| 5 | https://www.twinkl.co.uk/blog/home-learning-activities-for-4-year-olds | twinkl.co.uk | regional duplicate/variant | Same broad education family. |

Pattern: the exact age/STEM query has mixed results. This does not support a new
age-4 STEM page because KAL already has a hub and original pack.

### Sample C: `how to make a ramp with cardboard`

User job: build a ramp now, then possibly test it.

| Surfaced order | Exact URL | Domain | Page/result type | Notes |
|---:|---|---|---|---|
| 1 | https://www.diy.org/challenges/make-a-ramp-with-books | diy.org | interactive how-to | Direct cardboard/books answer plus measurement and extension. |
| 2 | https://www.instructables.com/Quick-and-Easy-Cardboard-Rc-Car-Ramp/ | instructables.com | RC craft how-to | Tool/cutting-heavy and not preschool-specific. |
| 3 | https://www.diy.org/challenges/build-a-zig-zag-ramp | diy.org | complex craft/experiment | Multiple cuts and sections; broader child age. |
| 4 | https://www.pbs.org/parents/crafts-and-experiments/cardboard-parking-garage | pbs.org | authority craft | Paint/glue-gun garage build with ramp. |
| 5 | https://www.diy.org/challenges/build-a-ramp | diy.org | experiment how-to | Strong direct answer and test framing; more measurement than preschoolers need. |

Pattern: intent is mixed between a simple toy-car slope, elaborate craft, and
non-preschool RC builds. KAL's no-cut two-minute route is distinctive, but its
evidence language must be honest.

### Sample D: `cardboard ramp toy cars preschool`

User job: run an age-appropriate toy-car ramp and know what to do next.

| Surfaced order | Exact URL | Domain | Page/result type | Notes |
|---:|---|---|---|---|
| 1 | https://www.pnc.com/en/about-pnc/corporate-responsibility/grow-up-great/lesson-center/transportation/rolling-with-ramps.html | pnc.com | structured preschool lesson | Multiple ramp heights, predictions, marks, and inquiry prompts. |
| 2 | https://www.pbs.org/parents/crafts-and-experiments/cardboard-parking-garage | pbs.org | authority craft | Elaborate craft rather than fastest start. |
| 3 | https://www.diy.org/challenges/build-a-ramp | diy.org | experiment how-to | Direct build and fair-test structure. |
| 4 | https://www.peepandthebigwideworld.com/en/educators/curriculum/family-child-care-educators/ramps/activity/guided-activity/244/roll-or-slide-indoors/ | peepandthebigwideworld.com | preschool curriculum | Predict/compare/sort and age-appropriate vocabulary. |
| 5 | https://myboredtoddler.com/tunnels-and-ramps-with-toy-cars/ | myboredtoddler.com | parent/teacher activity post | Photos, pretend play, tunnels, and longer cardboard setup. |

Pattern: direct activity pages combine build, prediction, one variable, and
visible examples. KAL has the first three but lacks source attribution and
currently overstates some experiential details.

### Sample E: `no cut preschool activities`

User job: avoid scissors and adult craft prep.

| Surfaced order | Exact URL | Domain | Page/result type | Notes |
|---:|---|---|---|---|
| 1 | https://kidsactivitiesblog.com/137851/60-no-prep-activities-for-preschoolers/ | kidsactivitiesblog.com | large no-prep roundup | Adjacent constraint, not exact no-cut framing. |
| 2 | https://www.naeyc.org/node/2519 | naeyc.org | playdough plan | Authority result but includes cutting suggestions. |
| 3 | https://www.friendsartlab.com/9-non-paper-cutting-activities-for-preschoolers/ | friendsartlab.com | scissor-skill article | Opposite intent: cutting non-paper materials. |
| 4 | https://preschoolponderings.com/2025/05/easy-last-minute-activities/ | preschoolponderings.com | no-prep teacher list | Adjacent last-minute intent. |
| 5 | https://teachingmama.org/no-cost-low-prep-preschool-activities/ | teachingmama.org | low-prep roundup | Adjacent intent and some cutting. |

Pattern: the exact modifier is ambiguous. The existing KAL page has useful
constraint definitions, but current evidence does not justify expansion or a
separate no-glue/no-tape page.

### Comparable-Set Overlap

| Query pair/family | Comparable? | `|A|` | `|B|` | Exact URL overlap | Domain overlap | Page-type overlap | Decision | Confidence |
|---|---|---:|---:|---|---|---|---|---|
| Broad age vs age-4 STEM | no | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | Broad roundups and authority guides recur qualitatively. | Keep distinct KAL hubs but do not add pages. | medium |
| Ramp build vs preschool ramp | no | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | DIY and PBS recur; preschool sample adds curriculum/parent pages. | One ramp guide can serve build plus one test; no second ramp page. | high |
| No-cut vs no-prep | no | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | Adjacent constraints blend and cutting-skill pages intrude. | Keep the current no-cut definition; observe. | medium |
| Ramp vs broad age | no | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | No meaningful qualitative page-type recurrence in retained rows. | Route from broad hub to focused ramp article. | medium |

## Representative Ranking-Page Analysis

| Page | What it does well | Weakness/opportunity | Advantage KAL cannot claim | Honest KAL response |
|---|---|---|---|---|
| PNC Rolling with Ramps | Structured predictions, height changes, marked distances, inquiry prompts, and extensions. | Classroom prep, multiple ramps, charts, and longer flow. | Kentucky Science Center curriculum contribution and institutional authority. | Offer one low ramp, one changed variable, one mark, and a stop/rescue line. |
| PEEP Roll or Slide | Age-appropriate compare/sort job, simple vocabulary, accommodation note. | Educator flow, multiple objects, 20-30 minute session. | NSF-funded curriculum and educator observation. | Use source-backed one-variable prompts without claiming a KAL-observed outcome. |
| PBS Cars on Ramps | Video makes height and friction visible; transcript models parent language. | Eight-minute video and cookie-sheet setup are slower than KAL's first start. | Public-media production and filmed parent/child demonstration. | Keep KAL text-first and link or cite sources rather than imply KAL testing. |
| Pre-K Pages Ramps and Friction | Strong photos, texture options, open exploration, and clear extension questions. | Teacher-oriented, many materials, optional measurement can become a lesson. | Firsthand educator/parent framing and original photography. | Limit to one chosen test and request a real KAL visual separately. |
| Toddler Approved Cardboard Ramps | Parent scenario, photos, tunnels, and open-ended play. | Requires cutting/tape and a more elaborate setup. | Firsthand family photos and reported experience. | Differentiate on no-cut speed and honest untested status. |
| DIY.org Build a Ramp | Direct-answer structure, material substitutions, fair-test steps, troubleshooting. | More tools, timing, measurement, and generic multi-age language than age 4 needs. | Interactive product and deeper challenge system. | Provide the useful default before optional testing; avoid stopwatch/math overload. |
| Nemours Age 4 | Strong age authority and clear learning taxonomy. | Narrow literacy focus; not a tired-parent activity runner. | Institutional child-development authority. | Avoid developmental promises; optimize for starting and adapting one activity. |
| Kids Activities Blog No Prep | Large breadth and strong match to "need ideas now." | Sixty-item scan burden and weak exact no-cut differentiation. | Established content inventory and domain breadth. | Keep KAL's smaller constraint chooser instead of inflating list size. |

## Persona Hypotheses

These are source-derived `RESEARCH_HYPOTHESIS` lenses, not demographic truth,
parent-test evidence, or claims about all parents.

| ID | Job to be done | Context | Child-age/pace constraint | Anxieties | Decision criteria | Failure mode | Evidence links | Pages/sections |
|---|---|---|---|---|---|---|---|---|
| P1 Start-now parent | Start one activity with materials already visible. | Dinner prep, after preschool, or a tired indoor stretch. | Four-year-old may move on before adult setup is complete. | Prep takes longer than play; activity needs a store trip. | First answer, exact materials, under-one-screen setup, easy reset. | Page opens with theory or a large list. | Queries: no prep, low mess, activities at home; Kids Activities Blog; Reddit low-effort threads; KAL current chooser. | Ramp quick answer; age-4 quick pick; no-cut chooser. |
| P2 Constraint-first parent | Avoid a specific burden: scissors, glue, tape, mess, small pieces, or constant fixing. | Shared room, younger sibling nearby, rented floor, limited cleanup capacity. | Child needs a runnable choice after adult removes unsafe or unavailable materials. | Damage, cleanup, unstable setup, sibling access. | Explicit exclusions, supervision boundary, stop rule, alternate material. | "No prep" still requires cutting, laminating, or a craft build. | No-cut SERP ambiguity; KAL no-cut sections; community low-mess questions. | No-cut definition/chooser; ramp materials/safety/troubleshooting. |
| P3 One-test STEM parent | Turn play into one visible prediction and comparison without delivering a lesson. | Parent has a car, cardboard, and a few minutes. | Child can choose and observe but may not sustain recording or repeated trials. | STEM language becomes abstract; adult takes over. | One variable, short script, release without pushing, visible finish mark. | Too many variables or measurement tasks cause free play/abandonment. | PNC, PEEP, PBS Cars on Ramps, Pre-K Pages, current Ramp Detective. | Ramp build/test module; original pack. |
| P4 Rescue-and-stop parent | Recover when the ramp slips, car stops, or child gets frustrated, then end cleanly. | First attempt failed or became chaotic. | Child needs one easier success or permission to switch to free play. | Parent must construct rails or keep correcting the child. | Problem-to-fix table, one rescue line, explicit stop condition. | Page treats failure as error or adds more setup. | Existing ramp troubleshooting; PEEP accommodations; DIY.org stability guidance. | Ramp troubleshooting, stop line, cleanup. |
| P5 Pretend-and-extend parent | Keep a successful setup useful through a story or one extension. | Child prefers cars, stories, or free play over formal experiments. | Testing may become garage, bridge, crash-zone, or race play. | "Learning activity" suppresses the play the child chose. | Optional story route, one extension at a time, clear handoff to free play. | Page demands a chart or correct explanation. | My Bored Toddler tunnels/ramps; PBS parking garage; current related pages and Bridge Rescue. | Ramp extensions; age-4 hub routing; original pack story activities. |

## Current Page Inventory

| URL/path | Primary job | GSC/index state | Personas | Strengths | Gaps | Overlap risk | Verdict | Blocker |
|---|---|---|---|---|---|---|---|---|
| `site/articles/cardboard-box-car-ramp-preschoolers.html` | Build and troubleshoot a simple toy-car ramp. | 24 impressions, position 16.58; indexed; crawled 2026-07-25. | P1-P5 | Strong direct answer, no-cut default, safety, troubleshooting, internal links. | Unsupported duration/parent-tested wording; experiment route lacks source attribution and compact fair-test structure. | Could overlap Ramp Detective if expanded into a full test pack. | improve | No validated KAL test or original photo. |
| `site/ages/activities-for-4-year-olds-at-home.html` | Route a parent among broad age-4 at-home choices. | 10 impressions, position 57.7; indexed. | P1, P2, P5 | Parent-situation chooser and links to focused pages. | "Proven" wording and precise times are unsupported; broad SERP rewards authority/breadth KAL lacks. | Should not absorb full ramp or STEM instructions. | keep/observe | Query rows and clicks unavailable. |
| `site/ages/stem-activities-for-4-year-olds.html` | Route age-4 parents among STEM prompts. | 1 impression, position 45; indexed. | P2, P3, P5 | Clear one-question model, chooser, original-pack route. | Exact-age SERP is mixed; "high engagement" and time precision lack validated KAL evidence. | Overlaps preschool STEM and engineering if expanded generically. | keep/observe | Parent-test evidence unavailable. |
| `site/collections/stem-activities-for-preschoolers.html` | Broad preschool STEM collection. | 5 impressions, position 38.6; indexed. | P2, P3 | Simple build/test framing and card routing. | Generic generated list, little differentiated parent decision support, precise time claims. | Strong overlap with age-4 STEM and engineering collections. | observe | No clicks, current query rows, or parent evidence. |
| `site/collections/engineering-activities-for-4-year-olds.html` | Broad build-test-redesign collection. | 5 impressions, position 21.4; inspection state `UNKNOWN`. | P2, P3 | Distinct engineering framing and relevant ramp card. | Generic list and precise time claims; no current query evidence. | Could compete with STEM hubs for broad activities, not the ramp build how-to. | observe | Query intent and index inspection unavailable. |
| `site/collections/no-cut-preschool-activities.html` | Route by excluded materials and cleanup burden. | 5 impressions, position 27; indexed. | P1, P2 | Useful definition, constraint chooser, small curated set. | Exact query SERP is ambiguous; "two-minute" language is not measured. | No-cut/no-prep/low-mess modifiers may not deserve separate URLs. | keep/observe | Complete queries and clicks unavailable. |
| `site/collections/original-stem-activities-for-4-year-olds.html` | Run five structured activity-test prompts. | No public page row; indexed. | P3-P5 | Parent job, kid script, safety, rescue, variants, observation prompt. | Test-pack label can be mistaken for tested content; precise duration and behavior expectations are not validated. | Should own KAL testing workflow, not broad ramp build intent. | defer improvement | Validated parent-test intake and original visual unavailable. |
| `site/cards/cardboard-car-ramp.html` | One-screen utility card. | 1 impression, position 46; inspection state `UNKNOWN`. | P1, P2 | Extremely fast steps and parent check. | Video-led source, unsupported two-minute label, no link to full guide. | Thin card should support, not compete with, the guide. | keep/support | Current index state and query role unavailable. |

## Every-Section Audit

### `site/articles/cardboard-box-car-ramp-preschoolers.html`

| Section | Current job | Persona fit | Evidence/trust | Repetition/scan cost | Verdict | Planned response |
|---|---|---|---|---|---|---|
| Title/meta/canonical/schema | Match direct ramp build intent. | P1, P2 | Query/page signal supports ramp topic; Article image provenance is not treated as testing. | Low. | keep/adjust | Preserve topic/canonical; update modified date only in implementation. |
| Hero answer | Give simplest setup. | P1 | Honest editorial instruction. | Low. | keep | Retain cardboard plus low books plus cars. |
| Hero image | Visualize the arrangement. | P1, P2 | Asset exists; original-session provenance is `UNKNOWN`. | Low. | keep with boundary | Do not call it a parent-test photo or observation. |
| Quick answer steps | Make the ramp immediately. | P1, P2 | Matches current source patterns. | Some duplication with four-step build. | keep/compress | Keep as the first answer; later build section can carry nuance. |
| Quick Verdict and facts | Set expectations. | P1, P2 | "Setup time 2 minutes" and "Play time 10-30 minutes" are not measured or labeled estimates. | Moderate duplication. | replace | Use "materials/setup" facts without claimed play duration; label any estimate editorially. |
| Intro/history paragraphs | Explain why setup is simple. | P1 | Editorial judgment. | Repeats quick verdict. | compress | One paragraph at most. |
| Safety callout | Bound climbing and stability risk. | P2, P4 | Practical supervision boundary; no outcome claim. | Useful. | keep | Retain conservative language; no expanded safety claim. |
| What You Need | Prevent a store trip. | P1, P2 | Directly useful. | Low. | keep | Keep explicit "do not need" exclusions. |
| Best cardboard | Choose a workable surface. | P1, P4 | Practical editorial advice; not tested evidence. | Low. | keep | Phrase as setup guidance, not a guaranteed result. |
| Build It In 4 Steps | Add detail after quick answer. | P1 | Source-consistent. | Duplicates first ordered list. | compress/merge | Retain only details not already in the first answer. |
| What To Say | Supply short prompts. | P3, P5 | Source-backed prompt pattern. | Low. | keep/adjust | Organize around predict, release, observe, change one thing. |
| Troubleshooting table | Rescue failed setup. | P2, P4 | Strong KAL differentiation; no firsthand outcome claimed. | Low. | keep | Add no new unverified safety outcome. |
| Make It More Fun | Offer extensions. | P3, P5 | Source-backed categories and editorial routes. | Current list blends experiment and pretend play. | split/replace | Use "pick one test" and "turn it into play" mini-routes. |
| What A 4-Year-Old Can Do | Set adult/child roles. | P3 | Capability wording is broad and not validated for every child. | Low. | adjust | Use invitation language: "Offer the child..." rather than universal ability. |
| Cleanup | End quickly. | P1, P4 | "Less than two minutes" is unsupported. | Low. | adjust | Remove exact duration or label as an editorial target. |
| FAQ | Resolve build/safety/role questions. | P1, P2, P4 | Useful, but "usually safe" can read as a safety outcome. | Moderate. | adjust | Keep practical supervision boundary; avoid universal safety assurance. |
| Related projects | Protect page architecture. | P3, P5 | Correct links to card, test pack, and hubs. | Low. | keep | Clarify guide vs Ramp Detective roles in anchor text if needed. |
| Footer | Brand promise. | all | "Parent-tested notes" is unsupported because no validated intake exists. | Low but high trust impact. | replace | Use "practical setup notes" or another evidence-honest promise. |

### `site/ages/activities-for-4-year-olds-at-home.html`

| Section | Current job | Persona fit | Evidence/trust | Repetition/scan cost | Verdict | Planned response |
|---|---|---|---|---|---|---|
| Title/meta/hero | Establish broad age/home route. | P1, P5 | Appropriate topic; age capability sentence is editorial. | Low. | keep | No implementation selected. |
| Quick pick | Route to ramp, pack, or pretend play. | P1, P5 | Useful, but not measured behavior. | Low. | keep/adjust later | Avoid implying tested preference. |
| Parent-situation chooser | Reduce decision effort. | P1-P3, P5 | Strong product structure. "Proven low-prep" is unsupported. | Low. | keep/claim-fix later | Replace "proven" when this page is next edited. |
| Summary activity table | Compare time/mess/materials. | P1, P2 | Precise times are unlabeled editorial estimates. | Medium. | audit later | Add estimate labels or remove precision in a future page-specific action. |
| Eight activity cards | Supply runnable previews. | P1, P5 | Utility is real; evidence depth varies. | High repeated structure. | keep/observe | Do not add more cards now. |
| Original-pack route | Protect broad vs test-pack roles. | P3 | Good architecture. | Low. | keep | Preserve. |
| "Searches this page is built for" | Expose internal SEO language publicly. | none | Search-target prose is not parent utility. | Adds scan cost. | replace later | Convert to useful related routes in a separate action. |
| Safety section/footer | Give general supervision boundaries. | P2 | Practical but not a tested outcome. | Low. | keep/claim-audit later | No new safety claim. |

### `site/collections/no-cut-preschool-activities.html`

| Section | Current job | Persona fit | Evidence/trust | Repetition/scan cost | Verdict | Planned response |
|---|---|---|---|---|---|---|
| Title/meta/hero | Define no-cut intent. | P1, P2 | Strong exact constraint; SERP alignment uncertain. | Low. | keep | Observe rather than expand. |
| Pick intro | Define materials and adult check. | P1, P2 | Honest utility. | Low. | keep | Preserve. |
| Constraint chooser | Route by no tape, mess, play length, sibling. | P1, P2, P5 | Differentiated structure; small-piece guidance is practical. | Low. | keep | No new page split. |
| Fastest-start quick card | Give immediate options. | P1 | "Two-minute" is an unmeasured estimate. | Repeats later fastest-start section. | compress later | Use one fastest-start surface, not two. |
| Tired-afternoon paragraph | Explain tradeoffs. | P1, P2 | Useful editorial judgment. | Some repetition. | merge later | Merge into chooser note. |
| What no-cut means | Set boundary and stop rule. | P2, P4 | Strong differentiation. | Low. | keep | Preserve. |
| Fastest no-cut starts | Curate links. | P1, P5 | Useful but overlaps quick card. | Moderate. | keep/compress later | One route list. |
| Related help | Route broad age/card library. | P1 | Appropriate. | Low. | keep | Preserve. |
| Library grid | Expose eight cards. | P1, P5 | Utility layer. | Moderate. | keep | Do not expand without evidence. |
| Footer | Restate parent check. | P2 | Evidence-honest supervision reminder. | Low. | keep | Preserve. |

## Page Architecture

| Query/user job | Treatment | URL | Rationale | Evidence gap |
|---|---|---|---|---|
| Broad age-4 home activities | existing hub | `/ages/activities-for-4-year-olds-at-home.html` | Broad SERP and current routing role. | No clicks or complete queries. |
| Age-4 STEM choices | existing hub | `/ages/stem-activities-for-4-year-olds.html` | Already distinct from broad home hub; mixed exact SERP. | Minimal page signal and no parent test. |
| Broad preschool STEM | existing collection | `/collections/stem-activities-for-preschoolers.html` | Existing page can remain a broader age route. | Generic utility and no clicks. |
| Age-4 engineering | existing collection | `/collections/engineering-activities-for-4-year-olds.html` | Existing build-test-redesign route; no need for more engineering URLs. | Complete query and index-inspection evidence unavailable. |
| Make a cardboard ramp for toy cars | existing-page improvement | `/articles/cardboard-box-car-ramp-preschoolers.html` | Strongest page signal and distinct build/troubleshoot job. | Current queries, clicks, validated test, and original photo unavailable. |
| Run a ramp surface/height test | section/module in ramp guide plus deeper test-pack route | same article, then `#ramp-detective` | Current SERPs blend build and one-variable experiments; a second ramp page would fragment intent. | No KAL observation of which test works best. |
| One-screen cardboard ramp steps | support card | `/cards/cardboard-car-ramp.html` | Utility role; should route to guide rather than compete. | Index role `UNKNOWN`. |
| No scissors/craft prep | existing collection | `/collections/no-cut-preschool-activities.html` | Useful constraint definition despite ambiguous SERP. | Exact query demand and ownership unavailable. |
| Parent-tested age-4 activity outcomes | defer | original test pack / future winning activity | Human evidence gate is not satisfied. | Validated intake and original visual unavailable. |

## Candidate Or Section Ledger

| Candidate/section | Retain/defer/remove | Role | Persona fit | Evidence | Reason |
|---|---|---|---|---|---|
| Ramp direct answer | retain | existing article first answer | P1, P2 | GSC page signal + current build SERP | Best current useful default. |
| Ramp compact one-variable test | retain/promote | article section | P3, P4 | PNC, PEEP, PBS, DIY.org, Pre-K Pages | Adds honest utility without a new URL. |
| Ramp full observation workflow | retain elsewhere | original pack Ramp Detective | P3-P5 | Current KAL architecture | Avoid article/test-pack duplication. |
| Ramp exact durations | remove or relabel | expectation metadata | P1 | `UNKNOWN` measured evidence | Precision implies experience KAL cannot support. |
| Ramp "parent-tested" footer | remove | trust claim | all | No validated intake | Direct evidence-integrity issue. |
| Ramp original photo | defer | trust/visual | all | `UNKNOWN` | User input required. |
| More broad age/STEM cards | defer | hub inventory | P1, P3 | No clicks/query evidence | More list items would not create differentiation. |
| Separate no-glue/no-tape/low-mess pages | defer | potential modifiers | P2 | Incomplete/ambiguous SERPs | Modifiers do not prove standalone intent. |
| New individual original activity pages | defer | future tested content | P3-P5 | No validated parent test or visual | Human gate. |

## Claim And Human Gates

- `VALIDATED_PARENT_TEST`: unavailable. Do not say KAL tested the ramp or any
  activity.
- Child quote, minutes engaged, repeat request, confusion, favorite material,
  and observed mess: `UNKNOWN`.
- Setup/play/cleanup duration: currently editorial estimates, not measured.
  Label clearly or remove exact precision.
- Original photo or diagram: unavailable. Do not describe the current asset as
  a real-session photo.
- Safety outcomes: unavailable. Keep only conservative supervision and
  setup-boundary language; do not claim an activity is universally safe.
- Developmental/learning outcomes: not in scope. Source-backed inquiry prompts
  do not justify guaranteed learning claims.
- Current complete GSC query ownership: `UNKNOWN`.
- Paid keyword metrics: not refreshed; historical values are stale
  `TOOL_ESTIMATE`.
- Indexing request: prohibited for this action and not needed with 7/7 priority
  URLs indexed.
- External accounts, monetization, and paid tools: not authorized.

## Promoted Next Action

- Action ID: `KAL-IMP-001`
- Primary target:
  `site/articles/cardboard-box-car-ramp-preschoolers.html`
- Exact/bounded paths: freeze in the implementation transaction before edits;
  expected boundary is the manual article, sitemap if its generator requires a
  changed lastmod, one page-review artifact, and the minimum roadmap/review
  state files. No new page.
- Required research refresh: confirm no newer GSC snapshot changes the selected
  page or exposes complete query evidence before implementation.
- Persona acceptance:
  - P1 sees the cardboard/books/cars answer before optional detail.
  - P2 sees no-cut/no-glue boundaries, low/stable setup, and alternatives.
  - P3 can run one test by changing only height, car, or surface.
  - P4 can rescue slipping/stopping/frustration or stop cleanly.
  - P5 can turn the setup into free play without being forced through a lesson.
- Search/cannibalization acceptance:
  - retain ramp build/troubleshooting as the article's primary job;
  - keep the quick card as one-screen support;
  - keep Ramp Detective as the deeper observation/test-pack route;
  - do not create another ramp URL or expand broad age/STEM lists.
- Evidence and human-review limits:
  - remove/relabel unsupported duration and parent-tested wording;
  - no parent/child outcome, quote, engagement, original-photo, developmental,
    or universal safety claim;
  - cite source-backed experiment structure without copying source prose.
- QA:
  - run required page generators and sitemap command under repository policy;
  - verify exact output scope and no unrelated generated churn;
  - `git diff --check`;
  - local link and fragment validation;
  - HTML title/meta/canonical/structured-data inspection;
  - focused desktop/mobile visual check for the edited page;
  - verify no unsupported evidence-class claims remain on the page.
- Independent review:
  - different read-only reviewer;
  - persona-by-persona and every-section review;
  - P0-P2 fixed for at most three cycles;
  - only `PASS` or `PASS_WITH_P3` may release.
- Release invariant:
  - exact reviewed commit on `main`;
  - GitHub Pages succeeds for the exact SHA;
  - live article returns 200, preserves canonical and source links, and
    contains the reviewed first answer/test/rescue structure;
  - no other public page changes unless declared before implementation.

## Measurement Plan

Release checks:

1. verify generated/local HTML and links before commit;
2. verify `main` equals `origin/main` after push;
3. verify the exact GitHub Pages run succeeds;
4. verify live title, canonical, first answer, source/test module,
   troubleshooting, and evidence-honest footer.

Search observation:

- Wait for a post-release recrawl before attributing movement.
- Compare finalized public-safe GSC snapshots at page level; use complete query
  evidence only through an approved private workflow.
- Continue observing if impressions/position fluctuate without clicks.
- Do not run a title/CTR experiment until click and query evidence exists.
- Revisit structure if two post-recrawl finalized comparison points show a
  durable page-level decline and no broader site explanation.
- Treat the first click or clearer query evidence as a new gate, not proof of
  parent usefulness.

Product observation:

- The next real parent-test intake may validate or reject setup duration,
  rescue usefulness, and repeatability.
- Until then, public copy remains instruction and editorial guidance, not
  observed KAL performance.

## Unresolved Evidence Gaps

- Complete current GSC query rows.
- Current paid-tool volume, KD, CPC, and SERP history.
- A provider-complete, device/market-specific organic SERP set suitable for
  numeric overlap.
- Validated intake for either activity the user previously tried.
- Original ramp photo or diagram with known provenance.
- Current index-inspection state for the engineering page and ramp card.
- Click/CTR evidence for any page.
- Evidence that no-cut, low-mess, no-tape, or no-glue modifiers deserve
  separate pages.

## Sources

Repository:

- `ops/gsc-snapshots/2026-07-27.json`
- `ops/gsc-snapshots/2026-07-28.json`
- `seo/gsc-seo-review-2026-07-09.md`
- `data/seo_keyword_targets.csv`
- the eight current KAL pages inventoried above

Current public sources inspected 2026-07-28:

- PNC/Kentucky Science Center, Rolling with Ramps:
  https://www.pnc.com/en/about-pnc/corporate-responsibility/grow-up-great/lesson-center/transportation/rolling-with-ramps.html
- PEEP and the Big Wide World, Roll or Slide:
  https://www.peepandthebigwideworld.com/en/educators/curriculum/family-child-care-educators/ramps/activity/guided-activity/244/roll-or-slide-indoors/
- PBS, Cars on Ramps:
  https://www.pbs.org/video/cars-ramps-jlzsqr/
- Pre-K Pages, Exploring Ramps and Friction:
  https://www.pre-kpages.com/science-kids-exploring-ramps-friction/
- Toddler Approved, Cardboard Car Ramps and Tunnels:
  https://toddlerapproved.com/cardboard-car-ramps-and-tunnels-for-kids/
- My Bored Toddler, Tunnels and Ramps with Toy Cars:
  https://myboredtoddler.com/tunnels-and-ramps-with-toy-cars/
- Chicago Children's Museum, Build a Ramp:
  https://www.chicagochildrensmuseum.org/parenting-playbook-posts/2020/5/18/at-home-activity-build-a-ramp
- DIY.org, Build a Ramp:
  https://www.diy.org/challenges/build-a-ramp
- Nemours, Activities by Age for 4-Year-Olds:
  https://www.nemours.org/reading-brightstart/at-home-activities/4-year-olds.html
- South Australia Department for Education, Explore STEM at Home:
  https://www.education.sa.gov.au/students/curriculum-and-learning/stem-learning/explore-stem-home
- Kids Activities Blog, No-Prep Activities for Preschoolers:
  https://kidsactivitiesblog.com/137851/60-no-prep-activities-for-preschoolers/

Qualitative community question sources:

- Low-effort preschool activities:
  https://www.reddit.com/r/Preschoolers/comments/1s17u9u/what_are_some_low_effort_activities_that_keep/
- Realistic screen-free ideas for a four-year-old:
  https://www.reddit.com/r/Preschoolers/comments/1sg5ghp/need_realistic_screenfree_activity_ideas_for_a/
- STEM for a fantasy-loving almost-four-year-old:
  https://www.reddit.com/r/Parenting/comments/1rjxs1p/fun_stem_activities_for_fantasy_loving_toddler/
