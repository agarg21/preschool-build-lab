# Preschool Indoor And Rainy-Day Ownership Decision Pack

Date: 2026-08-04

Action: `KAL-RES-008`

Frozen repository base:
`d6cdb4ee50c8f3110c8904ae691a6a55002b7ce1`

Publication state: research-only. This transaction changes no public page,
generator, sitemap, navigation, indexability, URL, indexing request, external
account, product recommendation, or family evidence.

## Decision

Consolidate the current preschool indoor and rainy-day ownership around the
existing indoor URL:
`/collections/indoor-activities-for-preschoolers.html`.

Promote one separate implementation candidate, `KAL-IMP-005`, that should:

1. Upgrade the indoor URL into one preschool indoor chooser organized by the
   parent's immediate moment: start with almost no setup, use some energy in a
   bounded space, make or build, play a game, or choose quieter play.
2. Retire the current rainy-day URL as a competing indexable page. Because the
   site is static on GitHub Pages and cannot issue a repository-defined server
   redirect, preserve the old URL as an accessible instant `meta refresh`
   redirect with its canonical set to the indoor owner, remove it from the
   sitemap and internal links, and test the redirect. Google documents an
   instant `meta refresh` as a permanent redirect signal when a server-side
   redirect is unavailable.
3. Treat rainy day as a context inside the indoor chooser, not as a second
   near-duplicate activity list.
4. Keep rain-themed crafts and weather exploration as a deferred research
   candidate. The distinct exact query exists, but the current rainy page does
   not satisfy that job and this evidence does not justify a replacement page.

This decision is supported by five independent boundaries:

- Fresh Semrush estimates show demand for `indoor activities for
  preschoolers` (390/KD 25), `indoor games for preschoolers` (390/KD 17), and
  `indoor gross motor activities for preschoolers` (260/KD 12). Close variants
  overlap and are never added together.
- `rainy day activities for preschoolers` is smaller and harder at 170/KD 31.
  Its current cached result set visibly recurs with the indoor preschool set:
  ParentMap, BrightPath, the same Reddit thread, the same Pinterest board, Penn
  State, the same Instagram reel, and the same YouTube video appear across the
  accessible modules. The samples are incomplete, so every numeric overlap
  field remains `UNKNOWN`.
- KAL's two current pages share eight of nine cards, the same chooser shape,
  the same generic safety block, and the same unsupported-looking exact time
  and mess labels. Rainy has only Paper Roll Drop where indoor has Block Tower.
- `rainy day crafts for preschoolers` (70/KD 18) produces a distinct,
  image-heavy weather-craft result mix. That is evidence of a different future
  product, not support for keeping the current duplicated rainy page.
- `preschool activities at home` (480/KD 21) produces a learning/curriculum
  result mix. It remains a boundary and should not become the indoor page's
  primary promise.

No search or family result is guaranteed. The candidate pages have no
public-safe GSC page row or priority inspection, complete GSC query rows are
unavailable, and all family-use outcomes remain `UNKNOWN`.

## Evidence Classification

| Evidence | Collected/freshness | Class and use | Limitation |
|---|---|---|---|
| August 3 and 4 public-safe GSC snapshots | Finalized data through 2026-08-01 and 2026-08-02 | `MEASURED` portfolio and configured-inspection context | Complete query rows, both candidate page rows, and both candidate inspections are unavailable. |
| 36 Semrush US keyword rows | Refreshed in logged-in Chrome on 2026-08-04; UI database August 2026; all rows showed `Now` | `TOOL_ESTIMATE` directional demand, difficulty, CPC, and intent | Variants overlap. Eight volumes are `n/a`, not zero; one row is an explicit zero estimate. |
| Six Semrush cached Google samples | Inspected in logged-in US desktop interface on 2026-08-04 | `TOOL_ESTIMATE` recurrence, module, result-type, and intent-shape evidence | No equal-depth complete organic export; numeric URL/domain overlap is `UNKNOWN`. |
| Nine ranking, extension, publisher, and commercial pages | Retrieved or inspected 2026-08-04 | `SOURCE_BACKED` within each page's limits | External narratives and claims do not become KAL family outcomes. |
| Six source-derived parent-job personas | Prepared 2026-08-04 | `RESEARCH_HYPOTHESIS` review lenses | Not demographic truth, demand totals, or family-test evidence. |
| Consolidation, page ownership, modules, and future scope | Prepared 2026-08-04 | `EDITORIAL_JUDGMENT` | Requires a separately registered implementation, native QA, independent review, and production verification. |
| Parent/child use, timing, comprehension, engagement, enjoyment, learning, repeatability, observed mess, and safety outcomes | Unavailable | `UNKNOWN` | No language may imply that KAL ran or observed an activity. |

## Fresh GSC Context

| Measure | 2026-08-03 snapshot | 2026-08-04 snapshot | Interpretation |
|---|---:|---:|---|
| Finalized rolling 28-day impressions | 116 | 119 | Small healthy movement; not candidate-query evidence |
| Clicks | 0 | 0 | No CTR evidence |
| Average position | 35.47 | 34.77 | Small portfolio movement |
| Discovered sitemap pages | 61 | 61 | Stable |
| Priority URLs indexed | 7/7 | 10/10 | Both configured cohorts healthy; monitored set expanded on August 4 |

Neither candidate URL has a public-safe page row in either snapshot or a
configured priority inspection. Their clicks, impressions, queries, crawl
state, canonical selection, and index state remain `UNKNOWN`, not zero or not
indexed. The GSC snapshots validate a healthy portfolio context; they do not
select the consolidation or establish release causality.

## Query Universe

The exact reusable register is
`data/indoor-rainy-consolidation-keywords-2026-08-04.csv`. It freezes 36 US
desktop queries. Twenty-seven rows have a positive numeric volume, one has an
explicit zero estimate, and eight have unavailable volume. Close variants,
ages, moments, and singular subjobs overlap and are not summed.

| Cluster | Rows | Positive | Zero | Unavailable | Largest estimate | Median positive volume | Median available KD |
|---|---:|---:|---:|---:|---:|---:|---:|
| Broad boundaries | 2 | 2 | 0 | 0 | 60,500 | 33,550 | 23.5 |
| Indoor owner | 15 | 7 | 1 | 7 | 390 | 170 | 15 |
| Active movement and games | 6 | 5 | 0 | 1 | 390 | 110 | 15.5 |
| Rainy context | 9 | 9 | 0 | 0 | 720 | 50 | 17 |
| Rain-themed craft | 1 | 1 | 0 | 0 | 70 | 70 | 18 |
| At-home learning boundary | 3 | 3 | 0 | 0 | 480 | 20 | 21 |

These are frozen-set descriptions, not market-size totals.

### Selection-Driving Rows

| Query | Observed likely job | US volume | KD | CPC | Architecture use |
|---|---|---:|---:|---:|---|
| `rainy day activities for kids` | Broad all-age weather ideas | 60,500 | 25 | $0.00 | Boundary; do not broaden a preschool page to chase it |
| `indoor activities for kids` | All-age indoor ideas plus local/venue intent | 6,600 | 22 | $0.78 | Boundary; preserve preschool specificity |
| `preschool activities at home` | At-home learning, curriculum, literacy, and math | 480 | 21 | $0.87 | Separate job; exclude from indoor primary ownership |
| `indoor activities for preschoolers` | Choose an activity for a preschooler inside | 390 | 25 | $0.23 | Primary owner query |
| `indoor games for preschoolers` | Active/group/classroom games inside | 390 | 17 | $0.18 | Distinct module, not a separate KAL page now |
| `indoor activities for 3 year olds` | Age-three indoor route | 260 | 6 | $0.20 | Route within the preschool owner |
| `indoor gross motor activities for preschoolers` | Use larger movement in a bounded indoor space | 260 | 12 | $0.26 | Movement module with stronger readiness and space checks |
| `indoor activities for 4 year olds` | Age-four indoor route | 170 | 15 | $0.21 | Route within the preschool owner |
| `rainy day activities for preschoolers` | Fill a weather-bound preschool period | 170 | 31 | $0.16 | Context inside indoor owner; current page is duplicative |
| `rainy day activities at home` | Broad-age rainy at-home ideas | 140 | 15 | $0.09 | Context/boundary |
| `active indoor games for preschoolers` | Active games in limited space | 110 | 14 | $0.30 | Movement/game module |
| `rainy day crafts for preschoolers` | Make rain, cloud, puddle, or umbrella art | 70 | 18 | $0.00 | Distinct future research candidate; current rainy page misses it |
| `quiet indoor activities for kids` | Quiet indoor reset | 0 | 0 | $0.00 | Explicit tool zero; still a useful parent filter, not a demand claim |
| `low prep indoor activities for preschoolers` | Start with minimal preparation | `n/a` | 19 | `n/a` | Volume unavailable; useful chooser constraint |
| `screen free indoor activities for preschoolers` | Avoid screens while inside | `n/a` | 34 | `n/a` | Volume unavailable; constraint, not mission |

## SERP Samples And Boundaries

All six samples came from Semrush cached Google results in the user's logged-in
US desktop session on 2026-08-04. Semrush exposed an August 2026 database,
United States market, and desktop device. Locale was not exposed; the result
and interface language was English. Exact collection time and requested
organic depth are `UNKNOWN`.

The accessible snapshots interleaved AI Overview citations, conventional web
results, images, videos, short videos, community modules, and PAA. The rows
below preserve accessible links in snapshot-exposure order with their modules;
they are not asserted conventional organic ranks. Omitted or unexposed rows
remain `UNKNOWN`, no sample is complete at a fixed depth, and all numeric URL
and domain intersection, union, and Jaccard fields are `UNKNOWN`.

| Exact query | Semrush snapshot | Accessible retained links | Complete fixed-depth organic set? | Dominant reading |
|---|---|---:|---|---|
| `indoor activities for preschoolers` | `s-h-99-0804-7354670731870865516` | 14 | No | Broad indoor blend: low-prep ideas, active play, crafts, social/video, and rainy context |
| `rainy day activities for preschoolers` | `s-i-05-0804-1665023277063827057` | 13 | No | Mostly the same indoor job plus weather-themed crafts and publishers |
| `indoor games for preschoolers` | `s-h-05-0804-13111354731705555320` | 13 | No | Group/classroom/recess and active games |
| `indoor gross motor activities for preschoolers` | `s-h-99-0804-7067155420992739528` | 11 | No | Movement, classroom/therapy-adjacent, product, visual, and video results |
| `rainy day crafts for preschoolers` | `s-h-99-0804-8680715530274140684` | 19 | No | Image-heavy rain/cloud/umbrella craft job |
| `preschool activities at home` | `s-f-99-0804-879955045285768427` | 12 | No | Learning, curriculum, literacy/math, community, and videos |

Exact Semrush cache URLs:

- `indoor activities for preschoolers`:
  `https://www.semrush.com/analytics/serp/?phrase=indoor%20activities%20for%20preschoolers&db=us&serpId=s-h-99-0804-7354670731870865516`
- `rainy day activities for preschoolers`:
  `https://www.semrush.com/analytics/serp/?phrase=rainy%20day%20activities%20for%20preschoolers&db=us&serpId=s-i-05-0804-1665023277063827057`
- `indoor games for preschoolers`:
  `https://www.semrush.com/analytics/serp/?phrase=indoor%20games%20for%20preschoolers&db=us&serpId=s-h-05-0804-13111354731705555320`
- `indoor gross motor activities for preschoolers`:
  `https://www.semrush.com/analytics/serp/?phrase=indoor%20gross%20motor%20activities%20for%20preschoolers&db=us&serpId=s-h-99-0804-7067155420992739528`
- `rainy day crafts for preschoolers`:
  `https://www.semrush.com/analytics/serp/?phrase=rainy%20day%20crafts%20for%20preschoolers&db=us&serpId=s-h-99-0804-8680715530274140684`
- `preschool activities at home`:
  `https://www.semrush.com/analytics/serp/?phrase=preschool%20activities%20at%20home&db=us&serpId=s-f-99-0804-879955045285768427`

### Exact Accessible Result Register

`Order` means snapshot-exposure order among retained accessible links, not an
organic rank. Domains preserve meaningful subdomains. Tracking parameters are
retained in exact URLs when Semrush exposed them.

#### `indoor activities for preschoolers`

| Order | Module | Exact URL | Normalized domain | Result type |
|---:|---|---|---|---|
| 1 | AI Overview | `https://www.parentmap.com/things-to-do/indoor-play-activities-preschool-teacher/` | `parentmap.com` | publisher roundup |
| 2 | AI Overview | `https://mybrightwheel.com/blog/indoor-recess` | `mybrightwheel.com` | commercial education article |
| 3 | AI Overview | `https://www.youtube.com/watch?v=4AW9Z0ys9ag&t=410` | `youtube.com` | video |
| 4 | AI Overview | `https://www.reddit.com/r/Preschoolers/comments/10bbipe/easylow_prep_indoor_activities_for_preschoolers/` | `reddit.com` | community thread |
| 5 | Web results | `https://brightpathkids.com/family-blog/50-rainy-day-activities-to-keep-kids-busy` | `brightpathkids.com` | child-care provider roundup |
| 6 | Web results | `https://www.reddit.com/r/Preschoolers/comments/10bbipe/easylow_prep_indoor_activities_for_preschoolers/j49dv3f/` | `reddit.com` | community answer |
| 7 | Web results | `https://ca.pinterest.com/preschoolkit/indoor-preschool-play/` | `ca.pinterest.com` | visual board |
| 8 | Images | `https://toddlerapproved.com/indoor-activities-for-toddlers-and-preschoolers/` | `toddlerapproved.com` | activity roundup |
| 9 | Images | `https://busytoddler.com/indoor-activities/` | `busytoddler.com` | activity library |
| 10 | Web results | `https://www.oregonchildcarealliance.org/5-fun-indoor-activities-for-preschoolers-this-january/` | `oregonchildcarealliance.org` | child-care organization article |
| 11 | Web results | `https://extension.psu.edu/programs/betterkidcare/content-areas/environment-curriculum/activities/all-activities/active-play-for-rainy-days` | `extension.psu.edu` | university extension activity page |
| 12 | Web results | `https://www.facebook.com/groups/sunshineandsabrina/posts/319782780806661/` | `facebook.com` | community post |
| 13 | Videos | `https://www.youtube.com/watch?v=eRhLIyfU9Nk` | `youtube.com` | video |
| 14 | Videos | `https://www.instagram.com/reel/DQ2R7vJkuhK/?hl=en` | `instagram.com` | social video |

#### `rainy day activities for preschoolers`

| Order | Module | Exact URL | Normalized domain | Result type |
|---:|---|---|---|---|
| 1 | AI Overview | `https://www.parentmap.com/things-to-do/indoor-play-activities-preschool-teacher/` | `parentmap.com` | publisher roundup |
| 2 | AI Overview | `https://www.reddit.com/r/Preschoolers/comments/10bbipe/easylow_prep_indoor_activities_for_preschoolers/` | `reddit.com` | community thread |
| 3 | AI Overview | `https://brightpathkids.com/family-blog/50-rainy-day-activities-to-keep-kids-busy` | `brightpathkids.com` | child-care provider roundup |
| 4 | Web results | `https://www.reddit.com/r/Preschoolers/comments/10bbipe/easylow_prep_indoor_activities_for_preschoolers/j49dv3f/` | `reddit.com` | community answer |
| 5 | Web results | `https://ca.pinterest.com/preschoolkit/indoor-preschool-play/` | `ca.pinterest.com` | visual board |
| 6 | Short videos | `https://www.instagram.com/reel/DQ2R7vJkuhK/?hl=en` | `instagram.com` | social video |
| 7 | Short videos | `https://www.facebook.com/happytoddlerplaytime/videos/rainy-days-call-for-simple-crafts-these-rain-themed-activities-are-perfect-for-l/961783116373515/` | `facebook.com` | social video |
| 8 | Short videos | `https://www.facebook.com/happytoddlerplaytime/videos/rainy-day-weve-got-you-httpshappytoddlerplaytimecomfun-easy-rain-crafts-for-todd/902673989021261/` | `facebook.com` | social video |
| 9 | Short videos | `https://www.instagram.com/reel/DYiTCpORp2L/?hl=en` | `instagram.com` | social video |
| 10 | Web results | `https://playteachrepeat.com/rainy-day-preschool-activities/` | `playteachrepeat.com` | themed activity roundup |
| 11 | Videos | `https://www.youtube.com/watch?v=eRhLIyfU9Nk` | `youtube.com` | video |
| 12 | Web results | `https://extension.psu.edu/programs/betterkidcare/content-areas/environment-curriculum/activities/all-activities/active-play-for-rainy-days` | `extension.psu.edu` | university extension activity page |
| 13 | Web results | `https://www.pbs.org/parents/rainy-day-activities` | `pbs.org` | publisher activity hub |

#### `indoor games for preschoolers`

| Order | Module | Exact URL | Normalized domain | Result type |
|---:|---|---|---|---|
| 1 | AI Overview | `https://www.pre-kpages.com/indoor-recess-games-and-activities-for-preschoolers/` | `pre-kpages.com` | teacher activity roundup |
| 2 | AI Overview | `https://www.reddit.com/r/ECEProfessionals/comments/1963aeb/fun_games_to_play_with_my_class_of_3_year_olds/` | `reddit.com` | educator community thread |
| 3 | AI Overview | `https://pencilstopigtails.com/circle-time-games-for-preschoolers-and-kindergarten/` | `pencilstopigtails.com` | teacher game roundup |
| 4 | Web results | `https://www.reddit.com/r/Preschoolers/comments/10bbipe/easylow_prep_indoor_activities_for_preschoolers/` | `reddit.com` | parent community thread |
| 5 | Web results | `https://www.reddit.com/r/ECEProfessionals/comments/1le4ijc/recommendations_for_prek_classroom/` | `reddit.com` | educator community thread |
| 6 | Videos | `https://www.youtube.com/watch?v=1ikl8lTp6_c&vl=en` | `youtube.com` | video |
| 7 | Videos | `https://www.youtube.com/watch?v=9UZpvB-NLb4` | `youtube.com` | video |
| 8 | Videos | `https://www.youtube.com/watch?v=skhIo_fB1mg` | `youtube.com` | video |
| 9 | Web results | `https://mybrightwheel.com/blog/indoor-recess` | `mybrightwheel.com` | commercial education article |
| 10 | Web results | `https://www.abcjesuslovesme.com/ideas/active-games` | `abcjesuslovesme.com` | curriculum publisher activity list |
| 11 | Web results | `https://mx.pinterest.com/pin/425590233541400863/` | `mx.pinterest.com` | visual pin |
| 12 | Web results | `https://earlyimpactlearning.com/21-circle-time-games-for-preschool-that-actually-work/` | `earlyimpactlearning.com` | teacher game roundup |
| 13 | Web results | `https://ffpeds.com/active-indoor-games-for-kids/` | `ffpeds.com` | pediatric practice article |

#### `indoor gross motor activities for preschoolers`

| Order | Module | Exact URL | Normalized domain | Result type |
|---:|---|---|---|---|
| 1 | AI Overview | `https://reachallreaders.com/indoor-gross-motor-activities/` | `reachallreaders.com` | education activity roundup |
| 2 | AI Overview | `https://www.youtube.com/watch?v=sWITxpL5ZdQ` | `youtube.com` | video |
| 3 | AI Overview | `https://www.reddit.com/r/ECEProfessionals/comments/sgipdi/indoor_gross_motor_activities/` | `reddit.com` | educator community thread |
| 4 | Web results | `https://www.pinterest.com/siseec/indoors-gross-motor-fun/` | `pinterest.com` | visual board |
| 5 | Web results | `https://ducklingselc.com/blog/2024/12/gross-motor-games-preschoolers/#:~:text=10%20Indoor%20Gross%20Motor%20Games,for%20Preschoolers&text=1.%20Animal%20Parade&text=2.%20Indoor%20Obstacle%20Course&text=3.%20Balloon%20Volleyball&text=4.%20Simon%20Says%20with%20a,Twist&text=5.%20Dance%20Party%20Freeze` | `ducklingselc.com` | child-care provider article |
| 6 | Videos | `https://www.youtube.com/watch?v=bLiEaJC-B3Y` | `youtube.com` | video |
| 7 | Videos | `https://www.pinterest.com/pin/easy-fun-gross-motor-games-with-masking-tape-kids-love-video--2744449768478666/` | `pinterest.com` | visual video pin |
| 8 | Web results | `https://funandfunction.com/blogs/blog/5-indoor-gross-motor-activities?srsltid=AfmBOorKaiycCPu1QVqsrGecTRrcn1nkJOQdv-6y_ZM_HQ0c3eWabL77` | `funandfunction.com` | product-publisher article |
| 9 | Short videos | `https://www.facebook.com/Weewatchchildcare/videos/this-january-were-focusing-on-indoor-gross-motor-activities-%EF%B8%8F-since-winter-weath/1804166900385304/` | `facebook.com` | child-care social video |
| 10 | Web results | `https://junglejumparoo.com/blogs/ultimate-kids-trampoline/5-activities-to-help-toddlers-develop-gross-motor-skills?srsltid=AfmBOopxOVm7SaDHo_yibRxqaU7qjcKrsmvJ1NWeq5Ug3PUHfbuApWmF` | `junglejumparoo.com` | product-publisher article |
| 11 | Web results | `https://developlearngrow.com/gross-motor-activities-for-indoor-recess/` | `developlearngrow.com` | education/therapy-adjacent roundup |

#### `rainy day crafts for preschoolers`

| Order | Module | Exact URL | Normalized domain | Result type |
|---:|---|---|---|---|
| 1 | Images | `https://www.youtube.com/watch?v=g33ZpwMnprE` | `youtube.com` | video |
| 2 | Images | `https://www.instagram.com/reel/C53gvisxNZn/` | `instagram.com` | social video |
| 3 | Images | `https://happytoddlerplaytime.com/fun-easy-rain-crafts-for-toddlers-and-preschoolers/` | `happytoddlerplaytime.com` | craft roundup |
| 4 | Images | `https://www.instagram.com/reel/C6EgsxXOPhP/` | `instagram.com` | social video |
| 5 | Images | `https://artsycraftsymom.com/rain-day-crafts/` | `artsycraftsymom.com` | craft roundup |
| 6 | Images | `https://www.craftsonsea.co.uk/rain-crafts-for-kids/` | `craftsonsea.co.uk` | craft roundup |
| 7 | Images | `https://www.today.com/parents/7-rainy-day-crafts-do-your-kids-t18206` | `today.com` | publisher craft roundup |
| 8 | Images | `https://www.farmwifecrafts.com/rain-cloud-craft/` | `farmwifecrafts.com` | individual craft article |
| 9 | Web results | `https://playteachrepeat.com/rainy-day-preschool-activities/` | `playteachrepeat.com` | themed activity roundup |
| 10 | Web results | `https://www.pinterest.com/jmm11683/rainy-day-ideas-kids-crafts/` | `pinterest.com` | visual board |
| 11 | Web results | `https://www.crayola.com/crafts/rainy-day-crafts` | `crayola.com` | product-publisher craft hub |
| 12 | Web results | `https://www.thesprucecrafts.com/simple-crafts-for-a-rainy-day-4035253` | `thesprucecrafts.com` | craft roundup |
| 13 | Web results | `https://countryhomelearningcenter.com/rainy-day-crafts-for-toddlers/` | `countryhomelearningcenter.com` | child-care provider craft article |
| 14 | Short videos | `https://www.facebook.com/happytoddlerplaytime/videos/rainy-days-call-for-simple-crafts-these-rain-themed-activities-are-perfect-for-l/961783116373515/` | `facebook.com` | social video |
| 15 | Short videos | `https://www.instagram.com/reel/DbYOhm7vVr4/` | `instagram.com` | social video |
| 16 | Short videos | `https://www.pinterest.com/pin/rainy-day-crafts--138133913565584408/` | `pinterest.com` | visual video pin |
| 17 | Short videos | `https://www.facebook.com/happytoddlerplaytime/videos/rainy-day-weve-got-you-httpshappytoddlerplaytimecomfun-easy-rain-crafts-for-todd/902673989021261/` | `facebook.com` | social video |
| 18 | Videos | `https://www.pinterest.com/ideas/rainy-day-crafts-for-preschoolers/907662472632/` | `pinterest.com` | visual ideas page |
| 19 | Web results | `http://ppppizzazz.blogspot.com/2013/04/rainy-day-crafts-for-toddlers.html` | `ppppizzazz.blogspot.com` | old craft article |

#### `preschool activities at home`

| Order | Module | Exact URL | Normalized domain | Result type |
|---:|---|---|---|---|
| 1 | AI Overview | `https://www.reddit.com/r/preschool/comments/1rjitle/what_learning_activities_actually_work_for_your/` | `reddit.com` | parent community thread |
| 2 | AI Overview | `https://www.learning-grove.org/preschool-activities-and-ideas-for-learning-at-home/` | `learning-grove.org` | early-learning provider article |
| 3 | Web results | `https://readingeggs.com/articles/preschool-learning-activities-home/` | `readingeggs.com` | commercial learning article |
| 4 | Web results | `https://www.reddit.com/r/preschool/comments/1rjitle/what_learning_activities_actually_work_for_your/o8divmd/` | `reddit.com` | community answer |
| 5 | Web results | `https://www.pinterest.com/dayswithgrey/preschool-activities/` | `pinterest.com` | visual board |
| 6 | Videos | `https://www.youtube.com/watch?v=EtZMreXxApE` | `youtube.com` | learning-activity video |
| 7 | Videos | `https://www.youtube.com/watch?v=4KJqpjKHVsM` | `youtube.com` | learning-activity video |
| 8 | Videos | `https://www.youtube.com/watch?v=5-flsloEj_4` | `youtube.com` | age-four at-home video |
| 9 | What people are saying | `https://www.facebook.com/groups/thehomeschoolmeltinghub/posts/1113233004460288/` | `facebook.com` | community post |
| 10 | What people are saying | `https://www.facebook.com/groups/541425542723577/posts/3210869922445779/` | `facebook.com` | community post |
| 11 | Web results | `https://www.gardenmontessorischools.com/blog/preschool-learning-activities-at-home` | `gardenmontessorischools.com` | preschool-provider learning article |
| 12 | Web results | `https://thestay-at-home-momsurvivalguide.com/preschool-at-home-curriculum/?srsltid=AfmBOopK3Hg_1LvZodxO6uqdvXtt1cpWmN5l61CMjcgtq1532TpSyLI-` | `thestay-at-home-momsurvivalguide.com` | curriculum article |

### Retained Recurrence And Boundary Map

| Query comparison | Numeric comparison valid? | Named retained recurrence | Result-type reading | Decision |
|---|---|---|---|---|
| Preschool indoor vs preschool rainy | No; all URL/domain counts and Jaccard values `UNKNOWN` | ParentMap, BrightPath, same Reddit thread and answer, same Pinterest board, Penn State, same Instagram reel, and same YouTube video | Rainy is mostly the indoor job with a weather frame; craft/social rows add a smaller theme branch | One indexable indoor owner; rainy becomes context and legacy redirect |
| Indoor activities vs indoor games | No; all numeric fields `UNKNOWN` | Same low-prep Reddit thread and Brightwheel recur | Games leans group/classroom/recess, circles, active play, and video | Indoor games is a module or route, not a new KAL page now |
| Indoor activities vs gross motor | No; all numeric fields `UNKNOWN` | General movement concepts recur, but retained exact URLs are mostly different | Gross motor has more educator, therapy-adjacent, product, visual, and safety/space burden | Bounded movement module; no broad motor-development claim |
| Preschool rainy vs rainy crafts | No; all numeric fields `UNKNOWN` | Play Teach Repeat and Happy Toddler social material recur | Craft SERP is distinctly image-heavy and weather-themed | Defer a separate rain-craft research candidate; do not preserve current duplicate for it |
| Indoor activities vs preschool at home | No; all numeric fields `UNKNOWN` | Community/visual/video result types recur, but the named owners differ | At-home results emphasize learning, literacy, math, and curriculum | Keep learning-at-home outside the indoor moment owner |

## Representative Ranking-Page Analysis

All rows were retrieved or visibly inspected on 2026-08-04. Retrieval date is
not publication date. A page's claims, author experience, photographs, or
commercial relationships are not evidence that KAL ran an activity.

| Page | What it answers well | Friction or boundary | Advantage KAL cannot claim | Honest KAL response |
|---|---|---|---|---|
| [ParentMap indoor preschool roundup](https://www.parentmap.com/things-to-do/indoor-play-activities-preschool-teacher/) | Updated 2026-06-26; frames low-stress, no-store indoor days and offers broad imagination, craft, and play ideas | Fourteen-minute grab bag with broad ages rather than a compact moment chooser | Preschool-teacher framing, publisher audience, and content history | Compete on a fast parent decision, not count; do not claim teacher or family use |
| [Brightwheel indoor recess](https://mybrightwheel.com/blog/indoor-recess) | Updated 2025-11-17; clearly separates active games, quieter activities, and short brain breaks | Classroom/recess orientation and commercial childcare-product context | Childcare-program reach, curriculum/business expertise, and development claims | Use active/quiet structure as result-shape evidence; avoid inherited outcomes and commercial framing |
| [Pre-K Pages indoor games](https://www.pre-kpages.com/indoor-recess-games-and-activities-for-preschoolers/) | Updated 2026-02-18; provides group games, movement, listening/cooperation, songs, dance, and classic rule routes | Most ideas assume a classroom group, open floor, music, or teacher-led play; product and membership modules are prominent | Teacher's classroom practice, photos, and commercial resource library | Keep the KAL games module home-facing, space-aware, and explicit about player/adult needs |
| [Penn State active play for rainy days](https://extension.psu.edu/programs/betterkidcare/content-areas/environment-curriculum/activities/all-activities/active-play-for-rainy-days) | Gives concrete indoor movement setups: paper puddles, box crawling, music, action stories, and an obstacle course | Several ideas require floor clearance, materials, group management, and local adult checks | University-extension authority | Support a bounded movement module and conservative setup/stop checks; do not imply safety in practice |
| [Reach All Readers indoor gross motor](https://reachallreaders.com/indoor-gross-motor-activities/) | Large list across home and classroom: beanbag targets, tape paths, animal movement, balloons, dance, and scavenger hunts | Old page, affiliate disclosure, high scan cost, and several space/material risks | Author's education practice and historical topical coverage | Use only for subjob shape and candidate-source discovery; keep movement choices few and locally checked |
| [Happy Toddler Playtime rain crafts](https://happytoddlerplaytime.com/fun-easy-rain-crafts-for-toddlers-and-preschoolers/) | Published 2025-03-10; provides 18 rain/cloud/umbrella craft routes with materials and setup | Craft-heavy preparation, cutting, paint, glue, small pieces, and a creator's firsthand family narrative | Original family narrative, photos, television/author credentials, and activity history | Treat rain craft as a distinct future lane; never reuse the narrative as KAL evidence |
| [Crayola rainy-day craft hub](https://www.crayola.com/crafts/rainy-day-crafts) | Current visual craft catalogue and recognizable rain/art category | Commercial product ecosystem, broad ages, and category-level scan burden | Brand authority, product access, photography, and craft catalogue depth | Do not create a generic craft catalogue or product recommendation; require a distinct KAL chooser before entering this lane |
| [Reading Eggs preschool activities at home](https://readingeggs.com/articles/preschool-learning-activities-home/) | Clear literacy, phonics, math, and school-readiness framing with concrete at-home exercises | Commercial trial funnel and a learning/curriculum job rather than a weather or indoor-moment job | Product curriculum, proprietary games, and learning claims | Route learning-at-home elsewhere; do not stretch the indoor page to own curriculum intent |
| [PBS Kids rainy-day hub](https://www.pbs.org/parents/rainy-day-activities) | Broad, trusted organization across movement, science experiments, printables, games, and media-linked activities | Very broad audience, deep media ecosystem, printables, and branded routes | PBS authority, characters, video, printable library, and content breadth | Do not chase breadth; use rainy day only as an indoor context unless KAL later builds a distinct weather product |

Google's current [redirect documentation](https://developers.google.com/search/docs/crawling-indexing/301-redirects)
recommends a server-side permanent redirect when possible and states that an
instant `meta refresh` is interpreted as a permanent redirect. The future
candidate uses that fallback only because GitHub Pages cannot provide a
repository-defined server redirect. This is implementation guidance, not a
claim that Google has already consolidated the URLs.

## Persona Hypotheses

These are source-traced parent-job review lenses, not demographics,
testimonials, or family-test evidence.

| ID | Job to be done | Context and constraints | Anxiety / decision criteria | Failure mode | Evidence trail | Required owner response |
|---|---|---|---|---|---|---|
| P1 Start-now parent | Pick one indoor activity from materials already available | Preschooler at home; available attention, room, and readiness vary | Wants a visible default, material list, adult role, and cleanup/stop boundary before scrolling | Leaves a long roundup or discovers hidden setup | Low/no-prep variants; ParentMap; recurring Reddit question; current KAL tables | First-screen default and chooser by setup/material, not exact measured time |
| P2 Energy-in-a-small-space parent | Let a child move without creating an unsafe running route or turning the room over | Furniture, neighbors, siblings, and floor space differ | Needs footprint, soft-material options, adult positioning, and an observable stop | Chooses a classroom-scale game or reads gross-motor wording as a safety guarantee | Indoor games/gross-motor queries; Penn State; Brightwheel; Pre-K Pages; Reach All Readers | Small-space movement module with local clearance/readiness checks and no outcome claim |
| P3 Quiet-reset parent | Choose something calmer or more independent-looking without assuming independence | Mixed-age home, younger sibling, mouthing, fatigue, or adult workload may matter | Wants piece-size, supervision, adult-help, and rescue information | Quiet gets treated as unsupervised or safe for every child | Quiet/no-prep variants; current KAL magnetic/pom-pom/card materials; Reddit concerns from prior pack | Quiet/build/pretend routes with material checks; never promise independent play |
| P4 Rain-context parent | Fill a rainy stretch without reading a second copy of the indoor page | Weather is why the family is inside, but desired activity may be movement, building, games, or quiet play | Wants one plan that can rotate jobs and end cleanly | Finds the same eight cards on two URLs with no weather-specific value | Preschool indoor/rainy recurrence; PBS; Penn State; KAL eight-of-nine overlap | Rainy context inside the indoor owner; old URL redirects rather than competing |
| P5 Rain-theme maker | Make something specifically about rain, clouds, puddles, umbrellas, or weather | Paint, glue, cutting, drying, and small-piece readiness vary | Wants a coherent weather craft, material substitutions, adult-only steps, and drying/stop guidance | Lands on a generic indoor activity list that contains no rain craft | Rain-craft query and image-heavy SERP; Happy Toddler Playtime; Crayola; PBS weather routes | Defer until a separate craft research pack can meet the evidence and utility bar |
| P6 Game-or-learning seeker | Find either a rule-governed game or an at-home learning activity | May involve multiple players, classroom/group assumptions, literacy/math goals, or commercial curriculum | Needs the site to say which job it is serving | Indoor page becomes an unfocused curriculum/game portal | Indoor-games and preschool-at-home SERPs; Pre-K Pages; Brightwheel; Reading Eggs | Include a bounded games route; keep curriculum/learning intent outside primary ownership |

## Current Page Inventory

| URL/path | Current primary job | Search/index evidence | Strengths | Material gaps | Verdict |
|---|---|---|---|---|---|
| `/collections/indoor-activities-for-preschoolers.html` | Small-room indoor preschool ideas | Page metrics, complete queries, and priority inspection `UNKNOWN` | Correct durable topic and URL; nine linked activities; visible home constraints | Generic table; exact time/mess/help labels look measured; no disclosure, source trail, moment chooser, rescue routes, or per-activity stop guidance | Keep as the single future owner and materially improve it |
| `/collections/rainy-day-activities-for-preschoolers.html` | Rainy-day energy/building/quiet rotation | Page metrics, complete queries, and priority inspection `UNKNOWN` | Clear weather context and nine linked activities | Eight cards duplicate indoor; one-card difference does not create a distinct product; no rain-themed craft or weather utility; same evidence/trust gaps | Retire as a competing indexable page; preserve old URL as a tested permanent-redirect fallback |
| `/collections/card-games-for-kids.html` | Choose among five standard-deck games | Released and under observation; complete queries remain unavailable | Distinct rule/player job with research-backed chooser | Not a substitute for one-child or movement activity | Link only as an optional game route; do not merge ownership |
| `/collections/building-activities-for-4-year-olds.html` | Preschool building chooser with age four visible | Released and under observation; complete queries remain unavailable | Strong adjacent make/build route | Does not own all indoor intent | Link as a deeper make/build route without duplicating its nine builds |
| `/ages/activities-for-4-year-olds-at-home.html` | Age-four at-home route | Existing age route; complete queries remain unavailable | Useful age-specific path | At-home is broader than indoor and may include learning intent | Keep distinct; use age routes sparingly and never create new age pages from this pack |

## Every-Section Audit

### Indoor Activities For Preschoolers

| Visible section | Primary persona/job | Evidence used | Current value | Risk or repetition | Verdict / future response |
|---|---|---|---|---|---|
| Header and navigation | All | Repository inspection | Stable route | None material | Keep |
| Hero kicker, H1, and intro | P1-P4 | Indoor query and SERP | Clearly names indoor preschool and real-room constraints | No evidence disclosure; does not distinguish moment choices | Keep URL/H1 job; rewrite around immediate parent decision and honest evidence |
| Quick pick | P1 | Low-prep variants and current page | Gives a direction | Bundles roads, blocks, and ramps without telling which moment it fits | Replace with one useful default and exact chooser destination |
| Activity chooser table | P1-P3 | Repository inspection | Materials are scannable | Exact 1-5 minute and all-low-mess values look measured; no adult role, footprint, rescue, or stop | Replace with moment/setup/adult-role chooser; remove measured-looking fields |
| Tape Road | P1/P3 | Current card and page | Low-floor pretend route | Tape/floor test is local, but no rescue or stop | Retain only if it serves a distinct moment; add adult setup/rescue/stop |
| Tape Train Tracks | P1/P3 | Current card and page | Familiar pretend route | Strongly overlaps Tape Road | Merge or differentiate by available toy/material; no repeated card prose |
| Sock Ball Roll | P2 | Gross-motor and current page | Soft-material movement candidate | Books/floor/throwing boundary underdeveloped | Use as bounded small-space movement with local clearance and stop |
| Blanket River | P2/P4 | Current page | Pretend and movement bridge | Blanket slip/running risk; overlaps building route | Keep only with floor-clearance, no-running/climbing, and explicit stop |
| Cardboard Car Ramp | P1/P3 | Current article/card/page | Start-now cause-and-effect route | Current short block under-serves deeper existing article and building page | Use a concise chooser route to the stronger owner; avoid duplicate instructions |
| Cup Tower | P1/P3 | Current card/page | Light household-material build | Generic height/knock-down framing and no graceful rescue | Route to building owner or provide low-wide local check; no outcome claim |
| Magnetic Tile House | P3 | Current card/page | Quieter building/pretend route | Magnet integrity and piece/readiness need prominent handling | Route to building owner with damaged-piece removal; never call it independent |
| Block Tower | P1/P3 | Current card/page | Familiar build route | Duplicates the building chooser and Cup Tower | Route to building owner instead of repeating a shallow block |
| Tape City | P1/P3 | Current card/page | Extended pretend/map route | Setup and footprint are hidden; overlaps Tape Road | Keep only if chooser surfaces footprint and adult setup; otherwise route deeper |
| Searches this page is built for | Search only | Repository inspection | Exposes intended variants | Visible SEO narration gives the parent no running utility | Remove; express routes naturally in copy and links |
| Generic safety block | P2/P3 | Repository inspection | Conservative readiness reminder | Detached from each activity and may read as blanket coverage | Replace with one global readiness note plus local checks/stops |
| Footer | All | Repository inspection | Stable card-library route | None material | Keep |

### Rainy-Day Activities For Preschoolers

| Visible section | Primary persona/job | Evidence used | Current value | Risk or repetition | Verdict / future response |
|---|---|---|---|---|---|
| Header and navigation | P4/P5 | Repository inspection | Stable old route | Becomes misleading if page is silently removed | Preserve as accessible redirect fallback with a direct link |
| Hero kicker, H1, and intro | P4 | Rainy query/SERP | Names weather-bound energy | Promise is mostly the indoor page with different framing | Replace entire document with instant redirect and indoor canonical in future action |
| Quick pick | P4 | Current page | Suggests movement/building/quiet rotation | No exact destinations; current cards do not form distinct weather product | Move the useful rotation concept into indoor owner |
| Activity chooser table | P1-P4 | Repository inspection | Materials are scannable | Eight of nine rows duplicate indoor and exact fields look measured | Do not preserve as a second chooser |
| Tape Road | P1/P3/P4 | Current page | Same as indoor | Duplicate | Consolidate into indoor owner |
| Tape Train Tracks | P1/P3/P4 | Current page | Same as indoor | Duplicate | Consolidate into indoor owner |
| Cardboard Car Ramp | P1/P3/P4 | Current page | Same as indoor | Duplicate | Route to stronger article/build owners from indoor |
| Sock Ball Roll | P2/P4 | Current page | Same as indoor | Duplicate | Consolidate into indoor movement module |
| Blanket River | P2/P4 | Current page | Same as indoor | Duplicate | Consolidate with stronger local checks |
| Magnetic Tile House | P3/P4 | Current page | Same as indoor | Duplicate | Route to building owner from indoor |
| Paper Roll Drop | P3/P4 | Current page | Only unique card | One shallow small-piece activity cannot support separate indexable ownership | Retain card elsewhere if useful; do not preserve rainy page for it |
| Cup Tower | P1/P3/P4 | Current page | Same as indoor | Duplicate | Route to building owner from indoor |
| Tape City | P1/P3/P4 | Current page | Same as indoor | Duplicate | Consolidate into indoor owner if it survives chooser review |
| Searches this page is built for | Search only | Repository inspection | States overlap directly | Visible SEO narration and `indoor activities for preschoolers` confirm ownership collision | Remove with retired document |
| Generic safety block | P2/P3 | Repository inspection | Same conservative reminder | Exact duplicate and detached from routes | Do not preserve as a second block |
| Footer | All | Repository inspection | Stable card-library route | Redirected page should still provide a crawlable/manual link fallback | Redirect document should include one plain link to indoor owner |

## Page Architecture

| Query/job | Treatment | Owner | Rationale | Remaining gap |
|---|---|---|---|---|
| Preschool indoor activities | Existing-page improvement | `/collections/indoor-activities-for-preschoolers.html` | Best durable topic/URL and current inventory; parent moment can unify modules | Candidate GSC rows and family outcomes `UNKNOWN` |
| Rainy-day activities for preschoolers | Context plus legacy redirect | Indoor owner | Strong named SERP recurrence and eight-of-nine KAL overlap | Exact numeric overlap and current index state `UNKNOWN` |
| Active indoor games | Section/module and route | Indoor owner, with optional link to card-game chooser | Meaningful demand and distinct player/group needs, but blended with indoor job | KAL has not family-tested any setup |
| Indoor gross-motor/movement | Section/module | Indoor owner | Meaningful subjob; higher space/readiness/safety burden does not justify a shallow new page | Safe-in-practice and developmental outcomes `UNKNOWN` |
| Quiet, low-prep, no-prep, screen-free | Chooser filters | Indoor owner | Parent constraints, not separate durable products in current evidence | Several tool volumes unavailable |
| Rain-themed crafts and weather exploration | Defer to a new research action | No KAL owner proposed | Distinct result types and job, but only one selection-driving exact query and no current KAL product | Source reconciliation, activity model, demand breadth, and family outcomes unavailable |
| Preschool learning at home | Exclude from primary owner | Existing age/learning routes only | Current SERP expects learning, literacy, math, and curriculum | No distinct KAL curriculum product |
| Broad indoor activities for kids | Do not target | No new owner | All-age and local/venue ambiguity | Clean at-home ownership not established |
| Broad rainy-day activities for kids | Do not target | No new owner | All-age weather breadth and strong publishers | KAL lacks the breadth/product to deserve this query |

## Claim And Human Gates

- Family-tested status, parent/child use, quotes, photos, activity duration,
  comprehension, engagement, enjoyment, learning, repeatability, frustration,
  observed mess, and safety outcomes remain `UNKNOWN`.
- Conservative material, supervision, floor-clearance, setup, stop, and rescue
  guidance may be source-backed or clearly editorial. It may not say a setup
  was safe in practice.
- Preschool and age routes are editorial guidance, not guarantees of fit.
  Local readiness, material condition and size, available space, siblings, and
  direct-supervision needs remain parent checks.
- Ranking pages support query and product-shape analysis within their limits.
  Their anecdotes, claims, photographs, and expertise do not become KAL
  evidence.
- No product comparison, buying recommendation, affiliate link, indexing
  request, external-account mutation, new URL, or family-evidence request is
  authorized.
- The user has already authorized research-backed non-product work without
  family testing. A separate implementation still requires registration,
  native QA, a different independent read-only reviewer, and exact-SHA release
  verification.

## Promoted Next Action

- Action ID: `KAL-IMP-005`
- Title: Consolidate preschool indoor and rainy-day ownership.
- Primary owner:
  `/collections/indoor-activities-for-preschoolers.html`.
- Legacy route:
  `/collections/rainy-day-activities-for-preschoolers.html`.
- Product promise: help a parent choose one interesting indoor activity by
  immediate moment, materials/space, and adult role, then make it easy to
  start, rescue, and stop.
- Preliminary exact paths for separate registration:
  - `scripts/generate_card_pages.py`
  - `scripts/generate_seo_pages.py`
  - `site/index.html`
  - `site/collections/indoor-activities-for-preschoolers.html`
  - `site/collections/rainy-day-activities-for-preschoolers.html`
  - `site/cards/blanket-river.html`
  - `site/cards/tape-city.html`
  - `site/cards/tape-train-tracks.html`
  - `data/seo_keyword_targets.csv`
  - `site/assets/preschool-indoor/indoor-moment-chooser.webp`
  - `site/styles.css`
  - `site/sitemap.xml`
  - `tools/preschool-indoor-consolidation.test.mjs`
  - `reviews/preschool-indoor-consolidation-implementation-review-2026-08-04.md`
  - `ops/seo-roadmap.json`
  - `ops/seo-roadmap.md`
  - `ops/current-cycle.md`
  - `ops/operator-review.md`
- Indoor acceptance: preserve URL/canonical; keep preschool primary; show a
  first-screen default; add one chooser by setup, movement/quiet/build/game
  moment, space, and adult role; provide bounded start/rescue/stop guidance;
  remove exact measured-looking time/mess/help labels and the visible SEO
  narration; disclose prominently that KAL has not family-tested the setups;
  cite sources within their limits; route deeper building and card-game jobs
  to their existing owners; add no URL.
- Rainy acceptance: replace generated content with a minimal valid HTML
  document containing a zero-second `meta refresh`, canonical to the indoor
  owner, and a visible crawlable manual link; remove the rainy URL from the
  sitemap, homepage, keyword owner register, and all generated card links; do
  not combine `noindex` with the permanent redirect signal.
- Generator acceptance: all three publishing generators are idempotent; only
  declared generated outputs change; every nondeclared card page remains byte-
  stable; current source ownership remains deterministic.
- Visual acceptance: one original WebP may explain the chooser, but it must be
  labeled as an illustration and not a family-test photo. No visual is proof
  of activity use.
- QA: Python compilation; focused and full Node tests; strict HTML and sitemap
  parsing; canonical/redirect and single-owner assertions; every local link
  and fragment; exact-path and generated-output isolation; image format,
  dimensions, alt text, and HTTP path; desktop/mobile layout, keyboard,
  accessibility, overflow, redirect behavior, console, and request checks;
  `git diff --check`.
- Independent review: different read-only reviewer must cover all six
  personas, every changed public section, evidence and human gates, redirect
  semantics, URL ownership, card-byte isolation, exact paths, and native QA.
  Resolve P0-P2 for at most three cycles; only `PASS` or `PASS_WITH_P3` may
  release.
- Release invariant: one focused reviewed commit may push to `main`, followed
  by exact-SHA Pages success, live indoor-page byte match, live legacy redirect
  behavior, sitemap/internal-link ownership, and desktop/mobile production
  checks. Do not request indexing.

The preliminary path list must be revalidated against the frozen base when
`KAL-IMP-005` is registered. It is not permission to edit those paths now.

## Measurement Plan

After a reviewed implementation release, verify local/origin alignment, exact-
SHA Pages success, live byte match for the indoor owner and redirect document,
the absence of the rainy URL from the sitemap and internal links, and clean
desktop/mobile behavior. Then observe finalized public-safe GSC snapshots.

A later crawl, canonical selection, or page row can establish discovery and
consolidation state, not complete query ownership, ranking causality, parent
usefulness, or any family outcome. Do not request indexing. Continue as a no-
op when evidence is healthy and unchanged.

## Unresolved Evidence Gaps

- Complete GSC query rows for both candidate URLs are unavailable.
- Candidate page rows and priority inspections are unavailable.
- Semrush cached samples are incomplete and do not support numeric overlap.
- Exact locale, collection time, requested organic depth, omitted rows, and
  current live Google result order are unavailable.
- Search volume is a tool estimate, not observed KAL demand, and close variants
  cannot be summed.
- Parent comprehension of the proposed moment labels is unmeasured.
- All setup duration, mess, independence, engagement, learning, repeatability,
  enjoyment, frustration, and safety outcomes are `UNKNOWN`.
- Rain-themed craft breadth and the research-backed activity model required to
  deserve a future page have not been established.
- Google has not yet crawled or selected the proposed consolidation; the
  redirect mechanics are a future implementation recommendation only.

## Sources

- Local measured evidence: `ops/gsc-snapshots/2026-08-03.json` and
  `ops/gsc-snapshots/2026-08-04.json`.
- Local ownership evidence: both current generated pages, their generator
  definitions, homepage links, card routes, sitemap, keyword targets, current
  strategy, and `KAL-RES-007`.
- Tool evidence: Semrush Keyword Overview bulk and cached Google SERP Analysis,
  United States desktop, August 2026 database, collected 2026-08-04 through the
  user's logged-in Chrome session.
- Public ranking, extension, and redirect sources are linked in the ranking-
  page analysis. They support only the bounded statements attached to them.
