# Master Audit - 2026-07-02

## Purpose

Before creating the multi-agent operating files, the master chat reviewed whether the current site and strategy were clean enough for SEO, Review, and Implementation agents to inherit.

## Findings

- The core strategy is aligned across `AGENTS.md`, `README.md`, `progress.md`, `decisions.md`, and `seo/content-model.md`: one domain, original/useful content first, activity cards as utility, video as support, age-4 STEM as the current focus.
- Some older historical notes still read like current instructions, especially `publish-notes.md`, which still references `preschoolbuildlab.com` and GitHub Pages preview URLs.
- Public pages had some internal/operator language. The most visible issue was `site/original/index.html`, which used phrases like "Content Standard" and "Publishing rule".
- Manual hub pages were missing canonical tags: home, cards index, video archive, no-cut collection, toy-car collection, cardboard material page, and painter-tape material page.
- `site/collections/no-cut-preschool-activities.html` is indexed but was very thin. It needed parent-useful chooser guidance.
- Some noindexed support pages exposed search-operations language such as "not indexed yet"; those pages can stay noindexed without explaining indexing status to parents.
- Local git hygiene needs attention before multi-chat work: the current folder appears to be an untracked snapshot on `main`, and no `origin` remote is configured in this checkout.

## Cleanup Completed

- Rewrote public-facing language on `site/original/index.html` so it reads as a parent hub instead of an internal publishing memo.
- Cleaned homepage copy that described the old long article as "no longer the main product".
- Reframed the video archive copy so it explains parent usefulness while keeping creator attribution.
- Added canonical tags to the manual public hubs and updated the card index generator so `site/cards.html` keeps its canonical after regeneration.
- Added parent-useful chooser copy to the no-cut preschool activities page.
- Replaced visible "not indexed yet" language on support pages with parent-facing browsing copy.

## Remaining Before Agent Setup

1. Fix local git/repo state and create a clean baseline commit.
2. Mark historical docs clearly, especially `publish-notes.md`, so agents do not revive old domain guidance.
3. Decide whether manual hub pages should stay hand-edited or move into generators.
4. Create the operating layer after cleanup: `strategy/`, `agents/`, `ops/`, and `backlog/`.
5. Run generation and link validation before publishing any site changes.
