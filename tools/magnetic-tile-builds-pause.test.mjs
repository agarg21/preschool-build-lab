import assert from "node:assert/strict";
import fs from "node:fs";
import {execFileSync} from "node:child_process";
import test from "node:test";

const read = p => fs.readFileSync("site/" + p, "utf8");
const hubs = ["ages/activities-for-4-year-olds-at-home.html", "ages/activities-for-5-year-olds-at-home.html", "ages/activities-for-6-year-olds-at-home.html", "collections/independent-activities-for-preschoolers.html", "collections/fine-motor-activities-for-preschoolers.html", "collections/math-activities-for-4-year-olds-at-home.html"];
const choices = ["Do not start this version.", "flat PICTURE", "ONE park-and-out job, NOT two rooms", "BEFORE handling", "EVERY reachable child", "not family-tested by Kid Activity Lab"];

test("Generic tile card is an early noindex pause, not a latent runnable recipe", () => {
  const h = read("cards/magnetic-tile-ideas.html");
  assert.match(h, /<h1>Magnetic Tile Ideas<\/h1>/);
  assert.match(h, /name="robots" content="noindex,follow"/);
  assert.match(h, /canonical" href="https:\/\/kidactivitylab.com\/cards\/magnetic-tile-ideas.html"/);
  for (const s of choices) assert.ok(h.includes(s), s);
  assert.doesNotMatch(h, /<iframe|<ol|class="steps-grid"|2 minutes|2 min|low mess|independent play|<li>Make a wall|adapted from a creator video/);
  assert.match(h, /not a finding that all magnetic tiles are unsuitable/);
  assert.ok(h.indexOf('class="tile-build-pause-cue"') < h.indexOf("Different flat house picture"));
  assert.match(h, /old linked creator video was not watched or transcribed/);
});

test("Actual CSV pause dispatch and all six compact owners reproduce published bytes", () => {
  const code = `import sys,csv,json
sys.path.insert(0,'scripts')
import generate_card_pages as c,generate_seo_pages as s
from contributor_pages import with_contributor_credit
row=next(r for r in csv.DictReader(open('data/video_activity_sources.csv')) if r['source_id']=='yt-magna-tiles-preschool')
assert row['kid_step_4']=='Knock it down.'
a=s.ACTIVITIES['magnetic-tile-ideas'];assert a['steps']==[] and a['tile_build_pause']
assert 'magnetic-tile-ideas' not in c.QUICK_CARD_SLUGS and 'magnetic-tile-ideas' not in c.QUICK_CARD_OVERRIDES
out={'cards/magnetic-tile-ideas.html':c.page(row,'magnetic-tile-ideas'),'cards.html':c.cards_index()}
for p in s.PAGES:
 if 'magnetic-tile-ideas' in p.get('activities',[]):out[p['path']]=s.page_html(p)
assert 'magnetic-tile-ideas' not in next(p for p in s.PAGES if p['path']=='collections/stem-activities-for-preschoolers.html')['activities']
print(json.dumps({p:with_contributor_credit(h,p) for p,h in out.items()}))`;
  const out = JSON.parse(execFileSync("python3", ["-B", "-c", code], {encoding: "utf8", maxBuffer: 16 * 1024 * 1024}));
  assert.equal(Object.keys(out).length, 9);
  for (const [p, h] of Object.entries(out)) assert.equal(h, read(p), p);
  for (const p of hubs) {
    const h = [...read(p).matchAll(/<article\b[\s\S]*?<\/article>/g)].map(m => m[0]).find(h => h.includes("<h2>Magnetic Tile Builds (paused)</h2>"));
    assert.ok(h, p);
    for (const s of choices) assert.ok(h.includes(s), p + ": " + s);
    assert.doesNotMatch(h, /<ol|Make a wall\.|Add a roof\.|Change the shape\.|2 min|low help/);
  }
});

test("Every NoCut tile cue and both earlier age-four choices retire the old start", () => {
  const h = read("collections/no-cut-preschool-activities.html");
  const surfaces = [
    h.match(/<h2>Pick a no-cut activity<\/h2>\s*(<p>[\s\S]*?<\/p>)/)[1],
    [...h.matchAll(/<tr>[\s\S]*?<\/tr>/g)].map(m => m[0]).find(s => s.includes("Longer pretend play")),
    [...h.matchAll(/<p>[\s\S]*?<\/p>/g)].map(m => m[0]).find(s => s.includes("tired afternoon")),
    h.match(/<h2>What no-cut should mean<\/h2>\s*(<p>[\s\S]*?<\/p>)/)[1],
    [...h.matchAll(/<li>[\s\S]*?<\/li>/g)].map(m => m[0]).find(s => s.includes("cards/magnetic-tile-ideas.html")),
    [...h.matchAll(/<a class="mini-card"[\s\S]*?<\/a>/g)].map(m => m[0]).find(s => s.includes("cards/magnetic-tile-ideas.html")),
  ];
  for (const s of surfaces) {assert.ok(s);assert.match(s, /paused/);}
  assert.doesNotMatch(h, /magnetic tiles need a quick magnet check|Magnetic tiles need a separate small-piece check|paper rolls, magnetic tiles, or DUPLO/);
  assert.match(surfaces[2], /small-piece check does not supply its missing instructions/);
  assert.match(surfaces[3], /not qualified by a quick magnet check/);
  assert.match(surfaces[4], /DUPLO Games<\/a> fit build-and-pretend play when pieces are in good condition/);
  const a = read(hubs[0]), cue = a.match(/<strong>Quick pick:<\/strong>([\s\S]*?)<\/div>/)[1];
  assert.match(cue, /Magnetic Tile Builds is paused/);
  const rows = [...a.matchAll(/<tr>[\s\S]*?<\/tr>/g)].map(m => m[0]).filter(s => s.includes("Magnetic Tile Builds"));
  assert.equal(rows.length, 2);for (const r of rows) assert.match(r, /paused/);
});

test("Connected Rooms is a different-job pause and only the generic sitemap owner leaves", () => {
  const h = read("collections/building-activities-for-4-year-olds.html").match(/<article[^>]*id="magnetic-tile-ideas"[\s\S]*?<\/article>/)[0];
  assert.match(h, /<h2>Connected Rooms<\/h2>/);
  for (const s of choices) assert.ok(h.includes(s), s);
  assert.match(h, /Two-room version paused/);
  assert.doesNotMatch(h, /<ol|Make one open shape|Build a second shape|Join them with a wall/);
  const sm = read("sitemap.xml");assert.equal((sm.match(/<loc>/g) || []).length, 65);
  assert.doesNotMatch(sm, /<loc>https:\/\/kidactivitylab.com\/cards\/magnetic-tile-ideas.html<\/loc>/);
  assert.match(sm, /<loc>https:\/\/kidactivitylab.com\/cards\/magnetic-tile-house.html<\/loc>/);
  assert.equal((read("cards.html").match(/class="mini-card"/g) || []).length, 36);
  const mini = [...read("cards.html").matchAll(/<a class="mini-card"[\s\S]*?<\/a>/g)].map(m => m[0]).find(s => s.includes("cards/magnetic-tile-ideas.html"));
  assert.match(mini, /Paused; different flat-picture or ONE box\/car job, not two rooms/);
});
