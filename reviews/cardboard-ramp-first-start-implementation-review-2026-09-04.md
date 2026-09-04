# Cardboard Ramp First-Start Implementation Review

Action: `KAL-IMP-006`

Frozen base: `f974aacc11e4902c87bd6bdd534ee37e746e8137`

Reviewed range: frozen base to the complete current working-tree diff

Reviewer: Parfit (review response label: Sagan;
`01a06d6c-d04a-7083-b6fa-7a41157de9ae`)

Read-only status: confirmed for both cycles

## Scope

Review exactly the thirteen paths frozen in `ops/seo-roadmap.json`. The action
changes one existing article, one new versioned PNG, shared CSS, the existing
sitemap row, one focused test, this review record, the two cumulative learning
logs, priority-page status, and four operator mirrors.

No new page, generator source, other generated page, workflow, snapshot,
indexing request, external account, product, affiliate, tracker, tested status,
family evidence, or universal safety or developmental claim is authorized.

## Evidence And Hypothesis

`KAL-LEARN-001` scored a source-traced caregiver task 17 of 24. The previous
page made users pass a 1672x941 image showing six books before reaching the
first runnable answer, although its text required a short, low, stable support.
The falsifiable implementation hypothesis is that a compact start before a
labeled two-book floor visual will remove that contradiction and expose the
start heading within the first viewport at 1280x900 and 390x844.

The September 4 public-safe GSC snapshot is finalized through September 2 and
reports 230 property impressions, one click, average position 18.09, 10 of 10
priority URLs indexed, and 158 ramp-page impressions at page-average position
13.33. Complete query rows remain unavailable. This is observation context,
not CTR, query-intent, release-causality, or family-use evidence.

## Implementation

- A three-step start now precedes the visual and names cardboard, exactly two
  broad closed books, cars, the adult role, and a climbing/throwing stop.
- A versioned 1672x941 PNG shows a low cardboard ramp resting on exactly two
  broad closed books on the floor. The caption calls it AI-generated and
  illustrative, not a Kid Activity Lab family-test photo.
- The setup boundary now covers the selected younger-child reach constraint
  with toys appropriate for every child present and direct supervision.
- Article `dateModified` and only the existing article's sitemap `lastmod` are
  2026-09-04.
- The established title, canonical, H1, ownership, three source links, one-
  change test, troubleshooting, free play, cleanup, FAQ, and related routes
  remain intact.

## Persona Task Recheck

The task is to start one no-cut indoor toy-car activity for a preschooler while
a younger child may reach the setup. Required outputs are materials, immediate
steps, adult role, stop conditions, cleanup, younger-child adaptation, and one
optional one-change extension. The secondary stress constraint is first-screen
and visual agreement.

The local candidate scores 23 of 24 across twelve relevant dimensions. Task
answerability, age/ability adaptation, materials, adult involvement, indoor
fit, mixed-age adaptation, educational purpose, trust boundaries, mobile
readability, directness, and decision completion score 2. Setup/duration/
cleanup scores 1 because no honest duration is measured. Sensory/accessibility
is N/A because the selected evidence did not establish that constraint.

## Every-Section Audit

| Section | Required review question | Local result |
| --- | --- | --- |
| Header and navigation | Are brand and three navigation routes unchanged and usable? | Preserved. |
| Hero copy | Are title, canonical, H1, and build-and-troubleshoot ownership unchanged? | Preserved. |
| First-start card | Are exact materials, three steps, adult role, and stop direct before the image? | Implemented. |
| Hero image and caption | Does the complete/cropped visual show exactly two broad books and disclose illustrative status? | Implemented at both target widths. |
| Quick verdict and materials | Do the default and material rows agree with the two-book setup? | Aligned. |
| Setup boundary | Is younger-child reach covered cautiously without a universal assurance? | Implemented. |
| Cardboard and setup checks | Are cardboard choice, stability, landing lane, and lower-support fallback retained? | Preserved. |
| Prompts and one-change test | Are the optional comparison, rescue, stopping point, and three sources retained without learning claims? | Preserved. |
| Troubleshooting | Are all four problems and bounded remedies retained? | Preserved; slipping now names one broad book instead of two. |
| Free play and child role | Are story choices and optional agency retained without promising engagement? | Preserved. |
| Cleanup and FAQ | Are cleanup, full-box, tape, younger-child, and taxonomy answers retained? | Preserved. |
| Related routes | Do all four existing deeper/broader routes still resolve? | Preserved. |
| Footer | Does the boundary-oriented footer remain unchanged? | Preserved. |

## QA Evidence

- Final reproducible generator command hashed every file under `site/` before
  and after running `python3 scripts/generate_card_pages.py`, `python3
  scripts/generate_seo_pages.py`, and `python3
  scripts/generate_sitemap.py`. The manifest expression was `find site -type f
  -print0 | sort -z | xargs -0 shasum -a 256 | shasum -a 256`; both hashes are
  `34bb7d9b429844608ea4bcc16872cbefb55cf9769f8271cea628752ccd6e5680`.
  Before and after, `git status --porcelain=v1 -z | shasum -a 256` returned
  `44a3aed35a3bc9f929aa0919e5eaf8c1ad334258ed7449fce3f3a285e7d9375f`.
  The whole site and changed-path scope were therefore byte-stable.
- `git diff --check`, `jq empty ops/seo-roadmap.json`, six focused tests, and
  all 41 repository tests pass.
- Across 65 HTML files, missing local links = 0 and missing fragments = 0.
  Article JSON-LD and sitemap XML parse.
- The RGB PNG is 1672x941 with SHA-256
  `c9571eb6bfbd0fef11fccb8ccbc3beebd6a0e8fa9f9203ad7805dfdd153ee4b5`.
- At 1280x900, heading y=421.71, card bottom y=747.33, and image y=765.33.
  At 390x844, heading y=514.05, card bottom y=1082.74, and image y=1100.74.
  Both document widths equal their viewports, the image loads at natural size,
  its support and caption are visible, 12 links are native href anchors with no
  negative tabindex, action-page HTML/CSS/image requests return 200 or 304,
  and console warnings/errors = 0.

## Cycle 1

Verdict: `FAIL`

- `P2`: the earlier recorded tracked-diff hash came from a pre-documentation
  checkpoint and could not be reproduced from the reviewed tree. It therefore
  did not prove final-state generator idempotence or output scope.
- `P3`: the caption disclosed illustrative and not-family-tested status but did
  not explicitly say that the image was AI-generated.
- `P3`: the focused test named preserved neighboring routes but did not assert
  their four exact href values.

The Master reran all three generators around the final whole-`site/` and
changed-path manifests recorded above. Both before/after pairs match. The
caption now explicitly states AI-generated provenance, and the test asserts
all four related href values.

## Cycle 2

Verdict: `PASS_WITH_P3`

The reviewer independently reconfirmed the exact thirteen-path diff and
read-only status; reproduced the current whole-site and changed-path hashes;
and verified the actual two-book PNG, responsive crop, explicit AI-generation
caption, 23-of-24 arithmetic, every-section audit, evidence and claim
boundaries, unchanged ownership and routes, sitemap uniqueness, parsers,
links/fragments, and all 41 tests. No P0, P1, or P2 findings remain.

One P3 remains: an earlier pre-review sentence in `ops/current-cycle.md`
mentions the superseded interim tracked-diff hash before a later correction
records the accepted final whole-site and status manifests. This is a
nonblocking audit-wording ambiguity, not a defect in the final proof.

## Review Gate

The independent reviewer must inspect the actual PNG and responsive evidence,
not infer visual compliance from filename or alt text. Record structured P0-P3
findings and return `PASS`, `PASS_WITH_P3`, `FAIL`, or `BLOCKED`. Only `PASS`
or `PASS_WITH_P3` may proceed to release.

## Residual Risk

Parent comprehension, child response, engagement, learning, repeatability,
duration, mess, safety outcomes, and search effect remain unknown. A generated
visual is editorial illustration, not proof of a setup used by a family.

Final verdict: `PASS_WITH_P3`

## Release Verification

Reviewed implementation commit:
`5d2c4d5edc2a85b6ce093afa3fa3b2dcffb2f387`

Exact-SHA Pages run: `33901993003`, success.

The live article, PNG, CSS, and sitemap byte-match the reviewed commit.
Production keeps the title, canonical, one H1, first-start/image order, exact
two-book setup, younger-child reach condition, explicit AI-generated/not-
family-tested caption, four related routes, metadata dates, and loaded image.
At 1280x900 and 390x844 the start heading remains in the first viewport at
y=421.71 and y=514.05, document width equals viewport width, and there are no
console warnings or errors. No indexing request was made.
