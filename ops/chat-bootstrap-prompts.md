# Historical Child Chat Bootstrap Prompts

Last updated: 2026-07-28

Archive status: the prior three-agent child-chat prompts are historical. Do not
use them to create independent schedulers, priority owners, or repository
writers.

## Current Model

- This permanent Master chat is the current scheduler and command center.
- The central Control Room is retained for future automation, but Kid Activity
  Lab scheduling is paused until the user explicitly re-enables it.
- The permanent Kid Activity Lab Master / Operator is the single repository
  writer for one registered action per transaction.
- SEO Research & Review, Implementation, and Operator Review agents may be
  invoked for bounded read-only tasks.
- The durable queue is `ops/seo-roadmap.json`; private chat memory and old
  backlogs do not independently set priority.
- Every material strategy, research, code, content, or configuration change
  requires native QA and a different independent read-only reviewer.
- There is no fixed daily action or commit quota. Multiple transactions may run
  sequentially, but independent actions keep independent scope and commits.

Current rules live in:

- `AGENTS.md`
- `agents/master-operator.md`
- `agents/seo-research-review-agent.md`
- `agents/implementation-agent.md`
- `agents/operator-review-agent.md`
- `seo/activity-cluster-research-protocol.md`
- `reviews/persona-review-protocol.md`
- `ops/operator.json`
- `ops/seo-roadmap.json`
- `ops/current-cycle.md`

## Bounded Supporting Task Pattern

A supporting task should receive:

- one action ID;
- exact read-only scope and paths;
- frozen base/range when reviewing changes;
- evidence and human gates;
- expected structured output;
- an explicit prohibition on editing, scheduling, committing, pushing,
  deploying, indexing, outreach, and external-account changes.

The Master records any accepted research, implementation, or review result in
the repository. Supporting tasks do not update the shared checkout themselves.

## Historical Threads

The former Implementation and SEO Research & Review threads may be read as
historical evidence. They are not active command centers. Do not send them
unscoped work or ask them to maintain roadmap/current-cycle state.
