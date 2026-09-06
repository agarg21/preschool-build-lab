# Preschool STEM Front-Door Implementation Review

## Review Request

- **Action:** `KAL-IMP-007`
- **State:** Implementation complete; independent read-only review pending.
- **Frozen base:** `b6732ba3d3cd4e9ae6c42ee6b33447306820a23f`
- **Target URL:**
  `https://kidactivitylab.com/collections/stem-activities-for-preschoolers.html`
- **Decision:** Apply the review-clean `KAL-RES-009` three-way front door to
  the existing broad preschool STEM owner. Do not add a URL or retain the old
  eight-card breadth merely for count.

## Exact Scope

The reviewer must inspect the complete working-tree diff from the frozen base
for exactly these 14 paths:

1. `scripts/generate_seo_pages.py`
2. `site/collections/stem-activities-for-preschoolers.html`
3. `site/assets/preschool-stem/preschool-stem-three-ways.webp`
4. `site/styles.css`
5. `site/sitemap.xml`
6. `tools/preschool-stem-front-door.test.mjs`
7. `reviews/preschool-stem-front-door-implementation-review.md`
8. `backlog/product-learning-ledger.md`
9. `backlog/persona-review-log.md`
10. `status/priority-pages.md`
11. `ops/seo-roadmap.json`
12. `ops/seo-roadmap.md`
13. `ops/current-cycle.md`
14. `ops/operator-review.md`

No new URL, unrelated generated page, workflow, snapshot, indexing request,
external account, product or affiliate surface, tracker, tested status,
parent/child evidence, or `KAL-IMP-006` path is authorized.

## Evidence And Claim Boundaries

- The September 5 GSC snapshot is finalized through September 3 and is
  observation context only. Complete query rows remain unavailable.
- HeadStart.gov, TERC, Smithsonian Science in Pre-K, and NAEYC support only
  the named inquiry, engineering, and pattern processes.
- The three-lane architecture, exact materials, readiness cues, adult roles,
  scripts, substitutions, stop points, routes, and illustration are Kid
  Activity Lab editorial judgment.
- The page states that Kid Activity Lab has not family-tested these setups.
  Parent comprehension, child response, timing, mess, engagement, enjoyment,
  learning, repeatability, frustration, safe completion, and causal search
  effect remain `UNKNOWN`.
- This implementation and its persona-task score are proxy evaluation, not
  human testing or evidence that any setup is appropriate for every child.

## Implementation Result

- Preserves the existing URL, title, canonical, one H1, indexability, and
  broad preschool STEM owner.
- Replaces the unlinked time/mess table, engineering-heavy eight-card grid,
  visible keyword narration, and unsupported object-teaching line.
- Adds one compact chooser with exactly three native same-page routes:
  `#shadow-change`, `#paper-bridge-test`, and `#continue-a-pattern`.
- Adds exactly three complete starts: `Shadow Builder`, `Bridge Rescue`, and
  `Pattern Path`. Each exposes materials, a substitution, observable
  readiness, adult setup, a child mission, three bounded actions, and a
  stop/reset boundary.
- Routes broader science, engineering, math, and age-four STEM jobs to their
  established owners. The original pack and card library are optional routes.
- Retains the legacy activity ID list as generator source data because the
  card-page generator uses it for backlinks; the custom preschool STEM
  renderer does not reproduce the legacy grid.
- Adds scoped responsive CSS without changing an unrelated page.

## Visual Provenance

The required illustration was created with the built-in `image_gen` tool as a
new image, then corrected once so the loose next pattern piece matches the
blue next item implied by the visible A-B sequence. The generation request
specified one clean horizontal editorial illustration with three plainly
separated material zones: a stable flashlight and large opaque block facing a
blank room wall; a white paper bridge across exactly two low closed books with
one large green plastic lid; and exactly four placed alternating blue/yellow
pieces with one loose blue next piece. It prohibited people, hands, faces,
children, logos, text, brands, watermarks, extra objects, and unsafe or
cluttered setups.

- Published asset:
  `site/assets/preschool-stem/preschool-stem-three-ways.webp`
- Measured output: WebP, 1672x941, 70,138 bytes; SHA-256
  `dab326d7063639eb5e6f45c7c43796ba0960db5cd08565fdd521eed077a007f0`.
- Caption boundary: AI-generated illustration, not a family-test photo or
  evidence of measured use or outcomes.

## Local Persona And Responsive Result

The same source-traced task moves from 8 of 24 on production to 23 of 24 on
the generated local page. The only one-point dimension is broader
indoor/outdoor, weather, and space comparison, which is outside this page's
three-lead job; sensory/accessibility remains N/A because the retained
evidence did not establish that task.

- Desktop 1280x900: chooser starts at y=455, first choice at y=456; the three
  choices are about 347px by 150px; document width is 1280 of 1280; no local
  horizontal scroller; the image loads at natural 1672x941.
- Mobile 390x844: chooser starts at y=589, first choice at y=590; choices
  stack at 350px; document width is 390 of 390; no component or text overflow;
  the image loads at natural 1672x941.
- Each native anchor reaches the expected hash and settles at about y=108
  below the sticky header. The browser logged no warnings or errors.
- A stitched full-page mobile capture repeated sections as a browser capture
  artifact. DOM counts, source, and ordinary viewport captures show one of
  each section; the stitched image is excluded as page evidence.
- Actual caregiver comprehension and child behavior were not measured.

## Pre-Review QA

- `python3 -m py_compile scripts/generate_seo_pages.py`: pass.
- All three required generators: pass.
- Second full generator run: byte-idempotent across 81 site files.
- Focused front-door tests: 8 of 8 pass.
- Full repository tests: 49 of 49 pass.
- `git diff --check`: pass.
- `jq empty ops/seo-roadmap.json`: pass.
- Local link and fragment validation: 65 HTML files, zero missing targets.
- Sitemap XML parse, target lastmod, HTML structure, source-boundary, image
  format/dimensions/signature, privacy, and exact-scope checks: pass.
- All 50 public-safe GSC snapshots validate.
- Generated-output diff is limited to the declared target HTML and sitemap;
  the card-page generator creates no unrelated diff.

## Independent Review Gate

A different read-only reviewer must reproduce the exact-scope and QA claims,
inspect the complete diff and visual, audit every section at 1280x900 and
390x844, verify every frozen lead field and source boundary, and return
structured P0-P3 findings plus `PASS`, `PASS_WITH_P3`, `FAIL`, or `BLOCKED`.
All P0-P2 findings must be resolved within at most three cycles. Only `PASS`
or `PASS_WITH_P3` may proceed to an exact-path commit and release.

## Review Cycle One

Independent read-only reviewer Caliper, thread
`01a07609-1ce0-7e82-8c66-eb37337df68f`, returned `FAIL` with no P0-P1,
three P2 findings, and one P3. Strict read-only status and the unchanged exact
14-path worktree were confirmed.

1. P2: Pattern Path directed a second placement after the one-extension frozen
   stop. The final step now ends after naming or pointing to the repeating
   part, and the focused test rejects a second extension.
2. P2: The first visual showed a board instead of the written wall and eight
   placed pattern pieces instead of the frozen four-piece starter. The edited
   asset now shows a blank room wall, exactly four A-B-A-B pieces, one loose
   blue next piece, and the unchanged two-book bridge setup. Alt text,
   provenance, dimensions, byte size, and SHA are reconciled.
3. P2: The provenance record exposed an ephemeral machine-local source path.
   That path is removed; the durable record retains the tool, final prompt
   constraints, repository asset, dimensions, byte size, and SHA.
4. P3: The custom renderer inherited the old shared stylesheet token. It now
   uses target-specific `preschool-stem-front-door-1`, and the focused test
   asserts it without regenerating unrelated pages.

Corrected QA again passes all three generators and 81-file idempotence, 8 of
8 focused tests, 49 of 49 full tests, 50 snapshot validations, 65-page links
and fragments, 60 unique sitemap URLs, exact 14-path scope, roadmap JSON,
image format/dimensions/SHA, and added-line privacy checks. At 1280x900 and
390x844 the geometry is unchanged, the target-specific stylesheet loads, no
overflow or console warning/error appears, and every native anchor settles at
about y=108. Cycle-two rereview is required.

## Review Cycle Two

Caliper reran strict read-only review on the corrected exact 14-path worktree
and returned `PASS` with no P0-P3 findings. The reviewer reproduced the
one-extension instruction and test, inspected the corrected image, confirmed
added-line privacy and the target-specific stylesheet token, and independently
passed in-memory generator idempotence, 8 of 8 focused tests, 49 of 49 full
tests, all 50 snapshot validations, 65-page links/fragments, 60 unique sitemap
URLs, and exact scope. Live checks on the existing server passed at 1280x900
and 390x844 with no overflow, warning, or error; native links were in keyboard
order with visible focus, and targets settled below the sticky header. Initial
and final worktree status matched. The implementation is review-clean and
eligible for exact-path release.

## Release Verification

- Reviewed commit:
  `df9e97eb43297e04b3158ac57e70bd541696e496`
- Exact-SHA Pages run: `34026333335`, successful.
- Live HTML, `styles.css?v=preschool-stem-front-door-1`, WebP, and sitemap
  byte-match the reviewed commit and return HTTP 200 with expected content
  types.
- Production at 1280x900 and 390x844 reproduces one canonical, one H1, three
  native choices, three complete starts, no overflow, image natural size
  1672x941, anchor targets below the sticky header, and zero warning/error
  logs.
- No new URL, indexing request, external account, product, tracker, tested
  claim, parent/child evidence, or outcome claim was created.
