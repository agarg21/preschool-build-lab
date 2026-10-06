import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import test from "node:test";

const root = process.cwd();
const card = fs.readFileSync(path.join(root, "site/cards/tape-road.html"), "utf8");
const guide = fs.readFileSync(path.join(root, "site/articles/painter-tape-road-kids.html"), "utf8");

test("Tape Road card exposes one full guide before the optional video and steps", () => {
  const href = 'href="../articles/painter-tape-road-kids.html"';
  assert.equal(card.split(href).length - 1, 1);
  assert.ok(card.indexOf(href) < card.indexOf('class="card-meta"'));
  assert.ok(card.indexOf(href) < card.indexOf('class="video-frame"'));
  assert.ok(card.indexOf('aria-label="Parent check"') < card.indexOf('aria-label="Steps"'));
  assert.ok(card.indexOf('aria-label="Steps"') < card.indexOf('class="video-frame"'));
  assert.match(guide, /<h1>Painter's Tape Road for Kids<\/h1>/);
});

test("card retains a bounded surface choice, stop, and four-step mission", () => {
  for (const marker of [
    "follow the tape maker's guidance",
    "test one strip in an inconspicuous area, then remove it and check the surface",
    "If the floor or finish is unknown or unsuitable",
    "large cardboard sheet, table, or tray",
    "not family-tested by Kid Activity Lab",
    "keeps loose tape and the roll out of reach",
    "Stop for peeling, chewing, wrapping, throwing, mouthing",
    "Adult makes one short road.",
    "Child drives to one parking spot.",
    "Change one short segment.",
    "Adult removes and stores the tape.",
  ]) assert.ok(card.includes(marker), `Missing card boundary: ${marker}`);
  assert.equal([...card.matchAll(/class="step-tile"/g)].length, 4);
  assert.match(card, /<strong>Mess<\/strong>Not measured/);
  assert.doesNotMatch(card, /safe for (?:all|every|any)|we (?:have )?tested this/i);
});

test("Tape Road card preserves its canonical owner and updates its sitemap date", () => {
  assert.match(card, /<link rel="canonical" href="https:\/\/kidactivitylab\.com\/cards\/tape-road\.html">/);
  assert.match(card, /styles\.css\?v=tape-road-card-1/);
  const sitemap = fs.readFileSync(path.join(root, "site/sitemap.xml"), "utf8");
  const entry = [...sitemap.matchAll(/<url>([\s\S]*?)<\/url>/g)]
    .map((match) => match[1]).find((url) => url.includes("cards/tape-road.html"));
  assert.match(entry ?? "", /<lastmod>2026-10-05<\/lastmod>/);
});
