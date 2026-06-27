# SEO Map For Video-Inspired Activity Cards

Date: 2026-06-26

## Working Thesis

The scalable SEO product is not "one blog post per activity." It is a structured catalog:

- Curated video sources.
- Kid-facing activity cards.
- Material pages.
- Collection pages.
- Age pages.
- A small number of parent-note pages where needed.

This is similar in shape to NoSugarForKids: database first, landing pages second.

## How Pages Show Up In Search

### 1. Collection Pages

Examples:

- `/collections/no-cut-preschool-activities.html`
- `/collections/toy-car-activities.html`
- `/collections/rainy-day-activities.html`
- `/collections/2-minute-activities.html`

Search intent:

- "no cut activities for preschoolers"
- "toy car activities for preschoolers"
- "rainy day activities for 4 year olds"
- "2 minute toddler activities"

Why they can rank:

- They answer a parent constraint directly.
- They can include 8-20 filtered cards.
- They are more useful than a generic list because each item has materials, time, mess, adult help, and safety.

Index rule:

- Index only when the collection has at least 8 strong cards and unique intro/safety notes.

### 2. Material Pages

Examples:

- `/materials/cardboard.html`
- `/materials/painter-tape.html`
- `/materials/paper-cups.html`
- `/materials/paper-rolls.html`

Search intent:

- "cardboard activities for preschoolers"
- "painter tape activities toddlers"
- "paper cup activities for preschoolers"
- "toilet paper roll activities preschool"

Why they can rank:

- Parents often search by what they have nearby.
- Material pages are natural hubs and can collect cards from many creators/sources.

Index rule:

- Index when the material has 8+ cards. Until then, use material pages for internal browsing only.

### 3. Kid-Facing Card Pages

Examples:

- `/cards/cardboard-car-ramp.html`
- `/cards/tape-road.html`
- `/cards/cup-tower.html`

Search intent:

- "cardboard car ramp preschool"
- "tape road activity toddlers"
- "cup tower preschool activity"

Why they can rank:

- Each card has a very specific activity.
- The page is faster to use than a long guide.
- Source attribution and parent safety notes add trust.

Index rule:

- Index tested cards or cards adapted from a strong source where the steps are clear and safe.
- Noindex weak, duplicate, or untested cards until reviewed.

### 4. Video Source Pages Or Video Clusters

Examples:

- `/video-ideas.html`
- `/video-ideas/toy-car-activities.html`
- `/video-ideas/cardboard-activities.html`

Search intent:

- "preschool activity videos"
- "toy car activity videos for kids"
- "cardboard activity videos preschool"

Why they can rank:

- They combine video inspiration with quick parent filters.
- Google's video SEO docs say pages with embedded video should have unique page titles/descriptions and relevant surrounding text.

Index rule:

- Index broad `/video-ideas.html` now.
- Index topic-specific video pages only once there are 8+ good sources.

### 5. Age Pages

Examples:

- `/ages/3-year-olds.html`
- `/ages/4-year-olds.html`
- `/ages/5-year-olds.html`

Search intent:

- "activities for 4 year olds at home"
- "easy activities for 3 year olds"
- "preschool activities for 5 year olds"

Why they can rank:

- Age fit is a real parent filter.
- These pages can group across materials and collections.

Index rule:

- Index when each age page has 12+ cards and clear age-fit guidance.

## What Not To Index Yet

- Thin tag pages with fewer than 8 cards.
- Creator pages unless we have permission or a strong attribution use case.
- One-card collection pages.
- Long parent guides unless they add real testing notes.

## Current Indexing Decision

Updated 2026-06-26:

- Index:
  - homepage
  - `/cards.html`
  - `/video-ideas.html`
  - specific high-confidence card pages
  - `/collections/no-cut-preschool-activities.html` because it now links to 8 real card pages
- Noindex, follow:
  - `/collections/toy-car-activities.html` until it has 8+ real cards and better unique intro/filter copy
  - `/materials/cardboard.html` until it has 8+ real cards and deeper material notes
  - `/materials/painter-tape.html` until it has 8+ real cards and deeper material notes

Reason:

The pages can be useful for browsing before they are worth indexing. `noindex,follow` lets users and crawlers follow links without asking Google to rank a thin hub.

## SERP Appearance

Likely initial search appearance:

- Standard blue-link results with title and snippet.
- Some pages may show video thumbnails if embedded videos are prominent and Google can process them.
- Image thumbnails may appear if card images are strong and descriptive.

Page titles should be plain:

- "No-Cut Preschool Activities: 12 Quick Cards"
- "Toy Car Activities For Preschoolers"
- "Cardboard Activities For Preschoolers"
- "Cardboard Car Ramp Activity Card"

Snippets should emphasize:

- age
- time
- materials
- mess level
- parent safety check

## Technical SEO Notes

- Keep crawlable HTML links between homepage, cards, collections, and materials.
- Add canonical URLs when custom domain is live.
- Keep XML sitemap updated.
- Do not create near-duplicate pages by indexing every tag too early.
- Add structured data later, likely `ItemList` on collection pages and `HowTo` only if we are confident it matches Google's current support and quality guidelines.
- For embedded videos, keep the video visible near relevant text and use unique page titles/descriptions.

## Next Build Steps

1. Expand source list to 100 candidates.
2. Adapt 20 into real cards.
3. Create collection pages for:
   - no-cut activities
   - toy car activities
   - cardboard activities
   - 2-minute activities
4. Keep only strong collection pages indexable.
5. Add Search Console after custom domain is connected.
