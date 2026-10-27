import assert from "node:assert/strict";
import fs from "node:fs";
import { execFileSync } from "node:child_process";
import test from "node:test";

const read = path => fs.readFileSync(`site/${path}`, "utf8");
const card = read("cards/color-mixing-cups.html");
const owners = ["ages/stem-activities-for-4-year-olds.html", "collections/science-experiments-for-4-year-olds.html"];
const entry = path => [...read(path).matchAll(/<article\b[\s\S]*?<\/article>/g)].map(m => m[0]).find(s => s.includes("<h2>Color Mixing Cups</h2>"));

test("Color Mixing complete receiver materials and adult controls precede observation", () => {
  for (const [i, html] of [card, ...owners.map(entry)].entries()) {
    assert.ok(html);
    const marker = i === 0 ? 'class="steps-grid"' : '<ol class="card-steps">';
    for (const text of ["3 clear nonbreakable cups", "owned red and yellow food coloring", "1 adult spoon", "1 rimmed tray", "1 towel", "Adult handles coloring, caps, spoon and liquids", "beyond every child&#x27;s reach", "Stay beside every reachable child", "Skip for mouthing", "End and collect if a child reaches", "not family-tested by Kid Activity Lab", "third empty receiving cup", "room for two small spoonfuls"]) assert.ok(html.indexOf(text) >= 0 && html.indexOf(text) < html.indexOf(marker), text);
    for (const text of ["one small spoonful of yellow water, then one of red", "gently mix once", "different, the same or unclear", "Naming a color is optional", "immediately empties and rinses all three cups", "No source image proves this arrangement or capacity", "not a tested setup"]) assert.ok(html.includes(text), text);
    assert.equal((html.match(i === 0 ? /class="step-tile"/g : /<li>/g) || []).length, 3);
    assert.doesNotMatch(html, /\b6 min\b|Fill two cups\.|Add two colors\.|Pour together\.|Name the new color\.|Use tiny drops and protect the table\./);
  }
});

test("Color Mixing readiness remains expanded and the complete set is not truncated", () => {
  const section = card.match(/<section class="parent-strip color-mix-readiness"[\s\S]*?<\/section>/)?.[0];
  assert.ok(section);
  assert.doesNotMatch(section, /<details|hidden|aria-hidden/);
  for (const label of ["Materials", "Adult and space", "Fit or skip", "Evidence", "Stop"]) assert.ok(section.includes(`<strong>${label}:</strong>`));
  assert.doesNotMatch(card, /class="meta-tile"/);
  assert.match(card, /class="color-mix-materials"[\s\S]*1 towel[\s\S]*Open-ended; duration and mess not measured/);
});

test("actual four Color Mixing renderers match contributor-credited output", () => {
  const script = `import json,sys
sys.path.insert(0,'scripts')
import generate_card_pages as c
import generate_seo_pages as s
from contributor_pages import with_contributor_credit
assert 'color-mixing-cups' in c.QUICK_CARD_SLUGS
out={'cards/color-mixing-cups.html':c.quick_page('color-mixing-cups'),'cards.html':c.cards_index()}
for p in s.PAGES:
 if 'color-mixing-cups' in p.get('activities',[]):out[p['path']]=s.page_html(p)
print(json.dumps({p:with_contributor_credit(h,p) for p,h in out.items()}))`;
  const out = JSON.parse(execFileSync("python3", ["-B", "-c", script], { encoding: "utf8", maxBuffer: 8 * 1024 * 1024 }));
  assert.equal(Object.keys(out).length, 4);
  for (const [path, html] of Object.entries(out)) assert.equal(html, read(path), path);
});

test("Color Mixing retains identity, inventory and scoped compact styling", () => {
  assert.match(card, /<h1>Color Mixing Cups<\/h1>/);
  assert.match(card, /rel="canonical" href="https:\/\/kidactivitylab.com\/cards\/color-mixing-cups.html"/);
  assert.match(card, /class="kid-card color-mix-card"/);
  assert.match(read("styles.css"), /\.color-mix-card \.steps-grid \{\s*grid-template-columns: 1fr/);
  assert.match(card, /styles\.css\?v=color-mix-card-1/);
  assert.equal((read("cards.html").match(/class="mini-card"/g) || []).length, 36);
  assert.match(read("cards.html"), /Adult mixes; child notices \| Open-ended/);
  const sitemap = read("sitemap.xml");
  assert.equal((sitemap.match(/<loc>/g) || []).length, 67);
  assert.ok(sitemap.includes("cards/color-mixing-cups.html</loc>\n    <lastmod>2026-10-27</lastmod>"));
});
