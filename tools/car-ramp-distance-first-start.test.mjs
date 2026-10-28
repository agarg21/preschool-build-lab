import assert from "node:assert/strict";
import fs from "node:fs";
import {execFileSync} from "node:child_process";
import test from "node:test";
const read=p=>fs.readFileSync("site/"+p,"utf8"),card=read("cards/car-ramp-distance-test.html");
const title=p=>p.includes("engineering")?"Target Ramp":p.includes("stem-activities-for-4-")?"Ramp Detective car test":p.includes("activities-for-4-")?"Cardboard ramp for toy cars":"Car Ramp Distance Test";
const target=(h,t)=>[...h.matchAll(/<article\b[\s\S]*?<\/article>/g)].map(m=>m[0]).find(h=>h.includes("<h2>"+t+"</h2>"));
test("Distance card defines one checked no-push stopping observation before optional comparison",()=>{
 assert.match(card,/<h1>Car Ramp Distance Test<\/h1>/);assert.match(card,/canonical" href="https:\/\/kidactivitylab.com\/cards\/car-ramp-distance-test.html"/);
 assert.doesNotMatch(card,/<iframe|5 minutes|5 min|low mess|adapted from a creator video and simplified/);
 for(const s of["TWO broad sturdy closed books","EVERY reachable child","WITHOUT pushing","SAME car, ramp, floor and release spot","no tape or loose marker required","no stronger push, taller support or forced repeat","not family-tested by Kid Activity Lab","The old creator video was not watched"])assert.ok(card.includes(s),s);
 const cue=card.indexOf('class="distance-start-cue"'),guide=card.indexOf('#ramp-start'),model=card.indexOf("Adult model:"),steps=card.indexOf('class="distance-steps"');
 assert.ok(cue>0&&guide>cue&&model>guide&&steps>model);assert.ok(card.indexOf("Stop for climbing")<steps);assert.ok(card.indexOf("EVERY reachable child")<steps);assert.ok(card.indexOf("Sources and testing status")>steps);
 assert.match(card,/farther stop means higher speed/);assert.match(card,/unclear/);assert.match(card,/store all materials out of reach/);
});
test("Distance actual CSV dispatcher and all intentional hub renderers match output",()=>{
 const code=`import sys,json,csv
sys.path.insert(0,'scripts')
import generate_card_pages as c,generate_seo_pages as s
from contributor_pages import with_contributor_credit
row=next(r for r in csv.DictReader(open('data/video_activity_sources.csv')) if r['source_id']=='yt-ramp-measure')
assert row['kid_step_3']=='Try another car.' and row['time']=='5 minutes'
out={'cards/car-ramp-distance-test.html':c.page(row,'car-ramp-distance-test'),'cards.html':c.cards_index()}
for p in s.PAGES:
 if p['path']=='collections/stem-activities-for-preschoolers.html':assert 'car-ramp-distance-test' not in p['activities']
 if 'car-ramp-distance-test' in p.get('activities',[]):out[p['path']]=s.page_html(p)
print(json.dumps({p:with_contributor_credit(h,p) for p,h in out.items()}))`;
 const out=JSON.parse(execFileSync("python3",["-B","-c",code],{encoding:"utf8",maxBuffer:16*1024*1024}));assert.equal(Object.keys(out).length,7);for(const[p,h]of Object.entries(out))assert.equal(h,read(p),p);
});
test("Distance existing compact forms retain separate jobs with before-action checks",()=>{
 const paths=["ages/activities-for-4-year-olds-at-home.html","ages/activities-for-5-year-olds-at-home.html","ages/activities-for-6-year-olds-at-home.html","ages/stem-activities-for-4-year-olds.html","collections/engineering-activities-for-4-year-olds.html"];
 for(const p of paths){const h=target(read(p),title(p));assert.ok(h,p);const step=h.indexOf('<ol class="card-steps">');assert.ok(h.indexOf("EVERY reachable child")>0&&h.indexOf("EVERY reachable child")<step,p);assert.ok(h.indexOf("Stop for")<step,p);assert.ok(h.indexOf("before handling")<step,p);assert.doesNotMatch(h,/5 min|low mess|Raise or lower the ramp by one book|painter tape target/);assert.match(h,/unclear/);assert.match(h,/not family-tested by Kid Activity Lab/)}
 const stem=target(read(paths[3]),title(paths[3]));assert.match(stem,/#before-start/);assert.match(stem,/#ramp-detective/);assert.match(stem,/OPTIONAL surface-change routine/);
 const eng=target(read(paths[4]),title(paths[4]));assert.ok(eng.indexOf("EVERY reachable child")<eng.indexOf("Kid mission:"));assert.match(eng,/adult may LOWER/);assert.match(eng,/moves the hand out before another roll/);
 const home=read(paths[0]);assert.doesNotMatch(home,/I need a proven low-prep activity|Google is already finding this page/);
});
test("Distance discovery, indexability and source-date scope stay bounded",()=>{
 for(const p of["cards.html","collections/toy-car-activities.html"]){const h=read(p).match(/<a class="mini-card" href="(?:\.\.\/)?cards\/car-ramp-distance-test.html">[\s\S]*?<\/a>/)?.[0];assert.ok(h);assert.match(h,/Adult checks, releases and stays/);assert.doesNotMatch(h,/5 min|tape marks/)}
 assert.equal((read("cards.html").match(/class="mini-card"/g)||[]).length,36);assert.equal((read("sitemap.xml").match(/<loc>/g)||[]).length,66);
 assert.doesNotMatch(card,/name="robots"/);assert.match(read("sitemap.xml"),/<loc>https:\/\/kidactivitylab.com\/cards\/car-ramp-distance-test.html<\/loc>\s*<lastmod>2026-10-28<\/lastmod>/);
 assert.match(read("collections/toy-car-activities.html"),/name="robots" content="noindex,follow"/);
 for(const p of["collections/stem-activities-for-preschoolers.html","collections/indoor-activities-for-preschoolers.html"]){assert.ok(read(p));}
});
