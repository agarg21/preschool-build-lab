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

## Operating Model

This Master chat is the current project command center. It selects and executes
one registered action per transaction and is the single repository writer for
that transaction. The central Control Room remains available for future
automation, but its Kid Activity Lab scheduling role is paused during this
manual phase.

Supporting agents operate read-only:

1. SEO Research & Review supplies query/SERP evidence, source-derived persona
   hypotheses, and every-section review.
2. Implementation supplies bounded code and patch recommendations.
3. A different Operator Review Agent independently reviews the frozen diff,
   evidence, behavior, and QA before commit.

Material work proceeds only after `PASS` or `PASS_WITH_P3`, green native QA,
and exact-path verification. The durable queue is `ops/seo-roadmap.json`;
historical child chats and backlogs do not independently set priority.

There is no fixed daily action or commit quota. The Master may run multiple
sequential transactions when each remains independently scoped, reviewed when
material, QA-green, and releasable. Independent actions stay in independent
commits.

Before adding or materially changing an indexable page, use
`seo/activity-cluster-research-protocol.md`. Use
`reviews/persona-review-protocol.md` for substantive research and page review.

## Current Priority

Install the activity-cluster research and persona-review operating model, then
produce a research-only age-4 activity cluster decision pack. Do not select a
content implementation from public-safe page rows alone.
