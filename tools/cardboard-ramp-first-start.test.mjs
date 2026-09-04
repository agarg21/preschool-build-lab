import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import test from "node:test";

const ROOT = process.cwd();
const PAGE_PATH = path.join(
  ROOT,
  "site",
  "articles",
  "cardboard-box-car-ramp-preschoolers.html",
);
const IMAGE_PATH = path.join(
  ROOT,
  "site",
  "assets",
  "cardboard-box-car-ramp-hero-v2.png",
);
const html = fs.readFileSync(PAGE_PATH, "utf8");

function pngDimensions(file) {
  const bytes = fs.readFileSync(file);
  assert.equal(bytes.subarray(1, 4).toString(), "PNG");
  assert.equal(bytes.subarray(12, 16).toString(), "IHDR");
  return {
    width: bytes.readUInt32BE(16),
    height: bytes.readUInt32BE(20),
  };
}

test("cardboard ramp keeps its established search ownership", () => {
  assert.match(
    html,
    /<title>How to Make a Cardboard Ramp for Toy Cars \| Kid Activity Lab<\/title>/,
  );
  assert.match(
    html,
    /<link rel="canonical" href="https:\/\/kidactivitylab\.com\/articles\/cardboard-box-car-ramp-preschoolers\.html">/,
  );
  assert.deepEqual(
    [...html.matchAll(/<h1>(.*?)<\/h1>/g)].map((match) => match[1]),
    ["How to make a cardboard ramp for toy cars."],
  );

  const structuredData = JSON.parse(
    html.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/)?.[1] ?? "{}",
  );
  assert.equal(structuredData.dateModified, "2026-09-04");
  assert.equal(
    structuredData.image,
    "https://kidactivitylab.com/assets/cardboard-box-car-ramp-hero-v2.png",
  );
});

test("the runnable three-step start appears before the illustrative image", () => {
  const start = html.match(
    /<div class="content ramp-first-start">([\s\S]*?)<\/div>\s*<figure class="hero-image">/,
  )?.[1] ?? "";
  assert.match(start, /<h2>Start now: make a cardboard ramp<\/h2>/);
  assert.match(start, /one flat, stiff piece of cardboard/);
  assert.match(start, /two broad sturdy closed books/);
  assert.match(start, /one or more toy cars/);
  assert.equal([...start.matchAll(/<li>/g)].length, 3);
  assert.match(start, /<strong>Adult job:<\/strong>/);
  assert.match(start, /Stop if anyone starts climbing on or throwing the setup/);

  const startIndex = html.indexOf('class="content ramp-first-start"');
  const imageIndex = html.indexOf('class="hero-image"');
  const verdictIndex = html.indexOf("<h2>Quick Verdict</h2>");
  assert.ok(startIndex >= 0 && imageIndex > startIndex && verdictIndex > imageIndex);
});

test("the visual matches the bounded two-book setup and states its evidence limit", () => {
  assert.deepEqual(pngDimensions(IMAGE_PATH), { width: 1672, height: 941 });
  assert.equal(
    [...html.matchAll(/cardboard-box-car-ramp-hero-v2\.png/g)].length,
    2,
  );
  assert.doesNotMatch(html, /cardboard-box-car-ramp-hero\.png/);
  assert.match(
    html,
    /<img src="\.\.\/assets\/cardboard-box-car-ramp-hero-v2\.png"[^>]*width="1672" height="941">/,
  );
  assert.match(
    html,
    /AI-generated illustrative setup image; not a Kid Activity Lab family-test photo/,
  );
});

test("the materials and boundaries remain specific without claiming outcomes", () => {
  assert.match(html, /Two broad, sturdy closed books for a low support/);
  assert.match(
    html,
    /If a younger child can reach the setup, use only toys appropriate for every child present and supervise directly/,
  );
  assert.match(html, /Use the floor, not stairs or furniture/);
  assert.match(html, /Stop if the setup becomes climbing or throwing play/);
  assert.match(html, /Kid Activity Lab has not recorded a parent test of this page/);
  assert.doesNotMatch(html, /(?:family|parent|child)[ -]tested by Kid Activity Lab/i);
  assert.doesNotMatch(html, /safe for (?:all|every|any) child/i);
});

test("the deeper activity and neighboring routes remain available", () => {
  for (const marker of [
    'id="one-change-test"',
    "Cardboard ramp troubleshooting",
    "Turn the ramp into free play",
    "Cleanup",
    "FAQ",
    "Next projects to build",
  ]) {
    assert.ok(html.includes(marker), `Missing preserved marker: ${marker}`);
  }
  for (const source of [
    "pnc.com/en/about-pnc/corporate-responsibility/grow-up-great/lesson-center/transportation/rolling-with-ramps.html",
    "peepandthebigwideworld.com/en/educators/curriculum/family-child-care-educators/ramps/activity/guided-activity/244/roll-or-slide-indoors/",
    "pbs.org/video/cars-ramps-jlzsqr/",
  ]) {
    assert.ok(html.includes(source), `Missing preserved source: ${source}`);
  }

  const related = html.match(
    /<section class="related" aria-label="Related projects">([\s\S]*?)<\/section>/,
  )?.[1] ?? "";
  assert.deepEqual(
    [...related.matchAll(/href="([^"]+)"/g)].map((match) => match[1]),
    [
      "../cards/cardboard-car-ramp.html",
      "../collections/original-stem-activities-for-4-year-olds.html#ramp-detective",
      "../ages/stem-activities-for-4-year-olds.html",
      "../ages/activities-for-4-year-olds-at-home.html",
    ],
  );
});

test("sitemap records the ramp page update once", () => {
  const sitemap = fs.readFileSync(path.join(ROOT, "site", "sitemap.xml"), "utf8");
  const entries = [...sitemap.matchAll(/<url>([\s\S]*?)<\/url>/g)]
    .map((match) => match[1])
    .filter((entry) => entry.includes("cardboard-box-car-ramp-preschoolers.html"));
  assert.equal(entries.length, 1);
  assert.match(entries[0], /<lastmod>2026-09-04<\/lastmod>/);
});
