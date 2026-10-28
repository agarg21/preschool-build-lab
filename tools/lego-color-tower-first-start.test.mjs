import assert from "node:assert/strict";
import fs from "node:fs";
import { execFileSync } from "node:child_process";
import test from "node:test";

const read = path => fs.readFileSync("site/" + path, "utf8");
const hubs = ["ages/activities-for-4-year-olds-at-home.html", "ages/activities-for-5-year-olds-at-home.html", "ages/activities-for-6-year-olds-at-home.html", "collections/fine-motor-activities-for-preschoolers.html", "collections/math-activities-for-4-year-olds-at-home.html"];
const card = read("cards/lego-color-tower.html");
const blocks = [card, ...hubs.map(path => [...read(path).matchAll(/<article\b[\s\S]*?<\/article>/g)].map(m => m[0]).find(s => s.includes("<h2>LEGO or DUPLO Color Tower</h2>")))];

test("Color Tower material, adult and stop checks precede matching in six runnable owners", () => {
  for (const [i, html] of blocks.entries()) {
    assert.ok(html, hubs[i - 1]);
    const marker = i === 0 ? 'class="steps-grid"' : '<ol class="card-steps">';
    for (const text of ["four intact large basic DUPLO bricks", "same compatible shape and footprint", "EVERY reachable child", "No small standard LEGO", "No suitable owned set?", "every reachable child", "younger reach you cannot control", "not family-tested by Kid Activity Lab", "BEFORE child access", "without teeth, force or tools", "Lay ALL FOUR loose again", "ONE brick of each color", "RETURN it to the choices", "leave both seeds in place", "Stop for mouthing"]) assert.ok(html.indexOf(text) >= 0 && html.indexOf(text) < html.indexOf(marker), text);
    assert.equal((html.match(i === 0 ? /class="step-tile"/g : /<li>/g) || []).length, 3);
    for (const text of ["BESIDE its matching-color seed", "or point for the adult", "two-brick stack", "studs up", "two bricks high", "flat pairs, watch or end", "Adult collects ALL FOUR", "checks surface and floor", "stores everything out of reach", "not an inspected creator-video procedure or tested setup"]) assert.ok(html.includes(text), text);
    assert.doesNotMatch(html, /Make it taller|Count them|Use DUPLO if younger|\b3 min\b|low mess|medium help/);
  }
});

test("Color Tower uses visible early checks and compact layout without creator dependency", () => {
  const early = card.match(/<section class="parent-strip color-tower-readiness"[\s\S]*?<\/section>/)?.[0];
  assert.ok(early);
  assert.doesNotMatch(early, /<details\b|<[^>]*\shidden\b|<[^>]*\saria-hidden=/);
  for (const label of ["Materials", "Adult and space", "Evidence", "Stop"]) assert.ok(early.includes("<strong>" + label + ":</strong>"));
  assert.doesNotMatch(card, /class="meta-tile"|<iframe|cSIeC-wbgI4/);
  assert.doesNotMatch(card, /aria-label="Best for"/);
  assert.match(card, /booklet, PDF page14 \/ printed26/);
  assert.match(card, /duplo-activity-booklet-pdf-1-140kb.pdf#page=14/);
  assert.doesNotMatch(card, /duplo-activity-booklet-pdf-1-140kb.pdf#page=15/);
  assert.match(card, /class="kid-card color-tower-card"/);
  assert.match(read("styles.css"), /\.color-tower-card h1 \{\s*font-size: 1\.7rem/);
  assert.match(read("styles.css"), /\.color-tower-card \.steps-grid \{\s*grid-template-columns: 1fr/);
});

test("seven actual Color Tower renderers agree and CSV dispatch uses the maintained QUICK card", () => {
  const script = `import json,sys
sys.path.insert(0,'scripts')
import generate_card_pages as c
import generate_seo_pages as s
from contributor_pages import with_contributor_credit
assert c.SLUGS['yt-lego-learning-preschool']=='lego-color-tower'
assert 'lego-color-tower' not in c.QUICK_CARD_SLUGS
out={'cards/lego-color-tower.html':c.quick_page('lego-color-tower'),'cards.html':c.cards_index()}
for p in s.PAGES:
 if p['path']=='collections/stem-activities-for-preschoolers.html':assert 'lego-color-tower' not in p['activities']
 if 'lego-color-tower' in p.get('activities',[]):out[p['path']]=s.page_html(p)
print(json.dumps({p:with_contributor_credit(h,p) for p,h in out.items()}))`;
  const out = JSON.parse(execFileSync("python3", ["-B", "-c", script], { encoding: "utf8", maxBuffer: 8 * 1024 * 1024 }));
  assert.equal(Object.keys(out).length, 7);
  for (const [path, html] of Object.entries(out)) assert.equal(html, read(path), path);
  assert.match(fs.readFileSync("scripts/generate_card_pages.py", "utf8"), /quick_page\(slug\) if slug in \{"cup-tower", "duplo-games", "tube-sculpture", "lego-color-tower", "tape-train-tracks", "block-tower", "tape-city"\} else page\(row, slug\)/);
});

test("Color Tower preserves identity, real routes, finder inventories and affected dates", () => {
  assert.match(card, /<h1>LEGO Color Tower<\/h1>/);
  assert.match(card, /rel="canonical" href="https:\/\/kidactivitylab.com\/cards\/lego-color-tower.html"/);
  for (const route of [hubs[0], hubs[3], hubs[4]]) assert.ok(card.includes(route));
  assert.doesNotMatch(card, /collections\/stem-activities-for-preschoolers.html/);
  assert.doesNotMatch(read("collections/stem-activities-for-preschoolers.html"), /<h2>LEGO or DUPLO Color Tower<\/h2>/);
  const entry = read("cards.html").match(/<a class="mini-card" href="cards\/lego-color-tower.html">[\s\S]*?<\/a>/)?.[0];
  assert.match(entry, /Adult checks and stays; match flat pairs or point \| Open-ended/);
  assert.match(entry, /<template data-search="LEGO Color Tower 4 intact large owned DUPLO bricks/);
  assert.equal((read("cards.html").match(/class="mini-card"/g) || []).length, 36);
  assert.equal((read("sitemap.xml").match(/<loc>/g) || []).length, 67);
  for (const p of ["cards/lego-color-tower.html", "cards.html", ...hubs]) assert.ok(read("sitemap.xml").includes(p + "</loc>\n    <lastmod>2026-10-28</lastmod>"));
});
