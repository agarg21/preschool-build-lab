import assert from "node:assert/strict";
import fs from "node:fs";
import { execFileSync } from "node:child_process";
import test from "node:test";

const read = path => fs.readFileSync(`site/${path}`, "utf8");
const owners = ["ages/stem-activities-for-4-year-olds.html", "collections/science-experiments-for-4-year-olds.html", "collections/no-prep-stem-activities-for-4-year-olds.html"];
const card = read("cards/ramp-texture-test.html");
const entries = owners.map(path => [...read(path).matchAll(/<article\b[\s\S]*?<\/article>/g)].map(m => m[0]).find(s => s.includes("<h2>Ramp Texture Test</h2>")));

test("Ramp Texture complete support and early control reach all instruction owners", () => {
  for (const [i, html] of [card, ...entries].entries()) {
    assert.ok(html);
    const marker = i === 0 ? 'class="steps-grid"' : '<ol class="card-steps">';
    for (const text of ["1 flat stiff cardboard piece", "2 broad sturdy closed books", "1 owned toy car", "thin flat dish towel", "owned masking tape", "steadies the ramp throughout", "watch the adult release", "not family-tested by Kid Activity Lab", "Adult first releases the car without pushing", "No forcing a launch"]) assert.ok(html.indexOf(text) >= 0 && html.indexOf(text) < html.indexOf(marker), text);
    for (const text of ["same car from the same spot without pushing", "nearer, farther, about the same, stuck or unclear", "skip this roll and finish", "puts away the car, tape, towel, books and cardboard", "single result does not prove friction alone", "not a tested setup"]) assert.ok(html.includes(text), text);
    assert.equal((html.match(i === 0 ? /class="step-tile"/g : /<li>/g) || []).length, 3);
    assert.doesNotMatch(html, /\b6 min\b|Try foil\.|Try paper or a placemat\.|low mess|medium help/);
  }
});

test("Ramp Texture has expanded readiness and complete materials rather than truncated tiles", () => {
  const section = card.match(/<section class="parent-strip ramp-texture-readiness"[\s\S]*?<\/section>/)?.[0];
  assert.ok(section);
  assert.doesNotMatch(section, /<details|hidden|aria-hidden/);
  for (const label of ["Materials", "Adult and space", "Fit or skip", "Evidence", "Stop"]) assert.ok(section.includes(`<strong>${label}:</strong>`));
  assert.doesNotMatch(card, /class="meta-tile"/);
  assert.match(card, /class="ramp-texture-materials"[\s\S]*owned masking tape[\s\S]*Open-ended; duration and mess not measured/);
});

test("actual five Ramp Texture renderers reconcile the target override only", () => {
  const script = `import json,sys
sys.path.insert(0,'scripts')
import generate_card_pages as c
import generate_seo_pages as s
from contributor_pages import with_contributor_credit
assert 'ramp-texture-test' in c.QUICK_CARD_SLUGS
out={'cards/ramp-texture-test.html':c.quick_page('ramp-texture-test'),'cards.html':c.cards_index()}
for p in s.PAGES:
 if 'ramp-texture-test' in p.get('activities',[]):
  assert 'ramp-texture-test' not in p.get('activity_overrides',{})
  out[p['path']]=s.page_html(p)
print(json.dumps({p:with_contributor_credit(h,p) for p,h in out.items()}))`;
  const out = JSON.parse(execFileSync("python3", ["-B", "-c", script], { encoding: "utf8", maxBuffer: 8 * 1024 * 1024 }));
  assert.equal(Object.keys(out).length, 5);
  for (const [path, html] of Object.entries(out)) assert.equal(html, read(path), path);
});

test("Ramp Texture preserves identity, inventories and honest depth destinations", () => {
  assert.match(card, /<h1>Ramp Texture Test<\/h1>/);
  assert.match(card, /rel="canonical" href="https:\/\/kidactivitylab.com\/cards\/ramp-texture-test.html"/);
  assert.match(card, /class="kid-card ramp-texture-card"/);
  assert.match(read("styles.css"), /\.ramp-texture-card \.steps-grid \{\s*grid-template-columns: 1fr/);
  for (const html of [card, ...entries]) {
    assert.match(html, /cardboard-box-car-ramp-preschoolers.html#ramp-start/);
    assert.match(html, /original-stem-activities-for-4-year-olds.html#ramp-detective/);
    assert.match(html, /not a cloth covering/);
  }
  assert.equal((read("cards.html").match(/class="mini-card"/g) || []).length, 36);
  assert.match(read("cards.html"), /Adult steadies; child releases or watches \| Open-ended/);
  assert.equal((read("sitemap.xml").match(/<loc>/g) || []).length, 67);
  assert.ok(read("sitemap.xml").includes("cards/ramp-texture-test.html</loc>\n    <lastmod>2026-10-27</lastmod>"));
});
