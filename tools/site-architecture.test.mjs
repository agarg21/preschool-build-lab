import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import fs from "node:fs";
import path from "node:path";
import test from "node:test";

const ROOT = process.cwd();
const SITE = path.join(ROOT, "site");
const BASE_URL = "https://kidactivitylab.com";
const VERIFICATION_FILE = "googled495b3fc6f0765f8.html";

function walk(directory) {
  return fs.readdirSync(directory, { withFileTypes: true }).flatMap((entry) => {
    const fullPath = path.join(directory, entry.name);
    return entry.isDirectory() ? walk(fullPath) : [fullPath];
  });
}

function htmlFiles() {
  return walk(SITE).filter((file) => file.endsWith(".html"));
}

function read(file) {
  return fs.readFileSync(file, "utf8");
}

function canonicalFromHtml(html) {
  return html.match(/<link\s+rel="canonical"\s+href="([^"]+)"/i)?.[1] ?? null;
}

function sitemapUrls() {
  const xml = read(path.join(SITE, "sitemap.xml"));
  return [...xml.matchAll(/<loc>([^<]+)<\/loc>/g)].map((match) => match[1]);
}

function sourceRouteOwnership() {
  const script = `
import json
import sys

sys.path.insert(0, "scripts")
from generate_seo_pages import PAGES

slugs = sorted({slug for page in PAGES for slug in page["activities"]})
print(json.dumps({
    slug: [page["path"] for page in PAGES if slug in page["activities"]]
    for slug in slugs
}))
`;
  return JSON.parse(execFileSync("python3", ["-c", script], {
    cwd: ROOT,
    encoding: "utf8",
    env: { ...process.env, PYTHONPYCACHEPREFIX: "/tmp/kal-site-architecture-tests" },
  }));
}

test("sitemap contains each canonical indexable content URL exactly once", () => {
  const expected = htmlFiles()
    .filter((file) => path.basename(file) !== VERIFICATION_FILE)
    .filter((file) => !/name="robots"\s+content="[^"]*noindex/i.test(read(file)))
    .map((file) => canonicalFromHtml(read(file)));
  const actual = sitemapUrls();

  assert.equal(expected.length, 61);
  assert.ok(expected.every(Boolean), "every indexable page must declare a canonical");
  assert.equal(new Set(actual).size, actual.length, "sitemap URLs must be unique");
  assert.deepEqual([...actual].sort(), [...expected].sort());
  assert.ok(!actual.includes(`${BASE_URL}/${VERIFICATION_FILE}`));
});

test("internal homepage links resolve directly to the root canonical", () => {
  const offenders = [];
  for (const file of htmlFiles().filter((item) => path.basename(item) !== VERIFICATION_FILE)) {
    const html = read(file);
    const canonical = canonicalFromHtml(html) ?? `${BASE_URL}/`;
    for (const match of html.matchAll(/href="([^"]+)"/g)) {
      const href = match[1];
      if (href.startsWith(("mailto:")) || href.startsWith("#")) continue;
      const target = new URL(href, canonical);
      if (target.origin === BASE_URL && target.pathname.endsWith("/index.html")) {
        offenders.push(`${path.relative(ROOT, file)} -> ${href}`);
      }
    }
  }
  assert.deepEqual(offenders, []);
});

test("generated cards expose a restrained set of existing hub routes", () => {
  const cards = walk(path.join(SITE, "cards")).filter((file) => file.endsWith(".html"));
  const ownership = sourceRouteOwnership();
  const unroutedCards = [];

  for (const file of cards) {
    const slug = path.basename(file, ".html");
    const html = read(file);
    const section = html.match(/<section class="parent-strip" aria-label="Related activity pages">([\s\S]*?)<\/section>/);
    if (!section) {
      unroutedCards.push(slug);
      continue;
    }
    const links = [...section[1].matchAll(/href="([^"]+)"/g)].map((match) => match[1]);
    assert.ok(links.length >= 1 && links.length <= 3, `${path.basename(file)} has ${links.length} route links`);
    for (const href of links) {
      const target = path.resolve(path.dirname(file), href);
      const routePath = href.replace(/^\.\.\//, "");
      assert.ok(target.startsWith(SITE), `${href} must remain inside site/`);
      assert.ok(fs.existsSync(target), `${href} must resolve to an existing page`);
      assert.match(href, /^\.\.\/(?:ages|collections)\//);
      assert.ok(ownership[slug]?.includes(routePath), `${slug} is not owned by ${routePath}`);
    }
  }

  assert.equal(cards.length, 37);
  assert.deepEqual(unroutedCards, ["paper-roll-play"]);
});

test("read-only priority inspection covers current release and visible hubs", () => {
  const monitor = JSON.parse(read(path.join(ROOT, "ops", "gsc-monitor.json")));
  const required = [
    `${BASE_URL}/collections/card-games-for-kids.html`,
    `${BASE_URL}/collections/engineering-activities-for-4-year-olds.html`,
    `${BASE_URL}/collections/math-activities-for-4-year-olds-at-home.html`,
  ];

  assert.equal(monitor.urls.length, 10);
  for (const url of required) assert.ok(monitor.urls.includes(url));
});
