import assert from "node:assert/strict";
import fs from "node:fs";
import { execFileSync } from "node:child_process";
import test from "node:test";

const read = path => fs.readFileSync(`site/${path}`, "utf8");
const card = read("cards/wind-tower-test.html");
const block = (path, heading) => [...read(path).matchAll(/<article\b[\s\S]*?<\/article>/g)].map(m => m[0]).find(s => s.includes(`<h2>${heading}</h2>`));
const age = block("ages/stem-activities-for-4-year-olds.html", "Windproof Tower");
const engineering = block("collections/engineering-activities-for-4-year-olds.html", "Wind Tower");
const pack = block("collections/original-stem-activities-for-4-year-olds.html", "Windproof Tower");

test("Wind Tower complete materials and adult control precede all child action", () => {
  for (const [i, html] of [card, age, engineering, pack].entries()) {
    assert.ok(html);
    const marker = i === 0 ? 'class="steps-grid"' : i === 3 ? "<h3>Read-aloud kid steps</h3>" : '<ol class="card-steps">';
    for (const text of ["6 matching intact lightweight nonmagnetic blocks", "1 adult-prepared folded paper fan", "not family-tested by Kid Activity Lab", "fan stops and pieces settle", "fan contact risk", "No electric fan", "Counts, layout and waves are editorial choices", "three-block base", "no more than two layers"]) assert.ok(html.indexOf(text) >= 0 && html.indexOf(text) < html.indexOf(marker), text);
    for (const text of ["standing, moved, fell or unclear", "without touching blocks or people", "Stop sooner if pieces move or fall", "force is not calibrated", "clears the floor", "not a tested setup"]) assert.ok(html.includes(text), text);
    const steps = i === 0 ? html.match(/<section class="steps-grid"[\s\S]*?<\/section>/)?.[0] : i === 3 ? html.match(/<ol>[\s\S]*?<\/ol>/)?.[0] : html.match(/<ol class="card-steps">[\s\S]*?<\/ol>/)?.[0];
    assert.equal((steps.match(i === 0 ? /class="step-tile"/g : /<li>/g) || []).length, 3);
    assert.doesNotMatch(html, /\b6 min\b|See what falls\.|Point to the part that fell first|Do two rebuilds|survive three gentle fans/);
  }
});

test("Wind Tower expanded compact readiness and identity retain honest evidence", () => {
  const section = card.match(/<section class="parent-strip wind-tower-readiness"[\s\S]*?<\/section>/)?.[0];
  assert.ok(section);
  assert.doesNotMatch(section, /<details|hidden|aria-hidden/);
  for (const label of ["Materials", "Adult and space", "Fit or skip", "Evidence", "Stop"]) assert.ok(section.includes(`<strong>${label}:</strong>`));
  assert.doesNotMatch(card, /class="meta-tile"/);
  assert.match(card, /<h1>Wind Tower Test<\/h1>/);
  assert.match(card, /rel="canonical" href="https:\/\/kidactivitylab.com\/cards\/wind-tower-test.html"/);
  assert.match(card, /class="kid-card wind-tower-card"/);
  assert.match(read("styles.css"), /\.wind-tower-card \.steps-grid \{\s*grid-template-columns: 1fr/);
});

test("actual five Wind Tower renderers match files including unchanged building route", () => {
  const script = `import json,sys
sys.path.insert(0,'scripts')
import generate_card_pages as c
import generate_seo_pages as s
from contributor_pages import with_contributor_credit
assert 'wind-tower-test' in c.QUICK_CARD_SLUGS
out={'cards/wind-tower-test.html':c.quick_page('wind-tower-test'),'cards.html':c.cards_index()}
for p in s.PAGES:
 if 'wind-tower-test' in p.get('activities',[]):out[p['path']]=s.page_html(p)
print(json.dumps({p:with_contributor_credit(h,p) for p,h in out.items()}))`;
  const out = JSON.parse(execFileSync("python3", ["-B", "-c", script], { encoding: "utf8", maxBuffer: 8 * 1024 * 1024 }));
  assert.equal(Object.keys(out).length, 5);
  for (const [path, html] of Object.entries(out)) assert.equal(html, read(path), path);
});

test("Wind Tower leaves Low Block Wall non-fan and preserves routes and inventories", () => {
  const wall = block("collections/building-activities-for-4-year-olds.html", "Low Block Wall");
  assert.ok(wall);
  assert.match(wall, /Make a low wall that marks a space for the toy/);
  assert.match(wall, /Place two blocks end to end/);
  assert.doesNotMatch(wall, /paper.fan|Adult alone|standing, moved|adult-prepared/);
  assert.match(wall, /wind-tower-test.html">Open the test-and-redesign version/);
  assert.equal((read("cards.html").match(/class="mini-card"/g) || []).length, 36);
  assert.match(read("cards.html"), /Adult controls paper fan; standing is a result \| Open-ended/);
  assert.equal((read("sitemap.xml").match(/<loc>/g) || []).length, 65);
  assert.ok(read("sitemap.xml").includes("cards/wind-tower-test.html</loc>\n    <lastmod>2026-10-27</lastmod>"));
  assert.match(pack, /id="windproof-tower"/);
  assert.equal((pack.match(/<details/g) || []).length, 1);
});
