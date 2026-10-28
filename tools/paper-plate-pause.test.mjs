import assert from "node:assert/strict";
import fs from "node:fs";
import {execFileSync} from "node:child_process";
import test from "node:test";
import {buildPublicUrlAllowlist,validatePublicSnapshot} from "./gsc-snapshot.mjs";
const read=p=>fs.readFileSync("site/"+p,"utf8"),card=read("cards/paper-plate-ramp.html");
const target=h=>[...h.matchAll(/<article\b[\s\S]*?<\/article>/g)].map(m=>m[0]).find(h=>/<h2>Paper Plate Ramp \(paused\)<\/h2>/.test(h));
test("Plate direct URL pauses before one checked different-material alternative",()=>{
 assert.match(card,/<h1>Paper Plate Ramp<\/h1>/);assert.match(card,/name="robots" content="noindex,follow"/);
 assert.match(card,/canonical" href="https:\/\/kidactivitylab.com\/cards\/paper-plate-ramp.html"/);
 const decline=card.indexOf("Do not start this version."),alt=card.indexOf('href="../articles/cardboard-box-car-ramp-preschoolers.html#ramp-start"');assert.ok(decline>0&&alt>decline);
 for(const h of[card,...[5,6].map(n=>target(read(`ages/activities-for-${n}-year-olds-at-home.html`)))]){
  assert.ok(h);for(const s of["Do not start this version.","Different materials: cardboard-ramp guide","flat stiff cardboard, TWO broad sturdy closed books","EVERY reachable child","BEFORE child handling","Only have a plate","Do not switch","Do not bend, cut or tape a plate","Pointing, watching or declining","use the guide&#x27;s rescue and collection","not family-tested by Kid Activity Lab"])assert.ok(h.includes(s),s);
  assert.doesNotMatch(h,/<iframe|class="steps-grid"|class="card-steps"|5 minutes|5 min|low mess|Make a slope\.|Let it roll\./);
 }
 assert.match(card,/different cut-and-taped spiral/);assert.match(card,/museum project is not being declared unsafe/);assert.match(card,/creator video was not watched/);
});
test("Plate actual CSV card and hub renderers match pause output, with phantom preschool removed",()=>{
 const code=`import sys,json,csv
sys.path.insert(0,'scripts')
import generate_card_pages as c,generate_seo_pages as s
from contributor_pages import with_contributor_credit
row=next(r for r in csv.DictReader(open('data/video_activity_sources.csv')) if r['source_id']=='yt-paper-plate-ramp')
assert row['materials']=='paper plate; toy car; books' and row['kid_step_1']=='Make a slope.'
assert s.ACTIVITIES['paper-plate-ramp']['steps']==[]
out={'cards/paper-plate-ramp.html':c.page(row,'paper-plate-ramp'),'cards.html':c.cards_index()}
for p in s.PAGES:
 if p['path']=='collections/stem-activities-for-preschoolers.html':assert 'paper-plate-ramp' not in p['activities']
 if 'paper-plate-ramp' in p.get('activities',[]):out[p['path']]=s.page_html(p)
print(json.dumps({p:with_contributor_credit(h,p) for p,h in out.items()}))`;
 const out=JSON.parse(execFileSync("python3",["-B","-c",code],{encoding:"utf8",maxBuffer:16*1024*1024}));assert.equal(Object.keys(out).length,4);for(const[p,h]of Object.entries(out))assert.equal(h,read(p),p);
});
test("Plate discovery stays honest while only one sitemap owner is withdrawn",()=>{
 for(const p of["cards.html","collections/toy-car-activities.html"]){const e=read(p).match(/<a class="mini-card" href="(?:\.\.\/)?cards\/paper-plate-ramp.html">[\s\S]*?<\/a>/)?.[0];assert.ok(e);assert.match(e,/Paused; cardboard-ramp alternative uses different materials/);assert.doesNotMatch(e,/5 min/)}
 assert.equal((read("cards.html").match(/class="mini-card"/g)||[]).length,36);
 const sm=read("sitemap.xml");assert.equal((sm.match(/<loc>/g)||[]).length,66);assert.doesNotMatch(sm,/<loc>https:\/\/kidactivitylab.com\/cards\/paper-plate-ramp.html<\/loc>/);assert.match(sm,/articles\/cardboard-box-car-ramp-preschoolers.html<\/loc>/);
 for(const p of["ages/activities-for-5-year-olds-at-home.html","ages/activities-for-6-year-olds-at-home.html"]){const h=read(p);assert.match(h,/<td>Paper Plate Ramp<\/td>\s*<td>Paused<\/td>/);assert.doesNotMatch(target(h),/Open card/)}
});
test("Plate historical URL allowance is finite and does not reinstate indexing",()=>{
 const config=JSON.parse(fs.readFileSync('ops/gsc-monitor.json','utf8')),url='https://kidactivitylab.com/cards/paper-plate-ramp.html';
 assert.deepEqual(config.historical_public_urls,['https://kidactivitylab.com/cards/magnet-hunt.html',url]);assert(!config.urls.includes(url));
 const urls=[...read('sitemap.xml').matchAll(/<loc>([^<]+)<\/loc>/g)].map(m=>m[1]);const allowed=buildPublicUrlAllowlist(config,urls);assert(allowed.has(url));
 for(const f of fs.readdirSync('ops/gsc-snapshots').filter(f=>f.endsWith('.json')))validatePublicSnapshot(JSON.parse(fs.readFileSync('ops/gsc-snapshots/'+f)),allowed);
});
