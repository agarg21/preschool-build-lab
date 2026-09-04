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
