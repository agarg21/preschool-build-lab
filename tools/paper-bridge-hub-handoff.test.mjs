import assert from 'node:assert/strict';
import fs from 'node:fs';
import {execFileSync} from 'node:child_process';
import test from 'node:test';

const names=['building','engineering'];
const pages=names.map(n=>fs.readFileSync(`site/collections/${n}-activities-for-4-year-olds.html`,'utf8'));
const moduleOf=h=>h.match(/<article[^>]*id="paper-bridge"[\s\S]*?<\/article>/)?.[0];

test('real paper bridge overrides offer a different checked task without inherited driving steps',()=>{
  const result=JSON.parse(execFileSync('python3',['-B','-c',`import json,sys;sys.path.insert(0,'scripts');import generate_seo_pages as g
p=[p for p in g.PAGES if p.get('building_layout') or p.get('engineering_layout')]
print(json.dumps([{'steps':g.page_activity(p,'paper-bridge')['steps'],'html':(g.building_activity_card if p.get('building_layout') else g.engineering_activity_card)(g.page_activity(p,'paper-bridge'))} for p in p]))`],{encoding:'utf8'}));
  assert.equal(result.length,2);
  for(const r of result){assert.deepEqual(r.steps,[]);assert.match(r.html,/Moving-toy road not provided/);assert.doesNotMatch(r.html,/<ol|<li>|Send the car|Move the toy along|Fold or curve|First change|Open the base activity card/);}
});

test('both hub choices put readiness and stop before the stationary card link',()=>{
  for(const h of pages){const m=moduleOf(h);assert(m);for(const s of ['Choose a DIFFERENT stationary-object test, or decline','does not fulfill','BEFORE handling or opening the card','adult stays beside','two low closed books','EVERY reachable child','no car, coins or marbles','follow a stop cue','Skip for mouthing','uncontrolled younger reach','uncertain adult attention','Remove loose paper pieces','child points or watches','not family-tested by Kid Activity Lab','editorial adaptations'])assert(m.includes(s),s);const link=m.indexOf('href="../cards/paper-bridge.html"');assert(link>m.indexOf('<strong>Stop:</strong>'));assert.doesNotMatch(m,/#first-try|#bridge-start-title|<ol|<iframe/);}
});

test('early paper cues and both illustrated bridges cannot invite the old moving road',()=>{
  for(const h of pages){const row=[...h.matchAll(/<tr>[\s\S]*?<\/tr>/g)].map(x=>x[0]).find(s=>s.includes('href="#paper-bridge"'));assert.match(row,/Different stationary/);assert.match(row,/checks before handling/);}
  assert.match(pages[1],/Read its adult, material and stop checks BEFORE handling, or decline/);
  assert.match(pages[1],/Use this loop for runnable challenges/);
  assert.match(pages[1],/different-card choices and paused versions are not local recipes/);
  const e=pages[1].indexOf('class="paper-bridge-image-warning"');assert(e>=0&&e<pages[1].indexOf('class="engineering-visual"'));assert.match(pages[1],/Do not copy that structure as instructions/);
  const b=pages[0].indexOf('class="building-image-warning"');assert(b>=0&&b<pages[0].indexOf('class="building-visual"'));assert.match(pages[0],/paper on stacked books is also not/);assert.match(pages[0],/not these stacks/);assert.match(pages[0],/larger-block\/watch suggestion does NOT override these checks/);
  assert.match(pages[0],/cup-doorway depiction is withdrawn as instructions/);assert.match(pages[0],/not the three-block start below or a child-bearing route/);assert.match(pages[0],/href="#straw-bridge"/);
});

test('paper handoffs retain existing page and fragment ownership',()=>{
  for(const h of pages)assert.match(h,/styles\.css\?v=[^"]*paper-bridge-1/);
  pages.forEach((h,i)=>{assert.equal([...h.matchAll(/<h1>/g)].length,1);assert(h.includes(`https://kidactivitylab.com/collections/${names[i]}-activities-for-4-year-olds.html`));assert.equal([...h.matchAll(/id="paper-bridge"/g)].length,1);assert(!h.includes('name="robots" content="noindex'));});
  assert.equal([...fs.readFileSync('site/sitemap.xml','utf8').matchAll(/<loc>/g)].length,65);
  for(const f of ['site/cards/paper-bridge.html','site/articles/paper-bridge-challenge-kids.html'])assert.doesNotMatch(fs.readFileSync(f,'utf8'),/Moving-toy road not provided/);
});
