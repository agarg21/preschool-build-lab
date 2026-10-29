import assert from "node:assert/strict";
import fs from "node:fs";
import test from "node:test";

const read = p => fs.readFileSync(`site/${p}`, "utf8");
const card = read("cards/blanket-river.html");
const block = (html, title) => [...html.matchAll(/<article\b[\s\S]*?<\/article>/g)]
  .map(m => m[0]).find(s => s.includes(`<h2>${title}</h2>`));
const entries = [
  ["card", card],
  ["age5", block(read("ages/activities-for-5-year-olds-at-home.html"), "Blanket River")],
  ["indoor", block(read("collections/indoor-activities-for-preschoolers.html"), "Blanket Toy Crossing")],
  ["building", block(read("collections/building-activities-for-4-year-olds.html"), "Blanket Crossing")],
];
const before = (html, marker, action) => {
  const first = html.indexOf(marker), second = html.indexOf(action);
  assert.ok(first >= 0 && second >= 0 && first < second, marker);
};

test("all Blanket River instruction owners identify toy-only fit and stops before action", () => {
  for (const [name, html] of entries) {
    assert.ok(html, name);
    const steps = name === "card" ? 'class="steps-grid"' : '<ol class="card-steps">';
    for (const marker of ["the route is for the toy, not for feet", "Stay beside every reachable child", "Skip if parts, space or attention do not fit", "Stop:", "blanket bunching or slipping", "not family-tested by Kid Activity Lab"]) before(html, marker, steps);
    for (const marker of ["3 large lightweight blocks", "not across its full width", "resting on both", "Carry the toy in your hand over the tiny bridge and back", "keep its weight in your hand, not on the bridge", "lay blocks flat", "Adult puts away the blanket, blocks and toy", "Duration and mess have not been measured"]) assert.ok(html.includes(marker), `${name}: ${marker}`);
    assert.doesNotMatch(html, /Cross the river\.|Move the bridge\.|2 min|low mess|firm cushions/);
  }
});

test("canonical and both override renderers retain one three-step toy story", () => {
  const source = fs.readFileSync("scripts/generate_seo_pages.py", "utf8");
  assert.match(source, /\*\*ACTIVITIES\["blanket-river"\]/);
  assert.match(source, /"parent": ACTIVITIES\["blanket-river"\]\["fit_cue"\]/);
  assert.equal((card.match(/class="step-tile"/g) || []).length, 3);
  for (const [, html] of entries.slice(1)) assert.equal((html.match(/<li>/g) || []).length, 3);
  assert.match(card, /class="kid-card blanket-river-card"/);
  assert.match(card, /Toy-only \| Adult-guided/);
});

test("all repaired owners disclose mechanism and editorial evidence boundaries", () => {
  for (const [name, html] of entries) {
    for (const marker of ["Sources and testing status", "extension.msstate.edu/publications/block-play", "extension.sdstate.edu/playing-blocks", "healthychildren.org", "not a tested setup or load test", "Source photos do not show this exact blanket arrangement", "safety outcomes are unknown"]) assert.ok(html.includes(marker), `${name}: ${marker}`);
  }
  assert.match(read("collections/building-activities-for-4-year-olds.html"), /toy-only material prompt, not the three-block start below or a child-bearing route/);
});

test("library, responsive owners and sitemap keep established routes", () => {
  const library = read("cards.html");
  assert.equal((library.match(/class="mini-card"/g) || []).length, 36);
  const entry = library.match(/<a class="mini-card" href="cards\/blanket-river.html">[\s\S]*?<\/a>/)?.[0];
  assert.match(entry, /Open-ended/);
  assert.match(entry, /Toy-only, adult stays beside/);
  assert.match(entry, /1 large lightweight toy/);
  assert.doesNotMatch(entry, /2 min/);
  assert.match(read("ages/activities-for-5-year-olds-at-home.html"), /font-size: min\(2\.5rem, 48px\)/);
  assert.match(read("collections/building-activities-for-4-year-olds.html"), /font-size: min\(2\.5rem, 43px\)/);
  const css = read("styles.css");
  assert.match(css, /\.blanket-river-card \.step-tile \{\s*min-height: 0;/);
  const sitemap = read("sitemap.xml");
  assert.equal((sitemap.match(/<loc>/g) || []).length, 65);
  for (const p of ["cards/blanket-river.html", "cards.html", "ages/activities-for-5-year-olds-at-home.html", "collections/indoor-activities-for-preschoolers.html", "collections/building-activities-for-4-year-olds.html"]) {
    const date = ["cards.html", "ages/activities-for-5-year-olds-at-home.html", "collections/building-activities-for-4-year-olds.html", "collections/indoor-activities-for-preschoolers.html"].includes(p) ? "2026-10-28" : "2026-10-27";
    assert.ok(sitemap.includes(`${p}</loc>\n    <lastmod>${date}</lastmod>`), p);
  }
});
