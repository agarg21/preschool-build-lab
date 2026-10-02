# Ball Maze Compact-Card Handoff Repair

Action `KAL-IMP-023`, October 2, 2026 afternoon. Base `21d4eb9`; exact 15
paths in the roadmap. This implements the separately reviewed
[RES028 card-only task audit](ball-maze-card-handoff-2026-10-02.md) on the
existing card, without another URL or a change to the dedicated guide.

## Parent Task And Boundaries

Retain the September 14 source-derived caregiver task: judge whether an
intact shallow-lid maze fits a child who can move chunky blocks and follow a
stop cue, then start one wide three-wall path with an adult-selected large
lightweight foam ball. The adult controls the ball, remains close and stops
after throwing, mouthing, hard shaking, spill or damage. The guide owns the
stuck-ball rescue, younger-child adaptation, cleanup and evidence details.
Secondary stress: a younger child can reach materials. Success for this
handoff repair is a visible route to that maintained depth, materials and
direct stop before the short execution sequence in normal mobile view, and a
visible route without clipping at 200% root text. Failure includes a lost
material/stop, misleading tested/safety claim, broken guide route, or drift
of other generated cards. This is a `RESEARCH_HYPOTHESIS` persona task, not a
parent interview or physical trial.

The maintained maze mechanism is `SOURCE_BACKED` within the September 14
reconciliation; the exact KAL loose-three-wall setup is editorial synthesis.
RES028 local geometry and this action's browser QA are `MEASURED` technical
evidence. The layout and rubric are `EDITORIAL_JUDGMENT`. The October 2
public-safe GSC snapshot is finalized through September 30: 383 impressions/
11 clicks overall versus 380/10 on October 1; ramp 294/9 versus 292/8;
compact Ball Maze card remains 1/0. Missing query/device/country and six
guide rows are not zero. This is no demand or causal SEO claim. Human
comprehension, enjoyment, engagement, duration, learning, mess, repeatability,
and safety in practice remain `UNKNOWN`.

## Implementation

The generator now emits one Ball Maze-specific early decision block: a direct
full-guide link for fit/rescue/cleanup, an ability-based check, and an explicit
not-family-tested label. The same existing parent-check wording moves before
the four steps; no stop trigger or step is removed. The guide link appears
once, separate from the broad engineering route. Only the Ball Maze card gets
the scoped mobile material/step tile styles and cache token. Its sitemap
lastmod advances to October 2. The guide body, canonical/H1/search owner,
card library, other 36 cards and other generated pages remain unchanged.

The card keeps the same shallow lid, chunky blocks, large lightweight ball,
three walls, gentle tilt/reset, adult control, open-ended time and existing
interest hook. It does not claim that an age label alone makes the setup fit,
or that KAL measured any family outcome. The full guide still specifies the
adult-selected foam ball; the card's shorter ball label is unchanged and the
direct guide route now sits above it.

## Local Browser Result

Bundled Playwright/headless Chromium against generated local `file:` HTML;
1280x844 keyboard and 390x844/390x844 root200%/320x844 root200% touch. The
200% root setting was applied before card and guide navigation. Screenshots
of normal mobile and narrow enlarged text were inspected. Coordinates below
are document-relative and comparable to RES028's same-size baseline.

| Card surface | Desktop1280 before -> after | Mobile390 before -> after | Mobile390 root200% before -> after | Mobile320 root200% before -> after |
|---|---:|---:|---:|---:|
| Guide-link top | 696 -> 240 | 1466 -> **232** | 2310 -> **413** | 2845 -> **528** |
| Parent-stop top | 514 -> 416 | 1207 -> **705** | 1639 -> **1398** | 1867 -> **1769** |
| Step-grid top | 319 -> 516 | 557 -> 856 | 891 -> 1804 | 1057 -> 2328 |
| Document width | 1280/1280 | 390/390 | 390/390 | 320/320 |

At 390x844 normal text, the complete parent stop ends at y836, just inside
the first viewport, before the steps. At root200%, the guide link is visible
before the first fold but the full stop and materials require scrolling. This
is not a claim of one-screen completion at enlarged text. The normal mobile
document height falls from 1709 to 1500px. Enlarged-text height rises from
2807 to 3081px at 390 and from 3393 to 3942px at 320 because the explicit
fit/untested block and full-size text take space; do not describe the entire
enlarged card as shorter. Material and step tiles themselves have reduced
mobile minimum height. The tradeoff is earlier critical routing and boundary,
not a universally shorter page.

All modes fit their client width and retain exactly one guide link, three
material tiles plus open-ended time and four steps. Desktop fifth Tab focuses
the guide link and Enter opens the correct guide; mobile taps in three modes
do the same, and Back returns to the card. The guide retained its H1,
`#first-run`, `#troubleshooting`, `#adapt`, `#cleanup`, untested statement and
no-width-overflow fit, including at 200% root text. No page/console errors.
An initial harness case-sensitive `Cleanup` text search returned false for
the actual “Reset and clean up” heading; direct DOM check confirmed
`#cleanup`, `#adapt`, and `#troubleshooting` present. No product edit followed.
These are browser proxy observations, not assistive-technology certification
or family use.

## Persona And Every-Section Review

The comparable RES028 card-only complete-task proxy moves from **8/24 to
11/24 across 12 applicable dimensions**; sensory/accessibility is N/A
because no named sensory, mobility or assistive-technology constraint was in
the frozen task. Age/ability 0->1 (new check, adaptation still guide-only) and
detours/repetition 0->2 (one guide link before materials/steps). Safety/trust
stays 1 despite the earlier stop and untested label because foam-ball choice
and full contextual controls remain in the guide. Other dimensions retain
their RES028 scores. The card alone **still fails**
the complete-task critical gate for rescue and cleanup; that is why it must
keep a clear guide handoff. The whole internal route remains answerable; its
detours dimension 1->2 yields a **24/26 to 25/26** same-task proxy across all
13 dimensions, with sensory/accessibility still 1. No score is a measured
parent success rate or proof of preference.

| Visible block | Job and evidence | Verdict |
|---|---|---|
| Header/kicker/H1 | Stable identity; age label not a readiness assurance | Preserve |
| Early decision/handoff | Guide depth, ability check, untested boundary; new, first mobile screen | Keep; no duplicated long guide answer |
| Material/time tiles | Three materials and honest open-ended time; mobile tile height reduced | Keep |
| Parent check | Same adult control/stop text before steps, normal-mobile first viewport | Keep exact boundary |
| Four steps | Same flat lid/three walls/adult ball/gentle tilt; mobile rows condensed | Keep |
| Best for | Interest hook and one-wall change without outcome promise | Keep |
| Related engineering route/footer | Broad comparison and return, distinct from direct guide | Keep |
| Guide hero/run/rescue/adapt/cleanup/evidence | Maintained depth, unchanged bytes | Preserve |

## QA And Release Gate

All three generators ran twice with byte-stable output. Only generated Ball
Maze card HTML and its one sitemap lastmod changed; shared CSS changed with
selectors restricted to the Ball Maze card. Seven guides, 37 cards and 66
sitemap URLs stay stable. Full native 113 tests, 76 public GSC snapshot
validations, JSON/whitespace and 71 HTML/834 local link-asset-fragment checks
pass. The focused native test locks link uniqueness/position, stop-before-step
order, trust label, scoped CSS/cache token and October 2 card lastmod.

Copernicus (`01a0f6c8-0580-7801-8534-fdf62d5fff22`) independently
reviewed the frozen 15-path diff read-only: **PASS, no P0-P3 findings**. It
verified the 71 prior roadmap items unchanged, one-card generator scope,
the original four steps and stop wording, card-only/whole-route proxy
arithmetic, 108 non-writing native tests, JSON/whitespace, 71 HTML/834
references, and desktop plus three mobile/text-mode browser routes/Back,
widths and errors. It did not run generators or fixture-writing tests;
Master ran all 113 native tests, generators twice and 76 snapshot validations.
Reviewed commit `a8018c787a7598d81584a4bceec78885e715c283` was pushed to main. Its exact-SHA Pages run [37054589106](https://github.com/agarg21/preschool-build-lab/actions/runs/37054589106) succeeded. No release marker exists; the live card, stylesheet, sitemap and guide each returned HTTP 200 and byte-matched the reviewed local file. Card and guide canonicals/H1s, one guide link, October 2 card sitemap lastmod, and guide section links passed. Live desktop keyboard, 390px mobile, 390px/root200% and 320px/root200% touch/Back, image, width and clean-error checks passed; screenshots were inspected. Live normal-mobile guide link y232 and stop y705-836, and enlarged link y413/y528, matched local geometry. Same-path factual closeout follows; no human-use or SEO outcome is inferred.
Reconsider if production or later evidence finds a P0-P2 issue,
production fails a width/route/stop check, the new route cannibalizes guide
ownership, or the enlarged-text scan tradeoff proves unacceptable for a
source-grounded task. Protected windows and October 4 weekly synthesis stay.
