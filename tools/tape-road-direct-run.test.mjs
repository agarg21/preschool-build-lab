import assert from 'node:assert/strict';
import {execFileSync} from 'node:child_process';
import fs from 'node:fs';
import test from 'node:test';

const html = fs.readFileSync('site/articles/painter-tape-road-kids.html', 'utf8');
const source = fs.readFileSync('scripts/generate_seo_pages.py', 'utf8');
const runOf = document => document.match(/<section id="one-road"[\s\S]*?<\/section>/)[0];

test('Tape Road direct run repeats its exact early stop and role before execution', () => {
  for (const document of [source, html]) {
    const quick = document.match(/<section class="road-start-panel"[\s\S]*?<\/section>/)[0];
    const stop = quick.match(/<p class="road-stop">[\s\S]*?<\/p>/)[0];
    const run = runOf(document);
    assert.equal(run.match(/<p class="road-stop">[\s\S]*?<\/p>/)[0], stop);
    assert.equal(
      run.match(/<div class="callout">\s*([\s\S]*?)\s*<\/div>/)[1],
      '<strong>Keep the roles clear:</strong> the adult selects, applies, checks, and removes the tape. The child owns the drive-and-park mission.',
    );
    assert.ok(run.indexOf(stop) < run.indexOf('<div class="callout">'));
    assert.ok(run.indexOf('<div class="callout">') < run.indexOf('<ol class="steps">'));
    const steps = [...run.matchAll(/<li>(.*?)<\/li>/g)].map(match => match[1]);
    assert.deepEqual(steps, [
      'The adult keeps loose tape out of reach and stays close enough to stop the listed actions or a surface change.',
      'The adult reads the tape guidance, checks the chosen surface, applies one test strip, and removes it.',
      'On the selected surface or removable board, the adult lays one broad tape route with one gentle turn.',
      'Add one parking box at the end. Put one adult-selected vehicle at the start.',
      'The child pushes the vehicle along the road and into the parking box.',
    ]);
    assert.ok(quick.indexOf(stop) < quick.indexOf('<ol>'));
  }
});

test('Tape Road relative arrival override is scoped and its guide requests revised CSS', () => {
  const css = fs.readFileSync('site/styles.css', 'utf8');
  assert.match(css, /\.road-article section\[id\] \{\s*scroll-margin-top: 104px;\s*\}/);
  assert.match(css, /\.road-article #one-road \{\s*scroll-margin-top: max\(104px, 7rem\);\s*\}/);
  assert.ok(css.indexOf('.road-article section[id]') < css.indexOf('.road-article #one-road'));
  for (const document of [source, html]) {
    assert.ok(document.includes('href="../styles.css?v=tape-road-direct-run-1"'));
  }
});

test('Tape Road pure source renderer matches the complete published guide', () => {
  const rendered = execFileSync('python3', ['-B', '-c', `
import sys
sys.path.insert(0, 'scripts')
from generate_seo_pages import tape_road_guide_html
from contributor_pages import with_contributor_credit
print(with_contributor_credit(tape_road_guide_html(), 'articles/painter-tape-road-kids.html'), end='')
`], {encoding: 'utf8'});
  assert.equal(rendered, html);
});
