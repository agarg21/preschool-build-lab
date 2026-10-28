import assert from "node:assert/strict";
import fs from "node:fs";
import test from "node:test";

const card = fs.readFileSync("site/cards/magnet-hunt.html", "utf8");
const library = fs.readFileSync("site/cards.html", "utf8");
const sitemap = fs.readFileSync("site/sitemap.xml", "utf8");
const hubs = [
  "site/ages/stem-activities-for-4-year-olds.html",
  "site/collections/science-experiments-for-4-year-olds.html",
  "site/collections/no-prep-stem-activities-for-4-year-olds.html",
].map((path) => fs.readFileSync(path, "utf8"));
const preschool = fs.readFileSync("site/collections/stem-activities-for-preschoolers.html", "utf8");

test("direct Magnet Hunt URL is a noindex pause with a first-screen decline", () => {
  assert.match(card, /<h1>Magnet Hunt<\/h1>/);
  assert.match(card, /name="robots" content="noindex,follow"/);
  assert.match(card, /rel="canonical" href="https:\/\/kidactivitylab\.com\/cards\/magnet-hunt\.html"/);
  const decline = card.indexOf("Do not start this version.");
  const alternate = card.indexOf('href="../cards/paper-bridge.html"');
  assert.ok(decline > 0 && alternate > decline);
  for (const text of ["high-powered or rare-earth", "type and power", "documentation", "younger-child reach", "divided adult attention", "not currently offer a runnable setup", "not been family- or physically tested"]) {
    assert.ok(card.includes(text), text);
  }
  assert.doesNotMatch(card, /<section class="steps-grid"|<ol class="card-steps"|5 min|low mess|safe objects|Make two piles/);
  assert.doesNotMatch(sitemap, /<loc>https:\/\/kidactivitylab\.com\/cards\/magnet-hunt\.html<\/loc>/);
  for (const path of [
    "cards.html",
    "ages/stem-activities-for-4-year-olds.html",
    "collections/science-experiments-for-4-year-olds.html",
    "collections/no-prep-stem-activities-for-4-year-olds.html",
    "collections/stem-activities-for-preschoolers.html",
  ]) {
    const date = ["cards.html", "collections/no-prep-stem-activities-for-4-year-olds.html", "ages/stem-activities-for-4-year-olds.html"].includes(path) ? "2026-10-28" : "2026-10-27";
    assert.ok(sitemap.includes(`<loc>https://kidactivitylab.com/${path}</loc>\n    <lastmod>${date}</lastmod>`), path);
  }
});

test("runnable hubs withdraw the magnet route without losing peer activities", () => {
  for (const [index, hub] of hubs.entries()) {
    assert.doesNotMatch(hub, /Magnet Hunt|cards\/magnet-hunt\.html|large magnet, safe objects/);
    assert.match(hub, [ /Bridge Rescue/, /Sink or Float Tray/, /Cup Tower/ ][index]);
  }
  assert.doesNotMatch(hubs[1], /using water, ice, magnets/);
  assert.doesNotMatch(hubs[2], /flashlights, magnets/);
  assert.match(hubs[2], /font-size: min\(2\.5rem, 48px\)/);
  assert.doesNotMatch(preschool, /light, water, magnets, motion/);
  assert.match(preschool, /light, water, motion/);
  assert.match(preschool, /\.preschool-stem-hero h1 \{ font-size: min\(2\.5rem, 43px\)/);
});

test("library preserves the direct route but labels it paused", () => {
  assert.equal([...library.matchAll(/class="mini-card" href="cards\//g)].length, 36);
  assert.match(library, /cards\/magnet-hunt\.html"><strong>Magnet Hunt<\/strong><span>Paused; choose a non-magnet activity<\/span>/);
  assert.doesNotMatch(library, /Magnet Hunt<\/strong><span>5 min/);
  assert.match(library, /cards\/paper-bridge\.html/);
});
