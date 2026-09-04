# Product Learning Ledger

This is the cumulative record for evidence-grounded product learning. Each
entry keeps research, measured behavior, editorial judgment, and actual human
experience separate. A persona task is a proxy evaluation, not user testing.

## 2026-09-04 - KAL-LEARN-001

- **Family decision:** Can a caregiver start a no-cut indoor toy-car activity
  with a preschooler while a younger sibling may reach the setup?
- **Persona task:** Find the materials, immediate steps, adult role, stop
  conditions, cleanup, younger-child adaptation, and one optional variable to
  test on the cardboard-ramp guide without another broad search.
- **Falsifiable hypothesis:** The current guide makes every required output
  direct on desktop and mobile, and its dominant visual reinforces the low,
  stable support described in the instructions.
- **Sources and evidence class:** The finalized September 2 and September 3
  public-safe GSC snapshots are `MEASURED`. The live page and responsive DOM
  observations collected September 4 are `MEASURED` for what was rendered.
  Persona P1 (start now) and P2 (constraint first) in
  `seo/age-4-activity-cluster-decision-pack-2026-07-28.md` are
  `RESEARCH_HYPOTHESIS`; their cited public questions and pages are qualitative,
  not demand or KAL family evidence. The task score and action choice are
  `EDITORIAL_JUDGMENT`.
- **Result:** `IMPROVE`. The guide supplies the materials, runnable steps,
  adult role, stop conditions, cleanup, troubleshooting, younger-child note,
  and one-change extension. However, the 1672x941 hero image visibly uses a
  six-book stack while the alt text and repeated instructions call for a
  short, low, stable stack. At 1280x900 the first runnable heading begins at
  document position 1025, below the first viewport; at 390x844 the quick-answer
  card begins at 674 but extends to 1357. There was no horizontal overflow or
  console error in either responsive check.
- **Confidence:** Medium-high for the documented visual and layout mismatch;
  unknown for parent comprehension, child response, and search effect.
- **Action:** Preserve the live page in this learning transaction. Promote at
  most one separate candidate, `KAL-IMP-006`, to put a compact start-now answer
  before the dominant visual and replace or clearly reframe the visual so it
  depicts the same low floor-level setup as the instructions. Reassess the
  younger-child guidance within that exact task; do not add generic prose.
- **Reusable lesson:** On a trust-sensitive activity page, the dominant visual
  is part of the instruction. A start-now page should not make the caregiver
  reconcile a safety-relevant visual contradiction or scroll past a large
  image to reach the runnable default.
- **Next falsification trigger:** Image provenance or page structure evidence
  contradicts this observation; an independent reviewer finds the mismatch
  immaterial; or newer query-level/user evidence identifies a different,
  narrower failure.
- **Measurement boundary:** The first click, 157 ramp-page impressions, and
  August 18 recrawl show discovery, not causality or family usefulness.
  Complete query rows, parent comprehension, child engagement, duration,
  learning, repeatability, mess, and safety outcomes remain `UNKNOWN`.

## 2026-09-04 - KAL-IMP-006

- **Family decision:** Can a caregiver see and start the default no-cut ramp
  setup before interpreting a large image, including when a younger child can
  reach the materials?
- **Persona task:** Re-run the `KAL-LEARN-001` start-now task against the local
  implementation at 1280x900 and 390x844, requiring exact materials, three
  steps, adult role, stop, cleanup, younger-child adaptation, optional
  comparison, and visual-text agreement.
- **Falsifiable hypothesis:** A compact start before a labeled two-book floor
  visual removes the six-book contradiction and puts the runnable heading in
  the first viewport at both target sizes without weakening deeper utility or
  evidence boundaries.
- **Sources and evidence class:** The completed review-clean learning action
  and its cited source-traced personas are `RESEARCH_HYPOTHESIS`; September 3
  and 4 public-safe GSC plus local DOM, asset, and repository checks are
  `MEASURED`; the exact two-book default, AI-generated visual, placement, and
  post-change score are `EDITORIAL_JUDGMENT`. The visual is illustrative, not
  parent/child evidence.
- **Result:** `IMPROVE` applied locally and independently review-clean with
  `PASS_WITH_P3`. The score moves from 17 of 24 to 23 of 24. The heading moves
  from y=1025 to y=421.71
  at 1280x900 and from y=674 to y=514.05 at 390x844. The two-book image follows
  the card, its caption states its AI-generated provenance and evidence limit,
  and the established deeper
  task, sources, and routes remain available.
- **Confidence:** High for current DOM order, dimensions, visible visual-text
  agreement, and preserved repository invariants; unknown for human use and
  search effect.
- **Action:** Released and production-verified in reviewed commit `5d2c4d5`
  through successful exact-SHA Pages run `33901993003`. Protect the structure
  through September 18 except a verified P0-P2 regression. Do not add timing,
  outcome, testing, or safety-performance claims to close the remaining score
  point.
- **Reusable lesson:** A start-now surface can resolve a demonstrated task
  failure by changing order and specificity rather than adding a new page or
  more generic prose. Generated visuals need explicit evidence labeling.
- **Next falsification trigger:** Independent review finds a P0-P2 visual,
  responsive, trust, or preserved-section defect; production differs from the
  reviewed commit; or the next inspected crawl or query evidence identifies a
  narrower conflict.
- **Measurement boundary:** The improved proxy score and layout positions are
  not parent comprehension, child engagement, duration, learning, safety, or
  ranking evidence. Those outcomes remain `UNKNOWN`.
