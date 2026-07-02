# Publish Notes

> Historical note: this file includes early launch and domain notes from before the current `kidactivitylab.com` direction was finalized. For current strategy, use `strategy/current-strategy.md`, `AGENTS.md`, `progress.md`, and `decisions.md`.

## Current Status

One article is publish-ready as a static HTML page:

- [site/articles/cardboard-box-car-ramp-preschoolers.html](site/articles/cardboard-box-car-ramp-preschoolers.html)

It has also been published to GitHub Pages:

- Homepage: https://agarg21.github.io/preschool-build-lab/
- Article: https://agarg21.github.io/preschool-build-lab/articles/cardboard-box-car-ramp-preschoolers.html
- Activity cards: https://agarg21.github.io/preschool-build-lab/cards.html
- First kid-facing card: https://agarg21.github.io/preschool-build-lab/cards/cardboard-car-ramp.html
- Video ideas: https://agarg21.github.io/preschool-build-lab/video-ideas.html
- GitHub repo: https://github.com/agarg21/preschool-build-lab

## 2026-06-25 Pivot

The site has pivoted from long parent-facing guides toward one-screen kid-facing activity cards.

Reference model: NoSugarForKids works because it is a structured catalog with filters, curated lists, and short reusable pages. The analogous model here is a catalog of activity cards, not manually written long guides.

New local files:

- [pivot.md](pivot.md)
- [data/activity_cards.csv](data/activity_cards.csv)
- [site/cards.html](site/cards.html)
- [site/cards/cardboard-car-ramp.html](site/cards/cardboard-car-ramp.html)

## 2026-06-26 Video Inspiration Layer

Added:

- [data/video_activity_sources.csv](data/video_activity_sources.csv)
- [site/video-ideas.html](site/video-ideas.html)

Live:

- https://agarg21.github.io/preschool-build-lab/video-ideas.html

Policy:

- YouTube embeds and source links are okay for the first version.
- Instagram/Reels should start as source links only unless we implement official oEmbed/API handling.
- Do not scrape, download, or rehost creator videos.
- Each source should be translated into our own structured card: materials, age, time, mess, adult help, safety, and 3-4 child-facing steps.

## 2026-06-26 SEO Starter Pages

Added live SEO surfaces:

- https://agarg21.github.io/preschool-build-lab/collections/toy-car-activities.html
- https://agarg21.github.io/preschool-build-lab/collections/no-cut-preschool-activities.html
- https://agarg21.github.io/preschool-build-lab/materials/cardboard.html
- https://agarg21.github.io/preschool-build-lab/materials/painter-tape.html

Local planning files:

- [data/seo_page_plan.csv](data/seo_page_plan.csv)
- [seo/video-card-seo-map.md](seo/video-card-seo-map.md)

Current source list:

- 51 video/activity rows.
- 33 candidate rows.
- 16 review rows.
- 1 adapted row.
- 1 reject row.

## 2026-06-26 Link And Indexing Fix

Fixed:

- Collection/material links no longer all point back to `video-ideas.html`.
- Generated 16 real card pages from curated video rows.
- Added `noindex,follow` to thin browsing pages:
  - toy car activities
  - cardboard material page
  - painter tape material page
- Kept no-cut activities indexable because it now links to 8 real cards.

Live examples:

- https://agarg21.github.io/preschool-build-lab/cards/tape-road.html
- https://agarg21.github.io/preschool-build-lab/cards/cup-tower.html
- https://agarg21.github.io/preschool-build-lab/cards/block-tower.html

## 2026-06-26 Page Strength Tracking

Added:

- [data/page_strength_scores.csv](data/page_strength_scores.csv)
- [seo/how-to-find-strong-pages.md](seo/how-to-find-strong-pages.md)

Rule:

- Strong pages are indexable.
- Browsing pages can exist earlier, but stay `noindex,follow` until they pass the page-strength threshold.

The local site includes:

- [site/index.html](site/index.html)
- [site/styles.css](site/styles.css)
- [site/assets/cardboard-box-car-ramp-hero.png](site/assets/cardboard-box-car-ramp-hero.png)
- [site/robots.txt](site/robots.txt)
- [site/sitemap.xml](site/sitemap.xml)

## Before Public Launch

The working domain is:

- `preschoolbuildlab.com`

This already appears in:

- [site/articles/cardboard-box-car-ramp-preschoolers.html](site/articles/cardboard-box-car-ramp-preschoolers.html)
- [site/robots.txt](site/robots.txt)
- [site/sitemap.xml](site/sitemap.xml)

If another domain is chosen, replace it in those files.

## Suggested Static Hosts

- GitHub Pages: currently active.
- Cloudflare Pages: recommended later if we buy/manage the domain through Cloudflare.
- Netlify or Vercel: also fine for a static site.

## Custom Domain Next Steps

Recommended domain: `preschoolbuildlab.com`

Registry check on 2026-06-21: Verisign WHOIS returned "No match", which means it appears available. Confirm in registrar checkout before buying.

Recommended path:

1. Buy `preschoolbuildlab.com` for 1 year.
2. Use domain privacy if included or cheap.
3. Do not buy add-ons or annual hosting bundles.
4. After purchase, connect it to GitHub Pages or move hosting to Cloudflare Pages.
5. Add the custom domain in GitHub Pages settings.
6. Update DNS records at the registrar.
7. Verify HTTPS.

## First Article To Improve After Real Testing

Test the cardboard ramp with a 4-year-old and add:

- Real photos.
- What worked.
- What failed.
- Exact setup time.
- How long attention lasted.
- Whether tape left residue.
- Which cars worked best.
