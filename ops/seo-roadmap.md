# Kid Activity Lab Operator Roadmap

The machine-readable queue is `ops/seo-roadmap.json`. It preserves the age-4
STEM strategy while replacing manual chat sequencing with one durable operator
queue.

## Current sequence

1. Compare each new validated GSC snapshot with the 2026-07-18 baseline.
2. Use GSC and optional Semrush evidence for pages Google is already
   testing.
3. Improve one existing evidence-bearing page before considering expansion.

## Completed on 2026-07-17

- `KAL-REL-001`: released GSC/Pages infrastructure in `046d840`; workflow run
  `29627800627` succeeded and snapshot commit `a782f62` established a baseline
  of 29 impressions, 0 clicks, 61 sitemap URLs discovered, and all 7 priority
  URLs indexed. Pages run `29627796105` succeeded for the exact infrastructure
  commit; the snapshot-only and later roadmap-only commits did not redeploy.
- `KAL-OPS-001`: added `templates/parent-test-evidence-intake.md` and
  `ops/validate_parent_test_evidence.py`, then linked the field-test pack to the
  validation workflow. Independent review cycle 3 returned `PASS` after closing
  incomplete-evidence and template-mode bypasses. This created no parent
  observation or tested-status claim; the first real completed intake remains
  a user dependency.

## Next eligible action

`KAL-MON-001` may now compare the validated baseline with future snapshots and
select one bounded existing-page improvement when the evidence supports it.
Semrush remains optional enrichment.
`KAL-IMP-001` stays planned until real parent-test or fresh search evidence
identifies one bounded existing-page improvement.

The Control Room may scan every two hours, but it may run at most one
substantive Kid Activity Lab action per day during the proving period. Missing
parent observations are a valid human dependency, not permission to fabricate
evidence or generate generic pages.
