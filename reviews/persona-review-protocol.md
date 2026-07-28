# Persona And Every-Section Review Protocol

State: reusable review protocol

Last updated: 2026-07-28

## Purpose

Review whether a Kid Activity Lab page helps a real parent start, adapt, stop,
or extend an activity without unsupported certainty. Apply this protocol to
research packs and substantive page implementations.

Personas must come from the action's decision pack. They are hypotheses derived
from evidence, not fictional testimonials or proof of parent/child use.

## Review Inputs

- action ID, frozen base/diff, and exact paths;
- primary page job and query cluster;
- source-traced persona table;
- current page and every-section audit;
- claim/evidence register;
- validated parent-test intake when one is actually in scope;
- focused QA and responsive evidence for implementations.

## Persona Review

For each relevant persona answer:

1. What decision or activity-running job must the page solve?
2. Does the first screen or first decision surface provide a useful default?
3. Are secondary routes visible without requiring a heavy filter workflow?
4. Are materials, setup time, adult role, kid mission, mess, supervision, stop,
   and rescue expectations proportionate to the evidence?
5. What would make this persona abandon, misunderstand, or misuse the page?
6. Does the page promise more originality, testing, safety, developmental
   value, or independence than the evidence supports?

Provisional examples such as start-now, constraint-first, learning-purpose,
rescue, and repeat/extend parents are not mandatory personas. The decision pack
must support whichever hypotheses it uses.

## Every-Section Review

Review every visible block, not only title and intro.

| Section | Primary job/persona | Evidence used | User value | Risk or repetition | Verdict |
|---|---|---|---|---|---|
| Hero/first answer |  |  |  |  | keep/compress/replace/remove |
| Chooser/routes |  |  |  |  |  |
| Activity/card blocks |  |  |  |  |  |
| Instructions |  |  |  |  |  |
| Safety/mess/stop/rescue |  |  |  |  |  |
| Variants/extensions |  |  |  |  |  |
| FAQ |  |  |  |  |  |
| Sources/related links |  |  |  |  |  |

Check:

- clarity and scan cost;
- useful defaults before interaction;
- within-page repetition;
- parent and kid language;
- source freshness and claim proportionality;
- search-intent fit and cannibalization;
- index-worthiness and original utility;
- mobile usability and accessibility;
- promised-versus-delivered content.

## Human And Evidence Gates

An independent reviewer may evaluate wording and evidence. It may not supply
the missing human evidence.

Require validated user evidence before claiming:

- a parent or child tested the activity;
- engagement duration, child quote, confusion, repeatability, or observed mess;
- an original photo or observation;
- a safety outcome from actual use;
- developmental, therapeutic, medical, or guaranteed learning benefit.

Desk research may support practical supervision boundaries, but any new or
material child-safety guidance remains a human gate under project policy.

## Review Findings

Use:

- `P0`: destructive, unsafe, privacy/security critical, or live-site breaking.
- `P1`: likely functional failure, serious misleading claim, or major
  regression.
- `P2`: material persona, evidence, SEO, accessibility, or maintainability
  problem that must be fixed before integration.
- `P3`: useful non-blocking improvement.

Each finding must include action ID, path/line when applicable, observed
evidence, expected behavior, and a bounded fix. Do not invent findings.

Verdicts:

- `PASS`: no P0-P2 findings.
- `PASS_WITH_P3`: only non-blocking findings.
- `FAIL`: one or more P0-P2 findings.
- `BLOCKED`: required evidence or dependency prevents a valid review.

The project writer may fix P0-P2 findings and request re-review for at most
three cycles. Only `PASS` or `PASS_WITH_P3` can proceed.

## Required Output

- reviewed action, base/range, and exact paths;
- read-only status and reviewer identity;
- persona-by-persona verdict;
- section audit coverage;
- claim/human-gate assessment;
- structured P0-P3 findings;
- final verdict and residual risks.
