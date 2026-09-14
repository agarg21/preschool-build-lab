import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import test from "node:test";

const ROOT = process.cwd();
const PAGE_PATH = path.join(ROOT, "site", "articles", "cardboard-ball-maze-kids.html");
const CARD_PATH = path.join(ROOT, "site", "cards", "ball-maze-box.html");
const CARD_INDEX_PATH = path.join(ROOT, "site", "cards.html");
const IMAGE_PATH = path.join(ROOT, "site", "assets", "ball-maze", "ball-maze-box-guide.webp");
const REVIEW_PATH = path.join(ROOT, "reviews", "ball-maze-guide-implementation-review-2026-09-14.md");
const html = fs.readFileSync(PAGE_PATH, "utf8");

test("ball maze guide owns one singular search job", () => {
  assert.match(html, /<title>Cardboard Ball Maze for Kids \| Kid Activity Lab<\/title>/);
  assert.match(html, /<link rel="canonical" href="https:\/\/kidactivitylab\.com\/articles\/cardboard-ball-maze-kids\.html">/);
  assert.deepEqual(
    [...html.matchAll(/<h1>(.*?)<\/h1>/g)].map((match) => match[1]),
    ["Cardboard Ball Maze for Kids"],
  );
  assert.match(html, /<article class="maze-article">/);
  const data = JSON.parse(html.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/)?.[1] ?? "{}");
  assert.equal(data["@type"], "Article");
  assert.equal(data.dateModified, "2026-09-14");
});

test("first start exposes the frozen parent decision", () => {
  const start = html.match(/<section class="maze-start-panel"[\s\S]*?<\/section>/)?.[0] ?? "";
  for (const marker of [
    "Try it when:",
    "one shallow intact box lid",
    "three chunky blocks",
    "one large lightweight foam ball",
    "Adult:",
    "Child:",
    "Mission:",
    "Stop:",
    "shaken hard",
  ]) {
    assert.ok(start.includes(marker), `Missing first-start marker: ${marker}`);
  }
});

test("wide path and one-wall change keep their boundaries", () => {
  for (const marker of [
    'id="first-run"',
    'id="one-wall"',
    "Move only the third wall",
    "no learning or engagement outcome is assumed",
    'id="troubleshooting"',
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
  assert.doesNotMatch(html, /marble|bead|ping-pong|scissors|hot glue/i);
  assert.match(
    fs.readFileSync(path.join(ROOT, "site", "styles.css"), "utf8"),
    /\.maze-article section\[id\] \{\s*scroll-margin-top: 104px;/,
  );
});

test("visual and compact routes agree with the guide", () => {
  const bytes = fs.readFileSync(IMAGE_PATH);
  assert.equal(bytes.subarray(0, 4).toString(), "RIFF");
  assert.equal(bytes.subarray(8, 12).toString(), "WEBP");
  assert.match(html, /ball-maze-box-guide\.webp/);
  assert.match(html, /intact shallow cardboard lid with three loose chunky block walls/);
  assert.match(html, /AI-generated setup illustration/);

  const card = fs.readFileSync(CARD_PATH, "utf8");
  assert.match(card, /href="\.\.\/articles\/cardboard-ball-maze-kids\.html">Full Cardboard Ball Maze guide<\/a>/);
  assert.match(card, /Open-ended/);
  assert.match(card, /large lightweight ball/);
  assert.match(card, /Set three blocks as wide walls/);
  assert.doesNotMatch(card, /8 min|ping-pong|planning, slopes, hand control/i);
  const related = card.match(/<section class="parent-strip" aria-label="Related activity pages">([\s\S]*?)<\/section>/)?.[1] ?? "";
  assert.equal([...related.matchAll(/<a /g)].length, 2);

  const cardIndex = fs.readFileSync(CARD_INDEX_PATH, "utf8");
  const indexEntry = cardIndex.match(/<a class="mini-card" href="cards\/ball-maze-box\.html">[\s\S]*?<\/a>/)?.[0] ?? "";
  assert.match(indexEntry, /Open-ended/);
  assert.match(indexEntry, /large lightweight ball/);
  assert.doesNotMatch(indexEntry, /8 min|ping-pong/i);
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
  assert.equal([...keywords.matchAll(/\/articles\/cardboard-ball-maze-kids\.html/g)].length, 1);
  assert.match(keywords, /cardboard ball maze/);

  const sitemap = fs.readFileSync(path.join(ROOT, "site", "sitemap.xml"), "utf8");
  const entries = [...sitemap.matchAll(/<url>([\s\S]*?)<\/url>/g)]
    .map((match) => match[1])
    .filter((entry) => entry.includes("cardboard-ball-maze-kids.html"));
  assert.equal(entries.length, 1);
  assert.match(entries[0], /<lastmod>2026-09-14<\/lastmod>/);
});
