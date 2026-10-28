import assert from "node:assert/strict";
import fs from "node:fs";
import { execFileSync } from "node:child_process";
import test from "node:test";

const read = path => fs.readFileSync("site/" + path, "utf8");
const hubs = ["ages/activities-for-5-year-olds-at-home.html", "ages/activities-for-6-year-olds-at-home.html", "collections/building-activities-for-4-year-olds.html"];
const card = read("cards/tube-sculpture.html");
const blocks = [card, ...hubs.map(path => [...read(path).matchAll(/<article\b[\s\S]*?<\/article>/g)].map(m => m[0]).find(s => s.includes("<h2>Tube Sculpture</h2>")))];

test("Tube Sculpture attachment, adult and stop controls precede placement in all four runnable owners", () => {
  for (const [i, html] of blocks.entries()) {
    assert.ok(html, hubs[i - 1]);
    const marker = i === 0 ? 'class="steps-grid"' : '<ol class="card-steps">';
    for (const text of ["2 whole clean dry paper-towel-type cardboard tubes", "sacrificial cardboard base", "every reachable child", "younger reach you cannot control", "not family-tested by Kid Activity Lab", "BEFORE child access", "FIRST tube on its long side", "press both free ends onto the base on opposite sides", "Repeat near the other end", "no loose ends", "keep tube openings clear", "Gently check", "Failed hold?", "untaped flat arrangement or end", "No launchers"]) assert.ok(html.indexOf(text) >= 0 && html.indexOf(text) < html.indexOf(marker), text);
    assert.equal((html.match(i === 0 ? /class="step-tile"/g : /<li>/g) || []).length, 3);
    for (const text of ["SECOND tube", "Or point for the adult", "same two-strip method", "if cardboard tears", "check table and floor", "store ALL materials", "not an inspected source procedure or tested setup"]) assert.ok(html.includes(text), text);
    assert.doesNotMatch(html, /Make it taller|Tape gently|Stand two tubes|vertical balance|\b8 min\b|medium mess|medium help/);
  }
});

test("Tube Sculpture has early visible checks, compact layout and no creator-video dependency", () => {
  const early = card.match(/<section class="parent-strip tube-sculpture-readiness"[\s\S]*?<\/section>/)?.[0];
  assert.ok(early);
  assert.doesNotMatch(early, /<details\b|<[^>]*\shidden\b|<[^>]*\saria-hidden=/);
  for (const label of ["Materials", "Adult and space", "Evidence", "Stop"]) assert.ok(early.includes("<strong>" + label + ":</strong>"));
  assert.doesNotMatch(card, /class="meta-tile"|<iframe|ld2wrKWqy4k/);
  assert.match(card, /class="kid-card tube-sculpture-card"/);
  assert.match(read("styles.css"), /\.tube-sculpture-card h1 \{\s*font-size: 1\.7rem/);
  assert.match(read("styles.css"), /\.tube-sculpture-card \.steps-grid \{\s*grid-template-columns: 1fr/);
});

test("five actual Tube Sculpture renderers agree and CSV dispatch uses the maintained QUICK card", () => {
  const script = `import json,sys
sys.path.insert(0,'scripts')
import generate_card_pages as c
import generate_seo_pages as s
from contributor_pages import with_contributor_credit
assert c.SLUGS['yt-cardboard-tube-sculptures']=='tube-sculpture'
assert 'tube-sculpture' not in c.QUICK_CARD_SLUGS
out={'cards/tube-sculpture.html':c.quick_page('tube-sculpture'),'cards.html':c.cards_index()}
for p in s.PAGES:
 if p['path']=='collections/stem-activities-for-preschoolers.html':assert 'tube-sculpture' not in p['activities']
 if 'tube-sculpture' in p.get('activities',[]):out[p['path']]=s.page_html(p)
print(json.dumps({p:with_contributor_credit(h,p) for p,h in out.items()}))`;
  const out = JSON.parse(execFileSync("python3", ["-B", "-c", script], { encoding: "utf8", maxBuffer: 8 * 1024 * 1024 }));
  assert.equal(Object.keys(out).length, 5);
  for (const [path, html] of Object.entries(out)) assert.equal(html, read(path), path);
  const source = fs.readFileSync("scripts/generate_card_pages.py", "utf8");
  assert.match(source, /quick_page\(slug\) if slug in \{"cup-tower", "duplo-games", "tube-sculpture", "lego-color-tower", "tape-train-tracks", "block-tower"\} else page\(row, slug\)/);
});

test("Tube Sculpture routes only to actual owners, keeps finder/inventories and corrects the target chooser", () => {
  assert.match(card, /<h1>Tube Sculpture<\/h1>/);
  assert.match(card, /rel="canonical" href="https:\/\/kidactivitylab.com\/cards\/tube-sculpture.html"/);
  for (const route of hubs) assert.ok(card.includes(route));
  assert.doesNotMatch(card, /collections\/stem-activities-for-preschoolers.html/);
  assert.doesNotMatch(read("collections/stem-activities-for-preschoolers.html"), /<h2>Tube Sculpture<\/h2>/);
  assert.match(read(hubs[2]), /Adult checks and attaches; child chooses a low arrangement or points/);
  assert.equal(blocks[3].split("No launchers, steps, climbing").length - 1, 1);
  const entry = read("cards.html").match(/<a class="mini-card" href="cards\/tube-sculpture.html">[\s\S]*?<\/a>/)?.[0];
  assert.match(entry, /Adult checks, tapes and stays; choose a low arrangement or point \| Open-ended/);
  assert.match(entry, /<template data-search="Tube Sculpture 2 whole clean dry/);
  assert.equal((read("cards.html").match(/class="mini-card"/g) || []).length, 36);
  assert.equal((read("sitemap.xml").match(/<loc>/g) || []).length, 67);
  for (const p of ["cards/tube-sculpture.html", "cards.html", ...hubs]) assert.ok(read("sitemap.xml").includes(p + "</loc>\n    <lastmod>2026-10-28</lastmod>"));
});
