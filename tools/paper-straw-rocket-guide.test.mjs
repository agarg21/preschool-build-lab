import assert from "node:assert/strict";
import fs from "node:fs";
import test from "node:test";
import { execFileSync } from "node:child_process";

const html = fs.readFileSync("site/articles/paper-straw-rocket.html", "utf8");
const route = "/articles/paper-straw-rocket.html";

test("rocket has one canonical article with no outcome schema", () => {
  assert.equal([...html.matchAll(/<h1>/g)].length, 1);
  assert.ok(html.includes(`rel="canonical" href="https://kidactivitylab.com${route}"`));
  const schema = JSON.parse(html.match(/application\/ld\+json">([\s\S]*?)<\/script>/)[1]);
  assert.equal(schema["@type"], "Article");
  assert.equal(schema.datePublished, "2026-09-21");
  assert.ok(!("aggregateRating" in schema));
  assert.ok(!("totalTime" in schema));
});

test("rocket fit and adult-launch boundary precede assembly", () => {
  const intro = html.slice(html.indexOf('<main>'), html.indexOf('<section id="prepare"'));
  for (const text of ["Printer required", "Adult-led throughout", "not family-tested", "not a child-launch", "away from people and faces"]) assert.ok(intro.includes(text), text);
  assert.ok(html.includes("print page 1"));
  assert.ok(html.includes("strawrocket_worksheet.pdf"));
  assert.ok(html.includes('href="paper-helicopter-kids.html"'));
});

test("rocket retains one template lineage with explicit fit and seal", () => {
  for (const text of ["both fin units", "middle scissors mark", "Remove the pencil to check the straw", "put the pencil back", "opposite side", "Nothing should extend below", "Tape the twisted nose closed", "then remove the pencil", "bottom stays open", "four triangular fins", "not a second straw or pipette"]) assert.ok(html.includes(text), text);
});

test("rocket recovery and child roles do not promise outcomes", () => {
  for (const text of ["no child needs to blow", "a child mouths the materials", "never", "suction", "Do not blow harder", "not guaranteed fixes", "end the trial", "not an age recommendation", "safety outcomes remain unknown"]) assert.ok(html.toLowerCase().includes(text.toLowerCase()), text);
  assert.doesNotMatch(html, /safe for (?:all|every)|guaranteed learning|\d+\s*minutes|toddler-safe/i);
  for (const id of ["prepare", "launch", "rescue", "finish", "evidence"]) assert.ok(html.includes(`id="${id}"`));
});

test("rocket adds one owner and one library route without a card", () => {
  for (const file of ["site/sitemap.xml", "data/seo_keyword_targets.csv"]) assert.equal(fs.readFileSync(file, "utf8").split(route).length - 1, 1);
  assert.equal(fs.readFileSync("site/cards.html", "utf8").split('href="articles/paper-straw-rocket.html"').length - 1, 1);
  assert.ok(!fs.existsSync("site/cards/paper-straw-rocket.html"));
});

test("rocket diagram has intrinsic dimensions and complete text alternative", () => {
  const png = fs.readFileSync("site/assets/paper-straw-rocket/fit-air-path.png");
  assert.equal(png.subarray(1, 4).toString(), "PNG");
  assert.equal(png.readUInt32BE(16), 900);
  assert.equal(png.readUInt32BE(20), 1000);
  assert.match(html, /alt="Side cutaway:[^"]+Remove the pencil before launch\./);
  assert.match(html, /width="900" height="1000"/);
  assert.match(html, /not to scale or a cutting template/);
});

test("rocket cutaway keeps the bore open and the nose closed", () => {
  execFileSync("python3", ["-c", `
from PIL import Image
im = Image.open('site/assets/paper-straw-rocket/fit-air-path.png').convert('RGB')
for point, color in [((400,245),(139,103,0)),((400,274),(23,107,98)),((400,295),(36,107,143)),((800,295),(139,103,0)),((170,800),(255,255,255))]:
    assert im.getpixel(point) == color, (point,im.getpixel(point))
assert im.getpixel((400,259)) != (23,107,98), 'sleeve/straw gap must remain visible'
`]);
});
