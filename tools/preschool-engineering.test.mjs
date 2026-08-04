import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import test from "node:test";

const ROOT = process.cwd();
const PAGE_PATH = path.join(
  ROOT,
  "site",
  "collections",
  "engineering-activities-for-4-year-olds.html",
);
const IMAGE_PATH = path.join(
  ROOT,
  "site",
  "assets",
  "preschool-engineering",
  "engineering-challenge-materials.webp",
);
const html = fs.readFileSync(PAGE_PATH, "utf8");

const challengeSlugs = [
  "paper-bridge",
  "straw-bridge",
  "foil-boat-test",
  "paper-chain-test",
  "wind-tower-test",
  "car-ramp-distance-test",
  "ball-maze-box",
  "box-garage",
  "cup-tower",
];

function webpDimensions(file) {
  const bytes = fs.readFileSync(file);
  assert.equal(bytes.subarray(0, 4).toString(), "RIFF");
  assert.equal(bytes.subarray(8, 12).toString(), "WEBP");

  const chunk = bytes.subarray(12, 16).toString();
  if (chunk === "VP8 ") {
    assert.equal(bytes.subarray(23, 26).toString("hex"), "9d012a");
    return {
      width: bytes.readUInt16LE(26) & 0x3fff,
      height: bytes.readUInt16LE(28) & 0x3fff,
    };
  }
  if (chunk === "VP8X") {
    return {
      width: bytes.readUIntLE(24, 3) + 1,
      height: bytes.readUIntLE(27, 3) + 1,
    };
  }
  throw new Error(`Unsupported WebP chunk ${chunk}`);
}

test("preschool engineering page keeps its established URL and broadens its search target", () => {
  assert.match(html, /<title>Engineering Activities for Preschoolers \| Kid Activity Lab<\/title>/);
  assert.match(html, /<link rel="canonical" href="https:\/\/kidactivitylab\.com\/collections\/engineering-activities-for-4-year-olds\.html">/);
  assert.deepEqual(
    [...html.matchAll(/<h1>(.*?)<\/h1>/g)].map((match) => match[1]),
    ["Engineering activities for preschoolers ages 4-6."],
  );

  const targetRow = fs
    .readFileSync(path.join(ROOT, "data", "seo_keyword_targets.csv"), "utf8")
    .split("\n")
    .find((line) => line.startsWith("/collections/engineering-activities-for-4-year-olds.html,"));
  assert.ok(targetRow);
  assert.match(targetRow, /,engineering activities for preschoolers,/);
  assert.match(targetRow, /engineering activities for 4 year olds/);
});

test("page states evidence limits and does not imply measured family outcomes", () => {
  const note = html.match(/<div class="engineering-disclosure"[\s\S]*?<\/div>/)?.[0] ?? "";
  assert.match(note, /not family-tested/);
  assert.match(note, /timing, mess, engagement, learning, repeatability, and safety outcomes are unknown/);
  const openingOrder = [
    'class="callout"',
    'class="engineering-disclosure"',
    'class="engineering-visual"',
    'class="chooser"',
  ].map((marker) => html.indexOf(marker));
  assert.ok(openingOrder.every((position) => position >= 0));
  assert.deepEqual(openingOrder, [...openingOrder].sort((a, b) => a - b));
  assert.doesNotMatch(html, /tested by (?:our|Kid Activity Lab) (?:family|parents?|children)/i);
  assert.doesNotMatch(html, /<span class="tag">[^<]*(?:minutes?|mess)<\/span>/i);
  assert.doesNotMatch(html, /Searches this page is built for/i);
});

test("chooser, engineering loop, and all nine challenges are complete", () => {
  const chooser = html.match(/<tbody>([\s\S]*?)<\/tbody>/)?.[1] ?? "";
  assert.equal([...chooser.matchAll(/<tr>/g)].length, 5);
  for (const label of ["What is ready", "Start with", "Adult role"]) {
    assert.equal([...chooser.matchAll(new RegExp(`data-label="${label}"`, "g"))].length, 5);
  }
  assert.deepEqual(
    [...chooser.matchAll(/<a href="([^"]+)">([^<]+)<\/a>/g)].map((match) => [match[2], match[1]]),
    [
      ["Paper Bridge", "#paper-bridge"],
      ["Foil Boat", "#foil-boat-test"],
      ["Wind Tower", "#wind-tower-test"],
      ["Cup Doorway", "#cup-tower"],
      ["Target Ramp", "#car-ramp-distance-test"],
      ["Box Garage", "#box-garage"],
      ["Straw Bridge", "#straw-bridge"],
      ["Ball Maze", "#ball-maze-box"],
    ],
  );

  const process = html.match(/<section class="engineering-process[\s\S]*?<\/section>/)?.[0] ?? "";
  assert.deepEqual(
    [...process.matchAll(/<li><strong>(.*?)<\/strong>/g)].map((match) => match[1]),
    ["Ask", "Imagine", "Plan", "Create and test", "Improve"],
  );

  const challenges = [...html.matchAll(/<article class="seo-activity engineering-challenge" id="([^"]+)">([\s\S]*?)<\/article>/g)];
  assert.deepEqual(challenges.map((match) => match[1]), challengeSlugs);
  for (const [slug, body] of challenges.map((match) => [match[1], match[2]])) {
    for (const label of ["Kid mission:", "Adult setup:", "Test", "First change", "If the build stalls", "Stop:", "Parent check:"]) {
      assert.ok(body.includes(label), `${slug} is missing ${label}`);
    }
    assert.match(body, /Open the base activity card/);
  }
});

test("the visual and neighboring routes are explicit and bounded", () => {
  assert.equal(fs.statSync(IMAGE_PATH).size, 132732);
  assert.deepEqual(webpDimensions(IMAGE_PATH), { width: 1672, height: 941 });
  assert.match(html, /<img src="\.\.\/assets\/preschool-engineering\/engineering-challenge-materials\.webp"[^>]*width="1672" height="941">/);
  assert.match(html, /not a Kid Activity Lab family-test photo/);

  const related = html.match(/<div class="related-routes">([\s\S]*?)<\/div>/)?.[1] ?? "";
  assert.deepEqual(
    [...related.matchAll(/href="([^"]+)"/g)].map((match) => match[1]),
    [
      "../collections/building-activities-for-4-year-olds.html",
      "../collections/stem-activities-for-preschoolers.html",
      "../ages/stem-activities-for-4-year-olds.html",
    ],
  );
  assert.equal([...html.matchAll(/<section class="related engineering-sources"/g)].length, 1);
  assert.match(html, /https:\/\/www\.terc\.edu\/hse\/everyday-engineering\//);
  assert.match(html, /https:\/\/www\.headstart\.gov\/school-readiness\/teacher-time-series\/exploring-engineering-preschoolers/);
});

test("legacy activity cards retain the age-four route label", () => {
  for (const slug of challengeSlugs) {
    const card = fs.readFileSync(path.join(ROOT, "site", "cards", `${slug}.html`), "utf8");
    assert.match(
      card,
      /href="\.\.\/collections\/engineering-activities-for-4-year-olds\.html">Engineering activities for 4 year olds<\/a>/,
    );
    assert.doesNotMatch(card, /Engineering activities for preschoolers ages 4-6/);
  }
});
