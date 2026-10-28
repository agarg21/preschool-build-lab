import assert from "node:assert/strict";
import fs from "node:fs";
import test from "node:test";
import vm from "node:vm";

const html = fs.readFileSync("site/cards.html", "utf8");
const script = fs.readFileSync("site/assets/cards-finder.js", "utf8");
const css = fs.readFileSync("site/styles.css", "utf8");
const cards = [...html.matchAll(/<a class="mini-card" href="([^"]+)"><strong>[^<]+<\/strong><span>[^<]+<\/span><template data-search="([^"]+)"><\/template><\/a>/g)];

test("library keeps its owner and all static routes without JavaScript", () => {
  assert.match(html, /<link rel="canonical" href="https:\/\/kidactivitylab.com\/cards.html">/);
  assert.equal([...html.matchAll(/<h1>/g)].length, 1);
  assert.equal(cards.length, 36);
  for (const [, href] of cards) assert.ok(fs.existsSync(`site/${href}`), href);
  assert.ok(html.indexOf('href="#activity-card-finder"') < html.indexOf('class="game-promo"'));
  assert.ok(html.indexOf('class="game-promo"') < html.indexOf('id="activity-card-finder"'));
  assert.ok(html.indexOf('href="articles/paper-helicopter-kids.html"') < html.indexOf('id="activity-card-finder"'));
  assert.ok(html.indexOf('href="articles/paper-straw-rocket.html"') < html.indexOf('id="activity-card-finder"'));
  assert.match(html, /<div class="card-finder-controls" hidden>/);
  assert.match(html, /<section class="library-grid" aria-label="Activity cards">/);
  assert.match(html, /<script src="assets\/cards-finder.js\?v=2" defer><\/script>/);
  assert.match(css, /\.library-grid \.mini-card\[hidden\]\s*\{\s*display: none;/);
  assert.match(fs.readFileSync("site/sitemap.xml", "utf8"), /<loc>https:\/\/kidactivitylab.com\/cards.html<\/loc>\s*<lastmod>2026-10-28<\/lastmod>/);
});

test("finder has a named input, status, and a truthful deck route", () => {
  assert.match(html, /<label for="card-finder-query">Find by title or material<\/label>/);
  assert.match(html, /id="card-finder-count" role="status" aria-live="polite"/);
  assert.match(html, /id="card-finder-empty" hidden>No activity cards match\. Try another title or material, or use Clear to see all cards\. Looking for a card game instead\? <a href="collections\/card-games-for-kids.html">/);
  assert.match(css, /\.card-finder\s*\{[^}]*scroll-margin-top: max\(104px, 6rem\)/s);
});

test("literal matching, empty state, and clear work without changing the card source", () => {
  const listeners = {};
  const links = cards.map(([, href, search]) => ({ href, hidden: false, querySelector: () => ({ dataset: { search } }) }));
  const controls = { hidden: true };
  const grid = { querySelectorAll: () => links };
  const query = { value: "", addEventListener: (name, listener) => { listeners[name] = listener; }, focus() { this.focused = true; } };
  const clear = { disabled: true, addEventListener: (name, listener) => { listeners[name] = listener; } };
  const count = { textContent: "" };
  const empty = { hidden: true };
  const nodes = new Map([
    [".card-finder-controls", controls], [".library-grid", grid],
    ["#card-finder-query", query], ["#card-finder-clear", clear],
    ["#card-finder-count", count], ["#card-finder-empty", empty],
  ]);
  vm.runInNewContext(script, { document: { querySelector: (selector) => nodes.get(selector) } });
  assert.equal(controls.hidden, false);
  assert.equal(count.textContent, "36 activity cards");
  assert.equal(links.filter((link) => !link.hidden).length, 36);

  query.value = "   ";
  listeners.input();
  assert.equal(count.textContent, "36 activity cards");
  assert.equal(clear.disabled, false);
  listeners.click();
  assert.equal(query.value, "");
  assert.equal(clear.disabled, true);

  query.value = "  PAPER   tape  ";
  listeners.input();
  assert.equal(count.textContent, "3 of 36 activity cards");
  assert.deepEqual(links.filter((link) => !link.hidden).map((link) => link.href), ["cards/tube-sculpture.html", "cards/paper-chain-test.html", "cards/water-drop-race.html"]);
  assert.equal(empty.hidden, true);
  assert.equal(clear.disabled, false);

  for (const value of ["water paint", "brush", "paint"]) {
    query.value = value;
    listeners.input();
    assert.equal(count.textContent, "0 of 36 activity cards", value);
    assert.equal(empty.hidden, false, value);
  }

  query.value = "painter tape";
  listeners.input();
  assert.deepEqual(links.filter((link) => !link.hidden).map((link) => link.href), ["cards/tape-road.html", "cards/tape-train-tracks.html", "cards/tube-sculpture.html", "cards/tape-city.html", "cards/measuring-tape-jumps.html"]);

  query.value = "painter's tape";
  listeners.input();
  assert.deepEqual(links.filter((link) => !link.hidden).map((link) => link.href), ["cards/tape-road.html", "cards/tape-train-tracks.html", "cards/tube-sculpture.html", "cards/tape-city.html", "cards/measuring-tape-jumps.html"]);

  for (const [term, expected] of [
    ["cup", "cards/color-mixing-cups.html"],
    ["block", "cards/block-tower.html"],
    ["bowl", "cards/spoon-transfer.html"],
    ["container", "cards/sound-shaker-match.html"],
  ]) {
    query.value = term;
    listeners.input();
    assert.ok(links.some((link) => !link.hidden && link.href === expected), `${term} should find ${expected}`);
  }

  query.value = "deck";
  listeners.input();
  assert.equal(count.textContent, "0 of 36 activity cards");
  assert.equal(empty.hidden, false);
  listeners.click();
  assert.equal(query.value, "");
  assert.equal(query.focused, true);
  assert.equal(clear.disabled, true);
  assert.equal(empty.hidden, true);
  assert.equal(links.filter((link) => !link.hidden).length, 36);
});
