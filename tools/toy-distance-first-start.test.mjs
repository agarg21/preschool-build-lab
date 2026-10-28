import assert from "node:assert/strict";
import fs from "node:fs";
import { execFileSync } from "node:child_process";
import test from "node:test";

const read = path => fs.readFileSync("site/" + path, "utf8");
const card = read("cards/measuring-tape-jumps.html");
const math = [...read("collections/math-activities-for-4-year-olds-at-home.html").matchAll(/<article\b[\s\S]*?<\/article>/g)].map(m => m[0]).find(s => s.includes("<h2>Toy Distance Marks</h2>"));

test("Toy Distance complete set and early controls precede hand placement", () => {
  for (const [i, html] of [card, math].entries()) {
    assert.ok(html);
    const marker = i === 0 ? 'class="steps-grid"' : '<ol class="card-steps">';
    for (const text of ["1 intact lightweight owned nonmagnetic block", "1 large flat cardboard board", "handled by the adult", "Adult stays beside every reachable child", "test a hidden spot", "not guaranteed damage-free", "not family-tested by Kid Activity Lab", "No child jumping, toy jumping", "three short parallel strips", "These facing edges define the two gaps"]) assert.ok(html.indexOf(text) >= 0 && html.indexOf(text) < html.indexOf(marker), text);
    for (const text of ["gently place it beside the nearer", "same named starting edge", "nearer, farther or unclear", "no repeats are needed", "removes and collects every tape strip", "qualitative gap comparison", "not an inspected source procedure"]) assert.ok(html.includes(text), text);
    assert.equal((html.match(i === 0 ? /class="step-tile"/g : /<li>/g) || []).length, 3);
    assert.doesNotMatch(html, /\b5 min\b|Jump a toy\.|See where it lands\.|Try again\.|active math|medium help|low mess/);
  }
});

test("Toy Distance compact materials and scoped heading fit remain explicit", () => {
  const section = card.match(/<section class="parent-strip toy-distance-readiness"[\s\S]*?<\/section>/)?.[0];
  assert.ok(section);
  assert.doesNotMatch(section, /<details\b|<[^>]*\shidden\b|<[^>]*\saria-hidden=/);
  assert.match(section, /test a hidden spot/);
  for (const label of ["Materials", "Adult and space", "Fit or skip", "Evidence", "Stop"]) assert.ok(section.includes("<strong>" + label + ":</strong>"));
  assert.doesNotMatch(card, /class="meta-tile"/);
  assert.match(card, /class="kid-card toy-distance-card"/);
  assert.match(read("styles.css"), /\.toy-distance-card h1 \{\s*font-size: 1\.7rem/);
  assert.match(read("styles.css"), /\.toy-distance-card \.steps-grid \{\s*grid-template-columns: 1fr/);
});

test("actual three Toy Distance renderers match the generated files", () => {
  const script = `import json,sys
sys.path.insert(0,'scripts')
import generate_card_pages as c
import generate_seo_pages as s
from contributor_pages import with_contributor_credit
assert 'measuring-tape-jumps' in c.QUICK_CARD_SLUGS
out={'cards/measuring-tape-jumps.html':c.quick_page('measuring-tape-jumps'),'cards.html':c.cards_index()}
for p in s.PAGES:
 if 'measuring-tape-jumps' in p.get('activities',[]):
  assert 'measuring-tape-jumps' not in p.get('activity_overrides',{})
  out[p['path']]=s.page_html(p)
print(json.dumps({p:with_contributor_credit(h,p) for p,h in out.items()}))`;
  const out = JSON.parse(execFileSync("python3", ["-B", "-c", script], { encoding: "utf8", maxBuffer: 8 * 1024 * 1024 }));
  assert.equal(Object.keys(out).length, 3);
  for (const [path, html] of Object.entries(out)) assert.equal(html, read(path), path);
});

test("Toy Distance preserves URL, legacy finder access, routing and inventories", () => {
  assert.match(card, /<h1>Toy Distance Marks<\/h1>/);
  assert.match(card, /rel="canonical" href="https:\/\/kidactivitylab.com\/cards\/measuring-tape-jumps.html"/);
  assert.match(card, /math-activities-for-4-year-olds-at-home.html">Math activities/);
  const entry = read("cards.html").match(/<a class="mini-card" href="cards\/measuring-tape-jumps.html">[\s\S]*?<\/a>/)?.[0];
  assert.match(entry, /<strong>Toy Distance Marks<\/strong>/);
  assert.match(entry, /Place by hand; compare marked gaps \| Open-ended/);
  assert.match(entry, /<template data-search="[^"]*Measuring Tape Jumps"/);
  assert.equal((read("cards.html").match(/class="mini-card"/g) || []).length, 36);
  assert.equal((read("sitemap.xml").match(/<loc>/g) || []).length, 67);
  assert.ok(read("sitemap.xml").includes("cards/measuring-tape-jumps.html</loc>\n    <lastmod>2026-10-27</lastmod>"));
});
