# Historical Manual Agent Cadence

Archive status: this weekly multi-agent sequence is historical. Do not use it
to schedule work or ask supporting agents to update repository state.

The current model lives in `AGENTS.md`, `agents/master-operator.md`, and
`ops/current-cycle.md`.

## Current Manual Mode

This permanent Master chat is the command center. It may run multiple
transactions sequentially without a fixed daily quota.

For each transaction:

1. Register one action and exact paths in `ops/seo-roadmap.json`.
2. Keep the Master / Operator as the only shared-checkout writer.
3. Use supporting research, implementation, and review agents read-only.
4. Run native QA and obtain independent review for material changes.
5. Commit and release the focused action, then verify its invariants.
6. Start another action only after the prior transaction no longer overlaps
   active work or unrelated dirty paths.

## Handoff Rule

Supporting agents read the frozen task context and return structured findings.
Only the Master updates `ops/current-cycle.md`, roadmap state, files, commits,
releases, or external accounts.
