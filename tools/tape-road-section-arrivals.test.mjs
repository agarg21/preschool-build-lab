import assert from 'node:assert/strict';
import fs from 'node:fs';
import test from 'node:test';

test('all six Tape Road sections retain relative sticky-header clearance', () => {
  const html = fs.readFileSync('site/articles/painter-tape-road-kids.html', 'utf8');
  assert.deepEqual([...html.matchAll(/<section id="([^"]+)"/g)].map(match => match[1]), [
    'one-road', 'one-change', 'troubleshooting', 'adapt', 'cleanup', 'evidence',
  ]);
  const css = fs.readFileSync('site/styles.css', 'utf8');
  const rule = css.match(/\.road-article section\[id\] \{([^}]+)\}/)[1];
  assert.match(rule, /^\s*scroll-margin-top: max\(104px, 7rem\);\s*$/);
  assert.doesNotMatch(rule, /scroll-margin-top: 104px;/);
  assert.match(css, /\.road-article #one-road \{\s*scroll-margin-top: max\(104px, 7rem\);\s*\}/);
});
