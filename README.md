# Kid Activity Lab

Kid Activity Lab is a static SEO experiment for low-prep kids activities, age pages, and curated activity cards.

Live site: https://kidactivitylab.com

For future Codex/agent work, start with [AGENTS.md](AGENTS.md).

## Current Direction

Kid Activity Lab should be one domain with multiple page types, but one clear promise: practical kids activities parents can run at home.

- Original activity content is the core ranking asset.
- Activity cards are the quick utility layer.
- SEO collection pages organize demand by age, material, and intent.
- Video curation stays as a supporting archive, not the main product.
- The current focus is age-4 STEM activities that can be tested at home and improved with real observations.

## Repo Structure

- `strategy/` contains the current strategic source of truth.
- `agents/` contains role instructions for the manual Codex agent chats.
- `ops/` contains the current-cycle baton, cadence notes, and user-input queue.
- `backlog/` contains SEO, review, implementation, and icebox backlogs.
- `site/` contains the generated static website published to GitHub Pages.
- `scripts/` contains generators for card pages, SEO pages, and the sitemap.
- `data/` contains keyword research, activity source data, page plans, and scoring sheets.
- `seo/` contains SERP validation and content opportunity notes.
- `reviews/` contains review-agent prompts and review-cycle notes for improving content.
- `briefs/`, `templates/`, `weekly/`, and the root markdown files contain strategy, operating notes, and publishing cadence.

## Publishing

GitHub Pages publishes the `site/` directory through the Pages workflow in `.github/workflows/pages.yml`.

Regenerate the site locally with:

```sh
python3 scripts/generate_card_pages.py
python3 scripts/generate_seo_pages.py
python3 scripts/generate_sitemap.py
```

Then commit and push the changed source files and generated files.

## Operating Cadence

Use the three-agent loop in `ops/current-cycle.md`:

1. Master / Operator coordinates strategy, cleanup, child chats, and user decisions.
2. SEO Research & Review Agent validates opportunities and reviews pages for search fit, parent usefulness, and index-worthiness.
3. Implementation Agent ships approved changes and validates the static site.
4. Master / Operator checks child outputs and advances or pauses the cycle.

Agents coordinate through `ops/current-cycle.md`, `backlog/seo-research-review-backlog.md`, and `backlog/implementation-backlog.md`.

## Current Priority

Improve the first GSC-visible pages while continuing to test the original age-4 STEM pack. The current implementation handoff is in `reviews/gsc-visible-page-review-2026-07-09.md`.
