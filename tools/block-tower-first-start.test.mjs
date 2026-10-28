import assert from "node:assert/strict";
import fs from "node:fs";
import {execFileSync} from "node:child_process";
import test from "node:test";
const read=p=>fs.readFileSync("site/"+p,"utf8"),card=read("cards/block-tower.html");
const hubs=["ages/activities-for-3-year-olds-at-home.html","collections/no-prep-activities-for-preschoolers.html","collections/independent-activities-for-preschoolers.html","collections/math-activities-for-4-year-olds-at-home.html","collections/no-prep-stem-activities-for-4-year-olds.html"];
const target=h=>[...h.matchAll(/<article\b[\s\S]*?<\/article>/g)].map(m=>m[0]).find(h=>/<h[12]>(Block Tower|Wide-Base Tower)<\/h[12]>/.test(h));
const building=target(read("collections/building-activities-for-4-year-olds.html"));
test("Block first-start fit, stop and adult geometry precede all seven runnable actions",()=>{
 for(const [i,h]of[card,...hubs.map(p=>target(read(p))),building].entries()){
  assert.ok(h);const marker=i===0?'class="steps-grid"':'<ol class="card-steps">',at=h.indexOf(marker);assert.ok(at>=0);
  for(const s of ["3 matching intact large lightweight non-interlocking blocks","EVERY reachable child","younger reach you cannot control","not family-tested by Kid Activity Lab","BEFORE child access","TWO blocks flat side by side","THIRD flat on ONE lower block","entire bottom supported","NOT across the seam","Keep only TWO blocks high","use a flat row or end","top block off FIRST","not a stability guarantee","End for mouthing"])assert.ok(h.indexOf(s)>=0&&h.indexOf(s)<at,s);
  for(const s of ["or point for the adult","adult removes any top FIRST","ALL THREE flat in a row","no required count, height or knockdown","collects ALL THREE blocks and any spares","out of reach","not an inspected creator-video procedure or tested setup"])assert.ok(h.includes(s),s);
  assert.doesNotMatch(h,/\b2 minutes\b|\b2 min\b|low mess|low help|Make it taller\.|Knock down\./);
 }
});
test("Block compact card uses actual CSV quick dispatch without video or purpose repetition",()=>{
 assert.match(card,/class="kid-card block-tower-card"/);assert.match(card,/block-tower-readiness/);
 for(const label of ["Trial","Offer"])assert.ok(card.includes("<p><strong>"+label+":</strong>"));
 assert.doesNotMatch(card,/<iframe|q3HXNJxREy8|class="meta-tile"|aria-label="Best for"|collections\/indoor-activities-for-preschoolers.html/);
 assert.match(card,/href="\.\.\/collections\/building-activities-for-4-year-olds.html"/);
 assert.match(read("styles.css"),/\.block-tower-card \.steps-grid \{\s*grid-template-columns: 1fr/);
 assert.match(fs.readFileSync("scripts/generate_card_pages.py","utf8"),/"tape-train-tracks", "block-tower", "tape-city"\} else page\(row, slug\)/);
});
test("Block eight generated surfaces agree, keeping actual indoor outside membership",()=>{
 const code=`import sys,json,csv
sys.path.insert(0,'scripts')
import generate_card_pages as c,generate_seo_pages as s
from contributor_pages import with_contributor_credit
assert c.SLUGS['yt-block-play-benefits']=='block-tower'
assert 'block-tower' not in c.QUICK_CARD_SLUGS
row=next(r for r in csv.DictReader(open('data/video_activity_sources.csv')) if r['source_id']=='yt-block-play-benefits')
assert row['activity_title']=='Block Play' and row['kid_step_3']=='Knock down.'
out={'cards/block-tower.html':c.quick_page('block-tower'),'cards.html':c.cards_index()}
for p in s.PAGES:
 if p['path']=='collections/indoor-activities-for-preschoolers.html':assert 'block-tower' not in p['activities']
 if 'block-tower' in p.get('activities',[]):out[p['path']]=s.page_html(p)
print(json.dumps({p:with_contributor_credit(h,p) for p,h in out.items()}))`;
 const out=JSON.parse(execFileSync("python3",["-B","-c",code],{encoding:"utf8",maxBuffer:16*1024*1024}));assert.equal(Object.keys(out).length,8);
 for(const[p,h]of Object.entries(out))assert.equal(h,read(p),p);
});
test("Block discovery qualifies direct host conflicts and preserves inventories and local dates",()=>{
 const noCut=read("collections/no-cut-preschool-activities.html"),build=read("collections/building-activities-for-4-year-olds.html");
 for(const s of ["Block Tower is an adult-guided three-block start","not a younger-sibling-nearby assurance","A height or size rule alone is not assurance","3 checked owned blocks; adult models and stays"])assert.ok(noCut.includes(s),s);
 assert.match(noCut,/<strong>Start choices<\/strong>/);
 assert.match(noCut,/<h2>Choose a no-cut start<\/h2>/);
 assert.doesNotMatch(noCut,/<strong>Fastest starts<\/strong>|<h2>Fastest no-cut starts<\/h2>/);
 assert.match(build,/Wide-Base Tower below instead requires skipping for mouthing/);
 assert.match(build,/Wide-Base Tower needs three checked matching blocks; adult models and stays/);
 assert.match(read("collections/math-activities-for-4-year-olds-at-home.html"),/overflow-wrap: anywhere; \} @media \(max-width: 480px\) \{ \.hero h1 \{ font-size: min\(2\.5rem, 43px\)/);
 assert.equal((read("cards.html").match(/class="mini-card"/g)||[]).length,36);
 assert.equal((read("sitemap.xml").match(/<loc>/g)||[]).length,66);
 for(const p of["cards/block-tower.html","cards.html",...hubs,"collections/building-activities-for-4-year-olds.html","collections/no-cut-preschool-activities.html"])assert.ok(read("sitemap.xml").includes(p+"</loc>\n    <lastmod>2026-10-28</lastmod>"),p);
 assert.match(read("sitemap.xml"),/collections\/indoor-activities-for-preschoolers.html<\/loc>\n    <lastmod>2026-10-27<\/lastmod>/);
});
