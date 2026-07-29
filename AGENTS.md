# Agent Start Here

This repo is the central workspace for Kid Activity Lab. Use this file first when continuing the project in Codex or another coding/research agent.

## Current Goal

Build Kid Activity Lab into a trusted decision and utility site that helps
parents find interesting things children can genuinely engage with. The site
can eventually earn revenue through search traffic, display ads, affiliate
links, and/or small digital products without making monetization the reason to
recommend an idea.

The current strategic direction is:

- One domain: `kidactivitylab.com`.
- One promise: help a parent choose something that fits the child and the
  moment, then make it easy to start.
- Original, useful content and honestly labeled firsthand evidence are the core
  assets.
- The main engagement lanes are making and experimenting, playing, creating
  and imagining, exploring and discovering, and going deeper through
  substantial projects or carefully evidenced resources.
- At-home, free, low-prep, screen-free, and age-specific are useful constraints
  and filters, not the site's mission.
- Activity and game cards are the utility layer.
- Video curation is a supporting archive, not the main ranking bet.
- Focus first on children ages 3-6. Age-4 STEM is the current firsthand-evidence
  wedge, not a permanent boundary for the site.

## Live Site

- Production URL: https://kidactivitylab.com
- GitHub repo: `agarg21/preschool-build-lab`
- GitHub Pages publishes from `site/` through `.github/workflows/pages.yml`.
- Custom domain and HTTPS are configured in GitHub Pages.

## Where Things Live

- `strategy/`: canonical current strategy, content principles, and monetization path.
- `agents/`: current charters for the Master / Operator and bounded read-only
  research, implementation, and independent review roles.
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
10. Read `seo/activity-cluster-research-protocol.md` before creating or
    materially changing an indexable page.
11. Read `reviews/persona-review-protocol.md` before substantive page or
    research review.
12. If editing generated pages, update the source generator first when possible.

## Agent Roles

- Master / Operator: uses `agents/master-operator.md`; operates this chat as
  the current project command center, executes one registered action per
  transaction, and is the single project-repository writer for that
  transaction.
- SEO Research & Review Agent: uses `agents/seo-research-review-agent.md`;
  provides bounded read-only research and persona/every-section review.
- Implementation Agent: uses `agents/implementation-agent.md`; provides
  bounded read-only code and patch analysis.
- Operator Review Agent: uses `agents/operator-review-agent.md`; independently
  reviews the frozen diff and evidence without editing.

This Master chat is the current scheduler and command center. The central
Control Room is retained for future automation but is not scheduling Kid
Activity Lab while manual mode is active. Supporting agents do not own
priority, update project state, or write the shared checkout. Historical
`agents/seo-research-agent.md`, `agents/review-agent.md`, and old role backlogs
remain archive evidence only.

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
- Use source-derived parent-job personas as review lenses, not as fictional
  testimonials or automatic reasons to create pages.
- Keep `MEASURED`, `TOOL_ESTIMATE`, `SOURCE_BACKED`,
  `RESEARCH_HYPOTHESIS`, `EDITORIAL_JUDGMENT`, and `UNKNOWN` evidence distinct.
- Keep videos as references or inspiration unless the page adds substantial original value.
- Original pages may include credited reference videos, but the Kid Activity Lab value must be the simplified setup, safety boundaries, kid-facing steps, test loop, and real observations.
- Make the interest hook and important parent constraints visible without
  promising that every child will engage, enjoy, learn from, or repeat an idea.
- Product recommendations require access to the product, firsthand use,
  current factual checks, original evidence, and clear disclosure before they
  can become an implementation lane.

## Current Priority Stack

1. Test the 5 activities in `site/collections/original-stem-activities-for-4-year-olds.html`.
2. Record observations in `briefs/age-4-original-stem-test-pack.md` or a new weekly note.
3. Upgrade winning activities into stronger cards/pages with parent-tested notes and visuals.
4. Run `KAL-RES-004` as a research-only test of the adjacent standard-deck
   card-game lane. It is a validation lane, not the site's identity.
5. Monitor pages in Google Search Console. Do not request indexing unless a
   separate explicit instruction authorizes it.
6. Expand only when a candidate serves a distinct engagement job and satisfies
   its research and firsthand-evidence gates.

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

## Manual Master Chat And Future Automation

- This project is enrolled in the central Control Room at `/Users/apoorvagarg/Documents/SEO Agent/seo-lab/operator/`.
- Control Room scheduling is paused for Kid Activity Lab while this Master chat
  operates the project manually. Do not write the central dispatch ledger or
  treat a central report as current authority unless the user explicitly
  re-enables automation or supplies a valid dispatch.
- First read this repository's local `ops/operator.json`,
  `ops/seo-roadmap.json`, `ops/seo-roadmap.md`, and
  `ops/portfolio-operator.md`. The local roadmap is authoritative during
  manual mode.
- The rolling roadmap is the durable execution queue. Historical role chats and role-specific backlogs remain supporting evidence rather than independent priority setters.
- For a direct manual user instruction, the Master must register one action and
  exact paths in the roadmap before substantive edits. If automation is later
  re-enabled and a Control Room dispatch arrives, validate its lease and
  immutable contract before reading or writing project state.
- Every material strategy, research, code, content, or configuration change
  requires native QA and a different independent read-only reviewer. Fix P0-P2
  findings for at most three cycles; only `PASS` or `PASS_WITH_P3` may proceed.
- The user granted standing reviewed-release authorization on 2026-07-17 and
  removed the fixed daily substantive-action and commit cap on 2026-07-28. The
  Master may run multiple sequential transactions when each has one registered
  action, exact scope that does not overlap another active transaction or
  unrelated dirty work, green native QA, required independent review, and a
  focused commit. Do not combine unrelated actions merely to reduce commit
  count. After each push, verify local/origin alignment and, when site or
  workflow paths changed, the native Pages run and action-specific production
  invariants. Stop on remote divergence or a production regression whose
  rollback scope is ambiguous.
- GitHub Actions collects a normalized public-safe GSC snapshot daily. At run start, validate and compare every new snapshot with the prior snapshot and `ops/seo-roadmap.json`. The first snapshot establishes a baseline and cannot satisfy a changed-evidence gate. New data may unlock or reprioritize an item, but an unchanged healthy snapshot is housekeeping and should produce a no-op rather than manufactured work.
- Never commit GSC credentials, complete raw query exports, country/device rows, or user data. Treat Semrush as optional enrichment; GSC API evidence is the unattended first-party measurement source.
- Sensor cadence is not a page-production quota. Healthy unchanged evidence
  should still produce a no-op rather than manufactured work.
- Never invent parent-test observations, child quotes, photos, engagement data, or tested status to unblock an autonomous run.
- Personas derived from queries, SERPs, or community questions are
  `RESEARCH_HYPOTHESIS` evidence. They never satisfy the parent-test or child
  safety human gates.
