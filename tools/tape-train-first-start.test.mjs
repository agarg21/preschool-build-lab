import assert from "node:assert/strict";
import fs from "node:fs";
import { execFileSync } from "node:child_process";
import test from "node:test";
const read = p => fs.readFileSync("site/" + p, "utf8");
const card = read("cards/tape-train-tracks.html");
const age = read("ages/activities-for-4-year-olds-at-home.html").match(/<article\b(?:(?!<\/article>)[\s\S])*<h2>Tape Train Tracks<\/h2>[\s\S]*?<\/article>/)?.[0];

test("Train station owned materials, adult trial and stop precede action in both runnable owners", () => {
  for (const [i, html] of [card, age].entries()) {
    assert.ok(html);
    const marker = i === 0 ? 'class="steps-grid"' : '<ol class="card-steps">';
    for (const s of ["ONE intact large owned hand-pushed toy train", "EVERY reachable child", "No magnets, batteries", "No suitable owned train?", "sacrificial cardboard board", "fully supported", "younger reach you cannot control", "not family-tested by Kid Activity Lab", "BEFORE child access", "ONE short tape test piece", "Cardboard may tear", "TWO short straight parallel strips", "wider apart than the actual train", "ONE short cross-strip", "BETWEEN the lines", "does not guide wheels mechanically", "Return the train to the open end", "Stop for tape peeling"]) assert.ok(html.indexOf(s) >= 0 && html.indexOf(s) < html.indexOf(marker), s);
    for (const label of ["Tape check", "Layout", "Train trial"]) assert.ok(html.includes("<p><strong>" + label + ":</strong>"));
    for (const s of ["or point for the adult", "stopping elsewhere is a valid finish", "spot on the bare board", "SAME train only if wanted", "or required repeat", "ALL THREE route strips if laid, whether still attached or already removed", "checks the surface and floor", "out of reach", "not an inspected creator-video procedure or tested setup"]) assert.ok(html.includes(s), s);
    assert.doesNotMatch(html, /\b5 minutes\b|\b5 min\b|low mess|low help|Change tracks\./);
  }
});

test("Train card has visible compact checks, real depth and no inherited video or duplicate purpose", () => {
  assert.match(card, /class="kid-card train-station-card"/);
  assert.match(card, /train-station-readiness/);
  assert.match(card, /ALL THREE route strips if laid, whether still attached or already removed/);
  assert.match(card, /extra pieces or required repeat/);
  for (const label of ["Tape check", "Layout", "Train trial"]) assert.ok(card.includes("<p><strong>" + label + ":</strong>"));
  assert.doesNotMatch(card, /<iframe|kDIYgjNRAUo|class="meta-tile"|aria-label="Best for"|collections\/indoor-activities-for-preschoolers.html/);
  assert.match(card, /href="\.\.\/articles\/painter-tape-road-kids.html">Tape Road surface and route help/);
  assert.match(card, /href="\.\.\/ages\/activities-for-4-year-olds-at-home.html"/);
  assert.match(read("styles.css"), /\.train-station-card \.steps-grid \{\s*grid-template-columns: 1fr/);
});

test("Train canonical card and library renderers agree and only actual membership routes remain", () => {
  const code = `import sys,json
sys.path.insert(0,'scripts')
import generate_card_pages as c,generate_seo_pages as s
from contributor_pages import with_contributor_credit
assert c.SLUGS['yt-train-tape']=='tape-train-tracks'
assert 'tape-train-tracks' not in c.QUICK_CARD_SLUGS
out={'cards/tape-train-tracks.html':c.quick_page('tape-train-tracks'),'cards.html':c.cards_index()}
for p in s.PAGES:
 if p['path']=='collections/indoor-activities-for-preschoolers.html':assert 'tape-train-tracks' not in p['activities']
 if 'tape-train-tracks' in p.get('activities',[]):out[p['path']]=s.page_html(p)
print(json.dumps({p:with_contributor_credit(h,p) for p,h in out.items()}))`;
  const out = JSON.parse(execFileSync("python3", ["-B", "-c", code], {encoding:"utf8",maxBuffer:8*1024*1024}));
  assert.equal(Object.keys(out).length,3);
  for (const [p,h] of Object.entries(out)) assert.equal(h,read(p),p);
  assert.match(fs.readFileSync("scripts/generate_card_pages.py","utf8"), /"lego-color-tower", "tape-train-tracks", "block-tower", "tape-city"\} else page\(row, slug\)/);
});

test("Train discovery keeps noindex, routes, inventories and corrected dates", () => {
  const material=read("materials/painter-tape.html"), noCut=read("collections/no-cut-preschool-activities.html");
  assert.match(material,/name="robots" content="noindex,follow"/);
  assert.match(material,/\.tape-material-page h1 \{ font-size: min\(2\.5rem, 43px\)/);
  assert.match(material,/adult-prepared cardboard station route/);
  assert.match(material,/brief tape test does not guarantee later clean removal/);
  assert.match(noCut,/One pretend station stop/);
  assert.match(noCut,/Tape Train Tracks is an adult-prepared cardboard station start; duration is not measured/);
  assert.doesNotMatch(noCut,/Tape Train Tracks<\/a> are better for longer floor play/);
  assert.equal((read("cards.html").match(/class="mini-card"/g)||[]).length,36);
  assert.equal((read("sitemap.xml").match(/<loc>/g)||[]).length,65);
  for(const p of ["cards/tape-train-tracks.html","cards.html","ages/activities-for-4-year-olds-at-home.html","collections/no-cut-preschool-activities.html"])assert.ok(read("sitemap.xml").includes(p+"</loc>\n    <lastmod>2026-10-28</lastmod>"));
  assert.doesNotMatch(read("sitemap.xml"),/<loc>[^<]+materials\/painter-tape.html/);
});
