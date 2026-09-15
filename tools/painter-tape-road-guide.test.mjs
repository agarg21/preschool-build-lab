import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import test from "node:test";

const ROOT = process.cwd();
const PAGE_PATH = path.join(ROOT, "site", "articles", "painter-tape-road-kids.html");
const ROAD_CARD_PATH = path.join(ROOT, "site", "cards", "tape-road.html");
const CITY_CARD_PATH = path.join(ROOT, "site", "cards", "tape-city.html");
const CARD_INDEX_PATH = path.join(ROOT, "site", "cards.html");
const IMAGE_PATH = path.join(ROOT, "site", "assets", "tape-road", "painter-tape-road-guide.webp");
const REVIEW_PATH = path.join(ROOT, "reviews", "painter-tape-road-guide-implementation-review-2026-09-15.md");
const html = fs.readFileSync(PAGE_PATH, "utf8");

test("Painter's Tape Road guide owns one singular search job", () => {
  assert.match(html, /<title>Painter's Tape Road for Kids \| Kid Activity Lab<\/title>/);
  assert.match(html, /<link rel="canonical" href="https:\/\/kidactivitylab\.com\/articles\/painter-tape-road-kids\.html">/);
  assert.deepEqual(
    [...html.matchAll(/<h1>(.*?)<\/h1>/g)].map((match) => match[1]),
    ["Painter's Tape Road for Kids"],
  );
  assert.match(html, /<article class="road-article">/);
  const data = JSON.parse(html.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/)?.[1] ?? "{}");
  assert.equal(data["@type"], "Article");
  assert.equal(data.dateModified, "2026-09-15");
});

test("first start exposes the frozen parent decision", () => {
  const start = html.match(/<section class="road-start-panel"[\s\S]*?<\/section>/)?.[0] ?? "";
  for (const marker of [
    "Try it when:",
    "surface-appropriate removable painter's tape",
    "one or two large intact toy vehicles",
    "Test one strip in an inconspicuous area and remove it",
    "large cardboard sheet, table, or tray",
    "Adult:",
    "Child:",
    "parking box",
    "Stop:",
    "any change to the surface",
  ]) {
    assert.ok(start.includes(marker), `Missing first-start marker: ${marker}`);
  }
});

test("route, change, rescue, adaptation, cleanup, and evidence keep their boundaries", () => {
  for (const marker of [
    'id="one-road"',
    'id="one-change"',
    "Keep the same surface, vehicle, starting place, and parking box",
    "no engagement or learning outcome is assumed",
    'id="troubleshooting"',
    "The vehicle does not fit the parking box",
    "widens the parking box",
    'id="adapt"',
    'id="cleanup"',
    'id="evidence"',
  ]) {
    assert.ok(html.includes(marker), `Missing guide marker: ${marker}`);
  }
  assert.match(html, /Kid Activity Lab has not recorded a family test of this setup/);
  assert.doesNotMatch(html, /safe for (?:all|every|any) child/i);
  assert.doesNotMatch(html, /(?:family|parent|child)[ -]tested by Kid Activity Lab/i);
  assert.doesNotMatch(html, /\b\d+\s*(?:minutes?|mins?)\b/i);
  assert.doesNotMatch(html, /will (?:love|learn|enjoy|stay busy)/i);
  assert.match(
    fs.readFileSync(path.join(ROOT, "site", "styles.css"), "utf8"),
    /\.road-article section\[id\] \{\s*scroll-margin-top: 104px;/,
  );
});

test("visual and both compact cards agree with one guide owner", () => {
  const bytes = fs.readFileSync(IMAGE_PATH);
  assert.equal(bytes.subarray(0, 4).toString(), "RIFF");
  assert.equal(bytes.subarray(8, 12).toString(), "WEBP");
  assert.match(html, /painter-tape-road-guide\.webp/);
  assert.match(html, /short blue painter's tape road and parking box on a removable cardboard board/);
  assert.match(html, /AI-generated setup illustration/);

  const roadCard = fs.readFileSync(ROAD_CARD_PATH, "utf8");
  const cityCard = fs.readFileSync(CITY_CARD_PATH, "utf8");
  assert.match(roadCard, /href="\.\.\/articles\/painter-tape-road-kids\.html">Full Painter&#x27;s Tape Road guide<\/a>/);
  assert.match(cityCard, /href="\.\.\/articles\/painter-tape-road-kids\.html">Start with the Painter&#x27;s Tape Road guide<\/a>/);
  for (const card of [roadCard, cityCard]) {
    assert.match(card, /Open-ended/);
    assert.match(card, /Adult (?:chooses|applies)/);
    assert.doesNotMatch(card, /3 minutes|5 minutes|masking tape;<\/div>/i);
  }

  const cardIndex = fs.readFileSync(CARD_INDEX_PATH, "utf8");
  for (const slug of ["tape-road", "tape-city"]) {
    const entry = cardIndex.match(new RegExp(`<a class="mini-card" href="cards\\/${slug}\\.html">[\\s\\S]*?<\\/a>`))?.[0] ?? "";
    assert.match(entry, /Open-ended/);
    assert.match(entry, /surface-appropriate painter&#x27;s tape/);
  }
});

test("implementation review preserves baseline and after-score arithmetic", () => {
  const review = fs.readFileSync(REVIEW_PATH, "utf8");
  const rows = [...review.matchAll(/^\| [^|]+ \| (N\/A|\d+) \| (N\/A|\d+) \|/gm)];
  const before = rows.reduce((sum, row) => sum + (row[1] === "N/A" ? 0 : Number(row[1])), 0);
  const after = rows.reduce((sum, row) => sum + (row[2] === "N/A" ? 0 : Number(row[2])), 0);
  assert.equal(rows.length, 13);
  assert.equal(before, 5);
  assert.ok(after >= 22);
});

test("keyword inventory and sitemap contain the guide once", () => {
  const keywords = fs.readFileSync(path.join(ROOT, "data", "seo_keyword_targets.csv"), "utf8");
  assert.equal([...keywords.matchAll(/\/articles\/painter-tape-road-kids\.html/g)].length, 1);
  assert.match(keywords, /masking tape road/);

  const sitemap = fs.readFileSync(path.join(ROOT, "site", "sitemap.xml"), "utf8");
  const entries = [...sitemap.matchAll(/<url>([\s\S]*?)<\/url>/g)]
    .map((match) => match[1])
    .filter((entry) => entry.includes("painter-tape-road-kids.html"));
  assert.equal(entries.length, 1);
  assert.match(entries[0], /<lastmod>2026-09-15<\/lastmod>/);
});
