# Ramp Library Discovery Audit

Action `KAL-RES-024`, September 28, 2026 afternoon.
Base `ab0ee26db8bcdf50a48e74cfd50c8bcee2ef0a4c`. Research only; no site edit.

## Decision

**IMPROVE the existing ramp card-to-guide journey.** Preserve both URLs and
the detailed guide's search ownership. The library's ramp link works, but its
compact destination lacks the guide's adult setup and rescue and has no direct
guide link. A working indirect route exists: card -> Indoor Activities -> full
ramp guide. Do not describe the guide as unreachable or claim another broad
search is necessary. The hypothesis is supported for reachability, but not for
a direct, adequately qualified compact start.

The same journey has a separate measured text-fit defect: the guide's H1 clips
at mobile390 with root text doubled. Plan one bounded existing-ramp journey
repair, `KAL-IMP-020`, separately registered and reviewed. No new page, new
keyword research, library-wide redesign or top-five prediction is justified.

## Frozen Task And Evidence

Before browser testing, the checkpoint and roadmap froze entry `cards.html`,
destination `articles/cardboard-box-car-ramp-preschoolers.html`, and required
outputs: suitable household materials, adult setup, first child mission and
stalled-car rescue. Secondary constraint: no video dependency. Preschool parent
reads instructions to/with the child; no invented family biography or trial.

- [September27 Q2](../seo/caregiver-job-discovery-2026-09-27.md): public request
  for manageable preschool preparation, indexed May26, inconsistent relative
  body label. SOURCE_BACKED qualitative constraint, not market demand. Its
  source URL/date and privacy-safe paraphrase are retained there; no new forum
  collection here. Exact cardboard/books/car and rescue probes come from the
  existing guide, not the question. Persona is RESEARCH_HYPOTHESIS.
- [Current content principles](../strategy/content-principles.md): compact
  utility can lead to a deeper owner; adult role, rescue and evidence boundaries
  should be clear. EDITORIAL_JUDGMENT quality criteria, not outcome evidence.
- Live library, ramp card, guide and Indoor Activities HTML plus styles.css:
  all HTTP200 and byte-identical to local base September28. MEASURED technical
  evidence; existing guide guidance is retained editorial/source synthesis,
  not independently revalidated physical or safety advice in this audit.
- GSC: no new snapshot after fetch. All71 validate; latest September27 through
  September25,267impressions/9clicks overall, ramp183/9. Card5/0 and library4/0
  are thin landing-page rows, not navigation analytics. Full query rows and six
  other article rows unavailable, not zero. No attribution to this journey.

## QA Inventory And Actual Route

Inventory frozen before test: library ramp link, visible focus and activation;
card material/step/parent/source/related blocks; direct guide link presence;
guide first-start and rescue; alternate internal route. No filter/search exists
on this static library, so no filter-state claim. Off-happy probes: browser
Back, blocked video, doubled root text. Screenshots before scroll and at targets.

Persistent Node REPL initialization failed with a module-export error. Used
bundled Playwright with isolated headless Chrome contexts, closed in finally.
No dependency/config install. This is browser emulation, not physical devices,
assistive-technology certification or real caregiver testing.

| Check | Desktop1280x900 | Mobile390x844 |
|---|---|---|
| Library -> card | Eight Tab presses select ramp; visible blue focus; Enter opens correct card | Scroll to ramp then touch tap opens correct card |
| Direct guide handoff | Absent among all nine card links | Same absence |
| Compact start | Four short steps and generic materials; no adult assignment, detailed support, rescue or cleanup | Same text; first step begins near bottom of initial viewport |
| Back | Returns to cards.html | Returns to cards.html; scroll restoration not asserted |
| No-video probe | YouTube requests blocked; all text remains | Same; reserved iframe area still occupies space |
| Internal recovery | Focus link + Enter to Indoor Activities, then fuller-guide link + Enter | Both links tapped; guide reached |
| Guide arrival | H1 top121.02, header bottom61 | H1 top152.92, header bottom92.91; both visible |
| Normal horizontal fit | Card and guide viewport/scroll width1280/1280 | Card and guide390/390 |

Recovery is three link activations from library, versus a possible two-link
library -> card -> guide route. The latter is a proposed acceptance criterion,
not a measured after-state. Alternate-link focus was staged before Enter;
only the library's eight-Tab traversal is a complete sequential keyboard test.

With YouTube unblocked, the iframe still precedes materials/steps: desktop
top207.27-bottom649.39, steps top768.98, parent check top964; mobile iframe
top234.45-bottom412.20, steps top777.80, parent check top1427.80. This measures
layout, not video playback/access success. The library's one-screen aspiration
does not hold for this card at these viewport sizes. No claim about other cards.

At doubled root text (32px), mobile library -> card touch still works and the
card remains390px wide. The recovery route also works with touch. On the guide,
requested viewport remains390 but innerWidth/scrollWidth expand to431; H1
top224.84, header bottom142.83, and the long word clips at the screenshot's
right edge. This is CSS root-text scaling, not browser zoom or WCAG certification.
One navigation wait raced and a retry waited for third-party load until timeout;
final controlled run blocked all non-site requests and waited for DOMContentLoaded.
No production failure is inferred from those harness errors.

Guide rescue exists in a horizontally scrollable table (348px container,
620px content). A horizontal mouse-wheel probe in mobile emulation moved272px
and exposed the right-hand answer; it is NOT a tested finger swipe. Text is
recoverable but requires extra scanning. No claim that numeric page-width checks
alone prove text fit. No direct hash route is present in the tested links.

## Compact Destination Score

Score concerns the ramp card at the first library landing, not the whole site
or a before/after guide comparison. Eleven applicable dimensions: **8/22**.
Critical failure: adult setup and rescue required by the frozen task are absent
and no direct depth handoff supplies them. Internal recovery remains possible.

| Dimension | Score | Observed basis |
|---|---:|---|
| Task answerability | 0 | Generic roll steps, no required stalled-car rescue |
| Age/ability | 1 | Age3-5 label; no role/readiness alternatives |
| Materials/substitutions | 1 | Materials named; quantities, stiffness and substitutions omitted |
| Setup/duration/cleanup | 0 | Unqualified two-minute label; no cleanup or specific adult setup |
| Adult involvement | 1 | Parent check exists, but does not assign stack/stability task |
| Setting/space | 1 | Low ramp/no stairs stated; floor and landing area not explicit |
| Mixed-age/difficulty | N/A | Frozen task is one preschool activity, not a sibling or harder-mode request |
| Sensory/accessibility | 1 | Text works without video, but adult must interpret terse directions |
| Educational purpose | N/A | Task requests an activity start, not a learning outcome |
| Safety/trust boundaries | 0 | Some specific cautions; two-minute claim unqualified and no explicit untested label; do not infer actual hazard or measured duration |
| Mobile interaction | 1 | Touch works and text fits normally, but video/material stack delays steps |
| Detours/repetition | 1 | Existing owner only reached by a collection detour from card |
| Decision without broad search | 1 | Possible via internal recovery; cannot complete required outputs on compact landing |

This editorial rubric is a task-completeness proxy, not a satisfaction,
engagement, developmental or physical-safety measurement. Guide large-text
failure is separately recorded; it does not alter this compact-card denominator.

## Every-Section Audit

All block types on the library and card inspected; neighboring activity links
are navigation context, not37 separate activity reviews. Full guide HTML read;
rendered checks targeted entry, first-start, rescue and large-text arrival,
not an assertion that every downstream guide block had a visual QA pass.

| Surface/block | Parent value and cost | Verdict |
|---|---|---|
| Library header/hero | Entry label and navigation useful; long one-screen promise not met by tested card | Preserve navigation; retain promise mismatch as scoped evidence |
| Game promotion + two guide links | Useful other jobs, push first card below mobile fold | Preserve here; not evidence for wholesale reorder |
| Library grid/footer | Ramp is first item, materials identifiable; timer repeated | Keep card location; align only ramp summary in repair |
| Card header/kicker | Correct identity; age and timer cannot substitute for readiness/estimate | Keep identity; replace unsupported timer certainty |
| Card iframe | Source inspiration takes space before runnable answer | Demote/remove embedded dependency for this card; retain source credit |
| Card material/time tiles | Names useful, quantities and book controls missing | Compress/align with maintained default |
| Card steps | Readable action words, adult job unspecified | Replace with concise guide-consistent start |
| Card parent strip | Low/no-stairs boundary useful but incomplete task controls | Align with existing guide, no invented safety promise |
| Card source/related/footer | Provenance and return route exist, no direct owner | Keep provenance/return; add explicit full-guide handoff |
| Guide header/start | Immediate default and adult role before image | Preserve words; repair large-text heading wrap |
| Guide illustration/caption | Shows setup, explicitly AI illustration/not test photo | Preserve |
| Guide verdict/materials/cardboard/setup | Detailed quantities/fit and stability available, some start repetition | Preserve scope; no wholesale rewrite from this audit |
| Guide prompts/one-change/source block | Optional mission, evidence and untested status | Preserve, do not infer outcomes |
| Guide troubleshooting | Existing recovery table, horizontal scan on mobile | Preserve content; record scanning cost, not inaccessible text claim |
| Guide free play/roles/cleanup | Optional play, adult role and end state | Preserve |
| Guide FAQ/related/footer | Extra help and internal routes after runnable answer | Preserve; not required before first roll |

## Bounded Repair Brief

Candidate `KAL-IMP-020`: make the existing ramp card a compact, guide-consistent
start and direct handoff; repair only the destination heading's large-text fit.
Use generator-owned per-card overrides/custom rendering, not hand-edited output
or global redesign. Replace unqualified timing with honest unknown/open-ended
wording, bring adult-controlled default before optional video, retain specific
supervision/stop wording and source/untested boundaries, link the existing guide.
Do not copy its whole rescue table into the card or invent new safety guidance.

Acceptance: same frozen materials/adult/mission/rescue job; visible direct guide
link and no need for Indoor Activities detour; text-first compact start; keyboard
and touch at1280/390 and root200%; H1 long word fits390 without hiding overflow;
readable arrival with sticky header; blocked-video/back probes. No new URL,
metadata/guide-body rewrite or unrelated card output. Source reconciliation and
exact generator-output scope must be registered in that implementation, all
native/generator/link/browser QA and independent review required before release.

Preserve chainOctober7/foilOctober8/packOctober9/bridgeOctober10 observations and
next weeklyOctober4. Ramp's September18 initial window has elapsed. Prioritize
this verified usability/trust-boundary repair over another speculative page.
Reconsider if a live direct route contradicts the absence finding or enlarged
text no longer reproduces. Human outcomes and any SEO uplift remain UNKNOWN.

## Reproduction And Evidence

Live base-matching SHA256:

- Library: `35c209cfab4d310c823f00f0126285dc5ed62b2a8fd41fb43014d03813706137`
- Card: `f762550d522372e922dff4fcc3c23a766589450e9890bfe1090d523ecbdbb71f`
- Guide: `591f733e607c015ffc1570e1280dbd3886826225a01fc9c75e782b1cab7bb4be`
- Indoor hub: `a30ac577760a0809331a2d28ae241efcd77257c9b717f0d0d286fee583aa9382`
- Styles: `f559c317c0fe367b383131d65148807059c9e68af321ac4b9a2661455d4faa6a`

Reproduce at the named viewports from `https://kidactivitylab.com/cards.html`:
Tab8/Enter or tap ramp, inspect all card links, follow Indoor Activities and
Open the fuller car-ramp guide. Block YouTube for the no-video probe. For text
scaling set `html {font-size:200% !important}` on each loaded page; use a390px
mobile context. Read h1/header rectangles and document scrollWidth, then inspect
a viewport screenshot. Reset styles/context between cases; do not equate root
scaling with browser zoom. Current live bytes may change after a later repair;
the frozen base reproduces this version.

Temporary screenshots `/tmp/res024-{desktop,mobile}-{library,selected,card,
card-bottom,guide,rescue,recovery-arrival,card-unblocked}.png`, plus
`/tmp/res024-mobile-{card-200,steps-200,rescue-scroll,recovery-200}.png`.
These are local QA evidence, not public assets; durable route, measurements and
hashes above survive their eventual removal. No photo or video is claimed as
family evidence. Release/independent-review facts live in
[operator review](../ops/operator-review.md).
