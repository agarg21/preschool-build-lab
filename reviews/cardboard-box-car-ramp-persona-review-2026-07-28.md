# Cardboard Box Car Ramp Persona Review

Action: `KAL-IMP-001`

State: review-clean

Frozen base:
`3e0169e94684be18f4dd150a1dbf79b5bf3b6069`

Decision pack:
`seo/age-4-activity-cluster-decision-pack-2026-07-28.md`

## Exact Scope

1. `site/articles/cardboard-box-car-ramp-preschoolers.html`
2. `site/sitemap.xml`
3. `reviews/cardboard-box-car-ramp-persona-review-2026-07-28.md`
4. `backlog/implementation-backlog.md`
5. `ops/seo-roadmap.json`
6. `ops/seo-roadmap.md`
7. `ops/current-cycle.md`
8. `ops/operator-review.md`
9. `progress.md`

No new page, generator, GSC snapshot, workflow, indexing request, external
account, parent/child evidence, original visual, or unrelated page is
authorized.

## Implementation

- Preserved the title, H1, canonical, hero image, immediate no-cut build answer,
  troubleshooting table, related architecture, and primary ramp
  build/troubleshooting ownership.
- Replaced unsupported age, setup/play duration, effort, cleanup-duration,
  universal child-capability, and safety-outcome wording with materials,
  adult-role, setup-boundary, invitation, and stop-condition guidance.
- Removed the historical "this page used to" commentary and the unsupported
  "parent-tested" footer.
- Added one optional height, car, or landing-surface comparison that asks the
  parent to change one thing, release without pushing, mark the stop point, and
  return to free play after one comparison.
- Cited the source-backed inquiry patterns from PNC Grow Up Great, PEEP, and
  PBS, while explicitly avoiding a Kid Activity Lab parent-test claim.
- Kept Ramp Detective as the deeper observation route and the quick card as
  the one-screen utility route.
- Updated only this article's existing sitemap `lastmod` to 2026-07-28.

## Persona Acceptance

All personas are `RESEARCH_HYPOTHESIS` review lenses.

| Persona | Required page behavior | Implemented surface |
|---|---|---|
| P1 Start-now parent | See the household-material setup before optional detail. | Hero, quick answer, and materials. |
| P2 Constraint-first parent | See no-cut/no-glue boundaries, adult role, clear stop conditions, and rescue options. | Quick Verdict, setup boundary, materials, and troubleshooting. |
| P3 One-test STEM parent | Change one variable and compare without a long lesson. | `#one-change-test`, short prompts, and source links. |
| P4 Rescue-and-stop parent | Recover from slipping, stopping, flying off, or frustration, then stop cleanly. | Setup check, troubleshooting, one-comparison stop line, and cleanup. |
| P5 Pretend-and-extend parent | Switch to free play without completing a test routine. | Free-play route, story options, and related projects. |

## Every-Section Review Map

The independent reviewer must inspect:

1. title, description, canonical, and Article JSON-LD;
2. hero answer and existing image;
3. quick build answer and adult job;
4. Quick Verdict facts;
5. setup boundary;
6. materials and cardboard choice;
7. pre-roll setup check;
8. parent prompts;
9. one-change comparison choices, steps, source links, and Ramp Detective route;
10. troubleshooting;
11. free-play options;
12. child-role invitation and adult role;
13. cleanup;
14. every FAQ answer;
15. related links and footer;
16. sitemap entry.

## Evidence And Human Gates

- GSC page/index rows are `MEASURED`; complete current query rows and clicks
  remain `UNKNOWN`.
- PNC, PEEP, and PBS instructions are `SOURCE_BACKED`.
- Persona fit and the selected structure are `RESEARCH_HYPOTHESIS` and
  `EDITORIAL_JUDGMENT`.
- Parent test, child outcome or quote, setup/play/cleanup timing, engagement,
  safety outcome, developmental outcome, and original-session visual remain
  `UNKNOWN` and prohibited.

## QA Before Review

- `git diff --check`: pass.
- `jq empty ops/seo-roadmap.json`: pass.
- XML parse of `site/sitemap.xml`: pass.
- Standard-library HTML and JSON-LD parse: one H1, one valid Article object,
  correct canonical, and `dateModified` 2026-07-28.
- Repository-local link checker: `missing links 0`.
- Repository-local fragment checker: `missing anchor links 0`.
- Unsupported-claim scan: no old parent-tested, exact-time, age-guarantee,
  cleanup-duration, or universal-safety phrases remain.
- Source checks: PNC, PEEP, and PBS links each return HTTP 200.
- Ramp Detective route: target fragment exists and loads.
- Desktop browser check at 1440x900: no horizontal page overflow, no detected
  text/element overlap, full-resolution hero image loaded, and no console
  errors.
- Mobile browser check at 390x844: no horizontal page overflow or text
  overflow; the comparison choices stack in one column with no overlap.
- The repository has no `tools/seo-qa.mjs`; native standard-library validators
  were used instead.
- Page generators were not run because this is a manual article and the
  current sitemap generator would rewrite every unrelated `lastmod`. The
  existing article entry was updated exactly and XML-validated.

## Production Verification

- Reviewed content commit:
  `a15dca7ceb4f3ead1b518fd0d8e4288a4e051e16`
- GitHub Pages run:
  `30394783721`
- Pages result: success for the exact reviewed SHA.
- Live article: HTTP 200 and byte-identical to the committed HTML.
- Live title, canonical, Article JSON-LD date, direct answer,
  `#one-change-test`, troubleshooting, footer, and removed-claim invariants:
  pass.
- Live desktop and mobile checks: no page-level overflow or text overflow;
  comparison blocks stack correctly; the full-resolution hero image loads.
- Local `main` and `origin/main` aligned at the reviewed content commit after
  push.

Release result: deployed and verified.

## Independent Review

Reviewer: Rawls (`019faa4c-79a3-71f0-a655-4a9949e498de`)

Read-only status: confirmed. The reviewer changed no file, Git state, site,
GSC, indexing state, external account, or deployment.

Cycle 1: `PASS`

Findings:

- `P0`: none.
- `P1`: none.
- `P2`: none.
- `P3`: none.

Persona results:

- P1 Start-now: pass; the direct cardboard/books/car answer precedes optional
  detail.
- P2 Constraint-first: pass; exclusions, adult role, stop conditions, and
  rescue guidance are practical and non-assuring.
- P3 One-test STEM: pass; the optional module limits the parent to one variable
  and one comparison without promising learning.
- P4 Rescue-and-stop: pass; setup checks, troubleshooting, stop language, and
  cleanup are present.
- P5 Pretend-and-extend: pass; free play is an equal route rather than a failed
  experiment.

Every section in the review map passed without a change request. The reviewer
independently confirmed source fidelity, the article/card/Ramp Detective
architecture, metadata/schema, sitemap uniqueness, links/fragments, desktop
and mobile layout, existing-image boundaries, evidence classes, and the
absence of fabricated or overclaimed evidence.

Final result: `PASS`.
