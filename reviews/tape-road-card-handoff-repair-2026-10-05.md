# Tape Road Compact-Card Handoff Repair

Action `KAL-IMP-024`, October 5, 2026. Existing-card improvement, not a new URL or a guide rewrite. Frozen base `c00ac7d01f662a21857f608d170eb53ad6429e39`. This is a source-grounded proxy task and technical browser check, not a parent/child test.

## Task, Sources, And Scope

- Reuse the [October 4 frozen task](tape-road-card-guide-handoff-2026-10-04.md): a caregiver of a child age 3-5 who can push a large vehicle and follow a stop cue has an uncertain floor finish. Required outputs are a product/surface or removable-board decision, one short road and parking mission, adult/child roles, stop, rescue and cleanup without another broad search. Critical failure means the card hides its full guide until after child steps or offers an unsupported surface assurance. A younger child who can reach tape and vehicles is the secondary stress; the adult must select objects for all children in reach and manage loose tape, mouthing, peeling and throwing. The guide, not the compact card, owns the full rescue and mixed-age detail.
- Current-source lineage was reconciled in [September 15 candidate and implementation reviews](painter-tape-road-guide-implementation-review-2026-09-15.md) and rechecked October 4. [The Genius of Play Tape Track](https://thegeniusofplay.org/tgop/genius/play-ideas-tips/play-ideas/tape-track.aspx) describes a floor track and table/tray alternatives while cautioning against its masking-tape wood-floor setup. [3M painter's-tape questions](https://www.scotchblue.com/3M/en_US/scotchblue/your-questions/) distinguish products/surfaces. [FrogTape use guidance](https://www.frogtape.com/how-to-use/painters-tape) advises a hidden-area test and cautions about unsuitable surfaces. These sources do not establish universal compatibility, easy removal, low mess, or a safety outcome for this KAL adaptation. The maintained [guide](../site/articles/painter-tape-road-kids.html) already carries the product-instruction, test-strip, board fallback, loose-tape, rescue and cleanup boundaries.
- `MEASURED`: October 4 before and October 5 after DOM geometry/route/viewport widths, and the latest validated public-safe GSC only in its stated window. `SOURCE_BACKED`: publisher guidance within its product/context limits. `RESEARCH_HYPOTHESIS`: caregiver/younger-child task. `EDITORIAL_JUDGMENT`: layout choice and scores. `UNKNOWN`: real parent/child use, comprehension, duration, mess, enjoyment, learning, surface performance, safety in practice, click behavior, and SEO effect.
- Only [card generator](../scripts/generate_card_pages.py), [target card](../site/cards/tape-road.html), scoped [styles](../site/styles.css), [sitemap source](../scripts/generate_sitemap.py) and [output](../site/sitemap.xml), focused [test](../tools/tape-road-handoff.test.mjs), and action records change. All other 36 generated cards, card library, 15 SEO pages, guide body, canonical ownership, data, workflow and other observation windows stay unchanged.

## Change And Same-Task Result

The compact card now starts with one labeled link to the maintained guide and a short product/surface decision: follow the tape maker's guidance, test a strip in an inconspicuous area, remove it and check the surface, and use a cardboard sheet/table/tray the adult is willing to tape when the floor/finish is unknown or unsuitable. The card visibly says research-backed, not family-tested. Materials and an adult supervision/loose-tape/stop note precede the unchanged four child steps. The optional credited video follows those steps. The card's previous `low` mess label is now `Not measured`; the source CSV remains historical input and no mess outcome is inferred. The late duplicate guide link is removed while the two prior broad alternative links remain. CSS changes are scoped to this card's decision panel and narrow tiles.

| Mode | Before guide link | After guide link | After parent stop | After steps | After video | Width and arrival |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1280x900 root100% | y1253 | y240 | y512-617 | y637-876 | y896-1338 | 1280/1280; guide H1 top121, header bottom61, start top261. |
| 390x844 root100% | y1727 | y232 | y859-1066 | y1086-1404 | y1424-1602 | 390/390; guide H1 top141, header bottom93, start top296. |
| 390x844 root200% | y3069 | y413 | y2166-2808 | y2828-3560 | y3580-3758 | 390/390; guide H1 top213, header bottom143, start top699. |
| 320x844 root200% | y3710 | y457 | y2722-3671 | y3691-4607 | y4627-4765 | 320/320; guide H1 top257, header bottom143, start top855. |

These are document y positions for the tested local Chrome/CSS modes. Root200% is an ephemeral root-font override, not OS zoom or an assistive-technology certification. The guide link is before any child step in every mode; at enlarged text the complete stop remains below the first fold, so the first screen offers the maintained guide and beginning of the surface decision rather than the full safety text. A child cannot reach the steps on this card without passing the stop. Desktop keyboard focus plus Enter, mobile touch at normal and root200%, and Back opened/restored the actual guide; the guide H1 and start panel were readable under the header. Browser page-error samples were empty. The video was intentionally blocked during one route test and was not necessary to find the guide; playback was not tested. Mobile and enlarged screenshots were visually inspected for whole-word text fit and no incoherent overlap.

## Persona Rubric

Same frozen task, 12 applicable dimensions, maximum24; sensory/accessibility is N/A because no specific sensory or assistive need is evidenced, though the guide's small/seated route was inspected. Before values come from the October4 audit, not a reconstructed baseline. Scores are editorial proxy judgments. Card-only remains incomplete because its full rescue/younger-child answer lives in the guide; a total cannot waive that critical gap. Whole-route success relies on the now-early guide link and maintained guide, not on treating the card as a full guide.

| Dimension | Card before | Card after | Route before | Route after | Reason for after |
| --- | ---: | ---: | ---: | ---: | --- |
| Answerability | 0 | 1 | 2 | 2 | Card resolves unknown floor but sends rescue to guide. |
| Age/ability | 0 | 0 | 2 | 2 | Age only on card; guide has push/stop-cue fit. |
| Materials/substitutions | 1 | 2 | 2 | 2 | Tape/vehicles plus board, table or tray fallback. |
| Setup/duration/cleanup | 1 | 1 | 1 | 1 | Adult remove/store is present; duration unmeasured. |
| Adult involvement | 1 | 2 | 2 | 2 | Decision and stop precede child steps. |
| Setting/space | 0 | 2 | 2 | 2 | Unknown floor has a removable-surface route. |
| Mixed age/difficulty | 1 | 1 | 2 | 2 | Card says large intact vehicles; guide handles every-child reach. |
| Sensory/accessibility | N/A | N/A | N/A | N/A | No specific need established; no claimed outcome. |
| Educational purpose | 1 | 1 | 2 | 2 | Card's one change remains bounded; guide explains observation. |
| Safety/trust | 1 | 1 | 2 | 2 | Early stop and untested label, but card alone lacks full younger-child/product context. |
| Mobile interaction | 1 | 2 | 1 | 2 | Early link in tested widths without overflow; arrival clears header. |
| Detours/repetition | 0 | 2 | 0 | 2 | Optional video moved after start; duplicate guide link removed. |
| Decision without broad search | 0 | 1 | 2 | 2 | Card-only rescue incomplete; guide route supplies it. |
| **Total** | **7/24** | **16/24** | **20/24** | **23/24** | **12 applicable; critical-output override retained.** |

## Every Visible Section

| Section | Job/value | Risk and verdict |
| --- | --- | --- |
| Card H1/kicker | Activity and age; unchanged. | Age is not readiness. Keep. |
| Card early guide/surface panel | One depth route, product-specific choice and untested limit before execution. | Avoid universal surface assurance or guide duplication. New, keep. |
| Card material/time/mess tiles | Tape, large intact vehicles, open-ended time, unmeasured mess. | `low` lacked observation; replace only that label. |
| Card parent check | Adult stays close, controls loose tape/roll and lists direct stops/removal. | Must remain ahead of child steps. Move/compress duplicate surface text. |
| Card four steps | One road, drive/park, one change, adult cleanup. | All four unchanged; keep. |
| Card optional video/source | Inspiration and attribution, not activity evidence. | Former first-screen detour; move below start/retain credit. |
| Card related/back routes | Two prior broad alternatives and library back route. | Remove duplicate guide link only; preserve others. |
| Guide hero/start | Readiness, surface fallback, roles, mission and stop. | Unchanged canonical depth; keep. |
| Guide illustration | Shows board default, labeled AI generated. | Not proof of use; keep. |
| Guide run/change | Executable short road and one comparison. | No measured outcome; keep. |
| Guide troubleshooting/adaptation/cleanup | Rescue, younger-child reach, seated route, adult removal. | Critical guide-held outputs; keep and test direct arrival. |
| Guide evidence/related/footer | Publisher limits, untested status, related routes. | No inherited endorsement/test claim; keep. |

## QA, Decision, And Release Gate

Local decision: **IMPROVE the existing card handoff**. No new indexable job or query-demand assertion. The October5 public-safe snapshot arrived on October6 as a disjoint remote commit; 79 checked-in snapshots validate, latest finalized through October3: property386 impressions/12 clicks versus prior357/11, card2/0 unchanged and guide2/0 versus1/0. Complete queries and route analytics are unavailable; overlapping 28-day windows cannot evaluate this repair. Preserve rampOct13, chainOct7, foilOct8, packOct9, bridgeOct10 and weeklyOct11.

Three generators ran and a second full run left the generated diff byte-identical; only Tape Road card and its one sitemap lastmod changed. Native116, 80 snapshot validations after the disjoint October6 sensor fast-forward, 71 HTML/834 local refs/fragments, roadmap JSON and whitespace checks passed. Mencius independent read-only cycle1 `PASS_WITH_P3`, no P0-P2: the surface test should specify an inconspicuous location and removal, and a test name overstated output isolation. Both P3s were corrected in the generator/test. Anscombe independent read-only cycle2 `PASS`, no P0-P3 or blockers; it confirmed exact15 scope, both corrections, source boundaries, scores/section coverage, focused tests, then-current 79 GSC snapshots and in-memory generated output. It did not rerun the full native suite, writing generators or browser. Reviewed `867de424f0d8d69c94698e57651b79d193a6c08f` pushed; exact-SHA Pages run [37500764705](https://github.com/agarg21/preschool-build-lab/actions/runs/37500764705) succeeded. Live card/CSS/sitemap/unchanged guide returned HTTP200 and byte-matched local; no release marker exists. Production card canonical/H1, single early guide, surface and untested wording, stop-before-four-steps/video-after, sitemap date and desktop/390/390-root200/320-root200 width and keyboard/touch/Back guide-arrival task passed with no sampled page errors. Confidence is high in measured technical order/route/fit, moderate in proxy planning gain, and unknown in human or search effects. Reconsider if later live route/heading fails, the early panel buries the stop in a real task, or genuine parent evidence contradicts this proxy.
