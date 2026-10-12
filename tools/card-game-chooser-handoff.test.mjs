import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import test from "node:test";

const root = process.cwd();
const page = fs.readFileSync(path.join(root, "site/collections/card-games-for-kids.html"), "utf8");
const styles = fs.readFileSync(path.join(root, "site/styles.css"), "utf8");
const guides = ["concentration", "short-war", "go-fish", "old-maid", "crazy-eights"];

test("all chooser routes land on an adult check before game steps", () => {
  for (const [index, id] of guides.entries()) {
    const link = page.indexOf(`href="#${id}"`);
    const start = page.indexOf(`class="game-guide" id="${id}"`);
    const end = index + 1 < guides.length
      ? page.indexOf(`class="game-guide" id="${guides[index + 1]}"`)
      : page.indexOf('class="rules-register"');
    assert.ok(link > 0 && start > link && end > start, `${id} route exists`);
    const section = page.slice(start, end);
    const heading = section.indexOf("<h2");
    const check = section.indexOf('class="game-guide-check"');
    const facts = section.indexOf('class="game-facts"');
    const steps = section.indexOf('class="game-steps"');
    assert.ok(heading > 0 && check > heading && facts > check && steps > facts, `${id} check is at arrival before facts and steps`);
    assert.match(section, /<strong>Adult stop:<\/strong> Stack cards/);
    assert.match(section, /Stack cards if they are grabbed, thrown, bent, or used to target someone/);
    assert.match(section, /href="#boundary-title">Full parent boundary/);
  }
  assert.equal((page.match(/class="game-guide-check"/g) ?? []).length, guides.length);
});

test("mobile chooser exposes pace and contact in every row", () => {
  const chooser = page.slice(page.indexOf('class="game-chooser"'), page.indexOf('class="parent-boundary"'));
  assert.equal((chooser.match(/data-label="Pace and contact"/g) ?? []).length, guides.length);
  assert.match(styles, /\.game-chooser \.table-wrap\s*\{\s*overflow-x: visible;/);
  assert.match(styles, /\.game-chooser table\s*\{\s*min-width: 0;/);
  assert.match(styles, /\.game-chooser td::before\s*\{\s*content: attr\(data-label\);/);
  assert.match(styles, /\.game-chooser td a\s*\{\s*display: block;/);
  assert.match(styles, /@media \(max-width: 390px\)\s*\{\s*\.game-guide-heading > div:first-child\s*\{\s*min-width: 0;/);
  assert.match(styles, /\.game-guide h2\s*\{\s*font-size: min\(1\.75rem, 40px\);/);
  assert.match(styles, /\.game-guide-heading p\.game-guide-check\s*\{[^}]*color: var\(--ink\);/);
});

test("source and editorial starting rules remain explicit", () => {
  assert.match(page, /ace through six of hearts and diamonds/);
  assert.match(page, /eight-card grid/);
  assert.match(page, /reduced layout is editorial and untested/);
  assert.match(page, /not evidence that KAL observed any setup to be safe or frustration-free/);
});
