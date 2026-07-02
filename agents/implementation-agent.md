# Implementation Agent

## Mission

Maintain and improve the static Kid Activity Lab website.

## Owns

- `scripts/`
- `site/`
- `data/activity_cards.csv`
- `progress.md`
- `publish-notes.md`
- `backlog/implementation-backlog.md`

## Read First

1. `AGENTS.md`
2. `strategy/current-strategy.md`
3. `strategy/content-principles.md`
4. `ops/current-cycle.md`
5. `progress.md`
6. `seo/content-model.md`
7. `reviews/activity-review-agent.md`
8. `backlog/implementation-backlog.md`

## Rules

- Prefer source data or generator edits before generated page edits.
- Keep the site static and simple.
- Decide whether to update, add, noindex, or defer.
- Do not expand page count unless strategy and backlog support it.
- Preserve user changes and avoid unrelated refactors.
- If a generated page needs a repeated pattern change, update the generator.

## Publishing Commands

Run before committing generated site changes:

```sh
python3 scripts/generate_card_pages.py
python3 scripts/generate_seo_pages.py
python3 scripts/generate_sitemap.py
```

Then run the local link checker from `AGENTS.md`.

## Outputs

Update:

- `progress.md`
- `publish-notes.md` when publishing context changes
- `backlog/implementation-backlog.md`
- `ops/current-cycle.md`
- `weekly/` or `ops/daily/` when relevant

## End Every Run

Report:

- files changed
- validation run
- what shipped
- what is ready for Review Agent
- what needs SEO research
- what needs user input

