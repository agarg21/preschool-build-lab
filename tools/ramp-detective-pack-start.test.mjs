import assert from "node:assert/strict";
import fs from "node:fs";
import { execFileSync } from "node:child_process";
import test from "node:test";

const html = fs.readFileSync("site/collections/original-stem-activities-for-4-year-olds.html", "utf8");
const ramp = html.match(/<article class="test-activity" id="ramp-detective">[\s\S]*?<\/article>/)?.[0] ?? "";

test("Pack Ramp Detective exposes maintained checks and local stop before its first roll", () => {
  const ol = ramp.indexOf("<ol>");
  for (const text of ['href="#before-start"', 'href="../cards/ramp-texture-test.html"', 'class="activity-start-cue"', "stay beside every reachable child", "Stop for slipping", "before handling", "Keep tape and spares out of reach"]) assert.ok(ramp.indexOf(text) > 0 && ramp.indexOf(text) < ol, text);
  assert.equal(ramp.split('href="../cards/ramp-texture-test.html"').length - 1, 1);
  assert.match(ramp, /covering on the ramp, not the landing surface/);
  assert.match(ramp, /Not measured; allow for setup and cleanup/);
});

test("Pack Ramp uses the maintained floor setup and controlled optional cover", () => {
  for (const text of ["1 flat stiff cardboard piece", "2 broad sturdy closed books", "1 owned toy car", "1 thin flat dish towel", "owned masking tape", "stack the two books flat", "the other on the floor", "clear landing and walking path", "without pushing", "same books and height", "same car from the same spot", "secures it flat", "skip this roll and finish", "Wait until it stops before retrieving"]) assert.ok(ramp.includes(text), text);
  assert.equal([...ramp.matchAll(/<ol>[\s\S]*?<\/ol>/g)].length, 1);
  assert.equal([...ramp.matchAll(/<li>/g)].length, 8);
  assert.doesNotMatch(ramp, /couch cushion|cardboard or tray|towel, paper|one last roll|farthest: plain/);
});

test("Pack Ramp admits non-results and immediate end without invented outcomes", () => {
  for (const text of ["nearer, farther, about the same, stuck or unclear", "One plain roll is enough", "end whenever wanted", "do not push harder or raise the ramp", "only if stable and wanted", "puts away the car, tape, towel, books and cardboard", "removes floor marks before leaving", "not proof that friction alone caused it", "not a calibrated measurement", "KAL editorial adaptations, not a tested setup", "Not family-tested by Kid Activity Lab"]) assert.ok(ramp.includes(text), text);
  assert.equal([...html.matchAll(/<details\b/g)].length, 5);
  assert.match(ramp, /<summary>Optional parent note<\/summary>/);
  assert.match(ramp, /pbs.org\/parents\/crafts-and-experiments\/friction-racing/);
  assert.match(ramp, /how-to-buy-safe-toys.aspx/);
});

test("Pack remains independently maintained with the existing URL and date", () => {
  const code = "import sys; sys.path.insert(0,'scripts'); import generate_seo_pages as g; assert all(p['path']!='collections/original-stem-activities-for-4-year-olds.html' for p in g.PAGES); print(len(g.ACTIVITIES),len(g.PAGES))";
  assert.equal(execFileSync("python3", ["-B", "-c", code], { encoding: "utf8" }).trim(), "36 15");
  const sitemap = fs.readFileSync("site/sitemap.xml", "utf8");
  assert.equal([...sitemap.matchAll(/<loc>/g)].length, 65);
  assert.match(sitemap, /collections\/original-stem-activities-for-4-year-olds\.html<\/loc>\s*<lastmod>2026-10-29<\/lastmod>/);
  assert.match(html, /rel="canonical" href="https:\/\/kidactivitylab.com\/collections\/original-stem-activities-for-4-year-olds.html"/);
});
