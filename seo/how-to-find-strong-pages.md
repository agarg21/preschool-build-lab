# How To Find Strong Pages

Date: 2026-06-26

## Definition

A strong page is a page we are comfortable asking Google to index because it has enough unique utility for a searcher.

Strong pages usually have:

- Clear search intent.
- Specific title and H1.
- Real internal links that go to useful pages.
- Enough unique content beyond a list of links.
- No placeholder links.
- A parent safety check when the activity needs one.
- Card depth: usually 8+ cards for collection/material pages.

## Scoring Rubric

Score each page out of 100:

- Search intent clarity: 20
- Unique usefulness: 20
- Card/link depth: 20
- Trust/safety/source quality: 15
- UX clarity: 15
- SEO hygiene: 10

## Indexing Rules

Index now:

- Specific card pages with clear steps and source attribution.
- Collection pages with 8+ real card links and unique guidance.
- Library/video index pages that help users discover cards.

Noindex, follow:

- Thin collection pages with fewer than 8 real card links.
- Material pages with fewer than 8 real card links.
- Pages that are useful for browsing but not yet strong enough to rank.

Do not publish/index:

- Duplicate card variants.
- Unsafe activities.
- Creator pages without a clear reason.
- Pages where most links are placeholders.

## Current Stronger Pages

See [../data/page_strength_scores.csv](../data/page_strength_scores.csv).

Current stronger pages:

- `/cards.html`
- `/video-ideas.html`
- `/collections/no-cut-preschool-activities.html`
- `/cards/cardboard-car-ramp.html`
- `/cards/tape-road.html`
- `/cards/cup-tower.html`

Current noindex pages:

- `/collections/toy-car-activities.html`
- `/materials/cardboard.html`
- `/materials/painter-tape.html`

## How To Find More Strong Pages

1. Sort `data/video_activity_sources.csv` to find clusters with 8+ candidate rows.
2. Turn the safest candidates into real card pages.
3. Create or upgrade the matching collection/material page.
4. Check that every card link goes to a real card page.
5. Add unique guidance to the hub page.
6. Remove `noindex` and add the URL to the sitemap only after the page passes the threshold.

