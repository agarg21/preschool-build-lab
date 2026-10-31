# Paper Bridge Discovery Diagnosis

Date: October 31, 2026. Action: `KAL-IDX-002`. Base: `a2b4446d79b6f989fbde240b7ae9b4a512048492`. Normal heartbeat actual start 17:02:02Z; public measurements completed 17:09:11Z. Independent review/release receipt: [operator review](../ops/operator-review.md).

## Decision

**PRESERVE the existing guide; DEFER speculative repair.** The first expanded inspection cohort reports Paper Bridge as not indexed, with coverage `URL is unknown to Google` and null last crawl. A new one-guide public diagnostic found no tested HTTP, robots, canonical, sitemap or missing-inbound-anchor defect. This does not establish why Google has not discovered it, guarantee indexing, or qualify a content rewrite. No site change or indexing request is authorized by this diagnosis.

This learning unit goes beyond snapshot sensing: it tests the proposed public-discovery-blocker hypothesis against current production bytes, an actual HTML-anchor graph, release history and current primary documentation. It is not a deep audit of the other four negative guides.

## Indexed-Version Baseline

Sources: [October 31 snapshot](../ops/gsc-snapshots/2026-10-31.json), [October 30 comparison](../ops/gsc-snapshots/2026-10-30.json), [monitoring expansion](../seo/gsc-guide-coverage-audit-2026-10-30.md). These are normalized read-only measurements, not a new live Google inspection.

- Collected October 31 at 15:54:31.799Z, finalized through October 29 under the conservative two-day-lag rule. All 16 configured identities appear exactly once. All ten previous inspection objects are unchanged and indexed.
- Six additions: Tape Road indexed; Cardboard Ball Maze, Paper Straw Rocket, Paper Bridge, Paper Helicopter and Paper Cup Tower each NEUTRAL/not indexed with the coverage string above, unspecified fetch/index/robots states and null crawl. Total 11 indexed, five negative, zero normalized UNKNOWN-verdict rows. Zero UNKNOWN verdicts does not mean that all URLs are known to Google. Guide-only coverage is two indexed of seven.
- The changed denominator is a first baseline, not deindexing from ten to eleven of sixteen. Tape Road's reported crawl is September 27, before its latest repair; indexed status does not verify latest bytes.
- Site performance: October 2-29 rolling window, 401 impressions, four clicks, 1% CTR, position 18.74. Previous October 1-28 window: 386/four/1.04%/18.77. Overlapping windows are not daily gains or causality. Paper Bridge has no retained page row: unavailable, not zero demand or zero traffic. Full queries/country/device are absent.
- The API sitemap record still says 61 discovered and last read July 5; live sitemap has 65 entries. Neither identifies exactly which URLs Google has discovered, or explains this target's status.

## Public Access

Target: [Paper Bridge guide](https://kidactivitylab.com/articles/paper-bridge-challenge-kids.html). Ordinary HTTP requests used `KidActivityLab-public-diagnostic/1.0`, no authentication, cookies or Googlebot impersonation. Redirect chains were explicitly recorded. MEASURED at 17:09:11Z:

| Check | Result |
| --- | --- |
| Target HTTP | 200, no redirects, final URL exactly target, HTML UTF-8 |
| Target body | 11,574 bytes, exact local match |
| SHA256 | `dab1f3e8fa7ac9a9a6fbba3a6bb86918293576af4574e023fb20a36011772779` |
| Canonical/H1 | Exactly one self-canonical and one H1 |
| Index exclusion | No robots/googlebot meta tags or X-Robots-Tag header observed |
| robots.txt | 200, no redirects; `User-agent: *`, `Allow: /`, canonical sitemap advertised |
| Sitemap | 200, no redirects, strict XML parse; 65 entries, target exactly once, exact local bytes |

Robots body is 72 bytes, SHA256 `07420044a1604936a31d238c751a5644d99f23e0ee6085353f791a17c5eff5af`. Sitemap is 8,321 bytes, SHA256 `db8c3e3a1ee3c3ffdc5baf792b12211a879d2a145a612d09d2f60b5e145a032d`. A standard robots parser also returns an Allow proxy for Googlebot; neither this nor an ordinary fetch proves verified Googlebot access, Google's selected canonical, indexing eligibility in all conditions, or indexing success.

## Static Discovery Paths

Method: standard Python HTMLParser over all 73 local HTML files; resolve actual `<a href>` values with URL joining/fragment removal, exclude external/self edges, breadth-first search from the ten previously inspected indexed URLs. This is the complete HTML-anchor graph, including navigation and contributor links, **not a body-only graph**. Canonical/schema/script references are not edges. Registration's shorthand "content-anchor" is clarified to this measured scope, not a claim about search discovery.

Four inbound anchors from four distinct pages were fetched live, with no redirects, HTTP 200 and exact local byte matches. Each target fragment exists. Relative links below are exactly as authored:

| Source under kidactivitylab.com | href | Source bytes / SHA256 |
| --- | --- | --- |
| `/cards/paper-bridge.html` | `../articles/paper-bridge-challenge-kids.html#bridge-start-title` | 4008 / `80a1c400193fa57eca86dd30c4139edd4bef1ffd70b252d72fbe7e443584ae45` |
| `/articles/paper-cup-tower-kids.html` | `paper-bridge-challenge-kids.html` | 10764 / `03bc3b9e7558092d3cc8c88c04ff9426bcf150b0ec1535033b89dba7b141eea3` |
| `/contributors/riley-hart.html` | `../articles/paper-bridge-challenge-kids.html` | 3397 / `fae48e08c41723585afb9b77b1669f6963e2cd0828c0d86e0492ed956eaa8a25` |
| `/collections/original-stem-activities-for-4-year-olds.html` | `../articles/paper-bridge-challenge-kids.html#one-change` | 26579 / `3e67ea84c6d0416023eeba05099992f45ef982cab1f73a3a26b6447ef06f692f` |

All ten indexed seeds have a static shortest path: Original STEM pack directly in one hop; the other nine in two. Root, Ramp article, age-four at-home, age-four STEM, preschool STEM and card-game chooser go through Original STEM pack; engineering goes through the Paper Bridge card; no-cut and math go through Riley's profile. All 13 unique nodes in those selected paths were fetched live, 200/no redirects/exact local bytes. The contributor profile is a support surface outside the inspected seed cohort; its Google indexing status is UNKNOWN. Independent review verified no robots meta or X-Robots-Tag exclusion and its sitemap presence; the earlier noindex label was incorrect. Cup Tower itself has the new URL-unknown result. These paths do not prove Google traversed them. The direct indexed-pack link alone defeats the hypothesis that there is no published inbound route from an inspected indexed source.

Reproduction: parse the two snapshots/config and assert unique identical identity sets; compare prior inspection objects by URL; build the graph as described; record HTTP headers/body SHA256/redirects for robots, sitemap, target, four sources and the union of shortest-path nodes; parse live anchors and target IDs; compare each body to its local file. The run's read-only implementation is retained at `/tmp/kal-idx002-bridge-audit.py` for independent rerun, not a new production tool or durable dependency. This packet retains the consequential measurements even if the temporary file expires. Fragment existence is not a browser-readable arrival, keyboard, mobile or parent task test.

## Interpretation And History

SOURCE_BACKED: Google's [URL Inspection documentation](https://support.google.com/webmasters/answer/9012289?hl=en) distinguishes indexed data from live testing and explains that the reported URL-unknown condition means Google has not seen the URL in that inspection's indexed data. A successful live check does not guarantee indexing or predict Google's canonical. We did not perform a Google live test or submit an indexing request. Its suggested external actions do not override this project's no-request boundary.

SOURCE_BACKED: Google's [crawlable-link guidance](https://developers.google.com/search/docs/crawling-indexing/links-crawlable) supports testing actual anchor elements with hrefs rather than script-only references. Existing links are a discoverable route, not evidence of actual crawl, parent usability or a ranking benefit.

Repository evidence: initial `KAL-IMP-008` release `0dbb1e9` on September 12 has recorded exact-SHA Pages success `34695547966` and production checks in [priority status](../status/priority-pages.md). Later September 26 starter/anchor changes and October 27 contributor release `48d93e0` changed guide bytes. [October 28 hub-handoff repair](paper-bridge-hub-handoff-repair-2026-10-28.md), `d5e80886c81a61af72ed071cb7cb9cebc7a7d91c`, records Pages `40720346574`; its engineering/building paths preserve a stationary-object task, not a moving-toy-car substitution. These are retained historical release records, not newly rerun deployment or UX tests. Null reported crawl provides no post-release crawl timestamp; it cannot establish which bytes Google fetched or the cause of the gap.

Demand is not requalified here: [keyword target source](../data/seo_keyword_targets.csv) and priority status retain September 6 Semrush US TOOL_ESTIMATE for "paper bridge challenge": 590 monthly/KD17. This historical estimate is not current measured KAL demand, additive variant volume, achievable rank or a reason to duplicate the existing owner.

## Task And Quality Review

Operational task grounded in the new negative inspection: decide whether to repair an existing guide's public discovery route, with the required output being a tested blocker or a bounded preserve disposition. Secondary stress: a changed cohort denominator and a coverage string containing "unknown" despite zero UNKNOWN verdicts. The indirect parent job is finding the maintained bridge activity; no parent-search, activity, safety or satisfaction outcome was observed.

All 13 protocol dimensions considered. This is an operational evidence rubric, not an activity-page score: answerability 2 (exact decision), safety/trust 2 (boundaries), detours/repetition 2 (no speculative rewrite/repeated UX repair), decision without another broad search 2 (next evidence specified): **8/8 across four applicable dimensions**. Nine N/A because no activity or UI is being changed/tested: age/ability, materials/substitutions, setup/duration/cleanup, adult involvement, setting/space, mixed-age/difficulty, sensory/accessibility, educational purpose, mobile interaction. It does not override any page's activity review or imply a gain.

Every-section check: decision distinguishes access from indexing; baseline preserves identities/finalization; access reports headers/bytes/limitations; graph excludes nonanchors and labels support routes; history keeps dates/old deployment separate; sources support only their stated interpretation; task/rubric does not claim family tests; next gate is falsifiable. No critical diagnostic instruction is missing; independent review remains the release gate.

## Next Gate

Confidence: high in measured ordinary public access and published anchor routes; UNKNOWN in Google's discovery cause, selected canonical, crawl scheduling, query intent and family/SEO effects. The tested public-blocker hypothesis is unsupported in these conditions, not disproven for every client or time.

At the next actual scheduled snapshot compare Paper Bridge's indexed/coverage/crawl fields against this first baseline. A new error, canonical conflict, failed public route, blocked robots or missing sitemap entry qualifies targeted diagnosis and potentially a separately registered repair. A new crawl/status supplies new evidence, not automatic improvement. Unchanged URL-unknown alone does not justify repeating the whole graph audit or rewriting content; include the unresolved discovery limitation in November 1 synthesis and select independently eligible work. No arbitrary waiting promise, new paid tool, page batch or indexing request. Research/decision release is docs-only; QA/reviewer/release evidence belongs in the operator receipt.

Release receipt: independently reviewed full-seven cycle2 PASS after correcting the sole profile-indexability P3. Master/independent309 native; diagnosis released `3cfe8a09411b941596daff6948ee05aa58897a1d`, all seven exact-SHA remote file bytes matched at17:20:47Z, subsequent fetch clean0/0. No site or Pages delivery. Final factual annotations are reviewed separately within this same action's three-cycle limit. Next invocation prioritizes due November1 synthesis; this diagnosis does not require a repeated graph audit without new evidence.
