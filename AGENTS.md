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

- `strategy/`: canonical current strategy, content principles, and monetization path.
- `agents/`: role charters for the Master Operator, SEO Research Agent, Review Agent, and Implementation Agent.
- `ops/`: current-cycle baton, cadence, daily logs, and user-input queue.
- `backlog/`: SEO, review, implementation, and icebox backlogs.
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
2. Read `strategy/current-strategy.md`.
3. Read `ops/current-cycle.md`.
4. Read the relevant role file in `agents/` if this is a role-specific chat.
5. Read `README.md`.
6. Read `progress.md` for the latest state.
7. Read `seo/content-model.md` before making new pages.
8. Read `reviews/activity-review-agent.md` before doing review-driven content upgrades.
9. Check `data/seo_keyword_targets.csv` before adding SEO pages.
10. If editing generated pages, update the source generator first when possible.

## Agent Roles

- Master Operator: uses `agents/master-operator.md`; coordinates the loop and resolves strategy/process questions.
- SEO Research Agent: uses `agents/seo-research-agent.md`; owns research, keyword targets, briefs, and SEO backlog.
- Review Agent: uses `agents/review-agent.md`; owns parent-usability reviews and implementation-ready fixes.
- Implementation Agent: uses `agents/implementation-agent.md`; owns website changes, generators, validation, and publishing notes.

Agents coordinate through repo artifacts, especially `ops/current-cycle.md` and the files in `backlog/`. Each role-specific run should read the baton first and update it last.

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
- `publish-notes.md` contains historical launch notes and may reference old GitHub Pages preview URLs or earlier domain ideas. Prefer `strategy/current-strategy.md`, `progress.md`, and `decisions.md` for current direction.

## Central Control Room Pilot

- This project is enrolled in the central Control Room at `/Users/apoorvagarg/Documents/SEO Agent/seo-lab/operator/`.
- Read `ops/operator.json`, `ops/seo-roadmap.json`, `ops/seo-roadmap.md`, and `ops/portfolio-operator.md` before selecting operator work.
- The rolling roadmap is the durable execution queue. Historical role chats and role-specific backlogs remain supporting evidence rather than independent priority setters.
- During the proving period through 2026-07-19, the operator may create one exact-path, independently reviewed, QA-green commit per day. Push and deployment still require user approval.
- A two-hour scan is a sensing cadence, not a page-production quota. Healthy unchanged runs should stop as no-ops.
- Never invent parent-test observations, child quotes, photos, engagement data, or tested status to unblock an autonomous run.
