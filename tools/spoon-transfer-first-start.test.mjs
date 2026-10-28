import assert from "node:assert/strict";
import fs from "node:fs";
import { execFileSync } from "node:child_process";
import test from "node:test";

const read = path => fs.readFileSync("site/" + path, "utf8");
const hubs = ["ages/activities-for-4-year-olds-at-home.html", "collections/no-prep-activities-for-preschoolers.html", "collections/fine-motor-activities-for-preschoolers.html", "collections/math-activities-for-4-year-olds-at-home.html"];
const card = read("cards/spoon-transfer.html");
const blocks = [card, ...hubs.map(path => [...read(path).matchAll(/<article\b[\s\S]*?<\/article>/g)].map(m => m[0]).find(s => s.includes("<h2>Spoon Transfer</h2>")))];

test("Spoon Transfer material fit, adult and stop controls precede movement in five runnable owners", () => {
  for (const [i, html] of blocks.entries()) {
    assert.ok(html, hubs[i - 1]);
    const marker = i === 0 ? 'class="steps-grid"' : '<ol class="card-steps">';
    for (const text of ["1 intact LARGE owned play pom-pom", "2 stable unbreakable bowls", "1 rimmed tray", "every reachable child", "No suitable owned play pom? Choose another activity.", "younger reach you cannot control", "Size and supervision are not a choking guarantee", "not family-tested by Kid Activity Lab", "BEFORE child access", "rest freely on the spoon", "Failed fit? Skip, not smaller filler", "anything leaving the tray"]) assert.ok(html.indexOf(text) >= 0 && html.indexOf(text) < html.indexOf(marker), text);
    assert.equal((html.match(i === 0 ? /class="step-tile"/g : /<li>/g) || []).length, 3);
    for (const text of ["point for the adult", "above the empty bowl", "Put the spoon down", "may replace it once", "checks table and floor", "stores ALL pom", "not an inspected source procedure or tested setup"]) assert.ok(html.includes(text), text);
    assert.doesNotMatch(html, /Use large non-choking objects|\b2 min\b|fine motor practice, focus|low mess|medium help/);
  }
});

test("Spoon Transfer early controls stay visible with scoped compact layout", () => {
  const early = card.match(/<section class="parent-strip spoon-transfer-readiness"[\s\S]*?<\/section>/)?.[0];
  assert.ok(early);
  assert.doesNotMatch(early, /<details\b|<[^>]*\shidden\b|<[^>]*\saria-hidden=/);
  for (const label of ["Materials", "Adult and fit", "Evidence", "Stop"]) assert.ok(early.includes("<strong>" + label + ":</strong>"));
  assert.doesNotMatch(card, /class="meta-tile"/);
  assert.match(card, /class="kid-card spoon-transfer-card"/);
  assert.match(read("styles.css"), /\.spoon-transfer-card h1 \{\s*font-size: 1\.7rem/);
  assert.match(read("styles.css"), /\.spoon-transfer-card \.steps-grid \{\s*grid-template-columns: 1fr/);
});

test("actual six Spoon Transfer renderers match generated files", () => {
  const script = `import json,sys
sys.path.insert(0,'scripts')
import generate_card_pages as c
import generate_seo_pages as s
from contributor_pages import with_contributor_credit
assert 'spoon-transfer' in c.QUICK_CARD_SLUGS
out={'cards/spoon-transfer.html':c.quick_page('spoon-transfer'),'cards.html':c.cards_index()}
for p in s.PAGES:
 if 'spoon-transfer' in p.get('activities',[]):
  assert 'spoon-transfer' not in p.get('activity_overrides',{})
  out[p['path']]=s.page_html(p)
print(json.dumps({p:with_contributor_credit(h,p) for p,h in out.items()}))`;
  const out = JSON.parse(execFileSync("python3", ["-B", "-c", script], { encoding: "utf8", maxBuffer: 8 * 1024 * 1024 }));
  assert.equal(Object.keys(out).length, 6);
  for (const [path, html] of Object.entries(out)) assert.equal(html, read(path), path);
});

test("Spoon Transfer keeps existing routes, finder and inventories while withdrawing host assurance", () => {
  const fine = read(hubs[2]);
  assert.doesNotMatch(fine, /If an item can fit in a mouth, treat it as a direct-supervision activity/);
  assert.match(fine, /Size or direct supervision is not permission to use unsuitable items/);
  assert.match(card, /<h1>Spoon Transfer<\/h1>/);
  assert.match(card, /rel="canonical" href="https:\/\/kidactivitylab.com\/cards\/spoon-transfer.html"/);
  for (const route of [hubs[0], hubs[1], hubs[3]]) assert.ok(card.includes(route));
  const entry = read("cards.html").match(/<a class="mini-card" href="cards\/spoon-transfer.html">[\s\S]*?<\/a>/)?.[0];
  assert.match(entry, /Adult checks, models and stays; scoop or point \| Open-ended/);
  assert.match(entry, /<template data-search="Spoon Transfer 1 intact LARGE owned play pom-pom/);
  assert.equal((read("cards.html").match(/class="mini-card"/g) || []).length, 36);
  assert.equal((read("sitemap.xml").match(/<loc>/g) || []).length, 67);
  assert.ok(read("sitemap.xml").includes("cards/spoon-transfer.html</loc>\n    <lastmod>2026-10-27</lastmod>"));
});
