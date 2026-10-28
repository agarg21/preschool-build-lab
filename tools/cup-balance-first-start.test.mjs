import assert from "node:assert/strict";
import fs from "node:fs";
import { execFileSync } from "node:child_process";
import test from "node:test";

const read = path => fs.readFileSync("site/" + path, "utf8");
const card = read("cards/balance-scale-baskets.html");
const math = [...read("collections/math-activities-for-4-year-olds-at-home.html").matchAll(/<article\b[\s\S]*?<\/article>/g)].map(m => m[0]).find(s => s.includes("<h2>Cup Balance Watch</h2>"));

test("Cup Balance complete assembly and empty baseline precede loading", () => {
  for (const [i, html] of [card, math].entries()) {
    assert.ok(html);
    const marker = i === 0 ? 'class="steps-grid"' : '<ol class="card-steps">';
    for (const text of ["plastic hanger with symmetric notches", "2 matching paper cups", "adult scissors and hole punch", "every reachable child", "beyond reach of yarn", "not family-tested by Kid Activity Lab", "Adult alone holds the central hook", "equal hanging lengths", "Start EMPTY", "uneven, touching, binding or unclear", "No door, cabinet, pencil or book supports"]) assert.ok(html.indexOf(text) >= 0 && html.indexOf(text) < html.indexOf(marker), text);
    assert.ok(html.indexOf("Adult setup:") < html.indexOf(marker));
    for (const text of ["rests both cups on the floor before adding", "at most one checked object to each", "left lower, right lower, roughly level or unclear", "not proof of equal weight", "uncalibrated", "disassembles the yarn handles", "not safety thresholds or load ratings", "editorial adaptations, not a tested setup"]) assert.ok(html.includes(text), text);
    assert.equal((html.match(i === 0 ? /class="step-tile"/g : /<li>/g) || []).length, 3);
    assert.doesNotMatch(html, /\b7 min\b|Try to balance\.|safe objects|low mess|medium help/);
  }
});

test("Cup Balance early controls and compact layout are not hidden", () => {
  const section = card.match(/<section class="parent-strip cup-balance-readiness"[\s\S]*?<\/section>/)?.[0];
  assert.ok(section);
  assert.doesNotMatch(section, /<details\b|<[^>]*\shidden\b|<[^>]*\saria-hidden=/);
  for (const label of ["Materials", "Adult and space", "Evidence", "Stop"]) assert.ok(section.includes("<strong>" + label + ":</strong>"));
  assert.doesNotMatch(card, /class="meta-tile"/);
  assert.match(card, /class="kid-card cup-balance-card"/);
  assert.match(read("styles.css"), /\.cup-balance-card h1 \{\s*font-size: 1\.7rem/);
  assert.match(read("styles.css"), /\.cup-balance-card \.steps-grid \{\s*grid-template-columns: 1fr/);
});

test("actual three Cup Balance renderers match generated files", () => {
  const script = `import json,sys
sys.path.insert(0,'scripts')
import generate_card_pages as c
import generate_seo_pages as s
from contributor_pages import with_contributor_credit
assert 'balance-scale-baskets' in c.QUICK_CARD_SLUGS
out={'cards/balance-scale-baskets.html':c.quick_page('balance-scale-baskets'),'cards.html':c.cards_index()}
for p in s.PAGES:
 if 'balance-scale-baskets' in p.get('activities',[]):
  assert 'balance-scale-baskets' not in p.get('activity_overrides',{})
  out[p['path']]=s.page_html(p)
print(json.dumps({p:with_contributor_credit(h,p) for p,h in out.items()}))`;
  const out = JSON.parse(execFileSync("python3", ["-B", "-c", script], { encoding: "utf8", maxBuffer: 8 * 1024 * 1024 }));
  assert.equal(Object.keys(out).length, 3);
  for (const [path, html] of Object.entries(out)) assert.equal(html, read(path), path);
});

test("Cup Balance keeps URL, legacy finder, math route and inventories", () => {
  assert.match(card, /<h1>Cup Balance Watch<\/h1>/);
  assert.match(card, /rel="canonical" href="https:\/\/kidactivitylab.com\/cards\/balance-scale-baskets.html"/);
  assert.match(card, /math-activities-for-4-year-olds-at-home.html">Math activities/);
  const entry = read("cards.html").match(/<a class="mini-card" href="cards\/balance-scale-baskets.html">[\s\S]*?<\/a>/)?.[0];
  assert.match(entry, /<strong>Cup Balance Watch<\/strong>/);
  assert.match(entry, /Adult holds and loads; child watches \| Open-ended/);
  assert.match(entry, /<template data-search="[^"]*Balance Basket Scale"/);
  assert.equal((read("cards.html").match(/class="mini-card"/g) || []).length, 36);
  assert.equal((read("sitemap.xml").match(/<loc>/g) || []).length, 66);
  assert.ok(read("sitemap.xml").includes("cards/balance-scale-baskets.html</loc>\n    <lastmod>2026-10-27</lastmod>"));
});
