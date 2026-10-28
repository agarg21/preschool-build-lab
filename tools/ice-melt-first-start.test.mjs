import assert from "node:assert/strict";
import fs from "node:fs";
import { execFileSync } from "node:child_process";
import test from "node:test";

const read = path => fs.readFileSync(`site/${path}`, "utf8");
const card = read("cards/ice-melt-rescue.html");
const science = read("collections/science-experiments-for-4-year-olds.html");
const entry = [...science.matchAll(/<article\b[\s\S]*?<\/article>/g)]
  .map(m => m[0]).find(s => s.includes("<h2>Melting Ice Watch</h2>"));

test("Ice Watch complete materials and adult reach/stop precede all observation steps", () => {
  for (const [i, html] of [card, entry].entries()) {
    assert.ok(html);
    const marker = i === 0 ? 'class="steps-grid"' : '<ol class="card-steps">';
    for (const text of ["1 plain water ice cube", "1 shallow nonbreakable tray", "1 adult spoon", "1 towel", "Adult handles the ice, spoon and meltwater throughout", "beyond every child&#x27;s reach", "Stay beside every reachable child", "Skip if a child mouths", "End and collect if a child reaches", "not family-tested by Kid Activity Lab", "empty dry tray"]) assert.ok(html.indexOf(text) >= 0 && html.indexOf(text) < html.indexOf(marker), text);
    for (const text of ["nothing frozen inside", "No added water, heat, salt, colour or embedded toys", "without touching", "is the ice smaller", "more liquid around it", "changed or not yet clear", "no need to wait for all the ice to melt", "empties the tray immediately", "dries the tray and work area", "Duration and mess have not been measured", "not a tested safety method"]) assert.ok(html.includes(text), text);
    assert.equal((html.match(i === 0 ? /class="step-tile"/g : /<li>/g) || []).length, 3);
    assert.doesNotMatch(html, /\b8 min\b|Add warm drops\.|Touch with a spoon\.|Use warm water, not hot water\./);
  }
});

test("Ice Watch readiness is expanded and materials are not truncated into three tiles", () => {
  const section = card.match(/<section class="parent-strip ice-watch-readiness"[\s\S]*?<\/section>/)?.[0];
  assert.ok(section);
  assert.doesNotMatch(section, /<details|hidden|aria-hidden/);
  for (const label of ["Materials", "Adult and space", "Fit or skip", "Evidence", "Stop"]) assert.ok(section.includes(`<strong>${label}:</strong>`));
  assert.doesNotMatch(card, /class="meta-tile"/);
  assert.match(card, /class="ice-watch-materials"[\s\S]*1 towel[\s\S]*Open-ended; duration and mess not measured/);
});

test("actual Ice Watch card, library and science renderers match contributor-credited output", () => {
  const script = `import json,sys
sys.path.insert(0,'scripts')
import generate_card_pages as c
import generate_seo_pages as s
from contributor_pages import with_contributor_credit
assert 'ice-melt-rescue' in c.QUICK_CARD_SLUGS
out={'cards/ice-melt-rescue.html':c.quick_page('ice-melt-rescue'),'cards.html':c.cards_index()}
for p in s.PAGES:
 if 'ice-melt-rescue' in p.get('activities',[]):out[p['path']]=s.page_html(p)
print(json.dumps({p:with_contributor_credit(h,p) for p,h in out.items()}))`;
  const out = JSON.parse(execFileSync("python3", ["-B", "-c", script], { encoding: "utf8", maxBuffer: 8 * 1024 * 1024 }));
  assert.equal(Object.keys(out).length, 3);
  for (const [path, html] of Object.entries(out)) assert.equal(html, read(path), path);
});

test("Ice Watch identity, inventory and scoped fit keep existing URL ownership", () => {
  assert.match(card, /<h1>Melting Ice Watch<\/h1>/);
  assert.match(card, /rel="canonical" href="https:\/\/kidactivitylab.com\/cards\/ice-melt-rescue.html"/);
  assert.match(card, /class="kid-card ice-watch-card"/);
  assert.match(read("styles.css"), /\.ice-watch-card h1 \{\s*font-size: min\(2rem, 48px\)/);
  assert.match(card, /styles\.css\?v=ice-watch-card-1/);
  const library = read("cards.html");
  assert.equal((library.match(/class="mini-card"/g) || []).length, 36);
  assert.match(library, /href="cards\/ice-melt-rescue.html"><strong>Melting Ice Watch<\/strong><span>Adult handles; child watches/);
  const sitemap = read("sitemap.xml");
  assert.equal((sitemap.match(/<loc>/g) || []).length, 65);
  assert.ok(sitemap.includes("cards/ice-melt-rescue.html</loc>\n    <lastmod>2026-10-27</lastmod>"));
});
