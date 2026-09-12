import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import test from "node:test";

const ROOT = process.cwd();
const PAGE_PATH = path.join(ROOT, "site", "articles", "paper-bridge-challenge-kids.html");
const CARD_PATH = path.join(ROOT, "site", "cards", "paper-bridge.html");
const CARD_INDEX_PATH = path.join(ROOT, "site", "cards.html");
const IMAGE_PATH = path.join(ROOT, "site", "assets", "paper-bridge", "paper-bridge-folds.webp");
const REVIEW_PATH = path.join(ROOT, "reviews", "paper-bridge-guide-implementation-review-2026-09-12.md");
const html = fs.readFileSync(PAGE_PATH, "utf8");

test("paper bridge guide owns one singular search job", () => {
  assert.match(html, /<title>Paper Bridge Challenge for Kids \| Kid Activity Lab<\/title>/);
  assert.match(html, /<link rel="canonical" href="https:\/\/kidactivitylab\.com\/articles\/paper-bridge-challenge-kids\.html">/);
  assert.deepEqual(
    [...html.matchAll(/<h1>(.*?)<\/h1>/g)].map((match) => match[1]),
    ["Paper Bridge Challenge for Kids"],
  );
  assert.match(html, /<article class="bridge-article">/);
  const data = JSON.parse(html.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/)?.[1] ?? "{}");
  assert.equal(data["@type"], "Article");
  assert.equal(data.dateModified, "2026-09-12");
});

test("first start exposes the frozen parent decision", () => {
  const start = html.match(/<section class="bridge-start-panel"[\s\S]*?<\/section>/)?.[0] ?? "";
  for (const marker of [
    "Try it when:",
    "one sheet of paper",
    "two low closed books",
    "one large lightweight block or soft toy",
    "Adult:",
    "Child:",
    "Stop:",
    "paper tears",
  ]) {
    assert.ok(start.includes(marker), `Missing first-start marker: ${marker}`);
  }
});

test("default and controlled comparison keep their boundaries", () => {
  for (const marker of [
    'id="first-try"',
    'id="one-change"',
    "Keep the same books, gap, object, and placement",
    "four to six broad accordion folds",
    "without promising which version will hold",
    'id="troubleshooting"',
    'id="adapt"',
    'id="cleanup"',
    'id="evidence"',
  ]) {
    assert.ok(html.includes(marker), `Missing guide marker: ${marker}`);
  }
  assert.match(html, /Kid Activity Lab has not recorded a family test of this setup/);
  assert.doesNotMatch(html, /The quick verdict/);
  assert.doesNotMatch(html, /safe for (?:all|every|any) child/i);
  assert.doesNotMatch(html, /(?:family|parent|child)[ -]tested by Kid Activity Lab/i);
  assert.doesNotMatch(html, /\b\d+\s*(?:minutes?|mins?)\b/i);
  assert.match(
    fs.readFileSync(path.join(ROOT, "site", "styles.css"), "utf8"),
    /\.bridge-article \.content section\[id\] \{\s*scroll-margin-top: 104px;/,
  );
  assert.doesNotMatch(
    fs.readFileSync(path.join(ROOT, "site", "styles.css"), "utf8"),
    /(?<!\.bridge-article )\.content section\[id\]/,
  );
});

test("visual and card route agree with the guide", () => {
  const bytes = fs.readFileSync(IMAGE_PATH);
  assert.equal(bytes.subarray(0, 4).toString(), "RIFF");
  assert.equal(bytes.subarray(8, 12).toString(), "WEBP");
  assert.match(html, /paper-bridge-folds\.webp/);
  assert.match(html, /one two-book flat setup plus a fold-detail inset/);
  assert.match(html, /AI-generated setup illustration/);

  const card = fs.readFileSync(CARD_PATH, "utf8");
  assert.match(card, /href="\.\.\/articles\/paper-bridge-challenge-kids\.html">Full Paper Bridge guide<\/a>/);
  assert.match(card, /Open-ended/);
  assert.match(card, /large lightweight object/);
  assert.match(card, /Fold the paper and compare/);
  assert.doesNotMatch(card, /3 min|toy car|stronger/i);
  const related = card.match(/<section class="parent-strip" aria-label="Related activity pages">([\s\S]*?)<\/section>/)?.[1] ?? "";
  assert.equal([...related.matchAll(/<a /g)].length, 3);

  const cardIndex = fs.readFileSync(CARD_INDEX_PATH, "utf8");
  const indexEntry = cardIndex.match(/<a class="mini-card" href="cards\/paper-bridge\.html">[\s\S]*?<\/a>/)?.[0] ?? "";
  assert.match(indexEntry, /Open-ended/);
  assert.match(indexEntry, /large lightweight object/);
  assert.doesNotMatch(indexEntry, /3 min|toy car|stronger/i);
});

test("implementation review preserves baseline and after-score arithmetic", () => {
  const review = fs.readFileSync(REVIEW_PATH, "utf8");
  const rows = [...review.matchAll(/^\| [^|]+ \| (N\/A|\d+) \| (N\/A|\d+) \|/gm)];
  const before = rows.reduce((sum, row) => sum + (row[1] === "N/A" ? 0 : Number(row[1])), 0);
  const after = rows.reduce((sum, row) => sum + (row[2] === "N/A" ? 0 : Number(row[2])), 0);
  assert.equal(rows.length, 13);
  assert.equal(before, 7);
  assert.equal(after, 23);
});

test("keyword inventory and sitemap contain the guide once", () => {
  const keywords = fs.readFileSync(path.join(ROOT, "data", "seo_keyword_targets.csv"), "utf8");
  assert.equal([...keywords.matchAll(/\/articles\/paper-bridge-challenge-kids\.html/g)].length, 1);
  assert.match(keywords, /paper bridge challenge/);

  const sitemap = fs.readFileSync(path.join(ROOT, "site", "sitemap.xml"), "utf8");
  const entries = [...sitemap.matchAll(/<url>([\s\S]*?)<\/url>/g)]
    .map((match) => match[1])
    .filter((entry) => entry.includes("paper-bridge-challenge-kids.html"));
  assert.equal(entries.length, 1);
  assert.match(entries[0], /<lastmod>2026-09-12<\/lastmod>/);
});
