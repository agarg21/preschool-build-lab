# Kid Activity Lab Operator Roadmap

The machine-readable queue is `ops/seo-roadmap.json`. It preserves the age-4
STEM strategy while replacing manual chat sequencing with one durable operator
queue.

## Current sequence

1. Release the review-clean parent-test intake and cloud measurement setup.
2. Refresh GSC and optional Semrush evidence for pages Google is already
   testing.
3. Improve one existing evidence-bearing page before considering expansion.

## Completed on 2026-07-17

- `KAL-OPS-001`: added `templates/parent-test-evidence-intake.md` and
  `ops/validate_parent_test_evidence.py`, then linked the field-test pack to the
  validation workflow. Independent review cycle 3 returned `PASS` after closing
  incomplete-evidence and template-mode bypasses. This created no parent
  observation or tested-status claim; the first real completed intake remains
  a user dependency.

## Next eligible action

`KAL-REL-001` pushes the review-clean local intake plus the independently
reviewed GSC/Pages infrastructure under the 2026-07-17 standing authorization.
After release, `KAL-MON-001` requires a fresh read-only GSC baseline with page
and priority URL Inspection rows. Semrush remains optional enrichment.
`KAL-IMP-001` stays planned until real parent-test or fresh search evidence
identifies one bounded existing-page improvement.

The Control Room may scan every two hours, but it may run at most one
substantive Kid Activity Lab action per day during the proving period. Missing
parent observations are a valid human dependency, not permission to fabricate
evidence or generate generic pages.
