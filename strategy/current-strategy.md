# Kid Activity Lab Current Strategy

## Goal

Build Kid Activity Lab into a trusted decision and utility site that helps
parents find interesting things children can genuinely engage with.

The working promise is:

> Find something that fits this child and this moment, then make it easy to
> start.

The site can eventually earn revenue through search traffic, display ads,
affiliate links, and/or small digital products without making monetization the
reason to recommend an idea.

## Current Focus

Focus first on children ages 3-6.

Age-4 STEM remains the strongest existing cluster. The completed 2026-07-28
decision pack selected the existing cardboard ramp article for one bounded
improvement. The no-cut preschool and age-4 at-home pages remain observation
context, not queued implementation targets.

The 2026-07-29 broader demand map established four distinct parent jobs:

1. find a free activity now;
2. find a household or no-equipment family game;
3. choose a board game worth buying;
4. find a game for a standard deck of cards.

The standard-deck card-game lane is the first adjacent implementation
candidate because completed `KAL-RES-004` research found current demand, a
parent-choice gap, and reconcilable public rules without requiring a product
purchase. It is not the site's identity or permission for a generic roundup.
`KAL-IMP-002` is the registered implementation of that candidate. It is
review-clean after green native/responsive QA and independent cycle 3 `PASS`;
reviewed release is pending.

## Strategic Bet

The core asset is trustworthy engagement guidance: useful original research
synthesis, honest evidence labels, and selection help that reduces a parent's
decision effort. Firsthand evidence can strengthen a page if it genuinely
exists, but the project does not assume that the user can supply it.

The site can serve five engagement lanes:

1. **Make and experiment:** builds, science, engineering, tinkering, and
   cause-and-effect play.
2. **Play:** card games, household games, movement games, cooperative games,
   and other repeatable play structures.
3. **Create and imagine:** art, storytelling, pretend play, music, and
   open-ended making.
4. **Explore and discover:** nature, neighborhoods, museums, scavenger hunts,
   observation, and curiosity-led outings.
5. **Go deeper:** substantial projects and carefully evidenced kits, books,
   toys, or resources that support sustained engagement.

At-home, free, low-prep, screen-free, age-specific, and similar modifiers are
constraints and filters. They are not the site's mission.

Activity and game cards are the utility layer. They should help a parent and
child start quickly from one screen.

Video curation is a supporting archive. It can help discover ideas or help parents visualize setup, but it is not the main ranking bet.

## Engagement Model

“Interesting” is a selection goal, not a universal outcome claim. A page can
explain why an idea may fit a particular child or moment, but it cannot promise
engagement, learning, enjoyment, or repetition without real evidence.

Candidate ideas and page sections should make the following useful dimensions
visible when relevant:

- age and readiness;
- interest hook or theme;
- energy level and pace;
- available time;
- parent involvement or independent-play potential;
- number of players and mixed-age fit;
- reading, counting, memory, or rule load;
- setup, materials, space, location, mess, and cost;
- cooperative or competitive structure;
- agency, surprise, challenge, creativity, and replayability;
- a rescue path when the child loses interest or the setup does not work.

The most useful page architecture normally answers five questions:

1. **Hook:** Why might this be interesting to this child right now?
2. **Start:** What does the parent need to begin?
3. **Fit:** Which constraints or readiness signals matter?
4. **Depth:** How can the child vary, repeat, or extend it?
5. **Evidence:** What is sourced, estimated, observed, or still unknown?

## Current Bottleneck

The site does not need many more generic pages. It needs stronger selection
utility and honest evidence in each lane it chooses to enter.

The user cannot run ongoing family tests. The current bottleneck is therefore
producing enough original utility from desk research without laundering
editorial judgment into observed experience. A research-backed page must
reconcile current sources, add a useful KAL chooser or explanatory visual,
state that it is untested when ambiguity is likely, and preserve every
parent/child outcome as `UNKNOWN`.

The validated 2026-08-01 public-safe GSC snapshot has finalized data through
2026-07-30 and shows 90 impressions, no clicks, 61 discovered pages, and 7 of
7 priority URLs indexed. The prior snapshot has 91 impressions and no clicks.
Average position moved from 33.24 to 33.56, while the cardboard ramp article
is unchanged at 31 impressions and 17.32. Complete query rows remain
unavailable, so this small rolling-window movement is monitoring context and
does not alter `KAL-IMP-002` or trigger another implementation.

The selected ramp improvement is released. Wait for a post-release recrawl and
at least two finalized public-safe comparison points before attributing
movement or selecting another content edit.

For commercial board-game or product guidance, the bottleneck is access,
firsthand use, current factual checks, original evidence, and disclosure.
Keyword demand alone is not enough.

## Do Now

1. Release the review-clean `KAL-IMP-002` chooser and verify its exact Pages
   run and production invariants.
2. Preserve its five-game boundary, six original diagrams, frozen starting
   versions, and visible source-versus-editorial labels.
3. After release, observe discovery and search evidence; do not immediately
   create individual game or age pages from the same research.
4. Keep every parent/child outcome unknown and make no claim that KAL ran any
   game.
5. Observe `KAL-IMP-001` without attributing small page-row movement to the
   release or inferring query intent from public-safe rows.
6. Use `seo/age-4-keyword-metrics-refresh-2026-07-28.md` as the current paid
   metric layer; do not treat `n/a` as zero or tool estimates as observed KAL
   demand.
7. Use `seo/at-home-kids-demand-competition-map-2026-07-29.md` and
   `seo/standard-deck-card-game-decision-pack-2026-07-31.md` as the broader
   demand and completed game-decision layers.

## Do Not Do Yet

- Do not publish many thin roundup pages.
- Do not make YouTube or video curation the main product.
- Do not treat the broader promise as an unbounded license to publish generic
  kids content. A new lane needs a distinct engagement job and its own evidence
  gate.
- Do not add affiliate or monetization pages before there is enough trust and useful content.
- Do not publish generic “best” product lists without access, firsthand use,
  current factual checks, original evidence, and disclosure.
- Do not use research-backed activity publishing as a loophole for product
  reviews, tested-status, setup-duration, engagement, learning, repeatability,
  frustration, mess, or safety-outcome claims.
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
- it supports one of the defined engagement lanes for the current age focus
- there is enough original KAL synthesis, decision support, troubleshooting,
  or visual value
- source-backed facts and editorial judgments are distinguishable
- untested status is explicit when a reasonable reader could infer firsthand
  use

Keep or set a page `noindex,follow` when:

- it is useful for browsing but thin for search
- it has too few cards or weak original notes
- it is mainly a material/tag support page
- it lacks current source support, original utility, or a maintainable evidence
  boundary

Ask the user before:

- changing domain, brand, navigation, or core positioning
- starting a new engagement lane or content cluster
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
