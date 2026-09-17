# Engineering Maze Boundary Correction

Action: `KAL-IMP-011`. Review date: September 17, 2026.

Registered base: `6a203f97323a37b01f217b668b7cefff136d941c`.
Incoming snapshot-only commit `3f404a1` was inspected and fast-forwarded;
it changes no registered path. Independent review: cycle-one `PASS`, no P0-P3.

## Evidence And Decision

`IMPROVE`: live Cup Tower routing exposed a maintained-evidence mismatch.
The engineering maze module names a ping-pong ball and asks an adult to
confirm it is too large to swallow. The released
`site/articles/cardboard-ball-maze-kids.html` and compact maze card instead
use an adult-selected large lightweight foam ball with explicit adult control
and stops. The correction removes the size assurance; it does not establish
that any ball or setup is safe in practice.

The existing guide supplies the reviewed editorial boundary, not official
safety certification. Live DOM and source agreement are `MEASURED` within
scope, the parent task is `RESEARCH_HYPOTHESIS`, and wording choices are
`EDITORIAL_JUDGMENT`. Every family outcome remains `UNKNOWN`.

Latest GSC is September 17, finalized through September 15: 228 impressions,
five clicks, average position 14.03, 10/10 priority URLs indexed. Ramp has
159 impressions and all five clicks. Complete query rows and new-guide
performance rows remain unavailable. Traffic is not the correction rationale.

## Frozen Task And Scope

A caregiver arriving at the maze module must identify the default ball,
three-wall start, adult entry/removal role, and direct stops. Secondary
constraint: a younger child may reach loose pieces. This is a website proxy
task, not physical activity testing.

Only the maze article changes in public HTML. All other modules, chooser,
identity, schema, links, and headings remain byte-identical. Only this URL's
sitemap lastmod advances. No page, asset, data row, indexing request, external
account, or tested status is added. Exact thirteen paths are in the roadmap.

| Relevant criterion | Before | After | Evidence |
|---|---:|---:|---|
| Materials agreement | 0 | 2 | Foam ball and three blocks match guide. |
| Adult entry/removal role | 1 | 2 | Adult places and removes the ball, stays beside lid. |
| Direct stop and trust boundary | 0 | 2 | Mouth, throw, shake, face, damage stops; no size assurance. |
| First start | 1 | 2 | Wide three-wall path before tilting. |

This focused rubric is not comparable with a complete 24-point guide review.
Other dimensions and the broad hub's scan cost are unchanged. The existing
sticky header covers the module heading after a fragment jump; this is a
pre-existing route limitation, not fixed or counted as a passing anchor here.

## QA

All 68 native tests and 62 public-safe snapshots validate. Three publishing
generators rerun byte-stably. All 68 HTML documents and 696 relative/root
local links and fragments pass. XML has 63 unchanged URL identities and one
changed date. Module-only HTML comparison passes.

Local CUA browser checks at 1280x900 and 390x844 verify updated text, no
horizontal overflow, material/adult/stop readability, Enter activation of the
chooser route and module-to-card route, and no warning/error logs. Mobile
module width is 350px inside 390px. No timing, comprehension, enjoyment,
learning, mess, feasibility, or safety outcome was measured.

Reviewer Pauli (`01a0b021-8827-72f3-b9c3-609caa5d2c5d`) confirmed read-only
status and reviewed all thirteen paths against the registered base. Independent
67 nonmutating tests, 62 snapshots, links/fragments, module-only/sitemap,
source/privacy, syntax/JSON/XML and whitespace checks pass. The reviewer
excluded the generator-invoking stability test; browser/idempotence remain
operator evidence. Released commit `2cda0a72b7f92588f97b6becce386b6e7a70dac0`
through successful exact-SHA Pages run `35245099209`, deployment `6507067502`.
Production HTML and sitemap return 200 and byte-match that commit. Desktop
and mobile text, chooser Enter route, canonical/H1, no overflow and clean logs
pass. No release-marker file exists; native deployment SHA and byte-match
provide release evidence without inventing a marker. Local/origin aligned.
