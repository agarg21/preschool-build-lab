import assert from "node:assert/strict";
import fs from "node:fs";
import { execFileSync } from "node:child_process";
import test from "node:test";

const read = path => fs.readFileSync("site/" + path, "utf8");
const card = read("cards/pattern-path.html");
const owners = ["ages/stem-activities-for-4-year-olds.html", "collections/math-activities-for-4-year-olds-at-home.html", "collections/no-prep-stem-activities-for-4-year-olds.html"];
const entries = owners.map(path => [...read(path).matchAll(/<article\b[\s\S]*?<\/article>/g)].map(m => m[0]).find(s => s.includes("<h2>Pattern Path</h2>")));

test("Pattern Path complete choices and early fit reach all four instruction owners", () => {
  for (const [i, html] of [card, ...entries].entries()) {
    assert.ok(html);
    const marker = i === 0 ? 'class="steps-grid"' : '<ol class="card-steps">';
    for (const text of ["6 intact lightweight nonmagnetic blocks", "3 of kind A and 3 of kind B", "not family-tested by Kid Activity Lab", "Size alone is not assurance", "not a walking path", "Adult stays beside every reachable child", "A-B-A-B", "Offer the remaining A and B together"]) assert.ok(html.indexOf(text) >= 0 && html.indexOf(text) < html.indexOf(marker), text);
    for (const text of ["No color names are needed", "one supported retry", "Matching is not a completed repeating pattern", "not drill or assess", "collects and stores all blocks", "not a tested setup"]) assert.ok(html.includes(text), text);
    assert.equal((html.match(i === 0 ? /class="step-tile"/g : /<li>/g) || []).length, 3);
    assert.doesNotMatch(html, /\b4 min\b|Pick two colors\.|Make a path\.|Say the pattern\.|Use pieces too large to mouth/);
  }
});

test("Pattern Path compact readiness and narrow math H1 wrap stay explicit", () => {
  const section = card.match(/<section class="parent-strip pattern-path-readiness"[\s\S]*?<\/section>/)?.[0];
  assert.ok(section);
  assert.doesNotMatch(section, /<details|hidden|aria-hidden/);
  for (const label of ["Materials", "Adult and space", "Fit or skip", "Evidence", "Stop"]) assert.ok(section.includes("<strong>" + label + ":</strong>"));
  assert.doesNotMatch(card, /class="meta-tile"/);
  assert.match(card, /class="kid-card pattern-path-card"/);
  assert.match(read("styles.css"), /\.pattern-path-card \.steps-grid \{\s*grid-template-columns: 1fr/);
  assert.match(read("styles.css"), /#continue-a-pattern \{\s*scroll-margin-top: max\(104px, 6rem\)/);
  assert.match(read(owners[1]), /<style>\.hero h1 \{ overflow-wrap: anywhere; \}<\/style>/);
  for (const path of [owners[0], owners[2], "collections/stem-activities-for-preschoolers.html"]) assert.doesNotMatch(read(path), /<style>\.hero h1 \{ overflow-wrap: anywhere; \}<\/style>/);
});

test("actual five Pattern Path renderers match committed output surfaces", () => {
  const script = `import json,sys
sys.path.insert(0,'scripts')
import generate_card_pages as c
import generate_seo_pages as s
from contributor_pages import with_contributor_credit
assert 'pattern-path' in c.QUICK_CARD_SLUGS
out={'cards/pattern-path.html':c.quick_page('pattern-path'),'cards.html':c.cards_index()}
for p in s.PAGES:
 if 'pattern-path' in p.get('activities',[]):
  assert 'pattern-path' not in p.get('activity_overrides',{})
  out[p['path']]=s.page_html(p)
print(json.dumps({p:with_contributor_credit(h,p) for p,h in out.items()}))`;
  const out = JSON.parse(execFileSync("python3", ["-B", "-c", script], { encoding: "utf8", maxBuffer: 8 * 1024 * 1024 }));
  assert.equal(Object.keys(out).length, 5);
  for (const [path, html] of Object.entries(out)) assert.equal(html, read(path), path);
});

test("Pattern Path keeps identity, maintained depth ownership and inventories", () => {
  assert.match(card, /<h1>Pattern Path<\/h1>/);
  assert.match(card, /rel="canonical" href="https:\/\/kidactivitylab.com\/cards\/pattern-path.html"/);
  for (const html of [card, ...entries]) assert.match(html, /stem-activities-for-preschoolers.html#continue-a-pattern/);
  const preschool = read("collections/stem-activities-for-preschoolers.html");
  assert.match(preschool, /id="continue-a-pattern"/);
  assert.match(preschool, /four-piece A-B-A-B start/);
  assert.match(preschool, /Stop after one correct extension or one supported retry/);
  assert.equal((read("cards.html").match(/class="mini-card"/g) || []).length, 36);
  assert.match(read("cards.html"), /Adult sets ABAB; choose or point once \| Open-ended/);
  assert.equal((read("sitemap.xml").match(/<loc>/g) || []).length, 67);
  for (const path of ["cards/pattern-path.html", owners[1]]) assert.ok(read("sitemap.xml").includes(path + "</loc>\n    <lastmod>2026-10-27</lastmod>"));
});
