# Site Architecture Implementation Review

Action: `KAL-SEO-001`

Frozen base: `b31ac9599817082c1c954e83b9e3843f46330059`

## Review Scope

Review the complete unstaged exact-path transaction declared in
`ops/seo-roadmap.json`. The implementation changes three generators, the
read-only GSC target list, one regression test, sitemap output, canonical home
links on existing HTML, and restrained reciprocal routes on generated activity
cards. It changes no URL, title, H1, description, canonical, body claim,
navigation label, indexability, credential, external account, or indexing
request.

## Acceptance Boundary

- Preserve the Google verification file on disk but exclude it from sitemap.
- Keep exactly 61 unique canonical indexable content URLs in sitemap.
- Point every internal homepage link directly to `/` rather than
  `/index.html`.
- Link a generated card only to an existing age or collection source that
  already contains it, with at most three routes.
- Keep `paper-roll-play` without a route because no current hub owns it.
- Add card games, engineering, and math only as read-only GSC inspection URLs.
- Preserve all content, evidence, indexing, and external-action boundaries.

## Pre-Review Evidence

- 17 public-safe snapshots valid.
- Python compilation and generator byte idempotence pass.
- 17 of 17 repository tests pass.
- Strict XML, 65-file links/fragments, metadata/headings, exact-path scope, and
  `git diff --check` pass.
- Sitemap: 61 canonical indexable content URLs; verification URL absent.
- Generated cards: 37 total, 36 routed, one to three routes each.
- Internal content-link counts: engineering 10, math 9, preschool STEM 9.
- Live public preflight: sitemap, robots, and 10 monitored URLs return 200.
- Local desktop/mobile browser checks: no overflow or console warnings/errors;
  card routes fit and the engineering target renders correctly.

## Independent Review

Reviewer: Hypatia (`019fc813-fd5b-7453-870e-d995e39847fd`)

Read-only status: confirmed

Review cycle 1: `FAIL`

Findings:

- `P2`: the initial `11/10/10` link claims included each destination's
  self-canonical. Actual internal content-link counts are `10/9/9`, from a
  baseline of one each.
- `P3`: the first regression test did not independently enforce source
  ownership or explicitly assert the sole unrouted card.
- No implementation, persona, evidence, indexing, safety, external-action, or
  functional defect was found.

Corrections:

- corrected every repeated count and clarified that the metric is internal
  content links;
- independently load the SEO page ownership map in the regression test,
  require every generated route to point to a page that contains that card,
  and assert `paper-roll-play` as the only unrouted card.

Review cycle 2: `PASS`

- Both cycle 1 findings are closed.
- Every current claim uses the corrected `10/9/9` internal content-link
  totals; historical `11/10/10` text is confined to the finding record.
- The strengthened test independently verifies source ownership and the sole
  unrouted card.
- Independent 17-test, 17-snapshot, corrected-counter, exact-scope, and
  `git diff --check` reruns pass.
- Final findings: none (`P0`-`P3`).

Final verdict: `PASS`

Residual risk: crawl, rank, and click changes remain unknown until later
measurement. The implementation creates no evidence of parent or child
usefulness.
