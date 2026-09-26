# Bridge Guide Enlarged-Text Anchor Review

Action `KAL-IMP-019`, September26 afternoon heartbeat17:01:06.365Z.
Time checked17:01:19UTC; base `36b5aa6e465e641975aa576627f70af415588afd`.
Initial clean1d0b77e, incoming two GSC snapshot files inspected then ff-only.
Exact11 registered paths; no Control Room, paid research, accounts or new URL.

## Evidence And Frozen Task

The morning [independent review](bridge-handoff-implementation-review-2026-09-26.md)
identified a P3: fixed104px anchor clearance behind an enlarged sticky header.
Reuse the source-grounded no-video caregiver handoff, not an invented biography
or a new demand claim. Task: follow the pack's folding link using enlarged text
and immediately identify the comparison heading and its first instruction.
Constraints: keyboard or touch,390px phone/1280px desktop. Secondary stress:
320px, direct fragment entry, browser back and image unavailable. Required
output: heading and beginning of instructions below the header, no corrective
scroll or horizontal overflow. No claim of real assistive-device/user testing.

QA inventory before implementation: normal/enlarged text at1280/390/320;
all guide section fragments, link activation/keyboard focus/touch, direct-entry
and back, normal layout/content unchanged, image-independent reading. Compare
header bottom against heading top and visually inspect screenshots. Required
success: no intersection, normal104px margin retained, no content/SEO drift.
Every visible guide section is preserved; only anchor placement changes.

Baseline reproduced by actual pack link tap at390x844/200%root font:
heading top104.328px, header bottom142.828px, margin104px, width390/390.
Heading overlaps header by38.5px; screenshot `/tmp/kal-imp019-before390.png`.
This is MEASURED browser geometry, not human comprehension evidence.

## Scope And Hypothesis

Page-local `max(104px, 6rem)` anchor margin should preserve ordinary spacing
and scale enough for the tested enlarged header. No JS, shared CSS, text,
source, schema, image or URL changes. Same-day lastmod remainsSeptember26.
Reconsider if any tested anchor clips, normal layout changes, generators write
unexpected outputs or a new viewport/font configuration defeats the clearance.
This is a bounded defect exception within IMP018's observation throughOctober10.

## Sensing, Not Action Justification

70 snapshots validate. September26 collected14:47:44UTC, finalized-conservative
throughSeptember24 vs prior through23:271->276impressions,9clicks both,
12.87->12.75position. Four changed page rows: ramp185->187 impressions and
11.53->11.3position; engineering24->25/8.71->9.64; no-cut4->5/6->6.6;
home11->12/3.64->3.92. Clicks unchanged. All10priority inspections including
crawls identical. Sitemap Success61 and July5 last read remains stale relative
to66current URLs. Pack3/0 and bridge card1/0 unchanged; guide row unavailable,
not zero. Full query rows unavailable; overlapping28-day data predates both
September26 repairs. No causal or query-intent inference; no queue promotion.

## Implemented And Evaluated

One page-local style rule overrides the inherited fixed margin after the
shared stylesheet. All six existing section targets use104px at100% and192px
at200%root text. No script or shared CSS. Removing only the new style block
reproduces the base HTML byte-for-byte, including all prose, schema and links.

36 direct-entry checks: six targets(first-try, one-change, troubleshooting,
adapt, cleanup, evidence) x1280/390/320 x100/200%text. Every heading is below
header bottom and scroll width equals viewport. At390/200 the folding heading
is192.328px vs header142.828px:49.5px clear, compared with38.5px overlap before.
At320/200 it is191.875px vs142.828px. Normal104px computed margin preserved.
Actual keyboard Enter(1280) and touch(390/320), each at both text scales,
follow the pack link and browser back successfully.320/200 images blocked:
comparison heading/instructions still readable. No page errors in interaction
checks. Screenshots `/tmp/kal-imp019-before390.png`, `after-WIDTH-SCALE.png`
and `image-fallback320.png` visually inspected; not committed. Root-font
enlargement is the tested mode, not every browser zoom/assistive technology.

### Narrow Persona Rubric

This is the same frozen navigation task before/after, not morning's full
activity task. Four applicable dimensions, maximum8;4/8->8/8:

| Dimension | Before | After | Observable basis |
| --- | --- | --- | --- |
| Task answerability | 1 | 2 | Destination title recoverable by scrolling before; immediately visible after. |
| Sensory/accessibility | 1 | 2 | Tested enlarged-text reading no longer obscured; no universal accessibility claim. |
| Mobile interaction | 1 | 2 | Touch handoff lands clear at390/320. |
| Detours/repetition | 1 | 2 | Corrective scrolling no longer required for heading. |

Nine N/A, not scored as successful: age/ability, materials/substitutions,
setup/duration/cleanup, adult involvement, setting/space, mixed-age/difficulty,
educational purpose, safety/trust and decision without another broad search.
This task evaluates reading/navigation geometry, not those activity-planning
outputs or new claims. Retained full-task evidence is IMP018, not rescored.
Critical navigation success requires an unobscured heading; scores cannot
override measured intersection. Proxy result IMPROVE, not real user testing.

### Every-Section Disposition

| Visible section | Disposition |
| --- | --- |
| Header/hero/fit-and-start | Preserve markup and layout; no selector reaches these. |
| Illustration/caption | Preserve asset/disclosure; no change to evidence status. |
| First try | Preserve content; direct anchor now scales. |
| Comparison/two variants | Preserve all instructions; motivating handoff clears header. |
| Troubleshooting | Preserve all recovery outputs; direct anchor clears. |
| Adaptation | Preserve child/sibling/ability limits; direct anchor clears. |
| Cleanup | Preserve steps; direct anchor clears. |
| Evidence | Preserve sources/unknowns; direct anchor clears. |
| Related routes/footer | Preserve all routes; outside selector. |

Native110 tests, roadmap jq and whitespace pass. All three generators run
twice with116site/data files byte-stable on both passes, no output change.
Changed JSON/HTML JSON-LD parse; no CSV edit. Operator link check71HTML/833
relative/root-local href-src refs and uniqueIDs passes; exact11 paths,
417 protected files,59prior roadmap items/top-level fields and unchanged
sitemap pass. No credentials/private data or new claims in the diff.

## Independent Review

Cycle1 PASS, no P0-P3, Mencius `01a0deaf-1737-7670-9afb-5439ddd7c11f`,
strictly read-only, full working tree against36b5aa6. Morning P3 addressed
within this matrix. Independently checked scope/protected files/prior items,
HTML-minus-style identity,109 non-writing tests,70snapshots,JSON/JSON-LD/XML,
whitespace,71HTML/903refs in reviewer's link check,18normal-text anchor cases,
mobile keyboard/back and all eight screenshots. Complete36case/enlarged
geometry/touch/image-blocking,110th temporary-fixture test and generators
are operator-supplied, not independently rerun. No broad accessibility claim.
Two material hashes frozen. Same-nine-doc factual QA/review/commit/release
metadata permitted; exact-range review and production release still pending.
Weekly synthesis stays dueSeptember27.
