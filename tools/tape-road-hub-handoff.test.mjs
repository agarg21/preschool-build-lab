import assert from 'node:assert/strict';
import {execFileSync} from 'node:child_process';
import fs from 'node:fs';
import test from 'node:test';

const owners = [
  'ages/activities-for-3-year-olds-at-home.html',
  'collections/no-prep-activities-for-preschoolers.html',
  'collections/indoor-activities-for-preschoolers.html',
  'collections/independent-activities-for-preschoolers.html',
  'collections/fine-motor-activities-for-preschoolers.html',
  'collections/no-prep-stem-activities-for-4-year-olds.html',
];
const read = p => fs.readFileSync(`site/${p}`, 'utf8');
const moduleOf = html => [...html.matchAll(/<article\b[\s\S]*?<\/article>/g)]
  .map(m => m[0]).find(s => /<h2>Tape Road(?: Delivery)?<\/h2>/.test(s));
const guideLink = 'href="../articles/painter-tape-road-kids.html"';

test('six Tape Road owners hand off before action without inherited local recipes', () => {
  for (const p of owners) {
    const h = read(p), m = moduleOf(h);
    assert.ok(m, p);
    assert.equal(m.split(guideLink).length - 1, 1, p);
    assert.ok(m.indexOf('Before handling tape or vehicles:') < m.indexOf(guideLink), p);
    assert.ok(m.indexOf(guideLink) < m.indexOf('Optional compact Tape Road card'), p);
    for (const s of ['read the guide', 'or skip this choice', 'Time not measured', 'Mess not measured',
      'Adult handles all tape', 'apply and remove all tape', 'every child who can reach',
      'Skip if you cannot do this', 'drive and park, point, watch or decline',
      'not family tested by Kid Activity Lab', 'outcomes are unknown']) assert.ok(m.includes(s), `${p}: ${s}`);
    assert.doesNotMatch(m, /<ol|<li>|<iframe|3 min|low mess|low help|Peel tape up|Choose where the delivery starts/);
  }
});

test('five shared Tape Road chooser rows disclose unknown time and mess', () => {
  for (const p of owners.filter(p => !p.includes('/indoor-'))) {
    const row = [...read(p).matchAll(/<tr>[\s\S]*?<\/tr>/g)].map(m => m[0])
      .find(s => /<td>Tape Road<\/td>/.test(s));
    assert.ok(row, p);
    assert.match(row, /<td>Time not measured<\/td>/);
    assert.match(row, /<td>Not measured<\/td>/);
    assert.match(row, /surface and vehicle checks in the full guide/);
    assert.doesNotMatch(row, /3 min|<td>low<\/td>/);
  }
});

test('Indoor earlier cues select checks while retaining the Delivery fragment', () => {
  const h = read(owners[2]);
  const row = [...h.matchAll(/<tr>[\s\S]*?<\/tr>/g)].map(m => m[0])
    .find(s => s.includes('href="#tape-road-delivery"'));
  assert.match(row, /time and mess not measured/);
  assert.match(row, /Read the guide before handling; adult chooses, applies and removes all tape/);
  assert.match(h, /Read the Tape Road guide checks first/);
  assert.match(h, /Quietness is not measured/);
  assert.equal(h.split('id="tape-road-delivery"').length - 1, 1);
});

test('maintained guide has its existing stop before quick-start actions with factual dates', () => {
  const h = read('articles/painter-tape-road-kids.html');
  const quick = h.match(/<section class="road-start-panel"[\s\S]*?<\/section>/)?.[0];
  assert.ok(quick);
  assert.ok(quick.indexOf('class="road-stop"') >= 0);
  assert.ok(quick.indexOf('class="road-stop"') < quick.indexOf('<ol>'));
  assert.equal((quick.match(/<li>/g) || []).length, 2);
  assert.match(quick, /for peeling, chewing, or wrapping tape; throwing or mouthing vehicles; leaving the activity area; or any change to the surface/);
  const data = JSON.parse(h.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/)[1]);
  assert.equal(data.datePublished, '2026-09-15');
  assert.equal(data.dateModified, '2026-10-28');
  assert.match(h, /AI-generated setup illustration/);
  assert.match(h, /Exact duration, mess, comprehension/);
});

test('actual six-owner source render matches published output without generator writes', () => {
  const code = `import json,sys
sys.path.insert(0,'scripts')
import generate_seo_pages as g
from contributor_pages import with_contributor_credit
pages=[p for p in g.PAGES if 'tape-road' in p.get('activities',[])]
assert len(pages)==6
assert g.ACTIVITIES['tape-road']['steps']==[]
print(json.dumps({p['path']:with_contributor_credit(g.page_html(p),p['path']) for p in pages}))`;
  const rendered = JSON.parse(execFileSync('python3', ['-B', '-c', code], {encoding:'utf8', maxBuffer:16*1024*1024}));
  assert.deepEqual(Object.keys(rendered).sort(), [...owners].sort());
  for (const [p,h] of Object.entries(rendered)) assert.equal(h, read(p), p);
  const xml = read('sitemap.xml');
  assert.equal((xml.match(/<loc>/g) || []).length, 65);
  for (const p of [...owners,'articles/painter-tape-road-kids.html']) {
    assert.ok(xml.includes(`${p}</loc>\n    <lastmod>2026-10-28</lastmod>`), p);
    assert.equal((read(p).match(/<h1>/g) || []).length, 1);
    assert.ok(read(p).includes(`rel="canonical" href="https://kidactivitylab.com/${p}"`), p);
  }
});
