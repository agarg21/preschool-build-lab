import assert from "node:assert/strict";
import fs from "node:fs";
import test from "node:test";

const html = fs.readFileSync("site/articles/paper-cup-tower-kids.html", "utf8");
const card = fs.readFileSync("site/cards/cup-tower.html", "utf8");

test("cup tower has one article owner and factual schema", () => {
  assert.match(html, /rel="canonical" href="https:\/\/kidactivitylab.com\/articles\/paper-cup-tower-kids.html"/);
  assert.equal([...html.matchAll(/<h1>/g)].length, 1);
  const schema = JSON.parse(html.match(/application\/ld\+json">([\s\S]*?)<\/script>/)[1]);
  assert.equal(schema["@type"], "Article");
  assert.equal(schema.dateModified, "2026-09-17");
});

test("cup tower exposes fit and runnable start before illustrative image", () => {
  const panel = html.match(/<section class="bridge-start-panel"[\s\S]*?<\/section>/)[0];
  for (const marker of ["Try it when:", "two matching intact lightweight paper cups", "two closed bottoms touching", "Adult:", "Child:", "Stop:", "mouthing", "damaged cups"]) {
    assert.ok(panel.includes(marker), marker);
  }
  assert.ok(html.indexOf(panel) < html.indexOf('<figure class="hero-image">'));
});

test("cup tower has proportionate rescue adaptation and evidence boundaries", () => {
  for (const id of ["first-try", "one-change", "rescue", "fit", "cleanup", "evidence"]) assert.ok(html.includes(`id="${id}"`));
  for (const marker of ["That is nesting", "side by side", "wide rim meeting", "remove the top cup first", "not a safety assurance", "has not recorded a family test", "Duration and mess have not been measured", "not automatically interchangeable"]) assert.ok(html.includes(marker), marker);
  assert.doesNotMatch(html, /safe for (?:all|every)|\b\d+\s*minutes?\b|guaranteed learning|FIRST-FSA/i);
});

test("cup card remains compact and agrees with guide without video detour", () => {
  assert.match(card, /Full Paper Cup Tower guide/);
  assert.match(card, /bottom-to-bottom/);
  assert.match(card, /Research-backed, not family-tested/);
  assert.match(card, /Not measured/);
  assert.doesNotMatch(card, /1 minute|low mess|<iframe|age 3-5/);
  const index = fs.readFileSync("site/cards.html", "utf8");
  const entry = index.match(/<a class="mini-card" href="cards\/cup-tower.html">[\s\S]*?<\/a>/)[0];
  assert.match(entry, /Open-ended/);
  assert.match(entry, /2 matching lightweight paper cups/);
});

test("cup tower visual and index inventory match one guide", () => {
  const bytes = fs.readFileSync("site/assets/cup-tower/paper-cup-start.webp");
  assert.equal(bytes.subarray(0, 4).toString(), "RIFF");
  assert.equal(bytes.subarray(8, 12).toString(), "WEBP");
  assert.match(html, /AI-generated setup illustration/);
  const keywords = fs.readFileSync("data/seo_keyword_targets.csv", "utf8");
  assert.equal([...keywords.matchAll(/\/articles\/paper-cup-tower-kids.html/g)].length, 1);
  const sitemap = fs.readFileSync("site/sitemap.xml", "utf8");
  assert.equal([...sitemap.matchAll(/\/articles\/paper-cup-tower-kids.html/g)].length, 1);
});

test("cup tower proxy score is consistent and not family evidence", () => {
  const review = fs.readFileSync("reviews/paper-cup-tower-guide-implementation-review-2026-09-17.md", "utf8");
  const rows = [...review.matchAll(/^\| [^|]+ \| (N\/A|\d+) \| (N\/A|\d+) \|/gm)];
  assert.equal(rows.length, 13);
  assert.equal(rows.reduce((s, r) => s + (r[1] === "N/A" ? 0 : +r[1]), 0), 4);
  assert.equal(rows.reduce((s, r) => s + (r[2] === "N/A" ? 0 : +r[2]), 0), 23);
  assert.match(review, /not evidence of/);
});
