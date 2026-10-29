import assert from "node:assert/strict";
import fs from "node:fs";
import { execFileSync } from "node:child_process";
import test from "node:test";

const read = p => fs.readFileSync(`site/${p}`, "utf8");
const hub = read("collections/engineering-activities-for-4-year-olds.html");
const card = read("cards/foil-boat-test.html");
const pack = read("collections/original-stem-activities-for-4-year-olds.html");
const block = (s, id) => s.match(new RegExp(`<article[^>]+id="${id}"[\\s\\S]*?</article>`))?.[0] ?? "";
const engineering = block(hub, "foil-boat-test");
const original = block(pack, "tiny-boat-cargo-test");

test("Engineering Foil Boat exact checks and required folds route precede execution", () => {
  const stop = engineering.indexOf('class="challenge-stop"');
  const link = engineering.indexOf('href="../cards/foil-boat-test.html"');
  const mission = engineering.indexOf('class="challenge-mission"');
  assert.ok(stop > 0 && stop < link && link < mission);
  assert.ok(mission < engineering.indexOf('<ol class="card-steps">'));
  assert.equal([...engineering.matchAll(/href="\.\.\/cards\/foil-boat-test\.html"/g)].length, 2);
  assert.match(engineering, /Read the empty-boat checks and folds before starting/);
  for (const text of ["Stop for mouthing, torn foil, spills, a moving tray, lost attention or wanting to leave.", "Shallow water still requires continuous adult supervision.", "Open the linked folds and diagram before starting."]) assert.ok(engineering.includes(text), text);
  assert.equal([...engineering.matchAll(/<li>/g)].length, 3);
});

test("card and static Pack stops precede steps including existing start-fragment entry", () => {
  const start = card.match(/<section class="start" id="start"[\s\S]*?<\/section>/)?.[0] ?? "";
  for (const [s, cue] of [[start, "Stop and clear up</strong>"], [original, "Stop and clear up:</strong>"]]) {
    assert.ok(s.indexOf(cue) > 0 && s.indexOf(cue) < s.indexOf("<ol>"));
    assert.equal(s.split(cue).length - 1, 1);
    assert.ok(s.includes("before leaving"));
  }
  assert.ok(start.indexOf('id="start-title"') < start.indexOf("Stop and clear up"));
  assert.equal([...start.matchAll(/<li>/g)].length, 4);
  assert.equal([...original.matchAll(/<li>/g)].length, 3);
  assert.match(original, /href="\.\.\/cards\/foil-boat-test\.html#start"/);
  assert.ok(original.indexOf("empty-boat steps and fold diagram") < original.indexOf("<ol>"));
  for (const text of ["Do not cut the corners", "not a tested best fit", "bottom and sides", "do not switch to a deeper vessel", "not family-tested", "not a cutting template or proof of flotation", "September 24, 2026"]) assert.ok(card.includes(text), text);
  for (const s of [engineering, original]) for (const text of ["no cargo", "without cutting", "bottom and sides", "deeper vessel"]) assert.ok(s.toLowerCase().includes(text), text);
});

test("Foil Boat pure renders match credited outputs without touching static Pack", () => {
  const code = "import sys; sys.path.insert(0,'scripts'); from pathlib import Path; import generate_card_pages as c, generate_seo_pages as s; from contributor_pages import with_contributor_credit as credit; p=next(p for p in s.PAGES if p['path']=='collections/engineering-activities-for-4-year-olds.html'); assert p['activity_overrides']['foil-boat-test']['stop_before_action'] is True; assert all(p['path']!='collections/original-stem-activities-for-4-year-olds.html' for p in s.PAGES); print(credit(c.foil_boat_page(),'cards/foil-boat-test.html')==Path('site/cards/foil-boat-test.html').read_text()); print(credit(s.page_html(p),p['path'])==Path('site',p['path']).read_text())";
  assert.equal(execFileSync("python3", ["-B", "-c", code], { encoding: "utf8" }).trim(), "True\nTrue");
});

test("Foil Boat date changes retain the existing inventory and Engineering date", () => {
  const xml = read("sitemap.xml");
  assert.equal([...xml.matchAll(/<loc>/g)].length, 65);
  for (const p of ["cards/foil-boat-test.html", "collections/original-stem-activities-for-4-year-olds.html", "collections/engineering-activities-for-4-year-olds.html"]) assert.ok(xml.includes(`${p}</loc>\n    <lastmod>2026-10-29</lastmod>`), p);
  assert.match(card, /rel="canonical" href="https:\/\/kidactivitylab.com\/cards\/foil-boat-test.html"/);
  assert.match(card, /width="900" height="1000"/);
  assert.match(card, /No cargo goes inside/);
});
