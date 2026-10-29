import assert from "node:assert/strict";
import fs from "node:fs";
import { execFileSync } from "node:child_process";
import test from "node:test";

const hub = fs.readFileSync("site/collections/engineering-activities-for-4-year-olds.html", "utf8");
const card = fs.readFileSync("site/cards/paper-chain-test.html", "utf8");
const module = hub.match(/<article[^>]+id="paper-chain-test"[\s\S]*?<\/article>/)?.[0] ?? "";

test("Engineering chain checks and required card route precede execution", () => {
  const stop = module.indexOf('class="challenge-stop"');
  const route = module.indexOf('href="../cards/paper-chain-test.html"');
  const mission = module.indexOf('class="challenge-mission"');
  assert.ok(stop > 0 && stop < route && route < mission);
  assert.ok(mission < module.indexOf('<ol class="card-steps">'));
  assert.equal([...module.matchAll(/href="\.\.\/cards\/paper-chain-test\.html"/g)].length, 2);
  assert.ok(module.includes("Read linked-loop checks and diagram before starting"));
  assert.ok(module.indexOf("Open the linked-loop steps and diagram") > module.indexOf("If the build stalls"));
});

test("book reach and linked-loop defaults remain distinct from optional one-sheet rules", () => {
  for (const text of ["Build a paper chain long enough to wrap around the book and meet at the top.", "Thread each open strip through the last loop, then overlap and tape that strip&#x27;s own ends.", "pre-cut paper strips, painter tape, one book", "Keep scissors out of the play area and use a light book with rounded corners."]) assert.ok(module.includes(text), text);
  assert.equal([...module.matchAll(/<li>/g)].length, 3);
  assert.ok(card.indexOf("Before you start:") < card.indexOf("<li>Curl one strip."));
  assert.match(card, /without the one-sheet rule/);
  assert.match(card, /not family-tested by Kid Activity Lab/);
  assert.match(card, /assets\/paper-chain\/linked-loops\.png/);
});

test("Engineering pure renders retain the reviewed output and contributor", () => {
  const result = execFileSync("python3", ["-B", "-c", "from pathlib import Path; import scripts.generate_seo_pages as g; from scripts.contributor_pages import with_contributor_credit as credit; p=next(p for p in g.PAGES if p['path']=='collections/engineering-activities-for-4-year-olds.html'); assert p['activity_overrides']['paper-chain-test']['stop_before_action'] is True; print(g.page_html(p)==g.page_html(p)); print(credit(g.page_html(p),p['path'])==Path('site',p['path']).read_text())"], { encoding: "utf8" });
  assert.equal(result.trim(), "True\nTrue");
});

test("Engineering date advances without changing card ownership or content inventory", () => {
  const xml = fs.readFileSync("site/sitemap.xml", "utf8");
  assert.equal([...xml.matchAll(/<loc>/g)].length, 65);
  assert.match(xml, /collections\/engineering-activities-for-4-year-olds\.html<\/loc>\s*<lastmod>2026-10-29<\/lastmod>/);
  assert.match(xml, /cards\/paper-chain-test\.html<\/loc>\s*<lastmod>2026-10-15<\/lastmod>/);
  assert.match(card, /rel="canonical" href="https:\/\/kidactivitylab.com\/cards\/paper-chain-test.html"/);
});
