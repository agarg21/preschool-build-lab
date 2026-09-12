# Paper Bridge Guide Implementation Review

Action: `KAL-IMP-008`

Review date: 2026-09-12

Surface: local candidate at
`/articles/paper-bridge-challenge-kids.html`, compared with the released
`KAL-LEARN-003` compact-card baseline.

Evidence basis: the source-dated `KAL-RES-010` candidate pack, the reproducible
7-of-24 `KAL-LEARN-003` proxy baseline, the September 11 public-safe GSC
snapshot, current repository output, and local browser observations. This is a
persona-task proxy review, not parent or child testing.

## Parent Task

A caregiver wants a simple indoor build for a child who can place one large
object gently and follow a stop cue. The caregiver needs to judge fit, gather
ordinary materials, set up the bridge, start the child, supervise and stop,
compare one paper-shape change, recover from common failures, adapt the motor
job or a younger-child condition, and clean up without another broad search.

Required first-screen outputs at 390x844: interest hook, observable readiness,
one sheet of paper, two low closed books, one large lightweight object, adult
setup, first child action, and a direct stop boundary.

Secondary constraint: a younger child may reach the setup. Coins, marbles,
scissors, tape, a printer, and a specialized kit are excluded from the default.

Observable success: the complete first-start panel and stop boundary fit before
the mobile fold; the rest of the page adds one controlled comparison,
troubleshooting, adaptation, cleanup, and evidence limits without repeating the
same generic instructions.

## Score

| Dimension | Before | After | Implementation evidence |
| --- | ---: | ---: | --- |
| Task answerability | 1 | 2 | The hook, fit cue, materials, adult setup, child action, and stop are one compact opening task. |
| Age and ability adaptation | 0 | 2 | Fit is observable rather than age-only; the page offers younger-child and folding support. |
| Materials and substitutions | 1 | 2 | The default names one sheet, two low closed books, and one large lightweight block or soft toy; troubleshooting excludes rolling small objects. |
| Setup, duration, and cleanup clarity | 0 | 1 | Setup and cleanup are direct. Exact duration remains unknown rather than invented. |
| Adult involvement and supervision clarity | 1 | 2 | Adult setup, direct supervision, reachable-item choice, support stability, and stop/reset duties are explicit. |
| Indoor, outdoor, weather, and space fit | 0 | 2 | The page names an indoor, low floor or table setup and a nonslip fallback. |
| Mixed-age or difficulty adaptation | 0 | 2 | The younger-child route changes the object and adult role; folding support changes the motor job without changing the comparison. |
| Sensory and accessibility considerations | N/A | N/A | The research did not establish a specific need; the page states that limit and avoids claiming an outcome. |
| Educational purpose without overstated claims | 1 | 2 | One-variable observation and comparison are direct, while learning outcomes remain unknown. |
| Safety and trust boundaries | 0 | 2 | Low supports, supervision, reachable objects, slipping, throwing, mouthing, climbing, tearing, reset, and evidence status are bounded without a universal assurance. |
| Mobile readability and interaction | 1 | 2 | The complete start and stop fit at 390x844, document width equals viewport width, links remain keyboard reachable, and no warning or error appears. |
| Detours, repetition, and buried answers | 2 | 2 | The guide removes the repeated post-image summary; the runnable task precedes the single visual and later sections each solve one distinct parent question. |
| Decision without another broad search | 0 | 2 | Fit, run, compare, rescue, adapt, stop, cleanup, and evidence limits live on one URL. |

**Before:** 7 of 24 across 12 relevant dimensions.

**After:** 23 of 24 across 12 relevant dimensions.

**Automatic-failure check:** no local automatic failure observed. Critical
instructions are present, trust-sensitive claims are qualified, and the core
task is completable. Exact duration remains `UNKNOWN`; adding an unsupported
estimate to reach 24 of 24 would make the page less trustworthy.

## Responsive Evidence

At 1280x900, document width is 1280 with no horizontal overflow. The H1 spans
y=121..229, the start panel y=319..607, the stop boundary y=523..583, and the
illustration starts at y=643. The complete runnable start is visible before the
first fold.

At 390x844, document width is 390 with no horizontal overflow. The H1 spans
y=143..213, the summary y=225..295, the start panel y=309..698, the stop
boundary y=586..677, and the illustration starts at y=734. The complete
first-screen requirement is visible before the fold.

At 390x844 the sticky header ends at y=92.91. After scoping the guide's
`scroll-margin-top` to 104px, all six in-page targets land at y=103.55..104.08
and clear the header. The protected cardboard-ramp guide receives no computed
margin from this rule.

All 11 links were reached in sequential keyboard order: brand, Home, Original,
Cards, three sources, the compact card, two broad owners, and the footer.
Every visible section was inspected at mobile width; text fits, the illustration
loads at 1672x941, anchor targets clear the sticky header, and browser logs
contain no warning or error.

## Section Audit

| Section | Parent-task contribution | Verdict |
| --- | --- | --- |
| Hero and fit/start panel | Answers fit, materials, adult role, first action, and stop before the image. | Preserve. |
| Illustration | Shows one flat sheet across exactly two low books, one large object nearby, and a fold-detail inset; caption labels it AI-generated and not family-test evidence. | Preserve. |
| First try | Gives the complete bounded default and adult boundary. | Preserve. |
| One change | Holds books, gap, object, and placement constant while changing paper shape; makes no guaranteed strength claim. | Preserve. |
| Troubleshooting | Resolves falling paper, sliding books, opening folds, rolling objects, and a child ending the task. | Preserve. |
| Adaptation | Changes the object, adult role, or folding job without claiming a sensory or developmental result. | Preserve. |
| Cleanup | Gives a specific removal order and torn-piece check. | Preserve. |
| Evidence and sources | Separates source-backed process ideas, editorial setup, generated illustration, and unknown family outcomes. | Preserve. |
| Related routes | Keeps the compact card and two broad owners distinct from the dedicated guide. | Preserve. |

## Decision

`PRESERVE` and release the review-clean local implementation. The complete
nineteen-path diff meets the bounded individual-
activity standard without expanding protected broad hubs. Search discovery,
rank, clicks, parent comprehension, child response, duration, mess, engagement,
learning, repeatability, frustration, and safety outcomes remain `UNKNOWN`.

## Independent Review Cycle One

Caliper (`01a07609-1ce0-7e82-8c66-eb37337df68f`) and Halley
(`01a07648-ac88-7ab1-9e51-bc475877cc9e`) reviewed the complete frozen diff in
strict read-only mode. Both returned `FAIL`; neither reported a P0, P1, or P3.

The operator corrected every P2: the Before column now reproduces the frozen
7-of-24 baseline; the anchor rule is page-scoped and clears the mobile header;
the protected ramp is unaffected; the illustration now contains one two-book
setup plus a fold-detail inset; the card and card index use no exact duration,
toy-car default, or guaranteed-strength wording; the repeated quick-verdict
section is removed; tearing is in the direct stop; and all current-state and
evidence mirrors are reconciled.

## Independent Review Cycle Two

Both reviewers verified the product, image, evidence, score, and browser
corrections. They returned `FAIL` only for bookkeeping P2s: one stale
eighteen-path label, an obsolete cycle-one queue instruction, two stale
`KAL-LEARN-003` release labels, and a public-surface contract that did not
explicitly authorize the compact-card/card-index wording corrections or name
`site/cards.html` for production verification. No P0, P1, or P3 was reported.

The operator corrected those records. The action now declares 19 paths,
authorizes and describes all three changed HTML surfaces, requires production
verification of each, reconciles the released learning item, and advances the
queue to cycle-three rereview.

## Independent Review Cycle Three

Caliper (`01a07609-1ce0-7e82-8c66-eb37337df68f`) and Halley
(`01a07648-ac88-7ab1-9e51-bc475877cc9e`) reviewed the complete corrected
19-path diff in strict read-only mode. Both returned `PASS` with no P0-P3
findings. They independently reproduced the 7-of-24 baseline and 23-of-24
result, exact scope, deterministic QA, image integrity, desktop/mobile
first-screen behavior, keyboard and sticky-anchor behavior, all three public
surface contracts, and protected-page invariants.

## Release Verification

Reviewed commit `0dbb1e9f78a950ce894d6efeee1bdbd6ed59dc74` was pushed to
`main`. Exact-SHA Pages run `34695547966` and deployment `6409957064`
succeeded. The article, compact card, card library, image, and stylesheet
return 200 and byte-match the reviewed commit. Desktop and mobile production
checks pass canonical, H1, complete first-screen task, 11-link keyboard order,
all six sticky-header targets, image load, text fit, and zero overflow. The
article has no warning/error logs. A direct desktop compact-card visit retains
the frozen base's missing-favicon 404; the base card has no favicon declaration,
so this is recorded as an unchanged legacy condition rather than an action
regression. Search discovery and every family outcome remain `UNKNOWN`.

## Visual Asset

The built-in image generator produced the final 1672x941 raster from the
previous comparison image as a composition reference. The final prompt required
exactly one physical two-book bridge, one flat sheet, one large lightweight
block, and a small paper-only fold-detail inset; it prohibited a second bridge,
extra books, people, hands, text, small pieces, cars, coins, tape, scissors,
rulers, glue, and measurement marks. The checked-in WebP is
`site/assets/paper-bridge/paper-bridge-folds.webp`.
