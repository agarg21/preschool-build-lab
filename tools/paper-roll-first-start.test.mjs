import assert from "node:assert/strict";
import fs from "node:fs";
import test from "node:test";

const read = p => fs.readFileSync(p, "utf8");
const card = read("site/cards/paper-roll-play.html");
const before = (html, marker, action) => {
  const first = html.indexOf(marker), second = html.indexOf(action);
  assert.ok(first >= 0 && second >= 0 && first < second, marker);
};

test("actual CSV card dispatches to the restricted empty-roll rule", () => {
  const source = read("scripts/generate_card_pages.py");
  assert.match(source, /if slug == "paper-roll-play":\s+return paper_roll_card_page\(row\)/);
  assert.match(card, /class="kid-card paper-roll-card"/);
  for (const marker of ["1 empty lightweight paper-towel roll", "skip if you cannot watch them all", "Stop for mouthing", "not family-tested by Kid Activity Lab", "Duration and mess have not been measured", "No hard mailing tubes"]) before(card, marker, 'class="steps-grid"');
  for (const marker of ["on its curved side, opening sideways", "push the empty roll and watch it move", "Wait until it stops", "put it back on its side", "Watching an adult push", "adult collects the roll and spares", "do not add toys, a slope or force"]) assert.ok(card.includes(marker), marker);
  assert.doesNotMatch(card, /Drop a toy\.|Make a tunnel\.|3 minutes|adapted from a creator video|<iframe/);
});

test("empty-roll sources and optional history follow the complete task", () => {
  before(card, 'class="steps-grid"', 'aria-label="Sources and testing status"');
  before(card, 'aria-label="Rescue and cleanup"', "Previous video reference (optional)");
  for (const marker of ["ei.northwestern.edu/toy-recommendations-toilet-paper-tubes/", "not the source of the empty-roll rule above", "not verified its current playback", "do not certify a reused roll", "editorial adaptation, not clinical guidance", "safety outcomes are unknown"]) assert.ok(card.includes(marker), marker);
  assert.equal((card.match(/<h1>/g) || []).length, 1);
  assert.equal((card.match(/data-kal-contributor="credit"/g) || []).length, 1);
});

test("both actual incoming owners align without growing the library", () => {
  for (const p of ["materials/cardboard.html", "collections/no-cut-preschool-activities.html"]) {
    const html = read(`site/${p}`);
    const block = html.match(/<a class="mini-card" href="\.\.\/cards\/paper-roll-play.html">[\s\S]*?<\/a>/)?.[0];
    assert.match(block, /1 empty paper-towel roll &middot; adult stays beside/);
    assert.match(html, /font-size: min\(2\.5rem, 43px\)/);
  }
  const collection = read("site/collections/no-cut-preschool-activities.html");
  assert.match(collection, /role="region" tabindex="0" aria-label="No-cut preschool activity chooser"/);
  assert.doesNotMatch(collection, /Paper rolls \+ small toys|Paper rolls and magnetic tiles|needs closer supervision around small toys/);
  const library = read("site/cards.html");
  assert.equal((library.match(/class="mini-card"/g) || []).length, 36);
  assert.doesNotMatch(library, /cards\/paper-roll-play.html/);
  assert.match(read("site/materials/cardboard.html"), /name="robots" content="noindex,follow"/);
});

test("empty-roll compact fit and sitemap retain existing URLs", () => {
  assert.match(card, /\.paper-roll-card \.step-tile \{ min-height: 0;/);
  assert.match(card, /font-size: min\(2rem, 48px\)/);
  assert.match(card, /rel="canonical" href="https:\/\/kidactivitylab.com\/cards\/paper-roll-play.html"/);
  const sitemap = read("site/sitemap.xml");
  assert.equal((sitemap.match(/<loc>/g) || []).length, 67);
  for (const p of ["cards/paper-roll-play.html", "collections/no-cut-preschool-activities.html"]) assert.ok(sitemap.includes(`${p}</loc>\n    <lastmod>2026-10-27</lastmod>`));
  assert.doesNotMatch(sitemap, /materials\/cardboard.html/);
});
