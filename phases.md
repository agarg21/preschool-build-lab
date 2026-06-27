# Phased SEO Research Plan

## Phase 0: Setup

Status: started on 2026-06-20.

Goals:

- Create the workspace structure.
- Define scoring criteria.
- Define continue, pause, and kill gates.
- Seed the first keyword and niche-score datasets.

Promising enough to continue:

- A niche scores **75+** overall after Phase 1.
- At least 40 plausible long-tail queries exist with clear parent intent.
- At least 10 page templates can be produced quickly by a solo builder.
- Search results show at least occasional small sites, forums, local publishers, Reddit, or niche blogs ranking.
- The user can add firsthand experience, photos, testing notes, or local knowledge.

Pause or kill criteria:

- Results are dominated by medical, legal, institutional, marketplace, or major-media domains.
- The content requires credentials or claims that are unsafe without expert review.
- Search intent mostly wants products, videos, apps, or downloads that are expensive to create.
- The niche cannot support 20-30 useful pages without thin repetition.
- Distribution channels are weak or feel spammy.
- The user cannot personally review, test, or maintain the content.

## Phase 1: Free Exploration

Status: started.

Use only free/manual sources:

- Google search results.
- Google autocomplete-style queries.
- People Also Ask-style questions where visible.
- Google Trends.
- Google Keyword Planner if available.
- Reddit, Quora, parenting forums, Facebook groups, local forums, parenting blogs.
- YouTube and Pinterest content patterns where relevant.

For each niche:

- Generate 75 long-tail Google-style queries.
- Group by intent.
- Estimate search demand qualitatively.
- Estimate competition qualitatively.
- Identify whether small blogs, forums, Reddit, or local sites seem able to rank.
- Identify safety/trust concerns.
- Suggest 10 page templates.
- Suggest 5 non-SEO distribution channels.
- Score from 1-100.

Phase 1 output files:

- [data/keyword_ideas.csv](data/keyword_ideas.csv)
- [data/niche_scores.csv](data/niche_scores.csv)
- [niches/](niches/)
- [recommendation.md](recommendation.md)

Decision gate:

- Continue to Phase 2 if at least one niche scores 75+.
- If two niches score 75+, validate both in Phase 2.
- If no niche scores 75+, refine candidates or narrow the angle before paid tools.

## Phase 2: SERP Validation

For the top 2 niches:

- Review 25 promising queries each.
- Track current top competitors.
- Note if results are dominated by huge domains or if small sites rank.
- Note content gaps.
- Note whether we can produce something meaningfully better.
- Recommend first 20 pages to publish.
- Create article briefs for the best 10 pages.

Manual review fields:

- Query.
- Date reviewed.
- Top ranking domains.
- SERP type.
- Weak-result evidence.
- Content gap.
- Can we beat it?
- Notes.

Use [templates/serp_review.md](templates/serp_review.md) and record structured rows in [data/serp_reviews.csv](data/serp_reviews.csv).

Decision gate:

- Continue if at least one niche has 15+ promising queries where small sites or weak pages are visible.
- Pause if the top 25 queries are dominated by authoritative sites and no differentiated content angle is visible.

## Phase 3: Paid Tool Validation

Do not buy tools by default. Paid tools are justified only after Phase 1 and Phase 2 show promise.

Policy:

- Start with free research.
- If 2 niches score above 75, consider LowFruits or KeySearch first.
- If one niche looks very promising and we are ready to publish 20-30 pages, consider one month of Ahrefs or Semrush.
- Prefer exported CSVs over giving Codex login access.
- Do not buy annual subscriptions at this stage.

Tool roles:

- Ahrefs: competitor pages, backlinks, keyword difficulty, traffic potential, parent topics, content gaps, also-ranks-for style discovery.
- Semrush: broad keyword research, keyword gap, competitor workflows, rank tracking, and newer AI/search visibility workflows.
- LowFruits: weak SERPs, low-authority results, clustering, long-tail opportunity filtering.
- KeySearch: budget keyword research, difficulty checks, rank tracking.
- Screaming Frog: later technical audits after publishing; free crawl may be enough for a small site.

See [data/paid_tool_exports_needed.md](data/paid_tool_exports_needed.md) for exact exports.

Decision gate:

- Buy LowFruits or KeySearch only if manual SERP review shows enough weak SERPs to batch validate.
- Buy Ahrefs or Semrush for one month only when the launch plan is ready and we need competitor/page-level data before publishing 20-30 pages.

## Phase 4: Launch Plan

For the selected niche:

- Recommend first 20-30 pages.
- Create page briefs.
- Define URL structure.
- Define internal linking structure.
- Define Search Console setup checklist.
- Define analytics checklist.
- Define non-SEO distribution experiments.
- Define metrics to review after 3-6 weeks.

Preferred first site shape:

- Static content library.
- Simple filters or comparison tables if helpful.
- No AI chat app.
- Clear by-age, by-time, by-mess, by-material, or by-location navigation depending on niche.

## Phase 5: Post-Launch Feedback Loop

Weekly review data:

- Google Search Console queries.
- Impressions.
- Clicks.
- CTR.
- Average position.
- Pages getting impressions but few clicks.
- Queries ranking positions 8-30.
- Pages needing title, H1, internal-link, intro, or intent improvements.

Weekly process:

1. Export Search Console performance data for the last 7 and 28 days.
2. Identify pages gaining impressions.
3. Identify pages with CTR below expectation.
4. Identify queries in positions 8-30.
5. Improve title/H1/meta for CTR gaps.
6. Add internal links toward pages near page-one rankings.
7. Add missing FAQ sections or comparison tables for query variants.
8. Decide whether to publish, refresh, consolidate, or pause.

