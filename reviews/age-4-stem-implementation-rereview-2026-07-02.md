# Age 4 STEM Implementation Re-Review

Date: 2026-07-02
Reviewer: Codex Review Agent
Pages:
- `site/ages/stem-activities-for-4-year-olds.html`
- `site/collections/original-stem-activities-for-4-year-olds.html`
Prior review:
- `reviews/age-4-stem-cluster-review-2026-07-02.md`

## Overall Verdict

Close, but not quite ready to publish/request indexing as the final reviewed version.

Implementation correctly added the prominent original-pack block, tired-parent chooser, ramp foil de-emphasis, global safety line, and concrete rescue lines. The remaining issue is click-path clarity on the age-4 STEM hub: several cards now use original pack names, but their "Open card" links still land on older generic card pages with different titles. That can make a parent think they clicked the wrong thing.

## Criteria Check

- Original pack block is prominent and useful: pass.
  It appears directly after the quick-pick callout, names the original test pack, explains the value, and links clearly to the pack.

- Tired-parent chooser helps a real parent decide: pass.
  The chooser uses parent situations instead of abstract categories. The bedtime, water, story, low-mess, and movement rows are practical.

- Original pack names are clear without confusing card links: needs fix.
  The hub now labels items as "Ramp Detective car test," "Bridge Rescue paper bridge," "Tiny Boat Cargo Test," "Shadow Builder," and "Windproof Tower," but the card links open pages titled "Car Ramp Distance Test," "Paper Bridge," "Foil Boat Test," "Shadow Shape Match," and "Wind Tower Test." The names are directionally aligned, but the link destination feels mismatched.

- Foil is de-emphasized appropriately in ramp content: pass.
  Ramp Texture Test now says towel/paper/placemat instead of foil. Foil still appears for Tiny Boat Cargo Test, which is appropriate.

- Global safety line and rescue lines are useful, concrete, and not too verbose: pass with one optional polish.
  The safety line is short and concrete. The rescue lines are useful. Tiny Boat repeats the same rescue line in both the kid steps and the side box; this is not a blocker, but it could be tightened later.

## Scores After Implementation

Age-4 STEM hub:
- Parent followability: 7.8/10
- Kid engagement potential: 7.6/10
- Original content strength: 6.6/10

Original STEM pack:
- Parent followability: 8.7/10
- Kid engagement potential: 8.5/10
- Original content strength: 7.4/10 before testing

## Required Fix Before Publish/Indexing Request

Fix the hub card-link mismatch for original-pack activities.

Preferred fix:
- For the five original-pack preview items on `site/ages/stem-activities-for-4-year-olds.html`, send parents to the original pack instead of generic card pages.
- Best version: add anchors to each activity in `site/collections/original-stem-activities-for-4-year-olds.html`, then link directly:
  - Ramp Detective -> `../collections/original-stem-activities-for-4-year-olds.html#ramp-detective`
  - Bridge Rescue -> `../collections/original-stem-activities-for-4-year-olds.html#bridge-rescue`
  - Shadow Builder -> `../collections/original-stem-activities-for-4-year-olds.html#shadow-builder`
  - Windproof Tower -> `../collections/original-stem-activities-for-4-year-olds.html#windproof-tower`
  - Tiny Boat Cargo Test -> `../collections/original-stem-activities-for-4-year-olds.html#tiny-boat-cargo-test`
- Link text should be "Open in original test pack" for those five items.

Acceptable smaller fix:
- Keep the current generic card URLs, but change each link text to make the mismatch explicit:
  - "Open related card: Car Ramp Distance Test"
  - "Open related card: Paper Bridge"
  - "Open related card: Foil Boat Test"
  - "Open related card: Shadow Shape Match"
  - "Open related card: Wind Tower Test"

## Optional Polish

- Tiny Boat Cargo Test repeats the same rescue line in the read-aloud steps and side box. If touching the page anyway, keep the child-facing version in the steps and change the side-box rescue to:
  "One sink is enough. After one redesign, empty the tray before it becomes splash play."

## Publish Guidance

After the card-link mismatch is fixed and local generation/link validation still pass, this cluster is ready to publish and request indexing for:
- `https://kidactivitylab.com/collections/original-stem-activities-for-4-year-olds.html`
- `https://kidactivitylab.com/ages/stem-activities-for-4-year-olds.html`

This does not remove the parent-testing dependency. Real observations, kid quotes, and visuals are still needed before building standalone SEO pages for individual activities.

