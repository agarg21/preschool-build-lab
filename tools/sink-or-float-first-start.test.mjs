import assert from "node:assert/strict";
import fs from "node:fs";
import test from "node:test";

const card = fs.readFileSync("site/cards/sink-or-float-tray.html", "utf8");
const collection = fs.readFileSync("site/collections/science-experiments-for-4-year-olds.html", "utf8");
const library = fs.readFileSync("site/cards.html", "utf8");
const sitemap = fs.readFileSync("site/sitemap.xml", "utf8");
const styles = fs.readFileSync("site/styles.css", "utf8");
const start = collection.indexOf("<h2>Sink or Float Tray</h2>");
const block = collection.slice(start, collection.indexOf("</article>", start));

test("sink or float stays on the existing card and collection URLs", () => {
  assert.equal([...card.matchAll(/<h1>/g)].length, 1);
  assert.equal([...collection.matchAll(/<h1>/g)].length, 1);
  assert.match(card, /rel="canonical" href="https:\/\/kidactivitylab.com\/cards\/sink-or-float-tray.html"/);
  assert.match(collection, /rel="canonical" href="https:\/\/kidactivitylab.com\/collections\/science-experiments-for-4-year-olds.html"/);
  for (const path of ["cards/sink-or-float-tray.html", "collections/science-experiments-for-4-year-olds.html", "cards.html"]) {
    assert.equal(sitemap.split(`<loc>https://kidactivitylab.com/${path}</loc>`).length - 1, 1);
    const lastmod = path === "cards/sink-or-float-tray.html" ? "2026-10-24" : path === "cards.html" ? "2026-10-28" : "2026-10-27";
    assert.match(sitemap, new RegExp(`<loc>https://kidactivitylab\\.com/${path.replaceAll(".", "\\.")}</loc>\\s*<lastmod>${lastmod}</lastmod>`));
  }
});

test("adult water, object, attention and stop decision precede child action", () => {
  const cardCue = card.indexOf('aria-label="Before starting"');
  const cardSetup = card.indexOf('aria-label="Adult setup"');
  const cardStep = card.indexOf("Guess: up or down?");
  assert.ok(cardCue > 0 && cardCue < cardSetup && cardSetup < cardStep);
  const collectionCue = block.indexOf("<strong>Adult check:</strong>");
  const collectionSetup = block.indexOf("<strong>Adult setup:</strong>");
  const collectionStep = block.indexOf("Guess: up or down?");
  assert.ok(collectionCue > 0 && collectionCue < collectionSetup && collectionSetup < collectionStep);
  for (const before of [card.slice(cardCue, cardStep), block.slice(collectionCue, collectionStep)]) {
    for (const text of ["one intact", "age label", "younger child", "No suitable toy? Skip", "watch constantly", "Stop and empty", "Not family-tested", "shallow tray", "Adult places and retrieves", "do not add water"]) {
      assert.ok(before.includes(text), text);
    }
  }
});

test("one-object result, unclear rescue, cleanup and source limits remain explicit", () => {
  for (const html of [card, block]) {
    for (const text of ["Off bottom? Floats", "Drops through water to bottom? Sinks", "Unsure? Say", "empties the tray immediately", "NAEYC sink-or-float example", "AAP water supervision", "CPSC toy age", "editorial synthesis", "outcomes are unknown"]) {
      assert.ok(html.includes(text), text);
    }
    assert.doesNotMatch(html, /5 min|medium mess|safe household objects|guaranteed|family-tested activity/i);
  }
  assert.match(collection, /<td>Sink or Float Tray<\/td>\s*<td>Not measured<\/td>\s*<td>Not measured<\/td>/);
  assert.match(card, /<strong>Time<\/strong>Not measured/);
  assert.match(card, /class="kid-card sink-float-card"/);
  assert.match(card, /styles\.css\?v=sink-float-card-1/);
  assert.match(styles, /\.sink-float-card \.steps-grid\s*\{\s*grid-template-columns: repeat\(2, minmax\(0, 1fr\)\)/);
});

test("library keeps 36 routes, a truthful format claim, and this summary", () => {
  assert.equal([...library.matchAll(/class="mini-card" href="cards\//g)].length, 36);
  assert.match(library, /cards\/sink-or-float-tray.html"><strong>Sink or Float Tray<\/strong><span>Not measured · shallow tray, a little water, one intact large bath toy<\/span>/);
  assert.doesNotMatch(library, /one-screen|one screen/i);
});
