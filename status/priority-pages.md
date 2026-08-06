# Priority Page Status

Last updated: 2026-08-06

Sources:

- Current public-safe GSC snapshot: `ops/gsc-snapshots/2026-08-06.md`
- Prior public-safe GSC snapshot: `ops/gsc-snapshots/2026-08-05.md`
- Current machine-readable roadmap and release evidence:
  `ops/seo-roadmap.json`
- Current human-readable roadmap: `ops/seo-roadmap.md`
- Age-four demand and ownership evidence:
  `seo/age-4-keyword-metrics-refresh-2026-07-28.md` and
  `seo/age-4-activity-cluster-decision-pack-2026-07-28.md`
- Card-game demand and ownership evidence:
  `seo/standard-deck-card-game-decision-pack-2026-07-31.md`
- Preschool engineering evidence:
  `seo/preschool-engineering-decision-pack-2026-08-04.md`
- Preschool building evidence:
  `seo/indoor-rainy-building-decision-pack-2026-08-04.md`
- Indoor and rainy-day ownership evidence:
  `seo/indoor-rainy-consolidation-decision-pack-2026-08-04.md`

Demand values below are directional US monthly Semrush estimates retained in
the dated project research. Close variants overlap and are not summed. `n/a`
means the tool did not return volume; `UNKNOWN` means the current research did
not measure that page's primary query. GSC positions are 28-day page-level
averages, not query ranks. Complete current GSC query rows remain unavailable.

## August 6 Monitoring Overlay

The snapshot collected August 6 is finalized through August 4. Property
performance moved from 122 to 127 impressions, clicks remain zero, and average
position moved from 34.27 to 33.16. GSC reports 61 discovered pages, while the
current generated sitemap intentionally contains 60 canonical content URLs;
the difference does not by itself identify an indexing defect. All 10
configured priority URLs are indexed, none are unknown, and no indexing request
was made.

The cardboard-ramp article has 45 impressions at page-average position 14.87,
and the engineering page has 10 impressions at 14.4. Their latest inspected
crawls predate their July 28 and August 4 releases, respectively. The card-game
chooser is indexed and was crawled August 3, but it has no public-safe
performance row. The released building and indoor owners are not in the
configured inspection cohort and have no public-safe page row. These facts are
discovery context, not evidence of query ownership, release causality, or
parent usefulness.

## Site Health

| Surface | Current state | Next check |
|---|---|---|
| Production | Live on `https://kidactivitylab.com`; latest material content release is `KAL-IMP-005` at `38b1c76` through successful Pages run `30996860494`. | Verify exact-SHA Pages and action-specific production invariants after any future `site/**` or Pages-workflow release. |
| Sitemap | Success in GSC; 61 discovered pages; current generated sitemap has 60 canonical content URLs. Last GSC sitemap read remains 2026-07-05. | Treat a refreshed sitemap read or verified technical defect as new evidence; do not request indexing from cadence alone. |
| Priority inspection | 10 of 10 configured URLs indexed; 0 unknown; 0 not indexed. | Expand or change the inspection cohort only in a separately registered monitoring or architecture action. |
| Search performance | 127 impressions, 0 clicks, 0% CTR, page-average position 33.16 for the 28 days through 2026-08-04. | Wait for coherent query evidence, a first click, or a material page/inspection change before diagnosing a snippet or ranking action. |
| Evidence boundary | Research-backed pages are explicitly not family-tested by Kid Activity Lab. All parent and child outcomes remain `UNKNOWN`. | Keep tested status, outcome claims, and product recommendations behind actual firsthand evidence. |

## Acquisition Pages

| Page | Full URL | Directional demand | Current public-safe GSC signal | Role and release state | Review coverage | Remaining / blocker | Next eligible action |
|---|---|---|---|---|---|---|---|
| Homepage | https://kidactivitylab.com/ | No single query owner | 3 impressions; position 18.67; indexed; crawled 2026-07-31 | Site promise and route hub. Current production includes the reviewed `KAL-IMP-005` route changes. | Action-scoped navigation and homepage changes reviewed under `KAL-SEO-001`, `KAL-IMP-002`, and `KAL-IMP-005`; no claim of a complete standalone homepage research cycle. | Sparse page signal and no complete query rows. | Keep as the router; change only when a registered cluster or navigation action requires it. |
| Cardboard ramp guide | https://kidactivitylab.com/articles/cardboard-box-car-ramp-preschoolers.html | `cardboard ramp`: 210; broad and ambiguous. `how to make a ramp with cardboard`: 50. Refreshed 2026-07-28. | 45 impressions; position 14.87; indexed; crawled 2026-07-25 before the release | Build-and-troubleshoot owner. `KAL-IMP-001` released and verified at `a15dca7` / run `30394783721`. | Current query/SERP, source-derived personas, every-section audit, claims, native QA, and independent implementation review completed under `KAL-RES-001` and `KAL-IMP-001`; final `PASS`. | No post-release inspected crawl and no complete current query rows. | Observe a post-release crawl and finalized comparisons; do not attribute current movement to the release. |
| Age-four at-home chooser | https://kidactivitylab.com/ages/activities-for-4-year-olds-at-home.html | `activities for 4 year olds at home`: 50. Refreshed 2026-07-28. | 15 impressions; position 57.47; indexed; crawled 2026-07-22 | Existing age-and-context owner; no recent material implementation. | Page and cluster audited in `KAL-RES-001`; not upgraded through the current research-backed implementation standard. | Sparse signal and broad roundup competition; complete queries unavailable. | Preserve ownership. Revisit only if fresh evidence identifies one bounded usefulness gap. |
| Original age-four STEM pack | https://kidactivitylab.com/collections/original-stem-activities-for-4-year-olds.html | Primary query demand `UNKNOWN`; supports the age-four STEM cluster. | 2 impressions; position 35.5; indexed; crawled 2026-07-09 | Original pack and deeper execution route; no recent material implementation. | Page and cluster audited in `KAL-RES-001`; current family outcomes remain `UNKNOWN`. | Very sparse search signal and no current primary-query measurement. | Keep as support; do not manufacture a rewrite from cadence. |
| Age-four STEM chooser | https://kidactivitylab.com/ages/stem-activities-for-4-year-olds.html | `stem activities for 4 year olds`: 30. Refreshed 2026-07-28. | 5 impressions; position 50.8; indexed; crawled 2026-07-09 | Broad age-four STEM owner; no recent material implementation. | Page and cluster audited in `KAL-RES-001`; not upgraded through a separate current implementation cycle. | Old crawl, sparse signal, and no complete queries. | Preserve the owner; research one bounded improvement only when current evidence supports it. |
| Preschool STEM chooser | https://kidactivitylab.com/collections/stem-activities-for-preschoolers.html | `stem activities for preschoolers`: 1,300. Refreshed 2026-08-04; variants overlap. | 8 impressions; position 50.38; indexed; crawled 2026-07-09 | Broad preschool STEM owner; distinct from engineering and open-ended building. | Boundary and current page role reviewed in `KAL-RES-006`; no recent standalone implementation review. | High directional demand but old crawl, weak page signal, and no complete query evidence; usefulness gap is not yet frozen. | Candidate for bounded research, not automatic implementation or a new URL. |
| Preschool engineering chooser | https://kidactivitylab.com/collections/engineering-activities-for-4-year-olds.html | `engineering activities for preschoolers`: 90. Refreshed 2026-08-04. Age-four exact volume is `n/a`, not zero. | 10 impressions; position 14.4; indexed; crawled 2026-07-26 before the release | Mission-test-redesign owner for editorial ages 4-6. `KAL-IMP-003` released and verified at `f75d414` / run `30909916581`. | Current demand, SERPs, sources, five personas, every section, claims, native/browser QA, and independent implementation review completed under `KAL-RES-006` and `KAL-IMP-003`; final `PASS`. | No post-release inspected crawl or complete query rows. | Observe a post-release crawl or changed finalized GSC evidence. |
| Age-four math chooser | https://kidactivitylab.com/collections/math-activities-for-4-year-olds-at-home.html | Current exact demand not refreshed in the active research: `UNKNOWN`. | 24 impressions; position 41.13; indexed; crawled 2026-07-14 | Existing hands-on math owner; no recent material implementation. | Current architecture links are covered by `KAL-SEO-001`; no current standalone demand/persona/every-section decision pack. | One of the stronger page rows, but query intent and the concrete usefulness gap remain unavailable. | Eligible for bounded research when selected; do not infer the needed edit from the page row alone. |
| No-cut preschool chooser | https://kidactivitylab.com/collections/no-cut-preschool-activities.html | `no cut preschool activities`: volume `n/a`, not zero. Refreshed 2026-07-28. | 2 impressions; position 64.5; indexed; crawled 2026-06-29 | Constraint-led preschool owner; no recent material implementation. | Audited as age-four cluster context under `KAL-RES-001`; no separate current implementation review. | Old crawl, sparse signal, and unavailable complete queries. | Keep as a constraint route; revisit only with distinct current evidence. |
| Standard-deck card-game chooser | https://kidactivitylab.com/collections/card-games-for-kids.html | `card games for kids`: 4,400; `easy card games for kids`: 1,000. Refreshed 2026-07-31; variants overlap. | No page row; indexed; crawled 2026-08-03 after the release | Five-game standard-deck owner. `KAL-IMP-002` released and verified at `3790570` / run `30699530311`. | Current demand, representative SERPs, public rules, source-derived personas, every section, claims, diagrams, native/browser QA, and three-cycle independent review completed under `KAL-RES-004` and `KAL-IMP-002`; final `PASS`. | Indexed but no public-safe performance row or complete queries. Family outcomes remain unknown. | Observe discovery; do not create individual game, age, product, Snap, or Slapjack pages from the same evidence. |
| Preschool building chooser | https://kidactivitylab.com/collections/building-activities-for-4-year-olds.html | `building activities for preschoolers`: 390. Refreshed 2026-08-04. | Page row and priority inspection `UNKNOWN` | Open-ended structure owner with age four retained as a route. `KAL-IMP-004` released and verified at `1c0c227` / run `30945353738`. | Current demand, SERPs, sources, six personas, every section, claims, generator isolation, native/browser QA, and three-cycle independent review completed under `KAL-RES-007` and `KAL-IMP-004`; final `PASS`. | No public-safe page row, configured inspection, or verified post-release crawl. | Observe until a page row, inspected crawl, or changed finalized evidence exists. |
| Preschool indoor chooser | https://kidactivitylab.com/collections/indoor-activities-for-preschoolers.html | `indoor activities for preschoolers`: 390. Refreshed 2026-08-04. | Page row and priority inspection `UNKNOWN` | Single indexable preschool indoor owner; rainy day is a context. `KAL-IMP-005` released and verified at `38b1c76` / run `30996860494`. | Current demand, six incomplete SERP samples, ranking/source pages, six personas, every section, redirect ownership, generated isolation, native/browser QA, and three-cycle independent review completed under `KAL-RES-008` and `KAL-IMP-005`; final `PASS_WITH_P3` with no P0-P2. | No public-safe page row or configured inspection; post-release crawl and Google canonical selection remain unknown. | Observe a post-release crawl or changed finalized evidence; do not request indexing. |
| Rainy-day legacy route | https://kidactivitylab.com/collections/rainy-day-activities-for-preschoolers.html | `rainy day activities for preschoolers`: 170. Refreshed 2026-08-04; treated as context, not a separate owner. | Not a performance target; page row and Google-selected canonical `UNKNOWN` | Accessible instant meta-refresh fallback to the indoor owner; indoor canonical; absent from sitemap and internal links. Released with `KAL-IMP-005`. | Consolidation, redirect semantics, accessibility fallback, sitemap ownership, source boundaries, and production behavior independently reviewed under `KAL-RES-008` and `KAL-IMP-005`. | Google recrawl and canonical selection remain unknown; this is not evidence of a defect. | Keep the fallback unless a verified redirect, canonical, or accessibility defect appears. |

## Supporting Surfaces

| Surface | Full URL | Current role | Current signal / boundary | Next action |
|---|---|---|---|---|
| Activity card library | https://kidactivitylab.com/cards.html | Quick one-screen utility layer for runnable activities. | 1 impression at page-average position 4 in the August 6 snapshot; too sparse for a ranking conclusion. | Improve individual cards only through a registered owner-page or utility action with source and evidence boundaries. |
| Original research hub | https://kidactivitylab.com/original/ | Deeper original packs and research-backed project routes. | No public-safe page row in the current snapshot. Family-use outcomes remain `UNKNOWN`. | Keep as a support hub; add only genuinely distinct, reviewed work. |
| Video archive | https://kidactivitylab.com/video-ideas.html | Supporting idea and setup-visualization archive. | Not the main ranking or product bet. | Preserve as support; do not turn curation cadence into page-production quota. |

## Current Decision

The site is technically healthy and Google is discovering its priority pages,
but search evidence is still early: 127 property impressions, no clicks, and
no complete current query rows. The current record supports neither a broad
title/CTR program nor new-page production from cadence.

The clearest next measurement gates are post-release crawls for the ramp,
engineering, building, and indoor owners; first page rows for the card-game,
building, and indoor pages; a first click; or complete query evidence that
identifies one coherent existing-page gap. The preschool STEM and math owners
are plausible bounded research candidates because their demand or current page
signals are visible, but neither has enough current query and every-section
evidence to authorize implementation from this status transaction.
