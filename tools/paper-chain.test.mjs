import assert from "node:assert/strict";
import fs from "node:fs";
import test from "node:test";

const html = fs.readFileSync("site/cards/paper-chain-test.html", "utf8");

test("paper chain upgrades its existing canonical without a sibling", () => {
  assert.equal([...html.matchAll(/<h1>/g)].length, 1);
  assert.match(html, /rel="canonical" href="https:\/\/kidactivitylab.com\/cards\/paper-chain-test.html"/);
  assert.equal(fs.readFileSync("site/sitemap.xml", "utf8").split("/cards/paper-chain-test.html").length - 1, 1);
  assert.ok(!fs.existsSync("site/articles/paper-chain-test.html"));
});

test("paper chain explains thread before closure without relying on its image", () => {
  const start = html.slice(html.indexOf('<section class="start"'), html.indexOf('<figure>'));
  for (const text of ["its own ends", "open strip through the hole", "new strip's own ends", "not taped to each other", "Repeat through the newest loop", "Stay beside your child"]) assert.ok(start.includes(text), text);
  assert.ok(start.indexOf("open strip through the hole") < start.indexOf("new strip's own ends"));
});

test("paper chain retains bounded recovery and an honest fit boundary", () => {
  for (const text of ["not family-tested", "not a tested best size", "put scissors away", "no wearing chains", "goes in a mouth", "original pieces", "Skip tape handling", "Gather all strips, tape and offcuts", "have not been measured", "outcomes remain unknown"]) assert.ok(html.includes(text), text);
  assert.doesNotMatch(html, /\b6 min\b|\blow mess\b|safe for (?:all|every)|guaranteed/i);
});

test("optional one-sheet rules follow the runnable answer", () => {
  const optional = html.slice(html.indexOf('<section id="challenge"'), html.indexOf('<details><summary>Sources'));
  for (const text of ["<details>", "one sheet per attempt", "same size and type", "interlocking loops only", "does not extend", "without stretching", "fresh sheet starts a new attempt", "without the one-sheet rule"]) assert.ok(optional.includes(text), text);
  assert.ok(html.indexOf('id="challenge"') > html.indexOf('id="rescue"'));
});

test("paper chain library and hub agree without replacing the book mission", () => {
  const library = fs.readFileSync("site/cards.html", "utf8");
  assert.match(library, /cards\/paper-chain-test.html"><strong>Paper Chain Test<\/strong><span>Open-ended/);
  const hub = fs.readFileSync("site/collections/engineering-activities-for-4-year-olds.html", "utf8");
  assert.match(hub, /Thread each open strip through the last loop, then overlap and tape that strip&#x27;s own ends/);
  assert.match(hub, /wrap around the book and meet at the top/);
  assert.match(html, /engineering-activities-for-4-year-olds.html#paper-chain-test/);
});

test("paper chain map has stable dimensions and a complete nonvisual alternative", () => {
  const png = fs.readFileSync("site/assets/paper-chain/linked-loops.png");
  assert.equal(png.subarray(1, 4).toString(), "PNG");
  assert.equal(png.readUInt32BE(16), 900);
  assert.equal(png.readUInt32BE(20), 1100);
  assert.match(html, /width="900" height="1100"/);
  assert.match(html, /alt="Three stages:[^"]+not taped to each other/);
  assert.match(html, /not to scale or a cutting template/);
});
