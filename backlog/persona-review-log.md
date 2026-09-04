# Persona Review Log

These records evaluate concrete tasks against the current product. Personas
are evidence-grounded hypotheses, not fictional testimonials or human tests.
Scores use `0` for missing, misleading, unusable, or unsupported; `1` for a
recoverable answer that requires unnecessary interpretation or outside work;
and `2` for a direct, actionable, appropriately qualified, traceable answer.

## 2026-09-04 - Cardboard Ramp First-Start Task

**Action:** `KAL-LEARN-001`

**Page:**
https://kidactivitylab.com/articles/cardboard-box-car-ramp-preschoolers.html

**Evidence basis:** P1 start-now and P2 constraint-first parent-job hypotheses
from `seo/age-4-activity-cluster-decision-pack-2026-07-28.md`, its source-dated
public-question and ranking-page research, the current live page inspected on
2026-09-04, and public-safe GSC snapshots collected 2026-09-02 and 2026-09-03.

**Decision:** Start one no-cut indoor toy-car activity using household
materials.

**Constraints:** Preschooler; a younger sibling may reach the setup; floor-level
indoor space; no cutting or glue; caregiver needs a runnable default rather
than a broad idea list.

**Required outputs:** Materials, immediate steps, adult role, stop conditions,
cleanup, younger-child adaptation, and one optional one-change STEM extension.

**Secondary stress constraint:** The first screen and dominant visual must make
the low, stable setup clear without contradicting the written safety boundary.

**Observable success:** The caregiver can identify and run the bounded setup
without another broad search; image, alt text, and instructions agree; desktop
and mobile have no overflow or broken interaction; no outcome is overstated.

**Observable failure:** A critical output is absent, a trust-sensitive visual
or claim contradicts the setup boundary, or the task requires outside research.

### Score

| Dimension | Score | Evidence |
| --- | ---: | --- |
| Task answerability | 2 | The quick answer provides five steps and an adult job. |
| Age and ability adaptation | 1 | Preschool framing is direct; the younger-child adaptation is useful but buried in the FAQ. |
| Materials and substitutions | 2 | Base materials, optional tape, cardboard choices, and unsuitable cardboard are explicit. |
| Setup, duration, and cleanup clarity | 1 | Setup and cleanup are clear, but no honest duration range is provided; duration remains `UNKNOWN`. |
| Adult involvement and supervision | 2 | Adult setup/stabilizing role and direct stop conditions are explicit. |
| Indoor, outdoor, weather, and space fit | 2 | Floor-level indoor setup, clear rolling lane, and stair/furniture boundaries are direct. |
| Mixed-age or difficulty adaptation | 1 | The younger-child note covers lower support, direct supervision, and mouthing, but appears late and does not alter the initial material check. |
| Sensory and accessibility considerations | N/A | The selected task did not establish a sensory or mobility constraint; no conclusion is inferred. |
| Educational purpose | 2 | One-variable comparison is optional, bounded, and does not promise a learning outcome. |
| Safety and trust boundaries | 0 | The dominant image shows a six-book stack while the alt text and instructions call it short, low, and stable. |
| Mobile readability and interaction | 1 | No overflow or console error; the quick card starts at y=674 but most runnable content falls below the 844px viewport. |
| Detours, repetition, and buried answers | 1 | The page is complete, but desktop users pass the large hero image before the quick answer and younger-child guidance is near the end. |
| Decision without another broad search | 2 | All required activity-running outputs exist on the page. |

**Total:** 17 of 24 across 12 relevant dimensions.

**Automatic-failure check:** `IMPROVE`. The core task is completable, but a
trust-sensitive dominant visual contradicts the written low-support boundary;
that defect prevents a preserve decision.

### Section Audit

| Section | Task contribution | Evidence boundary | Verdict |
| --- | --- | --- | --- |
| Header and navigation | Keeps Home, Original, and Cards available without interrupting the activity task. | Current rendered links; no navigation-use claim. | Preserve. |
| Hero and image | Names the exact activity, but the six-book visual support contradicts the low-stack text and alt. | Rendered page observation; not family-use evidence. | Replace or reframe in a separate action. |
| Quick answer | Gives the shortest complete start and adult job. | Editorial instructions with bounded stop language. | Preserve; test moving before the dominant visual. |
| Quick verdict and materials | Makes the no-cut default and materials scannable. | Duration and outcomes remain unmeasured. | Preserve. |
| Cardboard and setup check | Explains suitable material, stability, floor placement, lane, and stops. | Conservative local guidance, not a universal safety assurance. | Preserve; surface the essential check earlier. |
| Parent prompts and one-change test | Gives optional prediction, one variable, rescue, and stopping point. | Source-backed structure plus editorial adaptation; no learning claim. | Preserve. |
| Troubleshooting | Maps slipping, bending, stopping, wobbling, and frustration to bounded fixes. | No claim that a fix worked for a KAL family. | Preserve. |
| Free play, child role, and cleanup | Supports agency and a clear ending without promising engagement. | Editorial guidance; outcomes `UNKNOWN`. | Preserve. |
| FAQ | Answers full-box, tape, younger-child, and taxonomy questions. | Younger-child guidance is cautious but late. | Improve placement only if the separate task requires it. |
| Sources and related routes | Exposes three source limits and routes to deeper or broader existing pages. | References are not KAL testing. | Preserve. |
| Footer | Restates practical setup and supervision boundaries without adding an outcome claim. | Current rendered text; not parent or child evidence. | Preserve. |

### Decision

`IMPROVE`, with one candidate for future separate registration only: align the
hero visual with the low floor-level instructions and expose a compact runnable
answer before that visual. Do not rewrite for CTR, create a new page, request
indexing, or infer query intent from the page row. Parent and child outcomes
remain `UNKNOWN`.

## 2026-09-04 - Cardboard Ramp First-Start Recheck

**Action:** `KAL-IMP-006`

**Surface:** Review-clean local implementation for the existing cardboard-ramp
URL; production release is pending.

**Evidence basis:** The completed `KAL-LEARN-001` task and its source-traced P1
and P2 research hypotheses, September 3 and 4 finalized public-safe GSC
snapshots, the local implementation, its generated illustrative visual, and
responsive DOM observations collected on September 4. This is a proxy review,
not user testing.

**Decision and constraints:** Start one no-cut indoor toy-car activity for a
preschooler with a younger child able to reach the setup. Use household
materials on the floor, avoid cutting/glue, and make the runnable default clear
before the visual.

**Required outputs:** Exact materials, three immediate steps, adult role, stop
conditions, cleanup, younger-child adaptation, optional one-change extension,
and a visual that agrees with the low-support instruction.

**Observable success:** The start heading is in the first viewport at 1280x900
and 390x844; the complete/cropped image follows the start and visibly uses two
broad closed books; all required outputs and routes remain; no unsupported
outcome is introduced.

### Recheck Score

| Dimension | Score | Evidence |
| --- | ---: | --- |
| Task answerability | 2 | Exact materials, three steps, adult role, and stop appear before the image. |
| Age and ability adaptation | 2 | Preschool framing remains, and the younger-child reach condition now appears in the early setup boundary. |
| Materials and substitutions | 2 | The first start and full list agree on cardboard, two broad closed books, cars, and optional tape. |
| Setup, duration, and cleanup clarity | 1 | Setup and cleanup are direct; no measured duration is available. |
| Adult involvement and supervision | 2 | Setup, stability check, direct supervision, holding, and stop boundaries are explicit. |
| Indoor, outdoor, weather, and space fit | 2 | Floor placement, stair/furniture exclusion, landing lane, and rug fallback are direct. |
| Mixed-age or difficulty adaptation | 2 | The early boundary covers every child present; the FAQ retains lower support and mouthing stop guidance. |
| Sensory and accessibility considerations | N/A | The selected evidence did not establish this constraint, so no result is inferred. |
| Educational purpose | 2 | The optional one-change comparison is retained without promising a learning outcome. |
| Safety and trust boundaries | 2 | Text and two-book visual align; the caption says AI-generated, illustrative, and not family-tested; no universal assurance is made. |
| Mobile readability and interaction | 2 | At 390x844 the H2 starts at y=514.05, no document overflow occurs, and native links retain normal tab eligibility. |
| Detours, repetition, and buried answers | 2 | The runnable default now precedes the dominant image; deeper detail follows without duplicate instructions. |
| Decision without another broad search | 2 | The complete activity-running task, troubleshooting, cleanup, and extension remain on one URL. |

**Total:** 23 of 24 across 12 relevant dimensions.

**Automatic-failure check:** No local automatic failure observed. Critical
instructions are present, trust-sensitive claims remain qualified, and the
core task is completable. Independent review remains mandatory.

### Recheck Decision

`PRESERVE` the bounded local candidate. Independent review returned
`PASS_WITH_P3` with no P0-P2. Do not invent a duration to obtain a perfect
score. Parent and child comprehension, enjoyment, engagement, learning,
repeatability, mess, safety outcomes, and search effect remain `UNKNOWN`.
