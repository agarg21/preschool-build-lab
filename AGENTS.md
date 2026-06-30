# Agent Start Here

This repo is the central workspace for Kid Activity Lab. Use this file first when continuing the project in Codex or another coding/research agent.

## Current Goal

Build Kid Activity Lab into a practical kids activity site that can eventually earn revenue through search traffic, display ads, affiliate links, and/or small digital products.

The current strategic direction is:

- One domain: `kidactivitylab.com`.
- Original/useful content is the core asset.
- Activity cards are the utility layer.
- Video curation is a supporting archive, not the main ranking bet.
- Focus first on activities for 3-6 year old kids, with the strongest current push around age-4 STEM.

## Live Site

- Production URL: https://kidactivitylab.com
- GitHub repo: `agarg21/preschool-build-lab`
- GitHub Pages publishes from `site/` through `.github/workflows/pages.yml`.
- Custom domain and HTTPS are configured in GitHub Pages.

## Where Things Live

- `site/`: generated/static website served by GitHub Pages.
- `scripts/`: generators for card pages, SEO pages, and sitemap.
- `data/`: keyword targets, activity source rows, SERP scoring, and planning CSVs.
- `seo/`: SEO research, content model, opportunity notes, and strategy docs.
- `reviews/`: review-agent prompts and content review cycles.
- `briefs/`: content briefs and field-test packs.
- `weekly/`: weekly operating reviews.
- `templates/`: reusable research/content templates.

## Start Every Work Session

1. Read this file.
2. Read `README.md`.
3. Read `progress.md` for the latest state.
4. Read `seo/content-model.md` before making new pages.
5. Read `reviews/activity-review-agent.md` before doing review-driven content upgrades.
6. Check `data/seo_keyword_targets.csv` before adding SEO pages.
7. If editing generated pages, update the source generator first when possible.

## Publishing Commands

Run these before committing generated site changes:

```sh
python3 scripts/generate_card_pages.py
python3 scripts/generate_seo_pages.py
python3 scripts/generate_sitemap.py
```

Then validate local links:

```sh
python3 - <<'PY'
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urldefrag

class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            href = dict(attrs).get("href")
            if href:
                self.links.append(href)

missing = []
for path in Path("site").rglob("*.html"):
    parser = P()
    parser.feed(path.read_text())
    for href in parser.links:
        if href.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = Path(urldefrag(str(path.parent / href))[0]).resolve()
        if not target.exists():
            missing.append((path.as_posix(), href))

print("missing links", len(missing))
for item in missing:
    print(item)
PY
```

## Content Rules

- Do not create many thin roundup pages.
- Do not make YouTube curation the main product.
- Prefer original field-test packs, parent notes, photos, diagrams, or simple visuals.
- Every activity should have a clear parent safety note.
- Every SEO page should have enough unique utility to deserve indexing.
- Keep videos as references or inspiration unless the page adds substantial original value.
- Original pages may include credited reference videos, but the Kid Activity Lab value must be the simplified setup, safety boundaries, kid-facing steps, test loop, and real observations.

## Current Priority Stack

1. Test the 5 activities in `site/collections/original-stem-activities-for-4-year-olds.html`.
2. Record observations in `briefs/age-4-original-stem-test-pack.md` or a new weekly note.
3. Upgrade winning activities into stronger cards/pages with parent-tested notes and visuals.
4. Submit/monitor pages in Google Search Console.
5. Expand only after the current age-4 STEM cluster has real evidence.

## Important Current Pages

- Original hub: `site/original/index.html`
- Original age-4 STEM test pack: `site/collections/original-stem-activities-for-4-year-olds.html`
- Age-4 STEM page: `site/ages/stem-activities-for-4-year-olds.html`
- Activity card library: `site/cards.html`
- Video archive: `site/video-ideas.html`

## Operational Notes

- HTTPS is configured and enforced through GitHub Pages as of 2026-06-28.
- Sitemap is at `https://kidactivitylab.com/sitemap.xml`.
- The repo intentionally keeps source docs, strategy, data, scripts, and generated site together.
- The site should remain static and simple until traffic justifies more complexity.
- `agy` Antigravity CLI is available locally and can be used for independent read-only content review cycles.
