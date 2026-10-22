# Card-Finder Match And Recovery Repair - October 22, 2026

Action `KAL-IMP-035`; base `af429ff4f5a7c9601a9c1859f44bc647c496e444`. **IMPROVE the existing `cards.html` finder only.** No new activity, URL, product recommendation, or claim of family use.

## Frozen Task And Evidence

The [October 21 production audit](card-finder-no-match-recovery-audit-2026-10-21.md) retained four current public questions and source limits from the [water-painting qualification](../seo/pavement-water-painting-guide-discovery-2026-10-21.md). They support a `RESEARCH_HYPOTHESIS` caregiver of an approximately four-year-old considering water/brush outdoor marks. Younger-child access to a water container, divided attention, and hot pavement are secondary stresses, not observations of this setup. The adult needs (1) a truthful `water paint` result count, (2) a relevant existing same-material start or an honest decline, (3) a way to revise/reset without a false equivalent, and (4) no unrelated route presented as the answer. Success is choosing an appropriately evidenced card **or declining/resetting** on this surface; failure is a false-positive card, unrelated detour, or another broad search. This is a proxy task, not a parent trial.

`MEASURED` technical baseline on October 21: `water paint` 0/36, but `paint` matched Tape Road, Tape City, and Measuring Tape Jumps through the substring `painter`; the sole zero-state link pointed to a separate standard-deck game chooser. `SOURCE_BACKED` public questions and Illinois/Purdue/AAP limits are only as characterized in those dated artifacts; they do not certify a home activity. Word-boundary semantics and reset-first wording are `EDITORIAL_JUDGMENT`. Demand, family comprehension, physical safety, duration, mess, engagement, learning, and causal SEO effect are `UNKNOWN`.

## Change And Claim Boundary

The source-owned library generator now serves `assets/cards-finder.js?v=2` and an honest no-match message: try another title/material or use Clear to see all cards; the standard-deck chooser is framed as a *different* card-game job. The script tokenizes literal title/material text and the query into Unicode letter/number words, equates simple singular/plural forms and possessive `s`, then requires every normalized query word to be present. It does not stem `painter` into `paint` or make a semantic/age recommendation. The generated `site/cards.html` and sitemap `cards.html` lastmod change; no card body, metadata inventory, styling, data, or other site page changes. Version bump prevents a cached substring script from running against the revised copy.

## Same-Task Browser Result

Local generated page in headless Chrome at 1280x900, 390x844, 320x760 and 320x844 with injected 32px root text: `water paint`, `paint`, and `brush` each return **0 of 36 activity cards**, no visible grid links, and the reset-first message. Both `painter tape` and `painter's tape` return exactly Tape Road, Tape City and Measuring Tape Jumps; `paper tape` returns Paper Chain Test; `cup` returns three, `block` eight, `bowl` Spoon Transfer and `container` Sound Shaker Match. `water` returns the same five distinct water-material jobs as before, without claiming equivalence; `cardboard` returns three. A follow-up local Chrome check after normalization confirms `cars` returns five, correcting the initial exact-word two-card count. `deck` returns zero *activity cards* while the separate chooser link works. Clear by keyboard Enter returns all 36 and focus to the searchbox; chooser click and Back work. With JavaScript disabled at390, controls stay hidden and all36 static links remain. All checked modes have one H1, the same canonical, document width equal to viewport and no sampled page errors. Jump by keyboard Enter lands the heading below the sticky header at1280/390/320; named label, polite status and button type were checked. Desktop, normal320 and 320/root32 screenshots were visually inspected: controls/count are readable and no text overlaps; the separate chooser link extends below first view at320, while Clear is already visible. Root32 is text-size injection, not universal zoom or screen-reader evidence.

No claim is made that a water/brush start now exists. The successful answer for this persona is an honest decline/reset, not another activity substituted by the finder. Search is literal title/material words with narrow common-inflection equivalence, not a full language stemmer; reconsider on an important demonstrated false negative or false positive, not an invented prevalence claim.

## Every-Section Review

| Visible block | Task value and evidence | Verdict |
|---|---|
| Header, hero, early jump | Identifies library; jump remains before promotion. Tested canonical/H1 and width. | Preserve. |
| Standard-deck promotion | Distinct one-deck choice, not mark-making recovery. | Preserve separately. |
| Two long-guide links | Different paper jobs; no claim of same-material substitution. | Preserve. |
| Finder label, input, Clear, polite count | Named controls, whole-word literal search, visible truthful count and keyboard reset. | Improve matching; preserve owner and focus. |
| No-match text/link | Clear/revise is the first action; chooser explicitly for a card game instead. At root32 the link needs scrolling. | Improve hierarchy; retain distinct route. |
| 36-card grid | Static links remain without JS; word search hides only non-matches. | Preserve all direct owners. |
| Footer | General parent-check wording unchanged; no new task claim. | Preserve. |
| Destination chooser | Link/Back work; never counted as the art answer. | Preserve separately. |

## Persona Proxy And Critical Gate

All **13/13** dimensions apply, N/A none. Same recovery-task `EDITORIAL_JUDGMENT` proxy after repair: answerability2 (honest decline/reset); age/ability0 (no matching activity); materials/substitutions2 (does not mislabel tape as paint); setup/duration/cleanup0 (no fitting card to start); adult involvement0; setting/space0; mixed-age/difficulty0; sensory/accessibility1 (named controls and no-JS, no assistive session); educational purpose0; safety/trust2 (truthful zero and no false equivalent, no physical claim); mobile interaction2 (checked width and keyboard; enlarged link requires scroll); detours/repetition2 (separate route labeled); decision without broad search2 (decline/reset). **13/26**, versus the October21 same-task **3/26**. The numeric improvement is an editorial interface proxy, not human evidence. The critical misleading-match and unrelated-fallback failures clear in checked modes; absent activity instructions remain absent and cannot be counted as a runnable water-painting guide. Reconsider on real false negatives, clutter, assistive failure, source conflict, reviewer P0-P2 or live regression.

## Independent Review Cycle One And Repair

Franklin's read-only cycle-one verdict was **FAIL** with a P2: exact-word equality lost common material searches (`cup`/`cups`, `block`/`blocks`, `bowl`/`bowls`, `container`/`containers`) and `painter's tape` excluded one card. It also flagged a P3 stale checkpoint phase. The tokenizer now normalizes simple terminal plural `s` and possessive `s` symmetrically for data/query; focused tests assert the concrete material owners and all three painter-tape matches. The checkpoint phase is corrected. This is a bounded repair of a reviewer-found regression, not evidence of user demand.

Franklin's cycle-two read-only verdict is **PASS_WITH_P3/no P0-P2** on the repaired exact16-path diff. Its P3 identified the `cars` count above; local Chrome independently confirmed five and the record was corrected. The verdict did not include browser or generator reruns; those are operator evidence, not reviewer evidence.

## QA And Measurement Boundary

Focused and full native137/137 pass after cycle-one repair. All three generators ran twice after that repair and produced the same site diff hash `ba16959bcdf45c191c587915a8c8604a00951670adec7519c2f3a478266b4cc6`; exact generated site scope is `site/cards.html` and `site/sitemap.xml`, plus manually versioned JS. `git diff --check`, roadmap JSON parse, GSC existing-snapshot validator94, 71 HTML pages/750 local links/75 fragments with zero missing pass. October21 latest finalized-through-October19 GSC rolling490 impressions/7 clicks versus prior481/7 is monitoring context only; complete queries/routes are unavailable. No October22 snapshot exists at this run. Browser task is a technical simulation, not parent/child, touch, true zoom, screen-reader or physical-use testing. Independent review and production release evidence are recorded in `ops/operator-review.md` after those gates actually complete.
