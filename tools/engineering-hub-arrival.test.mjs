import assert from "node:assert/strict";
import fs from "node:fs";
import test from "node:test";

const html = fs.readFileSync("site/collections/engineering-activities-for-4-year-olds.html", "utf8");
const css = fs.readFileSync("site/styles.css", "utf8");
const card = fs.readFileSync("site/cards/paper-chain-test.html", "utf8");
const sitemap = fs.readFileSync("site/sitemap.xml", "utf8");

test("paper-chain book route keeps its owner and mission", () => {
  assert.match(card, /engineering-activities-for-4-year-olds\.html#paper-chain-test/);
  assert.match(html, /<article class="seo-activity engineering-challenge" id="paper-chain-test">/);
  assert.match(html, /<h2>Paper Chain Reach Test<\/h2>/);
  assert.match(html, /Build a paper chain long enough to wrap around the book and meet at the top/);
});

test("engineering hub ships its scoped readable-arrival styles", () => {
  assert.match(html, /styles\.css\?v=engineering-arrival-1/);
  assert.match(css, /\.engineering-hero h1\s*\{[^}]*overflow-wrap:\s*anywhere;/);
  assert.match(css, /@media \(max-width: 640px\)\s*\{\s*\.engineering-hero h1\s*\{\s*font-size:\s*1\.5rem;/);
  assert.match(css, /@media \(max-width: 350px\)\s*\{\s*\.engineering-hero h1\s*\{\s*font-size:\s*1\.4rem;/);
  assert.match(css, /\.engineering-page \[id\]\s*\{[^}]*scroll-margin-top:\s*7rem;/);
  assert.match(sitemap, /<loc>https:\/\/kidactivitylab\.com\/collections\/engineering-activities-for-4-year-olds\.html<\/loc>\s*<lastmod>2026-10-07<\/lastmod>/);
});
