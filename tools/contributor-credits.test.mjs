import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import fs from "node:fs";
import path from "node:path";
import test from "node:test";

function htmlFiles(dir) {
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap(entry => {
    const full = path.join(dir, entry.name);
    return entry.isDirectory() ? htmlFiles(full) : full.endsWith(".html") ? [full] : [];
  });
}
const excluded = new Set(["site/googled495b3fc6f0765f8.html", "site/collections/rainy-day-activities-for-preschoolers.html", "site/about.html", "site/contributors/riley-hart.html"]);

test("every editorial surface has one disclosed linked credit after its first H1", () => {
  const editorial = htmlFiles("site").filter(file => !excluded.has(file));
  assert.ok(editorial.length >= 69);
  for (const file of editorial) {
    const html = fs.readFileSync(file, "utf8");
    assert.equal([...html.matchAll(/data-kal-contributor="credit"/g)].length, 1, file);
    assert.equal([...html.matchAll(/data-kal-contributor="style"/g)].length, 1, file);
    const credit = html.match(/<p class="contributor-credit"[^>]*>[\s\S]*?<\/p>/)?.[0];
    assert.ok(credit, file);
    assert.match(credit, /Riley Hart/);
    assert.match(credit, /AI research contributor/);
    assert.ok(html.indexOf(credit) > html.indexOf("</h1>"), file);
    const href = credit.match(/href="([^"]+)"/)[1];
    assert.equal(path.resolve(path.dirname(file), href), path.resolve("site/contributors/riley-hart.html"), file);
  }
  for (const file of excluded) assert.doesNotMatch(fs.readFileSync(file, "utf8"), /data-kal-contributor=/, file);
});

test("profile and publisher explain AI contribution, review and firsthand limits", () => {
  const profile = fs.readFileSync("site/contributors/riley-hart.html", "utf8");
  const about = fs.readFileSync("site/about.html", "utf8");
  assert.match(profile, /<h1>Riley Hart<\/h1>/);
  assert.match(profile, /AI research contributor/);
  assert.match(profile, /separate read-only AI review/);
  assert.match(profile, /rather than sole original authorship/);
  assert.match(profile, /not family testing/);
  assert.match(profile, /no human biography, professional qualification or personal experience/);
  assert.match(profile, /Apoorva personally reviews every page/);
  assert.match(about, /id="apoorva-garg"/);
  assert.match(about, /https:\/\/www.linkedin.com\/in\/apoorvag20\//);
  assert.match(about, /source-check dates belong to the facts checked/);
  assert.doesNotMatch(profile + about, /"@type"\s*:\s*"Person"/);
});

test("credit parser preserves source bytes, accepts attributed H1 and rejects partial markup", () => {
  const script = [
    'import json,sys',
    'sys.path.insert(0,"scripts")',
    'from contributor_pages import with_contributor_credit',
    'original = \'<html><head><title>A</title></head><body><h1 class="title">Bridge &amp; Test</h1><p>Start.</p></body></html>\'',
    'once = with_contributor_credit(original,"articles/test.html")',
    'twice = with_contributor_credit(once,"articles/test.html")',
    'blocked = False',
    'try: with_contributor_credit(original.replace("<p>",\'<p data-kal-contributor="credit">\'),"test.html")',
    'except ValueError: blocked = True',
    'print(json.dumps({"original":original,"once":once,"twice":twice,"blocked":blocked}))'
  ].join("\n");
  const result = JSON.parse(execFileSync("python3", ["-c", script], { encoding: "utf8", env: { ...process.env, PYTHONPYCACHEPREFIX: "/tmp/kal-contributor-tests" } }));
  assert.equal(result.once, result.twice);
  assert.equal(result.blocked, true);
  const stripped = result.once
    .replace(/<link data-kal-contributor="style"[^>]*>\n/, "")
    .replace(/\n        <p class="contributor-credit"[^>]*>[\s\S]*?<\/p>/, "");
  assert.equal(stripped, result.original);
});

test("attribution keeps the paused activity excluded and the publisher schema truthful", () => {
  const ramp = fs.readFileSync("site/articles/cardboard-box-car-ramp-preschoolers.html", "utf8");
  assert.match(ramp, /"author":\s*\{\s*"@type": "Organization",\s*"name": "Kid Activity Lab"/);
  const magnet = fs.readFileSync("site/cards/magnet-hunt.html", "utf8");
  assert.match(magnet, /name="robots" content="noindex,follow"/);
  assert.doesNotMatch(magnet, /class="steps-grid"/);
  const sitemap = fs.readFileSync("site/sitemap.xml", "utf8");
  assert.doesNotMatch(sitemap, /<loc>https:\/\/kidactivitylab.com\/cards\/magnet-hunt.html<\/loc>/);
  for (const route of ["about.html", "contributors/riley-hart.html"]) assert.equal([...sitemap.matchAll(new RegExp("<loc>https://kidactivitylab.com/" + route.replaceAll(".", "\\.") + "</loc>", "g"))].length, 1);
});
