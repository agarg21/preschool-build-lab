# Activity Cluster Research And Page-Decision Protocol

State: reusable operating protocol

Last updated: 2026-07-28

Use this protocol before creating or materially changing an indexable activity,
age, collection, material, card, or parent-guide page. Search research is
product input, not a keyword-to-page factory.

## Differentiation Thesis

Kid Activity Lab should not try to win through page volume, generic activity
lists, unsupported developmental claims, or invented parent experience. Its
durable edge is a calm activity-running product:

- current, source-dated search and competitor research;
- fast parent setup and read-aloud kid steps;
- concrete mess, supervision, stop, and rescue boundaries;
- useful default routes for common parent constraints;
- validated parent-test observations and original visuals when they exist;
- explicit unknowns when they do not.

Desk research may improve structure, instructions, sourcing, and decision
support. It may not create a parent-tested claim, child quote, engagement
result, safety finding, photo, or firsthand observation.

## Required Inputs

- `AGENTS.md`, both roadmap mirrors, `ops/current-cycle.md`, and
  `ops/needs-user.md`.
- The latest and prior validated public-safe GSC snapshots.
- Current pages, generators, source data, and relevant briefs/reviews.
- Existing keyword targets and named SEO research.
- Representative current SERP inspection for every material query family.

Optional:

- Semrush, DataForSEO, or another named keyword source. Paid/API usage requires
  the project's explicit budget authorization.
- Protected GSC query evidence through its approved private workflow.
- Parent/community discussions as qualitative question discovery only.
- Validated parent-test intake supplied by the user.

Mark unavailable evidence `UNKNOWN`. Do not infer query intent from public-safe
page rows alone, treat unavailable metrics as zero, or sum overlapping keyword
variants as unique demand.

## Evidence Classes

| Class | Meaning | Permitted use |
|---|---|---|
| `MEASURED` | GSC, index state, validated parent-test intake, or another first-party measurement | State exactly what was measured with date and scope. |
| `TOOL_ESTIMATE` | Semrush, DataForSEO, autocomplete, or another named research tool | Directional prioritization with source, market, and date. |
| `SOURCE_BACKED` | Current official, primary, or clearly attributed external source | Factual setup/material/context support within the source's limits. |
| `RESEARCH_HYPOTHESIS` | Inference from queries, SERPs, community questions, or editorial analysis | Persona, page, or product hypothesis that still needs testing. |
| `EDITORIAL_JUDGMENT` | KAL's bounded recommendation or structural decision | Use with an explicit rationale; never present as measured behavior. |
| `UNKNOWN` | Evidence is absent, incomplete, stale, or unavailable | Preserve the gap; do not silently fill it. |

`VALIDATED_PARENT_TEST` is a subtype of `MEASURED`. It exists only after a real
intake passes `ops/validate_parent_test_evidence.py` and receives separate
content review.

## Workflow

### 0. Open The Transaction

- Confirm whether the action is a validated Control Room dispatch or a direct
  manual user instruction.
- Reconcile local `main` with `origin/main`, preserving unrelated dirty work.
- Record one action ID, transaction type, exact paths, evidence classification,
  and human/observation gates before substantive edits.
- Stop on invalid lease, divergence, overlapping dirty work, or a missing
  permission or real-world evidence gate.

### 1. Define One Activity Cluster

Start with one coherent parent job, normally an existing cluster. For the
current strategy, the first cluster is age-4 at-home/STEM and its closest
constraint-led pages.

Sample query families when evidence exists:

- age and context: age 3, 4, 5, preschool, at home;
- activity job: STEM, science, engineering, building, art, sensory, movement;
- parent constraint: no prep, low prep, low mess, no cut, indoor, rainy day,
  household materials, short activity;
- material or object: cardboard, tape, toy cars, blocks, paper;
- execution: how to make, setup, steps, what to say;
- failure/rescue: slipping, falling, not working, child loses interest;
- extension: easier, harder, repeat, compare, test, variation.

Record the exact query, likely job, source, market, collection date, and metric
availability.

### 2. Validate Keywords

For every selection-driving query, preserve:

- exact phrase;
- US monthly volume, KD, CPC, and intent when available;
- named source/tool and collection date;
- `0`, `n/a`, and `UNKNOWN` as distinct values;
- overlap warning for close variants.

Use a small, capped research batch. Save reusable raw exports only when their
license, privacy, and repository rules allow it.

### 3. Cluster By Observed SERP Overlap

Similar wording does not prove one page. For every retained SERP sample record:

- search provider/product and database or snapshot date when exposed;
- exact query, country/market, locale/language, device, and collection time;
- requested organic result depth and actual retained organic row count;
- whether the retained sample is complete at that depth;
- ordered organic rank, exact URL, normalized domain, and page/result type;
- omitted, errored, or unretained rows without treating them as absent results;
- separately observed SERP features such as AI summaries, maps, videos, forums,
  and PAA.

For representative query comparisons record:

- recurring exact ranking URLs;
- recurring domains when exact URLs differ;
- page and result types;
- SERP features;
- user job;
- overlap rationale and confidence.

Numeric overlap is allowed only when both samples use the same provider,
market, locale/language, device, requested organic depth, and a reasonably close
collection window, and both retain complete ordered organic sets at that
depth.

For each eligible comparison preserve:

- `|A|`, `|B|`, exact intersection count, and exact union count;
- exact-URL Jaccard overlap: `|URL_A intersect URL_B| / |URL_A union URL_B|`;
- domain intersection, union, and domain Jaccard calculated separately;
- page-type overlap as a qualitative observation, not merged into either
  numeric result.

If either sample is incomplete or not comparable, numeric exact-URL and domain
overlap are `UNKNOWN`. Retained recurrences may still be described
qualitatively with their limitations.

### 4. Inspect Ranking Pages

Inspect a representative mix: authoritative publishers, small independent
sites, official or educational sources, forums/community results, videos, and
pages that rank despite modest apparent authority.

For each page record:

- what it answers well;
- what is hard to scan, compare, trust, or run;
- firsthand, professional, community, or authority advantages KAL cannot copy;
- product opportunities KAL can honestly pursue;
- freshness and evidence limitations.

### 5. Derive Persona Hypotheses

Create four to six job-based persona hypotheses from query modifiers, recurring
parent questions, ranking-page gaps, product constraints, GSC evidence, and
validated parent-test evidence when available.

For each persona record:

- job to be done;
- activity context;
- evidenced child-age or pace constraint;
- anxieties;
- decision criteria;
- failure mode;
- evidence links;
- pages or sections that serve the job.

Personas are research hypotheses and review lenses. They are not demographic
truth, parent-test evidence, or automatic reasons to create pages.

### 6. Audit Every Relevant Page And Section

At page level record:

- URL/path and primary job;
- current index/GSC state;
- query cluster and personas served;
- strengths and missing decision support;
- evidence and trust gaps;
- internal-link and cannibalization risk;
- verdict: keep, improve, consolidate, observe, noindex, or retire.

For a page being considered for implementation, inspect every visible block:
hero, intro, chooser, cards, instructions, safety/mess text, stop/rescue text,
tables, variants, FAQs, sources, and related links. Mark each block keep,
compress, merge, move, replace, or remove.

### 7. Decide Page Architecture

- **Standalone page:** distinct recurring SERP, distinct user job, meaningful
  demand or value, sufficient evidence depth, and a maintenance path.
- **Existing-page improvement:** shared job/SERP with a current page or current
  GSC discovery on the appropriate URL.
- **Section/module:** useful constraint with blended SERPs or modest demand.
- **Filter/helper:** valuable refinement without evidence of standalone intent.
- **Noindex/support:** useful browsing surface that lacks unique search value.
- **Defer:** evidence, trust, testing, visual, or freshness burden is unresolved.

A query modifier and a persona do not automatically deserve an indexable URL.

### 8. Promote At Most One Implementation

Prefer one existing evidence-bearing page. Define:

- primary target URL;
- exact paths and generated-output boundary;
- retained/deferred candidates or sections;
- persona acceptance criteria;
- search/cannibalization acceptance criteria;
- evidence and human-review limits;
- focused, full, visual, privacy, and source QA;
- release invariant and measurement plan.

Research-only transactions do not edit `site/**` or generator paths.

## Required Decision-Pack Output

- decision and one promoted action, or a verified no-op;
- evidence classification and freshness;
- query universe and exact keyword register;
- SERP samples and overlap map;
- representative ranking-page analysis;
- source-traced persona hypotheses;
- every-page inventory and section audits for implementation candidates;
- page architecture map;
- claim/human-review boundaries;
- acceptance criteria, measurement plan, and unresolved evidence gaps.

Use `templates/activity-cluster-decision-pack.md`. Every material research or
strategy pack requires a different independent read-only reviewer before it can
be committed.
