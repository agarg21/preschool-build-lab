# Kid Activity Lab

Kid Activity Lab is a static SEO experiment for low-prep kids activities, age pages, and curated activity cards.

Live site: https://kidactivitylab.com

## Repo Structure

- `site/` contains the generated static website published to GitHub Pages.
- `scripts/` contains generators for card pages, SEO pages, and the sitemap.
- `data/` contains keyword research, activity source data, page plans, and scoring sheets.
- `seo/` contains SERP validation and content opportunity notes.
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

1. Review and publish new pages.
2. Monitor pages already live in Google Search Console.
3. Review strategy weekly and decide which page cluster to expand next.
