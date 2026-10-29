import assert from "node:assert/strict";
import fs from "node:fs";
import {execFileSync} from "node:child_process";
import test from "node:test";

const read=p=>fs.readFileSync("site/"+p,"utf8");
const hubs=[4,5,6].map(n=>`ages/activities-for-${n}-year-olds-at-home.html`);
const target=h=>[...h.matchAll(/<article\b[\s\S]*?<\/article>/g)].map(m=>m[0]).find(h=>/<h2>Tape City<\/h2>/.test(h));
const card=read("cards/tape-city.html");
test("City four runnable owners put maintained guide, material fit and stop before actions",()=>{
 for(const [i,h]of[card,...hubs.map(p=>target(read(p)))].entries()){
  assert.ok(h);const at=h.indexOf(i===0?'class="steps-grid"':'<ol class="card-steps">');assert.ok(at>=0);
  for(const s of ['href="../articles/painter-tape-road-kids.html"',"EVERY reachable child","hidden-area test","does not guarantee later clean removal","board can tear","Adult applies and removes ALL tape","younger reach you cannot control","not family-tested by Kid Activity Lab","End for peeling tape","BEFORE child access","ONE checked block lying FLAT BESIDE","OUTSIDE the wheel and parking path","No stacking, bridge, roof, ramp","No suitable block? Keep a plain road"])assert.ok(h.indexOf(s)>=0&&h.indexOf(s)<at,s);
  for(const s of ["no building is required","point or watch","ending is valid","collects ALL used tape and bits, roll, vehicle, optional block and spares","out of reach","editorial adaptations","not an inspected creator-video procedure or tested setup"])assert.ok(h.includes(s),s);
  assert.ok(h.includes("BOTH toys without small or detachable parts, magnets or batteries"));
  assert.doesNotMatch(h,/5 min|low mess|low help|Move the city\./);
 }
});
test("City actual CSV dispatcher and compact card remove creator and repeated metadata",()=>{
 assert.match(card,/class="kid-card tape-city-card"/);assert.match(card,/tape-city-readiness/);
 assert.equal((card.match(/href="\.\.\/articles\/painter-tape-road-kids.html"/g)||[]).length,1);
 assert.doesNotMatch(card,/<iframe|g6Sc9cOeD3A|class="meta-tile"|aria-label="Best for"|collections\/indoor-activities-for-preschoolers.html/);
 assert.match(fs.readFileSync("scripts/generate_card_pages.py","utf8"),/"block-tower", "tape-city"\} else page\(row, slug\)/);
 assert.match(read("styles.css"),/\.tape-city-card \.steps-grid \{\s*grid-template-columns: 1fr/);
});
test("City five generated and two static owners agree with historical CSV and bounded membership",()=>{
 const code=`import sys,json,csv
sys.path.insert(0,'scripts')
import generate_card_pages as c,generate_seo_pages as s
from contributor_pages import with_contributor_credit
assert c.SLUGS['yt-masking-tape-city']=='tape-city'
assert 'tape-city' not in c.QUICK_CARD_SLUGS
row=next(r for r in csv.DictReader(open('data/video_activity_sources.csv')) if r['source_id']=='yt-masking-tape-city')
assert row['activity_title']=='Tape City'
out={'cards/tape-city.html':c.quick_page('tape-city'),'cards.html':c.cards_index()}
for p in s.PAGES:
 if p['path']=='collections/indoor-activities-for-preschoolers.html':assert 'tape-city' not in p['activities']
 if 'tape-city' in p.get('activities',[]):out[p['path']]=s.page_html(p)
print(json.dumps({p:with_contributor_credit(h,p) for p,h in out.items()}))`;
 const out=JSON.parse(execFileSync("python3",["-B","-c",code],{encoding:"utf8",maxBuffer:16*1024*1024}));assert.equal(Object.keys(out).length,5);
 for(const[p,h]of Object.entries(out))assert.equal(h,read(p),p);
 for(const p of["collections/toy-car-activities.html","materials/painter-tape.html"])assert.match(read(p),/<meta name="robots" content="noindex,follow">/);
});
test("City discovery preserves guide ownership, unknown duration and bounded host repair",()=>{
 for(const p of["cards.html","collections/toy-car-activities.html","materials/painter-tape.html"]){const e=read(p).match(/<a class="mini-card" href="(?:\.\.\/)?cards\/tape-city.html">[\s\S]*?<\/a>/)?.[0];assert.ok(e);assert.match(e,/Guide first/);assert.doesNotMatch(e,/5 min|Masking tape/)}
 const age4=read(hubs[0]);assert.match(age4,/Quietness, mess and setup time are not measured/);assert.doesNotMatch(age4,/If you need quiet pretend play, choose Tape City/);
 assert.match(read("collections/toy-car-activities.html"),/\.toy-car-page h1 \{ overflow-wrap: anywhere;/);
 assert.equal((read("cards.html").match(/class="mini-card"/g)||[]).length,36);assert.equal((read("sitemap.xml").match(/<loc>/g)||[]).length,65);
 assert.match(read("sitemap.xml"),/cards\/tape-city.html<\/loc>\n    <lastmod>2026-10-28<\/lastmod>/);
 assert.match(read("sitemap.xml"),/articles\/painter-tape-road-kids.html<\/loc>\n    <lastmod>2026-10-28<\/lastmod>/);
});
