# Cardboard Ball Maze Guide Implementation Review

Date: 2026-09-14

Action: `KAL-IMP-009`

State: `PASS`; released and production-verified

Frozen base: `cbe30ba079ad92cdca5511d3f9c6142eaea0af6a`

## Decision Task

A caregiver must judge whether a no-cut cardboard Ball Maze fits a child who
can move chunky blocks and follow a stop cue, then run one wide-path attempt
while a younger child may reach the materials. The caregiver needs exact
materials, adult and child roles, a direct stop, one wall change, reset,
rescue, adaptation, cleanup, and evidence limits without another broad search.

This is a source-derived proxy task, not parent, caregiver, educator, or child
testing. The score and page choices are editorial judgment. Search discovery,
duration, comprehension, engagement, enjoyment, learning, repeatability, mess,
frustration, and safety outcomes remain `UNKNOWN`.

## Frozen Setup

- One shallow intact cardboard box lid.
- Exactly three loose chunky blocks used as wide movable walls.
- One large lightweight foam ball selected and controlled by the adult.
- No marble, bead, ping-pong ball, toy car, tape, glue, scissors, hot glue,
  printer, specialized kit, exact duration, or outcome promise.
- The adult sets the work area, controls when the ball enters and leaves the
  lid, and stays beside the activity.
- The child places walls and either tilts gently or directs the adult's tilt.

## Responsive Evidence

| Check | 1280x900 | 390x844 |
|---|---:|---:|
| Document width | 1280px of 1280px | 390px of 390px |
| Document height | 4,032px | 5,271px |
| H1 top/bottom | 121/175px | 143/213px |
| Start panel top/bottom | 265/636px | 309/774px |
| Stop boundary top/bottom | 552/612px | 668/753px |
| Illustration top | 672px | 810px |
| Horizontal overflow | None | None |
| Warning/error logs | None | None |

The complete hook, readiness cue, materials, adult setup and ball control,
first child action, mission, and stop boundary appear before the mobile fold.
The image loads at its natural 1,672 by 941 pixels. All 12 links are
sequentially keyboard reachable. Direct fragment checks for the six named
sections settle at y=104 on desktop and y=104 on mobile, below the sticky
headers. These are measured DOM observations, not evidence that a caregiver
understood or preferred the page.

## Persona Score

| Dimension | Before | After | Evidence |
|---|---:|---:|---|
| Task answerability | 1 | 2 | The first panel gives the complete decision and the body carries one runnable sequence. |
| Age and ability adaptation | 0 | 2 | Observable block-moving and stop-cue readiness replaces age-only fit; adult tilting is available. |
| Materials and substitutions | 0 | 2 | Lid, three chunky blocks, and one large lightweight foam ball agree across guide, visual, card, and index. |
| Setup, duration, and cleanup clarity | 0 | 1 | Setup, reset, and cleanup are direct; no measured duration exists. |
| Adult involvement and supervision | 0 | 2 | Adult setup, ball control, proximity, and handoff boundaries are explicit. |
| Indoor, outdoor, weather, and space fit | 0 | 2 | A clear floor or low-table area and below-face-level lid are direct. |
| Mixed-age or difficulty adaptation | 0 | 2 | Younger-child reach and adult-tilt routes are explicit without universal suitability. |
| Sensory and accessibility considerations | N/A | N/A | No specific sensory or assistive-technology need is established; the limit is named. |
| Educational purpose | 1 | 2 | One observable wall change is offered without a learning-outcome claim. |
| Safety and trust boundaries | 0 | 2 | Material conflict is removed; mouth, throw, spill, hard-shake, face-level, and damage stops are direct. |
| Mobile readability and interaction | 1 | 2 | Complete decision panel fits before the fold with no overflow, clipping, keyboard, anchor, or log failure. |
| Detours, repetition, and buried answers | 2 | 2 | The guide opens with the answer and every later section adds a distinct task output. |
| Decision without another broad search | 0 | 2 | Fit, start, rescue, adaptation, reset, cleanup, and evidence limits live on one URL. |

**Before: 5 of 24. After: 23 of 24 across 12 relevant dimensions.**

The missing point is exact duration. It remains unknown because Kid Activity
Lab has no measured family timing. No automatic-failure condition is present
in the local candidate.

## Every-Section Review

- **Hero and start panel:** keep; this is the complete parent decision and fits
  before the mobile fold.
- **Illustration:** keep; one intact lid, three loose chunky walls, one large
  ball, and an adult stabilizing hand agree with the frozen setup. The caption
  clearly labels AI generation and the absence of family-test evidence.
- **Make one wide path:** keep; it owns the complete run and adult handoff.
- **Change one wall:** keep; it adds one controlled comparison without
  promising learning or engagement.
- **Troubleshooting:** keep; each row resolves a named setup failure.
- **Adaptation:** keep; younger-child reach and motor-role changes stress-test
  the same task without claiming universal fit.
- **Cleanup:** keep; ball removal and damage inspection close the activity.
- **Evidence:** keep; it separates source-supported maze mechanisms from the
  KAL editorial variant and leaves every family outcome unknown.
- **Related routes:** keep; the compact card owns quick execution and the
  unchanged engineering hub owns broad comparison.

## Source And Visual Boundary

PBS KidVision Pre-K, KID Museum, Children's Home Society of California, and
the Children's Museum of Southern Minnesota support the public box/tray maze
mechanism. Several source versions use fixed walls, craft tools, or small
balls. The intact lid, loose chunky blocks, large lightweight ball, and exact
three-wall start are Kid Activity Lab editorial synthesis, not a measured
source outcome.

The illustration was created with the built-in image generation tool from a
constraint-locked prompt, then stored as a 1,672 by 941 WebP. It is an
illustrative asset, not a photo of family use.

## Local Decision

`PRESERVE` the review-clean bounded candidate for release. The guide reaches 23
of 24 without inventing duration, broadening into a roundup, or editing the
protected engineering hub.

## Independent Review

Reviewer: Antigravity CLI Parent-Task and Content-Trust Reviewer
(`agy-read-only-2026-09-14-ball-maze-parent`), read-only.

Verdict: `PASS` with no P0-P3 findings.

The reviewer independently verified the exact 20-path diff, generator
idempotence, 61 tests, 58 public-safe snapshot validations, links/fragments,
SEO ownership, image contents, responsive geometry, keyboard order, anchor
clearance, clean logs, every visible section, the 5-to-23 score, protected-
page isolation, privacy, evidence classes, and the absence of fabricated human
evidence.

## Release Verification

Reviewed commit `858ee051b44a808faf35aba6584b2373b27a5dfe` is pushed to
`main`. Exact-SHA Pages run `34828769448` and deployment `6434291751`
succeeded. The guide, compact card, card index, WebP, stylesheet, and sitemap
return 200 and byte-match the reviewed commit. Production canonical, H1,
first-screen task, image, desktop/mobile overflow, clean browser logs, and the
compact-card-to-guide route pass. These checks verify release integrity and
rendered behavior only; all caregiver and child outcomes remain `UNKNOWN`.
