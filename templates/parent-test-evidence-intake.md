# Parent-Test Evidence Intake

Use a fresh copy of this file for one activity after a real parent-observed
session. This intake records evidence; it does not authorize a public claim that
an activity is tested.

## Recording rules

- Record only what the observer directly saw or heard.
- Use `NOT_OBSERVED`, `UNKNOWN`, or `NONE` instead of guessing.
- Preserve a child's exact words under `Exact child quote`; do not paraphrase.
- Keep `Evidence status` as `DRAFT` and the attestation as `NO` until a real
  session has occurred.
- Before changing the status to `OBSERVED`, replace every `UNKNOWN` and
  `NOT_OBSERVED` value. Timing fields require whole minutes. Use `NONE` only
  when the real session established that no quote, confusion, change, mess, or
  asset occurred.
- A content upgrade still requires separate review before any observation or
  tested-status claim reaches the live site.

Validate this blank template with:

```sh
python3 ops/validate_parent_test_evidence.py \
  templates/parent-test-evidence-intake.md --template
```

Validate a completed copy by omitting `--template`.

## Intake

Evidence status: DRAFT
Activity: <Ramp Detective | Bridge Rescue | Shadow Builder | Windproof Tower | Tiny Boat Cargo Test>
Test date: YYYY-MM-DD
Observer: <name or role>
Setup minutes: UNKNOWN
Engagement minutes: UNKNOWN
Fast yes or hesitation: NOT_OBSERVED
Exact child quote: NOT_OBSERVED
Instruction confusion: NOT_OBSERVED
Child-led change: NOT_OBSERVED
Mess and cleanup: NOT_OBSERVED
Repeatability: UNKNOWN
Evidence assets: NONE
Next version: NONE
Additional notes: NONE

## Attestation

Observed in a real session: NO
