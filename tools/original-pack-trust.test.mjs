import assert from "node:assert/strict";
import fs from "node:fs";
import { createHash } from "node:crypto";
import { execFileSync } from "node:child_process";
import test from "node:test";

const pack = fs.readFileSync("site/collections/original-stem-activities-for-4-year-olds.html", "utf8");
const age = fs.readFileSync("site/ages/stem-activities-for-4-year-olds.html", "utf8");
const ids = ["ramp-detective", "bridge-rescue", "shadow-builder", "windproof-tower"];
const article = id => pack.match(new RegExp(`<article[^>]*id="${id}"[\\s\\S]*?</article>`))?.[0] ?? "";

test("pack makes no harmless-material, automatic age-down or measured-time promise", () => {
  assert.doesNotMatch(pack, /do not hurt|adjust down for younger|(?:5-8|6-10) minutes|child can run/);
  for (const text of ["Not family-tested by Kid Activity Lab", "Age four is an editorial starting point", "do not lower its age requirement", "Size alone does not establish fit", "skip the setup", "guaranteed ten-minute finish", "Gather and store materials"]) assert.ok(pack.includes(text), text);
  for (const id of ids) assert.match(article(id), /<strong>Time<\/strong>Not measured; allow for setup and cleanup/);
  for (const id of ids) assert.match(article(id), /href="#before-start"/);
});

test("existing five choices precede the runnable modules and retain unique anchors", () => {
  const opening = pack.slice(0, pack.indexOf('<article class="test-activity"'));
  for (const id of [...ids, "tiny-boat-cargo-test"]) {
    assert.ok(opening.includes(`href="#${id}"`), id);
    assert.equal(pack.split(`id="${id}"`).length - 1, 1);
    assert.ok(article(id));
  }
  assert.match(pack, /scroll-margin-top: 8rem/);
});

test("only optional notes collapse, not required setup or stop instructions", () => {
  const details = [...pack.matchAll(/<details\b[^>]*>([\s\S]*?)<\/details>/g)];
  assert.equal(details.length, 5);
  for (const [, body] of details) {
    assert.match(body, /<summary>Optional/);
    assert.doesNotMatch(body, /<h3>Setup|Read-aloud kid steps|<strong>Safety/);
  }
  assert.doesNotMatch(article("windproof-tower"), /magnetic tiles|DUPLO|do not hurt/);
});

test("reviewed empty-boat module remains exactly frozen", () => {
  assert.equal(createHash("sha256").update(article("tiny-boat-cargo-test")).digest("hex"), "815a41c350555e43d4f9acdf128a29ae1fa893e1ddacef696ba2b3c512bc2af5");
});

test("age-hub four local overrides qualify timing and effort without changing shared defaults", () => {
  const result = JSON.parse(execFileSync("python3", ["-c", `import runpy,json
g=runpy.run_path('scripts/generate_seo_pages.py')
p=next(p for p in g['PAGES'] if p['path']=='ages/stem-activities-for-4-year-olds.html')
keys=['car-ramp-distance-test','paper-bridge','shadow-shape-match','wind-tower-test']
print(json.dumps({'local':[g['page_activity'](p,k) for k in keys], 'global':[g['ACTIVITIES'][k] for k in keys]}))`], { encoding: "utf8" }));
  for (const row of result.local) {
    assert.equal(row.time, "Time not measured");
    assert.equal(row.mess, "Not measured");
    assert.equal(row.mess_label, "Dry setup; cleanup varies");
    assert.equal(row.help_label, "Adult stays involved");
  }
  assert.deepEqual(result.global.map(row => row.time), ["5 min", "3 min", "5 min", "6 min"]);
  assert.equal(age.split('class="tag">Time not measured</span>').length - 1, 4);
  assert.doesNotMatch(age, /fast reset|Calm, low mess|Adult stays involved help/);
});

test("source limits and existing SEO owners remain explicit", () => {
  for (const text of ["September 25, 2026", "December 19, 2024", "February 27, 2026", "They do not endorse these setups", "not tested adaptations", "not newly validated"]) assert.ok(pack.includes(text), text);
  for (const [html, path] of [[pack, "collections/original-stem-activities-for-4-year-olds.html"], [age, "ages/stem-activities-for-4-year-olds.html"]]) {
    assert.equal([...html.matchAll(/<h1>/g)].length, 1);
    assert.ok(html.includes(`rel="canonical" href="https://kidactivitylab.com/${path}"`));
    assert.doesNotMatch(html, /name="robots" content="noindex/);
  }
});
