# Ball Maze Library Journey Audit

Action `KAL-RES-027`, September 30, 2026 afternoon. Base `bb93ea3`.
Research only: no site, generator, URL, or paid-data change.

## Decision

**IMPROVE the existing journey, not the activity or page count.** Library ->
Ball Maze Box card -> dedicated guide works with keyboard and touch, and the
guide supplies the frozen task's critical instructions. The mobile 200%-root-
text library has a measured horizontal overflow: its unrelated card-game
promotion reaches x=460 in a 390px viewport. The card's full-guide link is at
y=1466 on normal mobile and y=2310 with enlarged root text; the source-derived
younger-child and cleanup decisions are only in that guide. This is a scan and
handoff cost, not evidence that the guide is unreachable or that a parent
actually abandoned it. A true enlarged-text `#first-run` arrival also hides
the heading 39px behind the sticky header, failing the readable-arrival gate;
the first instruction remains visible. Register a separately reviewed
existing-route repair; do not create another ball-maze page or change its
search ownership.

## Task And Evidence

The [September 14 implementation review](ball-maze-guide-implementation-review-2026-09-14.md)
froze the source-derived caregiver task: decide whether a no-cut shallow-lid
maze fits a child who can move chunky blocks and follow a stop cue, then run one
wide-path attempt. Required outputs are the intact lid, three chunky loose
blocks, adult-selected large lightweight foam ball, adult/child roles, gentle
tilt, stop, one-wall reset, stuck-ball rescue, adaptation and cleanup. A younger
child who may reach materials is the secondary stress. Success means finding
these without another broad search; failure includes a critical absent control,
unreachable guide, clipped start, or misleading certainty. This is a
`RESEARCH_HYPOTHESIS` task, not a person interviewed or an activity tried.

The current guide and its dated source reconciliation are `SOURCE_BACKED`
within that review's limits. Browser route and geometry below are `MEASURED`
local technical observations; scoring and the repair priority are
`EDITORIAL_JUDGMENT`. No physical or family test, material-size assurance,
duration, engagement, learning, mess, or safety outcome was measured.

New GSC snapshot collected September 30 at 16:32 UTC, finalized through
September 28: 387 impressions/10 clicks overall versus 385/10 prior; ramp
298/8 versus 298/8; all ten priority URLs indexed. Ball-maze card has one
impression/zero clicks, which does not establish demand or the library route.
Full query/device/country rows are absent; six other article rows are not
known zeros. This audit makes no SEO attribution or ranking claim. All existing
observation windows and October 4 weekly review remain unchanged.

## Browser Task

Bundled Playwright with an existing local Chromium headless shell; three
isolated contexts, no dependency install. `file:` versions of the current
site, not live production or physical devices. Screenshots were inspected;
the normal mobile card and full guide are readable. Root-text doubling is a
specified stress, not browser zoom or assistive-technology certification. The
enlarged-text library promotion screenshot visibly clips its paragraph/link at
the right viewport edge, consistent with measured overflow; the card and
guide screenshots do not show that horizontal spill.

| Check | 1280x900 keyboard | 390x844 touch | 390x844 touch, root text 200% |
|---|---|---|---|
| Library -> card -> guide | Focus/Enter twice reaches correct guide | Two taps reach correct guide | Two taps still reach correct guide |
| Library width | 1280/1280 scroll/client | 390/390 | 461/390 scroll/client; game promo link and text extend to x=460 |
| Card and guide width | Both 1280/1280 | Both 390/390 | Both 390/390 |
| Card depth link top | y=696 | y=1466 | y=2310 |
| Guide first panel top | y=265 | y=309 | y=684; first step y=1261, stop y=1808 |
| Direct `#first-run` after text settings applied | heading top104, header bottom61 | heading104, header93 | heading104, header143; heading partly hidden |
| Back and errors | Guide Back returns card; no console/page errors | Same | Same |

At the direct fragment, the first step starts below the sticky header in all
three modes (top152/153/265 respectively). The guide image loads at natural
1672x941. Browser Back from the fragment returns the unfragmented guide, as
expected. Normal mobile first panel includes the stop at y668-753 in the
initial 844px viewport; enlarged text requires scrolling to reach its stop.
An earlier harness set the hash before injecting the enlarged root style and
measured heading top244. That order is not a true enlarged-text arrival: when
text is enlarged before following the hash, top104 lies behind the 143px
header. The corrected screenshot shows the clipped heading and visible first
step. This direct-fragment stress fails readable arrival; the card's
unfragmented guide link does not jump to this hidden heading.
The card is 1709px tall on normal mobile and 2807px enlarged, versus 888px on
desktop. Its tall step tiles and three material tiles put the depth link after
the first viewport, but do not make it inaccessible. The library's ball-maze
entry is at y6164 on normal mobile and y10034 enlarged among 36 visible grid
links (37 card files exist); this position is not a measured search or filter
failure. `cards.html` offers a
static grid, not a tested search/filter state.

## Persona Score

Whole library-to-guide journey: **22/26, 13 applicable dimensions**, with no
N/A. The completed unfragmented path has no critical missing instruction; the
direct-fragment readable-arrival gate fails under enlarged text and the library
overflows. The score is a proxy, not a parent-success rate and not comparable
to September 14's direct-guide rubric.

| Dimension | Score | Basis |
|---|---:|---|
| Task answerability | 2 | Guide yields a runnable wide-path default and rescue. |
| Age/ability | 2 | Readiness uses ability and stop cue, not age alone. |
| Materials/substitutions | 2 | Exact no-cut set and wider/flatter block or smaller lid fallback. |
| Setup/duration/cleanup | 2 | Flat clear area, explicit cleanup; duration stays unknown/open-ended. |
| Adult involvement | 2 | Adult selects/controls ball, stays beside, may tilt. |
| Setting/space | 2 | Clear floor or low table; lid stays below face level. |
| Mixed-age/difficulty | 2 | Younger-child reach and harder-path adaptation explicit. |
| Sensory/accessibility | 1 | Adult-tilt role offered; individual sensory/mobility fit remains unknown. |
| Educational purpose | 2 | One-wall comparison stated without outcome promise. |
| Safety/trust | 2 | Direct stops and untested disclosure; no universal assurance. |
| Mobile readability/interaction | 0 | Route works, but root200% library overflows and direct hash hides heading. |
| Detours/repetition | 1 | Full guide link is below mobile first screen after tall compact steps. |
| Decision without broad search | 2 | Guide provides the required outputs through the internal route. |

## Every-Section Audit

| Surface/block | Parent job, evidence, and cost | Verdict |
|---|---|---|
| Library header/intro | Identify the card library; standard navigation works | Keep |
| Library game promotion | Different useful job, but its link/text cause root200% overflow | Repair width/wrapping only; do not infer game demand |
| Library other route links | Browse other jobs before grid; no ball-maze-specific claim | Keep; no wholesale reorder from one task |
| Library grid/footer | Ball Maze Box materials visible in entry; near grid end, no filter | Keep entry; not a navigation impossibility |
| Card title/material/time tiles | Correct identity and open-ended time; three loose blocks named in steps | Compress only if handoff repair retains clarity |
| Card four step tiles | Gives a runnable short start, but large empty tile space delays depth | Reduce scan cost in a separate action, without changing mechanism |
| Card parent/best-for strips | Specific adult/stop boundaries and mission; younger-child detail not here | Keep direct boundary; guide owns deeper adaptation |
| Card guide/related/footer | Direct full-guide link works, but below initial mobile view | Move/clarify handoff within existing card scope |
| Guide hero/fit/start | Hook, readiness, exact materials, roles, mission, stop before illustration | Preserve |
| Guide illustration/caption | Shows three-wall editorial variant; AI/not-test label explicit | Preserve |
| Guide first run | Five steps and adult boundary establish executable default; enlarged direct hash hides heading | Repair anchor clearance only; preserve instructions |
| Guide one-wall comparison | One controlled change, no learning promise | Preserve |
| Guide troubleshooting | Stuck/path/slide/lid/done rescues, distinct from first start | Preserve |
| Guide adaptation | Younger reach, adult tilt, sensory unknowns | Preserve |
| Guide cleanup | Adult removes ball, checks lid/floor | Preserve |
| Guide evidence/sources | Untested and unknown outcomes clear; cited public mechanisms differ | Preserve |
| Guide related/footer | Compact and broader routes after the full answer | Preserve |

## Next Gate

Separately register one bounded existing-route implementation, prioritizing
the reproducible `cards.html` game-promotion overflow and the guide's
enlarged-text `#first-run` clearance. The Ball Maze card's depth-link scan
cost is secondary. Inspect generator ownership before editing the card.
Acceptance: no horizontal overflow at 390/root200%, no text clipping; the
direct `#first-run` heading clears its sticky header with the first step
visible when text is enlarged before navigation; original 37 card files/seven
guides and SEO metadata remain stable. Retest keyboard/touch/Back/direct
arrival and actual text fit. Move the card's depth link earlier only if a
separately reviewed compact-layout change preserves its materials, adult role,
mission and stop; the verified overflow and heading defect take priority.
No new URL, demand inference, indexing request, claim, or activity build follows
from this audit.

Independent Pasteur read-only cycle1 identified the false post-navigation
enlarged-text clearance and 36-versus-37 count; both were reproduced/corrected.
Cycle2 PASS/no findings after exact-scope, rubric, JSON, reference and privacy
review. This review did not repeat the browser matrix in cycle2. Release is
pending the fresh-fetch/no-divergence and exact-path push gate.
