# Age 4 STEM Cluster Review

Date: 2026-07-02
Reviewer: Codex Review Agent
Pages:
- `site/collections/original-stem-activities-for-4-year-olds.html`
- `site/ages/stem-activities-for-4-year-olds.html`
Brief checked:
- `briefs/age-4-original-stem-test-pack.md`

## Overall Verdict

The original age-4 STEM pack is usable enough for parent testing now. A tired parent can start most activities within 60 seconds because the page has a quick start, adult job, stop cue, setup list, kid-facing steps, safety note, and parent observation prompt.

The age-4 STEM hub is weaker. It answers the keyword, but it still feels like a generic activity roundup and does not clearly route the parent toward the stronger original/test pack. For indexing, the hub should earn its place by featuring the original pack and giving a simple chooser based on parent constraints.

No new parent testing observations were found in the brief. That is still the main gap before upgrading activities into stronger standalone pages.

## Scores

Original STEM pack:
- Parent followability: 8.2/10
- Kid engagement potential: 8.4/10
- Original content strength: 7.2/10 before testing, likely 8+ with real notes and visuals

Age-4 STEM hub:
- Parent followability: 6.4/10
- Kid engagement potential: 7.0/10
- Original content strength: 4.8/10

## Top 5 Fixes

1. Add a prominent original-pack callout near the top of the age-4 STEM hub.
   Suggested copy:
   "Best first pick: Start with the original age-4 STEM test pack. It has five 5-10 minute activities with parent jobs, read-aloud kid steps, stop rules, and notes to capture what actually worked."

2. Make the hub chooser more parent-useful by adding a "Best when..." column or replacing the generic table with a tired-parent chooser.
   Suggested rows:
   - "Need the lowest mess: Ramp Detective or Shadow Builder."
   - "Need a story hook: Bridge Rescue."
   - "Need big laughs from failure: Windproof Tower."
   - "Okay with water: Tiny Boat Cargo Test."

3. Align hub activity names with the original pack for the strongest items.
   Current hub names like "Car Ramp Distance Test," "Paper Bridge," and "Wind Tower Test" should either link visibly to or mention "Ramp Detective," "Bridge Rescue," and "Windproof Tower" so the original work is the first-viewport signal.

4. Add one global "Before you start" safety line to the original pack.
   Suggested copy:
   "Before you start: keep pieces too large to mouth, keep ramps and towers low, point flashlights at the wall, and stay next to any water tray."

5. Keep the pack indexable but do not create standalone SEO pages for individual activities until at least two have real observations, kid quotes, and one original visual or diagram.

## Original Pack Notes

### Ramp Detective

Verdict: Keep, with optional small polish.

What works:
- Fast setup and clear stop cue.
- "Road" language is parent-friendly and kid-friendly.
- Safety note handles the main risk: climbing or standing on the ramp materials.

What is still confusing:
- "Plain, soft, or paper" may not map cleanly to the actual materials if the parent uses cardboard, towel, and placemat.

Suggested copy:
- Say this: "Which road will make the car go farthest: plain cardboard, towel, or placemat?"
- Rescue line: "If this turns into car play, do one last roll and say, 'Let's mark this finish spot, then the cars can play.'"

### Bridge Rescue

Verdict: Keep, strong candidate for testing.

What works:
- The story hook is strong for a 4-year-old.
- The failure moment is clear: the bridge bends.
- The visual reference is parent-only and does not replace the Kid Activity Lab instructions.

What is still confusing:
- "If it bends, ask me to fold..." is good, but the parent may still need a one-line rescue when the child smash-tests the bridge.

Suggested copy:
- Rescue line: "If the toy crashes on purpose, say, 'One gentle rescue test first, then you can do a crash test.'"
- Safety tweak: "Use light toys only. Keep fingers out from under books, and do not stack books higher than one book per side."

### Shadow Builder

Verdict: Keep, but add a walking-safety detail.

What works:
- The adult job is clear: keep the flashlight still.
- The kid mission is simple: make a tiny and giant shadow.

What is still confusing:
- "Dim the room" could make a real room harder to move around safely.

Suggested copy:
- Adult job: "Dim the room just enough to see the shadow, set the flashlight on a stable surface pointing at a wall, and keep it still."
- Rescue line: "If the flashlight becomes the toy, give the child one turn to aim at the wall, then park it and move only the block."

### Windproof Tower

Verdict: Keep, strong engagement potential.

What works:
- Three fan waves is a clear test.
- "Wider bottom" is concrete.
- Failure can be funny instead of discouraging.

What is still confusing:
- The stop rule says two rebuilds, but the page could make frustration management more explicit.

Suggested copy:
- Rescue line: "If the falling stops being funny, switch to: 'Can we build one short tower that survives?'"
- Safety tweak: "Keep towers below your child's chest and use light materials only."

### Tiny Boat Cargo Test

Verdict: Keep, but this is the messiest activity and needs the clearest boundary.

What works:
- The boat-making section fixes a major parent setup gap.
- The cargo guidance is safer than small coins or buttons.
- Stop after first big sink or one redesign is the right constraint.

What is still confusing:
- The child-facing rescue line asks the child to dump water and reshape foil. Some parents will want the adult to handle the wet reset.

Suggested copy:
- Rescue line: "If it sinks, I will dump the water out. You pinch the sides higher, then we try one more passenger."
- Mess boundary: "One inch of water only. Keep the towel under the tray, and empty the tray when the test ends."

## Age-4 STEM Hub Notes

Verdict: Change before relying on it as an indexable hub.

What works:
- It has the right keyword intent and a useful mix of low-prep activities.
- The safety section is broad and practical.

What is confusing:
- The original/tested pack is not visible from the top of the page.
- The page sends parents to older generic cards before it sends them to the stronger original pack.
- The table is factual but not decision-oriented enough for a tired parent.
- "Ramp Texture Test" still lists foil, while the original pack intentionally moved away from foil for the ramp activity.

Suggested structure:
1. Hero.
2. Quick pick callout.
3. New "Start here" block linking to `../collections/original-stem-activities-for-4-year-olds.html`.
4. Tired-parent chooser with mess, time, and best-use case.
5. Original pack preview cards for Ramp Detective, Bridge Rescue, Shadow Builder, Windproof Tower, and Tiny Boat Cargo Test.
6. Existing activity card grid as "More quick STEM cards."

Suggested "Start here" block:

```html
<section class="related">
  <h2>Start with the original age-4 STEM test pack</h2>
  <p>If you only have ten minutes, use the Kid Activity Lab original test pack first. It gives you five activities with parent jobs, read-aloud kid steps, stop rules, and notes to capture what worked with a real child.</p>
  <p><a href="../collections/original-stem-activities-for-4-year-olds.html">Open the original age-4 STEM test pack</a></p>
</section>
```

Suggested chooser copy:

| Parent situation | Best pick | Why |
| --- | --- | --- |
| I need low mess | Ramp Detective | Dry materials, fast reset, easy to stop. |
| My child likes stories | Bridge Rescue | The toy crossing the river gives the test a reason. |
| I need movement but not chaos | Windproof Tower | Building and rebuilding gives energy a job. |
| We can handle water | Tiny Boat Cargo Test | High engagement, but needs close supervision. |
| It is almost bedtime | Shadow Builder | Calm, low mess, and easy to end after two shadows. |

## Implementation Handoff

Ready for Implementation Agent:
- Add the age-4 STEM hub "Start here" block linking to the original pack.
- Add a parent chooser to the age-4 STEM hub.
- Align hub copy with the original pack names and remove foil from the ramp texture row or de-emphasize that card.
- Add the original pack's global "Before you start" safety line.
- Add rescue lines for Bridge Rescue, Shadow Builder, Windproof Tower, and Tiny Boat Cargo Test.

Waiting on parent testing:
- Do not promote individual activities into standalone polished SEO pages until real notes exist.
- Fill `briefs/age-4-original-stem-test-pack.md` with at least two activity logs, including setup time, engagement time, kid quote, confusion point, mess, repeatability, and photo/diagram need.

