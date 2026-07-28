# Age-4 Keyword Metrics Refresh

Action: `KAL-RES-002`

Collected: `2026-07-28T21:13:25Z`

Frozen base:
`b17c7a221e350d35878628c737f7af311d1fe3fb`

## Decision

Keep the current page architecture and observation sequence.

The refreshed estimates reinforce the existing age-4 at-home, age-4 STEM,
preschool STEM, and cardboard-ramp URLs. They do not support a new page, a
second ramp URL, or another content edit before the released ramp article's
post-release recrawl and two finalized public-safe comparison points.

## Source And Method

- Source: Semrush Keyword Overview, Bulk Analysis.
- Access: the user's logged-in browser session.
- Database shown: United States (`db=us`), currency USD.
- Database month exposed in result links: `202607`.
- Refresh action: all 17 frozen queries selected and refreshed together.
- Final row status: `Now` for all 17 queries.
- Query universe: the exact 17 phrases in
  `seo/age-4-activity-cluster-decision-pack-2026-07-28.md`.
- Stored output: this source-labeled summary only. No account data or raw
  export is committed.

Semrush values are `TOOL_ESTIMATE` evidence. Volume is Semrush's average
monthly-search estimate; KD is its estimated difficulty of ranking in the top
10; CPC is an advertising estimate. These are not observed KAL demand,
complete GSC query evidence, or parent behavior.

The source displayed `n/a` for ten volume rows and the corresponding CPC rows.
`n/a` is preserved and is not treated as zero. Competitive density, result
count, and a complete comparable SERP export were not retained and remain
`UNKNOWN`.

## Refreshed Query Register

| Theme | Exact query | Intent | US volume | KD | CPC USD | Updated |
|---|---|---|---:|---:|---:|---|
| STEM/preschool | `stem activities for preschoolers` | Informational, Commercial | 1,300 | 16 | 0.66 | Now |
| Ramp/build | `cardboard ramp` | Informational | 210 | 25 | 0.00 | Now |
| Age/context | `home activities for 4 year olds` | Informational | 90 | 4 | 0.40 | Now |
| Age/context | `activities for 4 year olds at home` | Informational | 50 | 23 | 0.40 | Now |
| Ramp/build | `how to make a ramp with cardboard` | Informational | 50 | 15 | 0.00 | Now |
| STEM/age | `stem activities for 4 year olds` | Informational, Commercial | 30 | 5 | 0.88 | Now |
| Age/context | `indoor activities for 4 year olds at home` | Informational | 20 | 9 | 0.15 | Now |
| Ramp/preschool | `cardboard ramp toy cars preschool` | Informational, Commercial | n/a | 17 | n/a | Now |
| Engineering | `engineering activities for 4 year olds` | Informational | n/a | 21 | n/a | Now |
| Engineering | `engineering activities for preschoolers at home` | Informational | n/a | 26 | n/a | Now |
| Constraint | `low mess activities for 4 year olds` | Informational, Commercial | n/a | 12 | n/a | Now |
| Constraint | `no cut preschool activities` | Informational | n/a | 16 | n/a | Now |
| Constraint | `no prep activities for preschoolers` | Informational | n/a | 8 | n/a | Now |
| Ramp/experiment | `preschool toy car ramp experiment` | Commercial | n/a | 19 | n/a | Now |
| STEM/age | `stem activities for 4 year olds at home` | Informational | n/a | 43 | n/a | Now |
| Ramp/experiment | `toy car ramp friction experiment preschool` | Commercial | n/a | 17 | n/a | Now |
| Ramp/rescue | `toy car ramp keeps falling preschool` | Informational | n/a | 33 | n/a | Now |

Coverage:

- 17 of 17 exact queries returned refreshed rows.
- 7 of 17 returned numeric volume and CPC.
- 10 of 17 returned `n/a` volume and CPC.
- 17 of 17 returned intent and KD.
- No close variants are summed.

## Change From The Stale Rows

| Exact query | Stale volume / KD | Refreshed volume / KD | Interpretation |
|---|---:|---:|---|
| `stem activities for preschoolers` | 1,300 / 11 | 1,300 / 16 | Demand estimate is unchanged; difficulty moved up. Existing preschool STEM hub owns the broad job. |
| `cardboard ramp` | 210 / 21 | 210 / 25 | Broad ramp demand remains the largest ramp estimate, but intent is ambiguous. Keep one ramp article. |
| `home activities for 4 year olds` | 90 / 21 | 90 / 4 | Difficulty moved sharply down; the existing age-4 at-home page already owns this job. Treat the volatility directionally. |
| `activities for 4 year olds at home` | 50 / 17 | 50 / 23 | Same volume, higher difficulty. Do not split the at-home job. |
| `how to make a ramp with cardboard` | 50 / 17-18 | 50 / 15 | Same volume, slightly lower difficulty. This supports the released article's existing how-to ownership. |
| `stem activities for 4 year olds` | 30 / 6 | 30 / 5 | Small numeric estimate and low KD remain; the existing age-4 STEM hub owns the broad chooser job. |
| `indoor activities for 4 year olds at home` | UNKNOWN / UNKNOWN | 20 / 9 | A numeric estimate is now available, but it is a modifier within the existing at-home job, not a new-page trigger. |

KD movement is not treated as measured traffic change. It is a tool-model
update and can be volatile, especially at low volume.

## Architecture Assessment

### Existing pages

- `site/articles/cardboard-box-car-ramp-preschoolers.html`: keep and observe.
  The 210-volume broad phrase and 50-volume how-to phrase support one existing
  ramp resource; they do not establish a separate preschool-ramp URL.
- `site/ages/activities-for-4-year-olds-at-home.html`: keep and observe. It
  already owns both 90-volume and 50-volume age-at-home variants, plus the
  20-volume indoor modifier.
- `site/ages/stem-activities-for-4-year-olds.html`: keep as the age-specific
  STEM chooser. The 30-volume phrase does not support another near-duplicate
  page.
- `site/collections/stem-activities-for-preschoolers.html`: keep as the broad
  preschool STEM hub. The 1,300-volume estimate raises the value of this
  existing URL, not a page-production quota.

### Sections or deferred modifiers

- No-prep, no-cut, low-mess, engineering-at-home, ramp-experiment, and
  ramp-rescue variants have refreshed KD but `n/a` volume. They may remain
  sections, filters, research hypotheses, or deferred ideas.
- `n/a` does not prove no demand, but it does not satisfy a standalone-page
  gate.
- Current complete GSC query rows remain `UNKNOWN`, so page-row impressions
  cannot assign these modifiers to a URL.

## Roadmap Recommendation

No implementation is promoted.

1. Keep `KAL-IMP-001` in observation until a post-release recrawl and two
   finalized public-safe comparison points exist.
2. Continue `KAL-MON-001` when a new validated GSC snapshot arrives.
3. Treat the first click or complete query evidence as a new decision gate.
4. Keep parent-tested claims, child outcomes, measured timing, safety outcomes,
   and original visuals human-gated.

The highest-value non-search input remains validated parent-test evidence.
This tool refresh does not create or replace it.
