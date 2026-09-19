import assert from "node:assert/strict";
import fs from "node:fs";
import test from "node:test";
import { createHash } from "node:crypto";
import { execFileSync } from "node:child_process";

const html = fs.readFileSync("site/articles/paper-helicopter-kids.html", "utf8");
const route = "/articles/paper-helicopter-kids.html";

test("helicopter has one canonical article with factual schema", () => {
  assert.equal([...html.matchAll(/<h1>/g)].length, 1);
  assert.ok(html.includes(`rel="canonical" href="https://kidactivitylab.com${route}"`));
  const schema = JSON.parse(html.match(/application\/ld\+json">([\s\S]*?)<\/script>/)[1]);
  assert.equal(schema["@type"], "Article");
  assert.equal(schema.datePublished, "2026-09-19");
  assert.ok(!("aggregateRating" in schema));
});

test("helicopter start and stop precede the map", () => {
  const panel = html.match(/<section class="bridge-start-panel"[\s\S]*?<\/section>/)[0];
  for (const marker of ["Adult:", "Child:", "Stop:", "adult-controlled scissors", "no printer", "no climbing", "younger children's reach"]) {
    assert.ok(panel.includes(marker), marker);
  }
  assert.ok(html.indexOf(panel) < html.indexOf('<figure class="helicopter-map">'));
});

test("helicopter preserves three-cut geometry and opposite folds", () => {
  for (const marker of ["7 cm wide by 21 cm tall", "8 cm below the top", "8.5 cm below the top", "middle third uncut", "2.5 cm above the bottom", "Do not connect the side cuts", "one blade toward you and the other away", "through all layers", "No ruler? Mark by halving the gaps"]) {
    assert.ok(html.includes(marker), marker);
  }
});

test("helicopter recovery does not introduce weights or outcome assurances", () => {
  for (const marker of ["not family-tested", "not NASA measurements", "not guaranteed repairs", "do not patch it with clips or weights", "Do not climb higher", "safety outcomes are unknown", "cardstock and tissue are not established equivalents"]) assert.ok(html.includes(marker), marker);
  assert.doesNotMatch(html, /safe for (?:all|every)|guaranteed learning|\d+\s*minutes|toddler-safe/i);
  for (const id of ["prepare", "drop", "rescue", "finish", "evidence"]) assert.ok(html.includes(`id="${id}"`));
});

test("helicopter discovery and inventory add one owner without a duplicate card", () => {
  for (const file of ["site/sitemap.xml", "data/seo_keyword_targets.csv"]) {
    assert.equal(fs.readFileSync(file, "utf8").split(route).length - 1, 1);
  }
  assert.ok(fs.readFileSync("site/cards.html", "utf8").includes(`href="articles/paper-helicopter-kids.html"`));
  assert.ok(!fs.existsSync("site/cards/paper-helicopter.html"));
});

test("helicopter map has stable intrinsic dimensions and text alternative", () => {
  const png = fs.readFileSync("site/assets/paper-helicopter/cut-fold-map.png");
  assert.equal(png.subarray(1, 4).toString(), "PNG");
  assert.equal(png.readUInt32BE(16), 900);
  assert.equal(png.readUInt32BE(20), 1400);
  assert.match(html, /alt="Upright rectangle:[^"]+No cut crosses the middle body\./);
  assert.match(html, /width="900" height="1400"/);
  assert.match(html, /Not a print-to-scale template/);
});

test("helicopter reviewed map retains cut stops, folds and intact body", () => {
  const png = fs.readFileSync("site/assets/paper-helicopter/cut-fold-map.png");
  // Change this baseline only after viewing and independently reviewing the new map.
  assert.equal(createHash("sha256").update(png).digest("hex"), "1be76e5cda7cbc452684e4ee8c9a8c1b0c43a7f532bcb51ae5989aa185d13675");
  execFileSync("python3", ["-c", `
from PIL import Image
im = Image.open('site/assets/paper-helicopter/cut-fold-map.png').convert('RGB')
cut, fold = (173,38,53), (23,107,98)
for p in [(220,240),(220,550),(80,650),(173,650),(360,650),(267,650)]:
    assert im.getpixel(p) == cut, ('cut endpoint/line', p)
for p in [(80,570),(360,570),(173,900),(267,900),(220,970)]:
    assert im.getpixel(p) == fold, ('fold landmark', p)
for p in [(220,600),(220,650),(220,700),(220,900)]:
    assert im.getpixel(p) not in [cut,fold], ('intact body',p)
`]);
});
