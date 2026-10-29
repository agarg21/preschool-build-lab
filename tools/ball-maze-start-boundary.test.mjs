import assert from "node:assert/strict";
import fs from "node:fs";
import { execFileSync } from "node:child_process";
import test from "node:test";

const guide = fs.readFileSync("site/articles/cardboard-ball-maze-kids.html", "utf8");
const hub = fs.readFileSync("site/collections/engineering-activities-for-4-year-olds.html", "utf8");
const module = hub.match(/<article[^>]+id="ball-maze-box"[\s\S]*?<\/article>/)?.[0] ?? "";

test("maze quick stop precedes adult and child execution", () => {
  const start = guide.match(/<section class="maze-start-panel"[\s\S]*?<\/section>/)?.[0] ?? "";
  assert.ok(start.indexOf('class="maze-stop"') > 0);
  assert.ok(start.indexOf('class="maze-stop"') < start.indexOf("<ol>"));
  assert.equal([...start.matchAll(/<li>/g)].length, 2);
  assert.ok(start.indexOf('class="maze-stop"') < start.indexOf("<strong>Mission:</strong>"));
});

test("maze full adult boundary precedes all five steps", () => {
  const first = guide.match(/<section id="first-run"[\s\S]*?<\/section>/)?.[0] ?? "";
  assert.ok(first.indexOf("Adult boundary:") > 0);
  assert.ok(first.indexOf("Adult boundary:") < first.indexOf('<ol class="steps">'));
  assert.equal([...first.matchAll(/<li>/g)].length, 5);
});

test("Engineering maze checks and one full guide precede unchanged mission", () => {
  assert.ok(module.includes('class="challenge-stop"'));
  const stop = module.indexOf('class="challenge-stop"');
  const link = module.indexOf('href="../articles/cardboard-ball-maze-kids.html"');
  const mission = module.indexOf('class="challenge-mission"');
  assert.ok(stop < link && link < mission && mission < module.indexOf('<ol class="card-steps">'));
  assert.equal([...module.matchAll(/href="\.\.\/articles\/cardboard-ball-maze-kids\.html"/g)].length, 1);
  assert.equal([...module.matchAll(/<li>/g)].length, 3);
  for (const text of ["three chunky blocks", "large lightweight foam ball", "The adult controls when the ball enters and leaves the lid.", "This editorial setup is not a safety assurance.", 'href="../cards/ball-maze-box.html"']) assert.ok(module.includes(text), text);
});

test("maze and Engineering renders remain pure and match output", () => {
  const result = execFileSync("python3", ["-c", "from pathlib import Path; import scripts.generate_seo_pages as g; from scripts.contributor_pages import with_contributor_credit as credit; p=next(p for p in g.PAGES if p['path']=='collections/engineering-activities-for-4-year-olds.html'); print(g.ball_maze_guide_html()==g.ball_maze_guide_html()); print(g.page_html(p)==g.page_html(p)); print(credit(g.ball_maze_guide_html(), 'articles/cardboard-ball-maze-kids.html')==Path('site/articles/cardboard-ball-maze-kids.html').read_text()); print(credit(g.page_html(p), p['path'])==Path('site',p['path']).read_text())"], { encoding: "utf8" });
  assert.equal(result.trim(), "True\nTrue\nTrue\nTrue");
  assert.match(guide, /"datePublished": "2026-09-14"/);
  assert.match(guide, /"dateModified": "2026-10-28"/);
  assert.match(guide, /Kid Activity Lab has not recorded a family test/);
});
