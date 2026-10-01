# Ball Maze Narrow Heading Repair

Action `KAL-IMP-022`, October 1, 2026 afternoon; base
`564b8551634bd458c2d4898868bb74abba2b1e41`. Exact 13 paths in the
roadmap. This closes the pre-existing 320px/200%-root-text H1 overflow noted
as P3 in [IMP021](ball-maze-journey-repair-2026-10-01.md), not an additional
activity guide or a change to the ball-maze instructions.

## Parent Task And Evidence

Reuse the September 14 source-derived caregiver task: decide whether an intact
shallow-lid maze fits a child who can move chunky blocks and follow a stop cue,
then start a wide path with adult-selected large foam ball, gentle tilt,
stop/reset, rescue and cleanup. A younger child who can reach materials is the
secondary stress. Success at this narrower viewport is a readable whole
activity name and fit/start route without horizontal scrolling or hidden
critical instruction. This is a `RESEARCH_HYPOTHESIS` persona, not a family
interview. Existing source reconciliation is `SOURCE_BACKED` within its
documented limits; browser geometry is local `MEASURED` technical evidence;
the scope and proxy judgment are `EDITORIAL_JUDGMENT`. No physical test,
accessibility certification, engagement, safety-in-practice, or SEO result.
Those outcomes remain `UNKNOWN`.

No new GSC snapshot arrived after the September 30 validation of 74
public-safe snapshots. Latest finalized September 28 overall 387/10;
ball-maze compact card 1/0, not an activity-guide demand or route measure.

## Implementation And Browser Result

At 320px and 200% root text, the guide document measured **348/320**
scroll/client width. Its H1 text extended beyond its 280px box. A first
`overflow-wrap: anywhere` trial yielded 320/320 but split “Cardboard” inside
the word, visibly lowering title quality. That trial was rejected before
release. The final scoped `max-width: 340px` rule uses `1.7rem` for this guide
H1, allowing whole-word wraps; normal desktop/390px typography is unchanged.
The generator-owned stylesheet token advances `ball-maze-guide-2` to `-3`.
No title text, article body, metadata, JSON-LD, URL, card/library output or
sitemap date changes; guide lastmod was already October 1.

| Local browser mode | Guide scroll/client | H1 observation | Direct hash heading/header |
|---|---:|---|---:|
| Desktop 1280x844 keyboard | 1280/1280 | Existing 53.75px high | 112/61 |
| Mobile 390x844 touch | 390/390 | Existing 70.53px high | 112/93 |
| Mobile 390x844, root200% | 390/390 | Existing 211.69px high | 224/143 |
| Mobile 320x844 touch | 320/320 | Whole words, 57.13px high | 112/93 |
| Mobile 320x844, root200% | **320/320** | Whole words, 171.38px high; was 348px document | 224/143 |

The 320/root200% screenshot shows the activity name as whole words on three
lines, with the supporting question and top of the fit/start panel still in
view. The complete first panel requires scrolling at this text size; no
critical text is hidden or clipped. In all five modes, the library/card/guide
route, Back, material/adult/stop/rescue/cleanup/younger/untested wording,
image decode and true text-before-hash navigation passed. Desktop keyboard
focus/Enter remained 42 tabs to the library card and five more to the guide;
touch modes used taps. No page/console errors. Local browser emulation is not
assistive-technology certification or human testing.

## Persona And Every-Section Review

The prior **24/26 across all 13 dimensions, no N/A**, remains the same-task
proxy; its 390px enlarged-text criterion did not include this harsher 320px
stress, so no new score improvement is asserted. The added failure gate was
readable activity identity at 320px/root200%; that gate now passes. Materials,
age/ability, adult role, mission, stop, rescue, adaptation, cleanup, trust and
decision without a broad search retain their prior scores because content did
not change. Sensory/accessibility and late compact-card depth link remain 1
each for the same reasons recorded in IMP021. No automatic critical failure
was observed in the final local modes.

| Surface/section | Decision and evidence | Verdict |
|---|---|---|
| Library header/promo/grid/footer | Existing entry and navigation; no bytes changed | Preserve |
| Compact card title/tiles/steps/parent/related | Existing quick start and late depth link; no bytes changed | Preserve; late link separate |
| Guide hero H1 | Names activity; formerly clipped at narrow enlarged text | Narrow size only; whole-word fit |
| Guide hero dek/fit/start | Hook, readiness, materials, adult and stop; unchanged | Preserve; readable after scroll |
| Illustration/caption | AI illustration and untested label; unchanged | Preserve |
| First run/one-wall/troubleshooting | Start, one change, rescue; unchanged | Preserve |
| Adapt/cleanup/evidence/sources/related/footer | Limits, removal and optional routes; unchanged | Preserve |

## QA And Release Gate

All three generators ran twice; site/script/tool diff hash was stable at
`fc88e46ea492a2f52739e7756c00e1f8f297af1c8d1647b46a8acbad006ac939`.
Only the guide's generated stylesheet token changed. Full native 113/113
tests, roadmap JSON parse, `git diff --check`, and 71 HTML / 764 local
links-assets-fragments passed. Focused test now asserts the narrow heading
rule. Hypatia independent read-only cycle1 `PASS`, no P0-P3: it independently
reproduced old348/320 and new320/320 with intact words, five viewport modes,
true hash, image, clean browser logs, 113 tests, JSON and whitespace. The
full-site link scan and generators were Master-run, not independently rerun.
Exact-SHA Pages/live verification remains pending at this writing.

Reconsider if production 320/root200% still overflows, another viewport or
guide changes, a critical start/stop is obscured, or independent review finds
a P0-P2 issue. Preserve all observation windows and October 4 weekly synthesis.
