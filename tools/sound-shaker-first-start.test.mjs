import assert from "node:assert/strict";
import fs from "node:fs";
import test from "node:test";

const card = fs.readFileSync("site/cards/sound-shaker-match.html", "utf8");
const collection = fs.readFileSync("site/collections/science-experiments-for-4-year-olds.html", "utf8");
const library = fs.readFileSync("site/cards.html", "utf8");
const sitemap = fs.readFileSync("site/sitemap.xml", "utf8");
const block = collection.slice(
  collection.indexOf("<h2>Sound Shaker Match</h2>"),
  collection.indexOf("</article>", collection.indexOf("<h2>Sound Shaker Match</h2>")),
);

test("sound shaker keeps existing page ownership", () => {
  assert.equal([...card.matchAll(/<h1>/g)].length, 1);
  assert.equal([...collection.matchAll(/<h1>/g)].length, 1);
  assert.match(card, /rel="canonical" href="https:\/\/kidactivitylab.com\/cards\/sound-shaker-match.html"/);
  assert.match(collection, /rel="canonical" href="https:\/\/kidactivitylab.com\/collections\/science-experiments-for-4-year-olds.html"/);
  for (const path of ["cards/sound-shaker-match.html", "collections/science-experiments-for-4-year-olds.html", "cards.html"]) {
    assert.equal(sitemap.split(`<loc>https://kidactivitylab.com/${path}</loc>`).length - 1, 1);
    assert.match(sitemap, new RegExp(`<loc>https://kidactivitylab\\.com/${path.replaceAll(".", "\\.")}</loc>\\s*<lastmod>2026-10-17</lastmod>`));
  }
});

test("adult prep, reach decision and spill stop precede child action on both routes", () => {
  const cardCue = card.indexOf('aria-label="Before starting"');
  const cardMaterials = card.indexOf('class="card-meta"');
  const cardSetup = card.indexOf('aria-label="Adult setup"');
  const cardStep = card.indexOf("Shake one closed container.");
  assert.ok(cardCue > 0 && cardCue < cardMaterials && cardMaterials < cardSetup && cardSetup < cardStep);
  const collectionCue = block.indexOf("<strong>Adult check:</strong>");
  const collectionMaterials = block.indexOf('class="activity-materials"');
  const collectionSetup = block.indexOf("<strong>Adult setup:</strong>");
  const collectionStep = block.indexOf("Shake one closed container.");
  assert.ok(collectionCue > 0 && collectionCue < collectionMaterials && collectionMaterials < collectionSetup && collectionSetup < collectionStep);
  for (const before of [card.slice(cardCue, cardStep), block.slice(collectionCue, collectionStep)]) {
    for (const text of ["two opaque lidded containers", "two more", "close and check every lid", "younger children", "Skip if lids", "Stop and collect pieces", "filler spills", "Not family-tested"]) {
      assert.ok(before.includes(text), text);
    }
  }
});

test("mission, rescue, cleanup and source limits remain explicit", () => {
  for (const html of [card, block]) {
    for (const text of ["Set two that sound alike together", "Compare just two again", "puts all containers and remaining filler away", "NAEYC sound-pair example", "AAP small-object guidance", "editorial choices", "outcomes are unknown"]) {
      assert.ok(html.includes(text), text);
    }
    assert.doesNotMatch(html, /5 min|low mess|safe for (?:all|every)|guaranteed/i);
  }
  assert.match(collection, /<td>Sound Shaker Match<\/td>\s*<td>Not measured<\/td>\s*<td>Not measured<\/td>/);
  assert.match(card, /<strong>Time<\/strong>Not measured/);
});

test("library keeps 36 direct card routes and updates only the sound shaker summary", () => {
  assert.equal([...library.matchAll(/class="mini-card" href="cards\//g)].length, 36);
  assert.match(library, /cards\/sound-shaker-match.html"><strong>Sound Shaker Match<\/strong><span>Not measured · 4 opaque lidded containers, rice, dry pasta \(adult fills\)<\/span>/);
  assert.match(library, /<template data-search="Sound Shaker Match 4 opaque lidded containers, rice, dry pasta \(adult fills\)"/);
});
