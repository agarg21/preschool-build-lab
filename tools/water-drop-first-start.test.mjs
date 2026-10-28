import assert from "node:assert/strict";
import fs from "node:fs";
import { execFileSync } from "node:child_process";
import test from "node:test";

const read = path => fs.readFileSync(`site/${path}`, "utf8");
const card = read("cards/water-drop-race.html");
const entry = [...read("collections/science-experiments-for-4-year-olds.html").matchAll(/<article\b[\s\S]*?<\/article>/g)].map(m => m[0]).find(s => s.includes("<h2>Water Drop Tilt</h2>"));

test("Water Drop Tilt complete set, grip and stop precede child movement", () => {
  for (const [i, html] of [card, entry].entries()) {
    assert.ok(html);
    const marker = i === 0 ? 'class="steps-grid"' : '<ol class="card-steps">';
    for (const text of ["1 shallow nonbreakable rimmed tray", "1 wax-paper piece", "owned tape", "1 adult dropper", "1 small water cup", "plain unheated water", "1 towel", "Adult handles tape, dropper, cup and spares", "steadies the far rim throughout", "Child holds the near rim with both hands", "Watching or pointing while the adult tilts", "Lower the tray flat and end", "not family-tested by Kid Activity Lab", "no bead is visible"]) assert.ok(html.indexOf(text) >= 0 && html.indexOf(text) < html.indexOf(marker), text);
    for (const text of ["one plain water drop near the middle", "tapes its dry edges down", "far edge stays on the table", "moved, stayed or unclear", "not a timed race", "immediately empties the tray and water cup", "Leave no accessible standing water", "not a tested setup"]) assert.ok(html.includes(text), text);
    assert.equal((html.match(i === 0 ? /class="step-tile"/g : /<li>/g) || []).length, 3);
    assert.doesNotMatch(html, /\b5 min\b|Blow gently\.|Race two drops\.|Try a bigger drop\.|gentle breath control/);
  }
});

test("Water Drop Tilt expanded readiness keeps complete material list", () => {
  const section = card.match(/<section class="parent-strip drop-tilt-readiness"[\s\S]*?<\/section>/)?.[0];
  assert.ok(section);
  assert.doesNotMatch(section, /<details|hidden|aria-hidden/);
  for (const label of ["Materials", "Adult and space", "Fit or skip", "Evidence", "Stop"]) assert.ok(section.includes(`<strong>${label}:</strong>`));
  assert.doesNotMatch(card, /class="meta-tile"/);
  assert.match(card, /class="drop-tilt-materials"[\s\S]*1 towel[\s\S]*Open-ended; duration and mess not measured/);
});

test("actual three Water Drop Tilt renderers match contributor-credited files", () => {
  const script = `import json,sys
sys.path.insert(0,'scripts')
import generate_card_pages as c
import generate_seo_pages as s
from contributor_pages import with_contributor_credit
assert 'water-drop-race' in c.QUICK_CARD_SLUGS
out={'cards/water-drop-race.html':c.quick_page('water-drop-race'),'cards.html':c.cards_index()}
for p in s.PAGES:
 if 'water-drop-race' in p.get('activities',[]):out[p['path']]=s.page_html(p)
print(json.dumps({p:with_contributor_credit(h,p) for p,h in out.items()}))`;
  const out = JSON.parse(execFileSync("python3", ["-B", "-c", script], { encoding: "utf8", maxBuffer: 8 * 1024 * 1024 }));
  assert.equal(Object.keys(out).length, 3);
  for (const [path, html] of Object.entries(out)) assert.equal(html, read(path), path);
});

test("Water Drop Tilt preserves URL and inventories with scoped compact styling", () => {
  assert.match(card, /<h1>Water Drop Tilt<\/h1>/);
  assert.match(card, /rel="canonical" href="https:\/\/kidactivitylab.com\/cards\/water-drop-race.html"/);
  assert.match(card, /class="kid-card drop-tilt-card"/);
  assert.match(read("styles.css"), /\.drop-tilt-card \.steps-grid \{\s*grid-template-columns: 1fr/);
  assert.match(card, /styles\.css\?v=drop-tilt-card-1/);
  assert.equal((read("cards.html").match(/class="mini-card"/g) || []).length, 36);
  assert.match(read("cards.html"), /Adult steadies; child tilts or watches \| Open-ended/);
  const sitemap = read("sitemap.xml");
  assert.equal((sitemap.match(/<loc>/g) || []).length, 65);
  assert.ok(sitemap.includes("cards/water-drop-race.html</loc>\n    <lastmod>2026-10-27</lastmod>"));
});
