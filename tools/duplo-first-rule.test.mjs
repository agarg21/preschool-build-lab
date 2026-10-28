import assert from "node:assert/strict";
import fs from "node:fs";
import test from "node:test";

const card = fs.readFileSync("site/cards/duplo-games.html", "utf8");
const entries = ["ages/activities-for-3-year-olds-at-home.html", "collections/no-prep-activities-for-preschoolers.html", "collections/independent-activities-for-preschoolers.html", "collections/fine-motor-activities-for-preschoolers.html"];
const before = (html, marker, steps) => {
  const position = html.indexOf(marker);
  const action = html.indexOf(steps);
  assert.ok(position >= 0 && action >= 0 && position < action, marker);
};

test("rendered DUPLO card dispatches to a complete visible-copy rule", () => {
  assert.match(fs.readFileSync("scripts/generate_card_pages.py", "utf8"), /slug in \{"cup-tower", "duplo-games", "tube-sculpture", "lego-color-tower", "tape-train-tracks", "block-tower", "tape-city"\}/);
  assert.match(card, /class="kid-card duplo-game-card"/);
  before(card, "Copy beside me:", 'aria-label="Before starting"');
  for (const marker of ["4 large DUPLO bricks: 2 matching pairs", "matching shape-and-colour pairs", "age/warning labels", "skip if parts, pairs or attention do not fit", "Stop for mouthing", "not family-tested by Kid Activity Lab", "Leave it visible", "No timer, winner or height target"]) before(card, marker, 'class="steps-grid"');
  for (const marker of ["Copy it beside the model", "bottom and top", "swap builder and copier", "Collect all four", "without teeth or pulling hard", "Duration and mess have not been measured"]) assert.ok(card.includes(marker), marker);
  assert.doesNotMatch(card, /Make a game\.|Play it\.|Switch rules\.|3 minutes|adapted from a creator video/);
});

test("all four DUPLO entries share material controls and the same executable loop", () => {
  for (const path of entries) {
    const html = fs.readFileSync(`site/${path}`, "utf8");
    const block = [...html.matchAll(/<article class="seo-activity">[\s\S]*?<\/article>/g)].map(m => m[0]).find(b => b.includes("<h2>DUPLO Games</h2>"));
    assert.ok(block, path);
    for (const marker of ["4 large DUPLO bricks: 2 matching pairs", "Adult stays beside setup", "Mess not measured", "Stop for mouthing", "Leave it visible", "not family-tested"]) before(block, marker, "<ol");
    for (const marker of ["Copy it beside the model", "Rescue and cleanup", "Collect all four", "Sources and testing status"]) assert.ok(block.includes(marker), `${path}: ${marker}`);
    assert.doesNotMatch(block, /Make a tiny game|3 min|low help|Switch the rule/);
  }
});

test("DUPLO source and optional old video never substitute for the first rule", () => {
  before(card, 'class="steps-grid"', "Previous video reference (optional)");
  assert.match(card, /not the source of the visible-copy rule above/);
  assert.match(card, /not verified its current playback/);
  assert.match(card, /Six_Bricks_Booklet\.pdf#page=15/);
  assert.match(card, /four-brick reduction/);
  assert.match(card, /No product recommendation or safety assurance/);
});

test("DUPLO discovery inventory and scoped fit retain one owner", () => {
  const library = fs.readFileSync("site/cards.html", "utf8");
  assert.equal([...library.matchAll(/class="mini-card"/g)].length, 36);
  assert.match(library, /Open-ended · 4 large DUPLO bricks: 2 matching pairs/);
  const css = fs.readFileSync("site/styles.css", "utf8");
  assert.match(css, /\.duplo-game-card \.step-tile/);
  const fine = fs.readFileSync(`site/${entries[3]}`, "utf8");
  assert.match(fine, /font-size: min\(2\.5rem, 43px\)/);
  const sitemap = fs.readFileSync("site/sitemap.xml", "utf8");
  assert.equal([...sitemap.matchAll(/<loc>/g)].length, 65);
  for (const path of ["cards/duplo-games.html", entries[3]]) {
    const date = path === entries[3] ? "2026-10-28" : "2026-10-27";
    assert.ok(sitemap.includes(`${path}</loc>\n    <lastmod>${date}</lastmod>`));
  }
});
