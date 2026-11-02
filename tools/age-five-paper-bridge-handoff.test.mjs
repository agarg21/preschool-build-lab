import assert from 'node:assert/strict';
import fs from 'node:fs';
import {execFileSync} from 'node:child_process';
import test from 'node:test';

const agePath = 'ages/activities-for-5-year-olds-at-home.html';
const html = fs.readFileSync('site/' + agePath, 'utf8');
const moduleOf = h => [...h.matchAll(/<article class="seo-activity[^"]*">[\s\S]*?<\/article>/g)]
  .map(m => m[0]).find(m => m.includes('<h2>Paper Bridge</h2>'));

test('only the age-five real override dispatches the different-choice renderer', () => {
  const result = JSON.parse(execFileSync('python3', ['-B', '-c', `import json,sys
sys.path.insert(0,'scripts')
import generate_seo_pages as g
p=next(p for p in g.PAGES if p['path']=='${agePath}')
a=g.page_activity(p,'paper-bridge')
print(json.dumps({'steps':a['steps'],'html':g.activity_card(a),'flagged':[p['path'] for p in g.PAGES if g.page_activity(p,'paper-bridge').get('age_five_bridge_choice')],'canonical':g.ACTIVITIES['paper-bridge']}))`], {encoding:'utf8'}));
  assert.deepEqual(result.flagged, [agePath]);
  assert.deepEqual(result.steps, []);
  assert.equal(result.html.trim(), moduleOf(html).trim());
  assert.deepEqual(result.canonical.steps, ['Put books apart.', 'Lay paper across.', 'Try a car.', 'Fold paper stronger.']);
  assert.equal(result.canonical.materials, 'paper, two books, toy car');
  assert.equal(result.canonical.time, '3 min');
  assert.equal(result.canonical.mess, 'low');
});

test('age-five checks and explicit decline precede the one primary card-top route', () => {
  const m = moduleOf(html);
  const link = m.indexOf('href="../cards/paper-bridge.html"');
  assert(link > 0);
  for (const cue of ['Car start not provided', 'did not specify a procedure', 'DIFFERENT stationary-object test, or decline', 'does not supply a car-crossing activity', 'Before handling or opening the card', 'two low closed books', 'EVERY reachable child', 'not a car, coins or marbles', 'gentle placement and a stop cue', 'Skip for mouthing', 'uncontrolled younger-child reach', 'uncertain adult attention', '<strong>Stop:</strong>', 'Remove loose paper pieces', 'points or watches, or end']) {
    assert(m.indexOf(cue) >= 0 && m.indexOf(cue) < link, cue);
  }
  assert.equal([...m.matchAll(/href="[.][.]\//g)].length, 1);
  assert(m.includes('full-guide link adds the optional fold, rescue and cleanup'));
  assert(m.includes('not family-tested by Kid Activity Lab'));
  assert(m.includes('Time and mess are not measured'));
  assert(m.includes('editorial adaptations, not tested protection'));
  assert.doesNotMatch(m, /<ol|<li>|<span class="tag">|#bridge-start-title|Moving-toy road not provided/);
});

test('chooser withdraws the inherited unmeasured car start without changing page identity', () => {
  const row = [...html.matchAll(/<tr>[\s\S]*?<\/tr>/g)].map(m => m[0])
    .find(r => r.includes('Paper Bridge'));
  for (const cue of ['different stationary choice or decline', 'Not measured', 'not a car start', 'read all checks below before handling, or skip']) assert(row.includes(cue), cue);
  assert.doesNotMatch(row, /3 min|<td>low<\/td>|toy car|href=/);
  assert.equal([...html.matchAll(/<h1>/g)].length, 1);
  assert(html.includes('https://kidactivitylab.com/' + agePath));
  assert.equal([...fs.readFileSync('site/sitemap.xml', 'utf8').matchAll(/<loc>/g)].length, 65);
});
