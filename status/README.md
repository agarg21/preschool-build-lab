# Page Status Convention

Files in this directory are durable page-level decision records. They are not
daily dashboards and they do not replace `ops/seo-roadmap.json`.

Each status file must identify:

- the dated evidence snapshot used for the current page decision;
- the full production URL for every public page or legacy route;
- directional demand with source date, evidence class, and overlap limits;
- page-level GSC performance unless protected query evidence supports a
  query-specific statement;
- page role, review coverage, release state, blocker, and next eligible action;
- the action ID and repository-known release evidence for the latest material
  implementation.

Daily search evidence belongs in `ops/gsc-snapshots/`. Update a status file
when a page role, material evidence-based decision, review state, release
state, blocker, or next eligible action changes. Do not rewrite it merely
because another daily snapshot arrived.

Use `Implementation baseline` or `Decision baseline` when a number is
intentionally frozen at an action boundary. Use `Current public-safe GSC` only
for the latest snapshot actually cited by the file. Never call a page-level
average position a query rank.

When a newer snapshot materially changes discovery or a blocker, add a short
dated monitoring overlay above the durable page table. Do not silently replace
an implementation baseline or infer complete query intent from public-safe page
rows. Public-safe snapshots omit complete query rows, so absent rows are
`UNKNOWN`, not zero.

Demand estimates are `TOOL_ESTIMATE`, not measured Kid Activity Lab traffic.
Close variants can overlap and must not be summed as unique demand. Preserve
`n/a` as unavailable rather than converting it to zero.

Personas derived from searches, ranking pages, or community questions remain
`RESEARCH_HYPOTHESIS`. Status records may describe completed research and
review, but they must never imply parent or child use, engagement, learning,
enjoyment, repeatability, timing, mess, comprehension, or safety outcomes that
were not actually measured.

Repository release evidence may include the reviewed commit, native Pages run,
and production verification already recorded in the roadmap. Do not create a
status-only commit merely to backfill routine mechanical evidence. Reconcile a
status file as part of another registered transaction or an explicit status
maintenance action.
