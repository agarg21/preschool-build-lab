# GSC Page Indexing Review - 2026-07-18

## Evidence

- Source: authenticated Google Search Console browser report.
- Property: `https://kidactivitylab.com/`.
- Collected: 2026-07-18.
- Report last updated by Google: 2026-07-09.
- Summary: 40 indexed pages and 23 not-indexed URLs across four reasons.
- Newer API baseline: 29 impressions, 61 sitemap URLs discovered, and all 7
  configured priority URLs indexed.

## Exclusion Groups

### Intentional or already corrected

- `Excluded by 'noindex' tag` (1):
  `https://kidactivitylab.com/materials/cardboard.html`. The live page retains
  the intended `noindex,follow` directive and self-canonical. It is a supporting
  material page, not an indexing target.
- `Duplicate without user-selected canonical` (1):
  `https://kidactivitylab.com/index.html`. The live root and `/index.html` now
  both declare `https://kidactivitylab.com/` as canonical. Treat the report as
  stale until Google refreshes it; no code fix or indexing request is due.

### Discovery and quality candidates

- `Discovered - currently not indexed` (18): two age pages, five activity
  cards, nine collection pages, `/original/`, and Google's verification HTML
  file. Google had not crawled these URLs as of the report. The verification
  file is not content and should not be indexed.
- `Crawled - currently not indexed` (3):
  `cards/color-mixing-cups.html`, `cards/sink-or-float-tray.html`, and
  `cards/shadow-shape-match.html`. Each returns `200`, has a self-canonical,
  appears in the sitemap, and has multiple internal links. The pages are short,
  generic activity cards, so this is a content-value or consolidation question,
  not an identified technical defect.

The complete discovered group observed in GSC was:

- `ages/activities-for-5-year-olds-at-home.html`
- `ages/activities-for-6-year-olds-at-home.html`
- `cards/car-ramp-distance-test.html`
- `cards/pom-pom-drop.html`
- `cards/straw-bridge.html`
- `cards/tape-train-tracks.html`
- `cards/wind-tower-test.html`
- `collections/building-activities-for-4-year-olds.html`
- `collections/fine-motor-activities-for-preschoolers.html`
- `collections/independent-activities-for-preschoolers.html`
- `collections/indoor-activities-for-preschoolers.html`
- `collections/math-activities-for-4-year-olds-at-home.html`
- `collections/no-prep-activities-for-preschoolers.html`
- `collections/no-prep-stem-activities-for-4-year-olds.html`
- `collections/rainy-day-activities-for-preschoolers.html`
- `collections/science-experiments-for-4-year-olds.html`
- `googled495b3fc6f0765f8.html`
- `original/`

## Decision

Do not bulk-request indexing and do not create a blanket technical-fix project.
The current site signals are healthy for the configured priority set. On a
fresh changed report, reconcile the stale canonical/noindex groups, then select
at most one strategically important page for a utility improvement,
consolidation, or intentional exclusion. Favor `/original/` or an
evidence-bearing age-4 STEM page; never invent parent-test evidence to make a
thin card look differentiated.
