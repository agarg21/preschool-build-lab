# Kid Activity Lab Current Strategy

## Goal

Build Kid Activity Lab into a practical kids activity site that can eventually earn revenue through search traffic, display ads, affiliate links, and/or small digital products.

## Current Focus

Focus first on activities for 3-6 year old kids.

The strategic content bet remains original age-4 STEM. The completed
2026-07-28 decision pack selected the existing cardboard ramp article for one
bounded improvement. The no-cut preschool and age-4 at-home pages remain
observation context, not queued implementation targets.

This is not a pivot away from age-4 STEM. It is a near-term response to early Search Console signal.

## Strategic Bet

The core asset is original, useful activity content: field-tested setup notes, clear parent safety boundaries, kid-facing steps, simple test loops, observations, photos, diagrams, and practical variants.

Activity cards are the utility layer. They should help a parent and child start quickly from one screen.

Video curation is a supporting archive. It can help discover ideas or help parents visualize setup, but it is not the main ranking bet.

## Current Bottleneck

The site does not need many more generic pages right now. It needs stronger evidence and parent usefulness in the current age-4 STEM cluster.

The highest-value input is real testing:

- setup time
- minutes engaged
- exact kid quotes
- what confused the child
- what failed
- what the child changed
- safety or mess surprises
- whether the child asked to repeat it

The validated 2026-07-28 public-safe GSC snapshot shows 72 impressions, no
clicks, 61 discovered pages, and 7 of 7 priority URLs indexed. The cardboard
ramp article has 24 page-level impressions, but complete query rows remain
unavailable. The completed cluster decision pack used current query variants,
SERP samples, ranking-page inspection, five source-traced persona hypotheses,
and direct page audits. A separately authorized 2026-07-28 Semrush US bulk
refresh updated all 17 exact queries. Seven returned numeric volume, ten
returned `n/a` volume, and all returned intent and KD. These remain
`TOOL_ESTIMATE` evidence and reinforce existing-page ownership rather than a
new URL.

The selected ramp improvement is released. Wait for a post-release recrawl and
at least two finalized public-safe comparison points before attributing
movement or selecting another content edit.

## Do Now

1. Observe `KAL-IMP-001` until its post-release recrawl and two finalized
   public-safe comparison points exist.
2. Keep comparing validated GSC snapshots without inferring query intent from
   page rows alone.
3. Test the five activities in
   `site/collections/original-stem-activities-for-4-year-olds.html`.
4. Record real observations through the validated parent-test intake.
5. Upgrade a winning activity only after separate evidence and content review.
6. Use `seo/age-4-keyword-metrics-refresh-2026-07-28.md` as the current paid
   metric layer; do not treat `n/a` as zero or tool estimates as observed KAL
   demand.

## Do Not Do Yet

- Do not publish many thin roundup pages.
- Do not make YouTube or video curation the main product.
- Do not expand into unrelated clusters until the current age-4 STEM cluster has real evidence.
- Do not add affiliate or monetization pages before there is enough trust and useful content.
- Do not make medical, therapeutic, developmental, or safety-sensitive claims beyond practical parent supervision notes.

## Page Decision Rules

Before applying these rules, run the activity-cluster workflow in
`seo/activity-cluster-research-protocol.md`. Page architecture should come from
current query evidence, observed SERP overlap, ranking-page inspection,
source-derived persona hypotheses, current page/section audits, and
evidence/maintenance constraints.

Update an existing page when:

- the search intent overlaps an existing page
- the page is indexed but thin
- Search Console shows impressions but weak click-through or position
- Review Agent finds parent-usability problems
- real testing creates better notes for a current activity

Create a new page only when:

- the intent is distinct
- the page adds real utility beyond a list
- it supports the age-4 STEM or broader 3-6 activity strategy
- there is enough original setup, safety, testing, or observation value

Keep or set a page `noindex,follow` when:

- it is useful for browsing but thin for search
- it has too few cards or weak original notes
- it is mainly a material/tag support page
- it lacks parent-tested evidence

Ask the user before:

- changing domain, brand, navigation, or core positioning
- starting a new content cluster
- spending money on tools, assets, or contractors
- adding affiliate links, ads, or products
- publishing safety-sensitive claims

## Persona Review

Use four to six job-based persona hypotheses derived from current search
modifiers, SERP patterns, recurring parent questions, product constraints, and
validated parent-test evidence when available.

Personas should help answer:

- what useful default belongs in the first screen;
- which secondary parent constraints deserve visible routes;
- where instructions, stop rules, rescue lines, or variants are missing;
- whether a section reduces or adds decision effort.

They are `RESEARCH_HYPOTHESIS` evidence. They are not demographic truth,
parent/child testing, or automatic reasons to create separate pages.

## Operating Model

This Master chat is the current scheduler and command center. The permanent
Master / Operator executes one registered action per transaction and is the
single repository writer for that transaction. The central Control Room remains
configured for future automation but does not schedule Kid Activity Lab while
manual mode is active.

Bounded supporting roles are read-only:

- SEO Research & Review Agent: query/SERP research, persona hypotheses,
  page-architecture analysis, and every-section review.
- Implementation Agent: source/generator, implementation, and QA analysis.
- Operator Review Agent: independent severity-based review of the frozen
  requirements, diff, evidence, and behavior.

Every material change requires native QA and an independent review. P0-P2
findings must be fixed and re-reviewed for at most three cycles. Only `PASS` or
`PASS_WITH_P3` may proceed to an exact-path commit and authorized release.

There is no fixed daily substantive-action or commit limit. Multiple
transactions may run sequentially when each has an explicit action ID, exact
scope, evidence decision, focused commit, and release verification. Separate
actions must not be collapsed into an omnibus change.
