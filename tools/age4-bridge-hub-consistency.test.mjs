import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import fs from "node:fs";
import test from "node:test";

const hub = fs.readFileSync("site/ages/stem-activities-for-4-year-olds.html", "utf8");
const pack = fs.readFileSync("site/collections/original-stem-activities-for-4-year-olds.html", "utf8");
const bridge = hub.match(/<article class="seo-activity">\s*<div>\s*<h2>Bridge Rescue paper bridge<\/h2>[\s\S]*?<\/article>/)?.[0] ?? "";

test("age-four Bridge override changes only the local execution copy", () => {
  const result = JSON.parse(execFileSync("python3", ["-c", `import runpy,json
g=runpy.run_path('scripts/generate_seo_pages.py')
p=next(p for p in g['PAGES'] if p['path']=='ages/stem-activities-for-4-year-olds.html')
print(json.dumps({'local':g['page_activity'](p,'paper-bridge'),'global':g['ACTIVITIES']['paper-bridge']}))`], { encoding: "utf8" }));
  assert.match(result.local.materials, /large lightweight block or soft toy/);
  assert.match(result.local.materials, /each child who can reach it/);
  assert.match(result.local.steps.join(" "), /Gently place one checked object/);
  assert.match(result.local.steps.join(" "), /try one fold or stop/);
  assert.match(result.local.parent, /Stop for sliding books/);
  assert.match(result.local.parent, /fingers clear underneath/);
  assert.match(result.local.parent, /check the empty bridge/);
  assert.doesNotMatch(result.local.steps.join(" "), /toy car|stronger/i);
  assert.equal(result.global.materials, "paper, two books, toy car");
  assert.deepEqual(result.global.steps, ["Put books apart.", "Lay paper across.", "Try a car.", "Fold paper stronger."]);
});

test("rendered hub table and runnable card agree with the maintained pack", () => {
  assert.match(pack, /One large lightweight block or soft toy; check suitability for every child who can reach it/);
  assert.match(pack, /Place the object gently/);
  assert.match(pack, /neither version is promised to hold/);
  assert.match(hub, /<td>Bridge Rescue paper bridge<\/td>[\s\S]*?<td>paper, two low books, one large lightweight block or soft toy; check it for each child who can reach it<\/td>/);
  for (const text of ["one large lightweight block or soft toy", "Gently place one checked object", "try one fold or stop", "fingers clear underneath", "check the empty bridge", "Stop for sliding books", "Collect materials when done", "#bridge-rescue"]) assert.ok(bridge.includes(text), text);
  assert.doesNotMatch(bridge, /toy car|Try a car|Fold paper stronger|testing strength/i);
  assert.match(hub, /A checked block or soft toy crossing a pretend river/);
  assert.equal([...hub.matchAll(/<h1>/g)].length, 1);
  assert.match(hub, /rel="canonical" href="https:\/\/kidactivitylab\.com\/ages\/stem-activities-for-4-year-olds\.html"/);
});

test("sitemap advances only the existing age-four hub URL", () => {
  const sitemap = fs.readFileSync("site/sitemap.xml", "utf8");
  assert.match(sitemap, /<loc>https:\/\/kidactivitylab\.com\/ages\/stem-activities-for-4-year-olds\.html<\/loc>\s*<lastmod>2026-10-09<\/lastmod>/);
  assert.equal(sitemap.split("<loc>https://kidactivitylab.com/ages/stem-activities-for-4-year-olds.html</loc>").length - 1, 1);
});
