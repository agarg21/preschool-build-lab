# Implementation Backlog

The roadmap is authoritative. This backlog supplies implementation context; it
does not independently schedule work. The Master / Operator is the single
repository writer for a validated transaction.

## Ready

- `KAL-IMP-001`: improve only
  `site/articles/cardboard-box-car-ramp-preschoolers.html`.
- Keep the immediate cardboard/books/cars answer and troubleshooting, add one
  optional one-variable test, and remove or relabel unsupported tested,
  duration, child-capability, engagement, cleanup, developmental, and
  safety-outcome language.
- Preserve the article as the ramp build/troubleshooting owner, the card as
  one-screen utility, and Ramp Detective as the deeper test-pack route.
- Do not create a new page, add invented evidence, or broaden other hubs in
  this transaction.
- Generator QA and manual-hub migration remain possible future technical work,
  but must be selected separately rather than bundled into research or content.

## Review Requirement

Every material implementation must use the source-derived personas and
every-section audit from its decision pack, pass native/focused/visual QA as
applicable, and receive a different independent read-only review with no
unresolved P0-P2 findings.

## Next After User Testing

- Add real observations to the age-4 STEM test pack.
- Upgrade the strongest activity card/page with tested notes and visuals.
- Strengthen internal links from age-4 STEM and preschool STEM pages to the tested winner.

## Technical

- Keep canonical tags on all indexable pages.
- Keep noindex support pages out of the sitemap.
- Run generation and link validation before publishing generated site changes.

## Done

- SEO Research & Review Agent rereviewed the three GSC-visible pages after the 2026-07-09 Implementation Agent pass; verdict: pass, no publish-blocking fixes.
- Applied the 2026-07-09 GSC-visible improvement pass:
  - strengthened the cardboard ramp article for `how to make a ramp with cardboard`
  - updated `scripts/generate_seo_pages.py` and regenerated the age-4 at-home page so it routes to the ramp parent guide, original age-4 STEM pack, and age-4 STEM hub
  - enriched the no-cut preschool collection with a constraint chooser, parent boundaries, grouped picks, and internal links while keeping it indexable
  - regenerated card pages, SEO pages, and sitemap; validation reported `missing links 0` and `missing anchor links 0`
- Review Agent completed the 2026-07-09 GSC-visible improvement pass for the cardboard ramp article, no-cut preschool collection, and age-4 at-home hub.
- Differentiated age-4 STEM hub and original-pack metadata to reduce cannibalization risk while keeping both pages indexable.
- Fixed the age-4 STEM hub's original-name/generic-card link mismatch by adding five original-pack activity anchors and changing the matching hub preview links to "Open in original test pack."
- Tightened the repeated Tiny Boat Cargo Test rescue side box after adding its anchor.
- Re-reviewed the age-4 STEM implementation; original pack block, chooser, foil de-emphasis, safety line, and rescue lines passed, but link clarity needs one implementation fix.
- Added a prominent "Start with the original age-4 STEM test pack" block to `site/ages/stem-activities-for-4-year-olds.html`.
- Added a tired-parent chooser to `site/ages/stem-activities-for-4-year-olds.html` with best picks by mess, story hook, movement, water tolerance, and bedtime/calm use.
- Aligned the age-4 STEM hub's strongest activity names/copy with the original pack: Ramp Detective, Bridge Rescue, Shadow Builder, Windproof Tower, and Tiny Boat Cargo Test.
- Removed/de-emphasized foil from the age-4 STEM hub ramp texture row by using towel, paper, or placemat language.
- Added a global "Before you start" safety line and short rescue lines to `site/collections/original-stem-activities-for-4-year-olds.html`.
- Marked `publish-notes.md` as historical so agents do not revive old domain guidance.
- Cleaned public-facing internal strategy language from manual hub pages.
- Added canonical tags to manual hub pages.
