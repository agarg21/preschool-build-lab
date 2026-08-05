# Preschool Indoor Consolidation Implementation Review

- Action: `KAL-IMP-005`
- State: review-clean; focused commit and release pending
- Frozen base: `8751893088e3de56695b92fad513bd2a71559650`
- Writer: permanent Master / Operator chat
- Requested independent reviewer: Averroes
- Reviewer mode: read-only
- Review outcome: cycle one `FAIL`; cycle two `PASS`

## Exact Scope

The registered transaction owns exactly these twenty paths:

1. `scripts/generate_card_pages.py`
2. `scripts/generate_seo_pages.py`
3. `scripts/generate_sitemap.py`
4. `site/index.html`
5. `site/collections/indoor-activities-for-preschoolers.html`
6. `site/collections/rainy-day-activities-for-preschoolers.html`
7. `site/cards/blanket-river.html`
8. `site/cards/tape-city.html`
9. `site/cards/tape-train-tracks.html`
10. `data/seo_keyword_targets.csv`
11. `site/assets/preschool-indoor/indoor-moment-chooser.webp`
12. `site/styles.css`
13. `site/sitemap.xml`
14. `tools/site-architecture.test.mjs`
15. `tools/preschool-indoor-consolidation.test.mjs`
16. `reviews/preschool-indoor-consolidation-implementation-review-2026-08-05.md`
17. `ops/seo-roadmap.json`
18. `ops/seo-roadmap.md`
19. `ops/current-cycle.md`
20. `ops/operator-review.md`

The shared architecture test was registered before editing after its old
every-HTML-is-indexable assumption treated the required canonicalized legacy
redirect as a duplicate indexable page. Its only behavior change excludes
instant-meta-refresh legacy documents from the expected indexable set and
asserts the resulting sixty-URL sitemap.

## Frozen Requirements

- Preserve `/collections/indoor-activities-for-preschoolers.html` as the only
  indexable preschool indoor owner; create no URL.
- Treat rainy day as one context on the indoor owner, not a second generic
  roundup or an unresearched rain-craft owner.
- Replace the old rainy content with a zero-second `meta refresh`, canonical to
  indoor, visible manual link, no `noindex`, no sitemap entry, and no internal
  link.
- Lead with a usable default and chooser by parent moment, space/materials, and
  adult role. Provide bounded start, rescue, stop, and parent checks.
- Remove measured-looking time, mess, and help labels and visible SEO narration.
- State prominently that Kid Activity Lab has not family-tested the setups.
- Label the generated visual as an illustration, not a family-test photo.
- Keep deeper building, standard-deck game, and no-prep jobs on existing URLs.
- Preserve every undeclared generated page byte. Only the three cards that
  linked to rainy may change.
- Do not request indexing or create product, affiliate, external-account,
  tested-status, safety-performance, or parent/child outcome evidence.

## Evidence Boundaries

- August 3 and August 4 GSC aggregate and indexing context is `MEASURED`.
  Candidate page rows, candidate inspections, and complete queries are
  `UNKNOWN`.
- Semrush metrics and six incomplete cached Google samples are
  `TOOL_ESTIMATE`; numeric overlap remains `UNKNOWN`.
- The inspected publisher, education, extension, and Google redirect pages are
  `SOURCE_BACKED` only within the limits stated on the page and in
  `seo/indoor-rainy-consolidation-decision-pack-2026-08-04.md`.
- Personas and the consolidation hypothesis are `RESEARCH_HYPOTHESIS`.
- The seven-route chooser, six starts, exact wording, illustration, internal
  links, and redirect implementation are `EDITORIAL_JUDGMENT`.
- Fit, timing, mess, comprehension, engagement, enjoyment, learning,
  repeatability, frustration, safe use, and every parent/child outcome remain
  `UNKNOWN`.

## Resulting Product

The indoor owner now opens with a soft-sock target default, a prominent
not-family-tested disclosure, an every-child readiness note, and a labeled
1672x941 object-only illustration. Its seven-row chooser separates start-now,
bounded movement, pretend, cause-and-effect, building, larger-floor pretend,
and rule-game jobs by footprint/materials and adult role.

The page gives four reusable adult-support moves and six activity starts. Each
start exposes a child-facing idea, materials, adult setup, three short steps,
smaller rescue, observable stop, local parent check, and a source or deeper
existing route. A rainy-context section rotates movement, making/building, and
quieter jobs while explicitly deferring rain crafts and weather learning.

The rainy document is now a valid accessible fallback with a relative zero-
second redirect to indoor, an absolute indoor canonical, one visible manual
link, one H1, stable navigation, and no `noindex`. The rainy URL is absent from
the keyword owner register, homepage, every generated card route, and sitemap.

## Persona And Every-Section Checklist

| Lens | Required response | Implementation evidence | Pre-review assessment |
|---|---|---|---|
| P1 Start-now parent | Visible default, need, adult role, rescue and stop before a long roundup | Opening sock-roll default; seven-row chooser; six complete starts | Covered |
| P2 Energy in a small space | Defined footprint, soft option, adult position, observable stop, no safety guarantee | Sock lane and secured paper path; global readiness; local movement stops | Covered; reviewer must scrutinize floor, tape, throwing and movement language |
| P3 Quiet reset | Piece/readiness and adult-help boundaries; no independence promise | Tape-road and large-material toy-place routes; every-child note; no independent claim | Covered |
| P4 Rain context | One rotation plan rather than a duplicate page | Rainy-context module plus accessible legacy redirect | Covered |
| P5 Rain-theme maker | Do not promise a rain craft without separate research | Explicitly states rain crafts and weather learning are separate jobs | Covered by boundary, not implementation |
| P6 Game or learning seeker | Bounded game route; do not absorb curriculum intent | Existing standard-deck chooser link; weather learning excluded | Covered |
| Header, hero and opening | Stable navigation, one H1, honest immediate decision | One H1; start, evidence, readiness, image, chooser in that order | Covered |
| Chooser and rainy module | Exact destinations; no hidden measured labels or duplicate ownership | Seven destinations; three rainy rotation links; no time/mess/help tags | Covered |
| Six starts | Distinct job plus setup, steps, rescue, stop and check | Six complete `indoor-start` articles with exact anchors | Covered |
| Deeper routes and sources | Existing owners and visible source limits | Three internal owners; six sources with per-source limit text | Covered |
| Redirect | Permanent fallback semantics and accessible destination | Zero-second refresh, indoor canonical, visible link, no `noindex` | Covered |
| Homepage/cards/sitemap | No internal rainy owner remains | Homepage card removed; exactly three declared card files changed; 60-URL sitemap | Covered |

## Native And Browser QA

| Check | Result before independent review |
|---|---|
| Frozen base and alignment | Clean local/origin base confirmed at `8751893088e3de56695b92fad513bd2a71559650` before registration |
| New GSC evidence | No snapshot newer than `2026-08-04`; prior validated evidence remains current |
| All three generators | Run successfully; complete before/after SHA-1 manifests for `site/**` and the keyword target are byte-identical after the cycle-one fixes |
| Python compilation | All three publishing generators pass `py_compile` |
| Focused tests | Six of six indoor-consolidation tests pass |
| Full repository tests | Thirty-five of thirty-five pass, including an isolated two-date sitemap regression |
| Roadmap JSON | Parses successfully |
| Generated-output isolation | Only the two declared collection files and three declared card files differ from the frozen base; all other generated SEO/card bytes are stable |
| Local links | All local HTML links resolve; zero missing |
| HTML and fragments | Indoor and rainy each have one H1; indoor has twelve unique IDs, no missing fragment targets, and no image without alt text |
| Sitemap | Strict XML parse; 61 to 60 URLs; only rainy removed; only indoor lastmod changes to `2026-08-05` |
| Source availability | Brightwheel, Pre-K Pages, Penn State, Reach All Readers, PBS, and Google redirect guidance return HTTP 200; ParentMap blocks command-line access with 403 but loaded successfully in the independent browser with the intended current title |
| Desktop browser | 1440x1000: one H1, seven chooser links, six starts, loaded 1672x941 image, no page overflow, no section overlap, no console warning/error |
| Mobile browser | 390x844: document width equals viewport; chooser rows stack; all starts are 350px inside the 390px viewport; image loads; no visible-page overflow or backward section order |
| Anchor behavior | Mobile `#sock-target-roll` lands at 111.8px below a 92.9px sticky header |
| Redirect behavior | Local rainy URL automatically lands on the indoor URL and title; fallback source remains directly parseable |
| Local requests | Target HTML, CSS, WebP and redirect requests return 200/304; only the pre-existing site-wide `/favicon.ico` 404 appears |
| Diff hygiene | `git diff --check` passes |
| Exact scope | All twenty registered paths differ; zero paths outside scope |

## Independent Review Cycles

### Cycle One

Independent reviewer Averroes (`019fce24-dbea-7c20-8277-a9ce9ec90623`)
returned `FAIL` with three P2 findings and no P0, P1, or P3 finding:

1. Blanket Toy Crossing said to “step between” supports even though the setup
   was explicitly for the toy rather than feet.
2. The indoor sitemap lastmod used the runtime date, so same-day hashes did not
   prove output stability across future calendar dates.
3. The shared architecture test excluded every meta-refresh document rather
   than allowlisting only the intended rainy legacy path.

The Master replaced the blanket step with the unambiguous toy-only action
“Move the toy along or between the supports” and added positive and negative
regression assertions. Sitemap generation now uses the fixed content-review
date `2026-08-05` for the indoor owner and preserves checked-in dates for other
existing URLs. A temporary-site regression runs the same generator under
`2099-01-01` and `2100-01-01`, proves byte equality, retains the unrelated
root lastmod, retains the indoor `2026-08-05` lastmod, and emits neither future
runtime date. The shared test now allowlists only the exact rainy path, asserts
it is the sole refresh document, and verifies its zero-second indoor target and
canonical.

All thirty-five repository tests, complete generated-output manifests, mobile
browser wording and width, generator compilation, JSON parsing, exact scope,
and `git diff --check` pass after the fixes. Cycle two must inspect the complete
corrected twenty-path diff and close all three P2 findings before release.

### Cycle Two

Averroes returned `PASS`. All three prior P2 findings are closed, and no P0-P3
finding remains. The reviewer independently checked all twenty paths, all six
personas, every changed public section, canonical and query ownership, rainy
redirect semantics, source and evidence limits, generated-output isolation,
image labeling and accessibility, the shared-test correction, 35 passing
tests, JSON and XML parsing, exact scope, responsive evidence, and
`git diff --check`.

The reviewer reconfirmed strict read-only status. Complete GSC queries,
candidate page rows and inspections, recrawl timing, Google canonical choice,
ranking impact, search causality, parent comprehension, and every family or
child outcome remain `UNKNOWN`. Cycle three is limited to verifying that these
final review-state mirrors accurately record the cycle-two verdict; no code,
content, generator, public output, or strategy decision changes after `PASS`.
