# Kid Activity Lab

Kid Activity Lab is a static decision and utility site for finding interesting
things children can genuinely engage with.

Live site: https://kidactivitylab.com

For future Codex/agent work, start with [AGENTS.md](AGENTS.md).

Current repository status:
[priority pages](status/priority-pages.md) and
[status maintenance convention](status/README.md).

## Current Direction

Kid Activity Lab should be one domain with multiple page types, but one clear
promise: help a parent choose something interesting that fits the child and
the moment, then make it easy to start.

- The engagement lanes are making and experimenting, playing, creating and
  imagining, exploring and discovering, and going deeper.
- At-home, free, low-prep, screen-free, age-specific, and similar modifiers are
  constraints and filters, not the site's mission.
- Original research synthesis, decision support, diagrams, and honestly
  labeled evidence are the core ranking assets.
- Activity and game cards are the quick utility layer.
- SEO collection pages can organize demand by age, interest, energy, time,
  people, setup, location, and cost when the intent is distinct.
- Video curation stays as a supporting archive, not the main product.
- Age-4 STEM remains the strongest existing cluster. The completed and released
  standard-deck card-game chooser is an adjacent Play-lane validation under
  observation, not a site-wide pivot.

The user cannot supply ongoing family tests. Non-product pages may therefore
publish from current source reconciliation, original KAL synthesis or diagrams,
and independent review when they are explicit about untested status and keep
all parent/child outcomes unknown. Product reviews and tested-status claims
still require real firsthand evidence.

## Repo Structure

- `strategy/` contains the current strategic source of truth.
- `agents/` contains role instructions for the manual Codex agent chats.
- `ops/` contains the current-cycle baton, cadence notes, and user-input queue.
- `status/` contains durable page roles, evidence baselines, review and release
  state, blockers, and next eligible actions.
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

The age-4 activity cluster decision pack is complete. It selected one bounded
improvement to the existing cardboard ramp article, and that reviewed change is
now released.

Observe the article until Google recrawls the release and at least two
finalized public-safe comparison points exist. Complete current GSC query rows
remain unavailable. The July 28 decision pack used current query variants,
SERP samples, ranking-page inspection, source-traced persona hypotheses, and
page audits. A separately authorized Semrush US bulk refresh then updated all
17 exact queries: seven returned numeric volume and ten returned `n/a` volume,
with intent and KD available for all. The estimates reinforce existing-page
ownership and do not select another implementation.

The broader 2026-07-29 demand map established four distinct parent jobs:
finding a free activity now, finding a household/no-equipment family game,
choosing a board game worth buying, and finding a game for a standard deck of
cards. `KAL-RES-004` then reconciled current demand, representative SERPs, and
authoritative rules for seven standard-deck games. It supports one future
chooser for Go Fish, Concentration, finite short-form War, Old Maid, and simple
Crazy Eights. `KAL-IMP-002` is now registered and implemented as one
explicitly untested chooser with six original diagrams, frozen starting rules,
and source-versus-editorial labels. Native, structural, link, source, and
responsive browser QA are green. Independent persona/every-section review
closed two bounded correction cycles and returned `PASS` in cycle 3 with no
P0-P3 findings. Commit `3790570` is released through successful exact-SHA
Pages run `30699530311`, and the live chooser byte-matches the reviewed HTML.
No product recommendation is authorized.
