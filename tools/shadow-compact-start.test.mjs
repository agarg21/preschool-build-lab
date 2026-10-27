import assert from "node:assert/strict";
import fs from "node:fs";
import { execFileSync } from "node:child_process";
import { createHash } from "node:crypto";
import test from "node:test";

const read = path => fs.readFileSync(`site/${path}`, "utf8");
const card = read("cards/shadow-shape-match.html");
const shadow = html => [...html.matchAll(/<article\b[\s\S]*?<\/article>/g)]
  .map(m => m[0]).find(s => s.includes("<h2>Shadow Builder</h2>"));
const owners = [card, shadow(read("collections/science-experiments-for-4-year-olds.html")), shadow(read("collections/no-prep-stem-activities-for-4-year-olds.html"))];

test("Shadow compact owners assign light, object, fit and stop before three comparison steps", () => {
  for (const [i, html] of owners.entries()) {
    assert.ok(html);
    const marker = i === 0 ? 'class="steps-grid"' : '<ol class="card-steps">';
    for (const text of ["Keep light on wall, never faces", "Stay beside every reachable child", "closed, secured battery compartment", "Skip if materials", "Switch off if the beam leaves the wall", "not family-tested by Kid Activity Lab", "Set the flashlight on a stable low surface"]) {
      assert.ok(html.indexOf(text) >= 0 && html.indexOf(text) < html.indexOf(marker), text);
    }
    for (const text of ["1 owned flashlight", "1 checked large opaque block", "opaque (not see-through)", "clear walking path visible", "nearer the wall", "not the light itself", "Look for a bigger shadow", "bigger, smaller or unclear", "restores a steady wall-pointed beam and a visible shadow", "Otherwise end", "puts away the light, block and spares", "Duration and mess have not been measured", "neither validates this exact home geometry"]) assert.ok(html.includes(text), text);
    assert.equal((html.match(i === 0 ? /class="step-tile"/g : /<li>/g) || []).length, 3);
    assert.doesNotMatch(html, /5 min|low mess|Shine the light\.|Move it closer\./);
    assert.ok(html.indexOf("restores a steady") < html.indexOf("the child moves the block or watches"));
  }
  const readiness = card.match(/<section class="parent-strip shadow-readiness"[\s\S]*?<\/section>/)?.[0];
  assert.ok(readiness);
  assert.doesNotMatch(readiness, /<details|hidden|aria-hidden/);
  for (const label of ["Materials", "Adult and space", "Fit or skip", "Evidence", "Stop"]) assert.ok(readiness.includes(`<strong>${label}:</strong>`));
});

test("actual Shadow card, library and three page renderers match contributor-credited output", () => {
  const script = `import json, sys
sys.path.insert(0,'scripts')
import generate_card_pages as cards
import generate_seo_pages as seo
from contributor_pages import with_contributor_credit
assert 'shadow-shape-match' in cards.QUICK_CARD_SLUGS
out={'cards/shadow-shape-match.html':cards.quick_page('shadow-shape-match'),'cards.html':cards.cards_index()}
for p in seo.PAGES:
 if 'shadow-shape-match' in p.get('activities',[]):out[p['path']]=seo.page_html(p)
print(json.dumps({p:with_contributor_credit(s,p) for p,s in out.items()}))`;
  const result = JSON.parse(execFileSync("python3", ["-B", "-c", script], { encoding: "utf8", maxBuffer: 8 * 1024 * 1024 }));
  assert.equal(Object.keys(result).length, 5);
  for (const [path, html] of Object.entries(result)) assert.equal(html, read(path), path);
});

test("independently maintained Shadow depth contracts do not inherit the compact rewrite", () => {
  for (const [path, expected] of [
    ["ages/stem-activities-for-4-year-olds.html", "c1f385b9fa0da6ce43c378f868c3904bf47f9c5e8ccbb742f45730bb586addf0"],
    ["collections/original-stem-activities-for-4-year-olds.html", "fe4a3cad165c5b4638b9530b7b843a336595afcb78951d4a9f70bb144c7299ac"],
  ]) assert.equal(createHash("sha256").update(shadow(read(path))).digest("hex"), expected, path);
});

test("Shadow identity, library count, scoped layout and sitemap retain their owners", () => {
  assert.match(card, /<h1>Shadow Builder<\/h1>/);
  assert.match(card, /rel="canonical" href="https:\/\/kidactivitylab.com\/cards\/shadow-shape-match.html"/);
  assert.match(card, /class="kid-card shadow-card"/);
  assert.match(card, /styles\.css\?v=shadow-card-1/);
  assert.match(read("styles.css"), /\.shadow-card h1 \{\s*font-size: min\(2rem, 48px\)/);
  const library = read("cards.html");
  assert.equal((library.match(/class="mini-card"/g) || []).length, 36);
  assert.match(library, /href="cards\/shadow-shape-match.html"><strong>Shadow Builder<\/strong><span>Adult-controlled wall light/);
  const sitemap = read("sitemap.xml");
  assert.equal((sitemap.match(/<loc>/g) || []).length, 67);
  assert.ok(sitemap.includes("cards/shadow-shape-match.html</loc>\n    <lastmod>2026-10-27</lastmod>"));
});
