import assert from 'node:assert/strict';
import fs from 'node:fs';
import {execFileSync} from 'node:child_process';
import test from 'node:test';

const names=['building','engineering'];
const pages=names.map(n=>fs.readFileSync(`site/collections/${n}-activities-for-4-year-olds.html`,'utf8'));
const moduleOf=h=>h.match(/<article[^>]*id="cup-tower"[\s\S]*?<\/article>/)?.[0];

test('both real doorway overrides render the pause, not inherited or old instructions',()=>{
  const result=JSON.parse(execFileSync('python3',['-B','-c',`import json,sys;sys.path.insert(0,'scripts');import generate_seo_pages as g
p=[p for p in g.PAGES if p.get('building_layout') or p.get('engineering_layout')]
print(json.dumps([{'steps':g.page_activity(p,'cup-tower')['steps'],'html':(g.building_activity_card if p.get('building_layout') else g.engineering_activity_card)(g.page_activity(p,'cup-tower'))} for p in p]))`],{encoding:'utf8'}));
  assert.equal(result.length,2);
  for(const r of result){assert.deepEqual(r.steps,[]);assert.match(r.html,/Do not start this version/);assert.doesNotMatch(r.html,/<ol|<li>|Place one cup across|Make two short|Build two short|Move the two walls/);}
});

test('both published pauses distinguish jobs and put chosen checks before handling',()=>{
  for(const h of pages){const m=moduleOf(h);assert(m);for(const s of ['Cup doorway version paused','Do not start this version.','BEFORE handling','EVERY reachable child','Adult stays beside','Skip for mouthing','Different Cup Tower stacking','no toy opening','Different one-car Box Garage','DIFFERENT materials','ONE park-and-out job','Neither choice fulfills','not family-tested by Kid Activity Lab'])assert(m.includes(s),s);assert(m.includes('href="../cards/cup-tower.html"'));assert(m.includes('href="../cards/box-garage.html"'));assert.doesNotMatch(m,/<ol|<li>|Open the base activity card|If the build stalls|First change/);}
});

test('earlier chooser and before-image cues cannot invite the withdrawn doorway',()=>{
  for(const h of pages){const row=[...h.matchAll(/<tr>[\s\S]*?<\/tr>/g)].map(x=>x[0]).find(s=>s.includes('href="#cup-tower"'));assert.match(row,/Cup Doorway \(paused\)/);assert.match(row,/before handling/);}
  assert.match(pages[1],/Wind Tower: Keep the build low and run one gentle test/);
  const warning=pages[0].indexOf('class="building-image-warning"');assert(warning>=0&&warning<pages[0].indexOf('class="building-visual"'));assert.match(pages[0],/Material checks do not supply its missing instructions/);assert.match(pages[0],/cup-doorway depiction is withdrawn as instructions/);
});

test('doorway pause retains existing identity and does not change sitemap ownership',()=>{
  pages.forEach((h,i)=>{assert.equal([...h.matchAll(/<h1>/g)].length,1);assert(h.includes(`https://kidactivitylab.com/collections/${names[i]}-activities-for-4-year-olds.html`));assert(!h.includes('name="robots" content="noindex'));assert.equal([...h.matchAll(/id="cup-tower"/g)].length,1);});
  assert.equal([...fs.readFileSync('site/sitemap.xml','utf8').matchAll(/<loc>/g)].length,65);
  assert.doesNotMatch(fs.readFileSync('site/cards/cup-tower.html','utf8'),/Cup doorway version paused/);
});
