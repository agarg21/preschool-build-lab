import assert from "node:assert/strict";
import fs from "node:fs";
import test from "node:test";

const hub = fs.readFileSync("site/ages/stem-activities-for-4-year-olds.html", "utf8");
const pack = fs.readFileSync("site/collections/original-stem-activities-for-4-year-olds.html", "utf8");

function section(html, start, end) {
  const from = html.indexOf(start);
  const to = html.indexOf(end, from);
  assert.ok(from >= 0 && to > from, `Missing bounded section ${start}`);
  return html.slice(from, to);
}

test("age-four Shadow summary puts the adult light boundary before action", () => {
  const shadow = section(hub, "<h2>Shadow Builder</h2>", "<h2>Pattern Path</h2>");
  assert.ok(shadow.indexOf("Adult check:") < shadow.indexOf('<ol class="card-steps">'));
  assert.match(shadow, /Keep light on wall, not faces/);
  assert.match(shadow, /Adult lights the wall/);
  assert.match(shadow, /If it becomes the toy, switch it off and park it/);
  assert.match(shadow, /Resume only if an adult can relight it and keep it steady on the wall/);
  assert.ok(shadow.indexOf("relight it") < shadow.indexOf("the child moves the block"));
  assert.match(shadow, /one checked large opaque block/);
  assert.match(shadow, /original-stem-activities-for-4-year-olds\.html#shadow-builder/);
});

test("pack Shadow start and rescue retain adult control", () => {
  const shadow = section(pack, '<article class="test-activity" id="shadow-builder">', '<article class="test-activity" id="windproof-tower">');
  assert.ok(shadow.indexOf("Adult check:") < shadow.indexOf("Read-aloud kid steps"));
  assert.match(shadow, /Keep light on wall, not faces/);
  assert.match(shadow, /One checked large opaque block/);
  assert.match(shadow, /If the flashlight becomes the toy, switch it off and park it/);
  assert.match(shadow, /Resume only if an adult can relight it and keep it steady on the wall/);
  assert.ok(shadow.indexOf("relight it") < shadow.indexOf("your child moves the block"));
  assert.doesNotMatch(shadow, /give your child one turn to aim/);
  assert.match(shadow, /not the light/);
});
