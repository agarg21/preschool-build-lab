# Pivot: From Parent Guides To Kid-Facing Activity Cards

Date: 2026-06-25

## Trigger

The first article was too hard to follow. Even after simplification, long parent-facing project guides do not feel like the scalable wedge.

The reference site, NoSugarForKids, works because it is not primarily a blog. It is a structured catalog:

- Product database.
- Filters.
- Category pages.
- Curated lists.
- Simple rating system.
- Short pages generated from repeatable data.

## New Direction

Build **kid-facing activity cards** for preschoolers.

The parent opens a card. The child can mostly follow the picture and short steps. The parent only needs to check materials and safety.

## Product Shape

Each activity card has:

- Big title.
- One image.
- 3-4 tiny steps.
- Materials shown as short words.
- Parent check box.
- Cleanup note.
- Related cards.

## SEO Shape

Instead of long guides:

- `/cards/cardboard-car-ramp.html`
- `/materials/cardboard.html`
- `/materials/tape.html`
- `/ages/4-year-olds.html`
- `/collections/rainy-day.html`
- `/collections/no-cut.html`
- `/collections/2-minute-activities.html`

## Why This Scales Better

- Cards can be generated from structured data.
- The format is easier to QA.
- The promise is clearer: one screen, one activity.
- The child-facing format creates a stronger product than generic SEO articles.
- Collection pages can target SEO while card pages serve the actual user.

## New Content Standard

A card fails if:

- A parent needs to read more than 30 seconds before starting.
- The child-facing steps use abstract language.
- The activity requires special materials.
- The image looks harder than the real build.
- Safety notes are hidden in prose.

## First Prototype

Created:

- [site/cards.html](site/cards.html)
- [site/cards/cardboard-car-ramp.html](site/cards/cardboard-car-ramp.html)
- [data/activity_cards.csv](data/activity_cards.csv)

## Video Aggregation Layer

Added on 2026-06-26:

- [data/video_activity_sources.csv](data/video_activity_sources.csv)
- [site/video-ideas.html](site/video-ideas.html)

Policy:

- Start with YouTube embeds and source links.
- Use Instagram/Reels links only until the official oEmbed/API path is worth implementing.
- Do not scrape or rehost videos.
- Always preserve source links and avoid implying creator endorsement.
- Translate the idea into our own kid card: materials, age, time, mess, adult help, safety note, and short steps.

## Good-Enough Source List

Added on 2026-06-26:

- Expanded [data/video_activity_sources.csv](data/video_activity_sources.csv) to 51 rows.
- Status breakdown:
  - `adapted`: ready and already turned into a card.
  - `candidate`: likely usable after light review.
  - `review`: interesting but needs safety/simplicity review.
  - `reject`: too complex or not right for this catalog.

This prevents the catalog from becoming a blind video scrape. The source list is an editorial queue.

## SEO Architecture

Added:

- [data/seo_page_plan.csv](data/seo_page_plan.csv)
- [seo/video-card-seo-map.md](seo/video-card-seo-map.md)
- [site/collections/toy-car-activities.html](site/collections/toy-car-activities.html)
- [site/collections/no-cut-preschool-activities.html](site/collections/no-cut-preschool-activities.html)
- [site/materials/cardboard.html](site/materials/cardboard.html)
- [site/materials/painter-tape.html](site/materials/painter-tape.html)

Search-facing pages should be collection and material hubs, not thin one-off articles.

## Link And Indexing Fix

Updated on 2026-06-26:

- Generated 16 real activity card pages from curated video rows.
- Replaced placeholder links that sent collection items back to `video-ideas.html`.
- Added `noindex,follow` to thin hub pages that are useful for browsing but not ready to rank.
- Kept only stronger pages in the sitemap.

Rule:

- A page can exist for users before it is SEO-worthy.
- A page should enter the sitemap only when it has enough unique utility.
