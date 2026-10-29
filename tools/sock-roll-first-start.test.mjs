import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import test from "node:test";

const read = (p) => readFileSync(`site/${p}`, "utf8");
const card = read("cards/sock-ball-roll.html");
const owners = [
  "ages/activities-for-3-year-olds-at-home.html",
  "collections/no-prep-activities-for-preschoolers.html",
  "collections/no-prep-stem-activities-for-4-year-olds.html",
];
const indoor = read("collections/indoor-activities-for-preschoolers.html");
const sockBlock = (html) => [...html.matchAll(/<article\b[\s\S]*?<\/article>/g)]
  .map(m => m[0]).find(block => block.includes("<h2>Sock Ball Roll</h2>"));

test("sock card and all generic entries agree on one early adult decision", () => {
  for (const [label, html] of [["card", card], ...owners.map(p => [p, sockBlock(read(p))])]) {
    assert.ok(html, label);
    const steps = html.indexOf(label === "card" ? 'aria-label="Steps"' : '<ol class="card-steps">');
    for (const cue of ["skip if you cannot watch them all", "pause on request", "Stop for throwing", "not family-tested"]) {
      assert.ok(html.indexOf(cue) >= 0 && html.indexOf(cue) < steps, `${label}: ${cue}`);
    }
    assert.match(html, /two clean soft socks/);
    assert.match(html, /one low empty basket/);
    assert.match(html, /without ties or hard fillers/);
    assert.match(html, /not a rim to roll over/);
    assert.match(html, /touching it is optional/);
    assert.match(html, /bring the basket closer/);
    assert.match(html, /putting away the socks and basket/);
    assert.doesNotMatch(html, /Make a tunnel|Move the tunnel|2 min|low mess|low help/);
  }
});

test("indoor target start preserves early stop and matching compact handoff", () => {
  const block = indoor.match(/<article class="seo-activity indoor-start" id="sock-target-roll">([\s\S]*?)<\/article>/)?.[1];
  assert.ok(block);
  assert.ok(block.indexOf("Stop:") < block.indexOf("Kid idea:"));
  assert.ok(block.indexOf("Parent check:") < block.indexOf('<ol class="card-steps">'));
  assert.match(block, /skip if you cannot watch them all/);
  assert.match(block, /Touching the target is optional/);
  assert.doesNotMatch(block, /into a low basket|collect both bundles|Make a tunnel/);
  assert.equal([...block.matchAll(/<li>/g)].length, 3);
  assert.match(block, /href="\.\.\/cards\/sock-ball-roll.html">Open the matching sock-roll card/);
  const genericSteps = sockBlock(read(owners[0])).match(/<ol class="card-steps">([\s\S]*?)<\/ol>/)?.[1];
  assert.equal(block.match(/<ol class="card-steps">([\s\S]*?)<\/ol>/)?.[1], genericSteps);
});

test("sock source limits, existing ownership and library discovery stay explicit", () => {
  assert.match(card, /Sources and testing status/);
  assert.match(card, /raisingchildren.net.au\/guides\/activity-guides\/movement\/sock-balls/);
  assert.match(card, /not a tested safety method/);
  assert.match(card, /Time, mess, comprehension, enjoyment, learning and physical outcomes are unknown/);
  assert.match(card, /<link rel="canonical" href="https:\/\/kidactivitylab.com\/cards\/sock-ball-roll.html">/);
  assert.equal([...card.matchAll(/<h1>/g)].length, 1);
  assert.equal([...card.matchAll(/data-kal-contributor="credit"/g)].length, 1);
  const library = read("cards.html");
  assert.equal([...library.matchAll(/class="mini-card"/g)].length, 36);
  const entry = library.match(/<a class="mini-card" href="cards\/sock-ball-roll.html">[\s\S]*?<\/a>/)?.[0];
  assert.match(entry, /Open-ended/);
  assert.match(entry, /two clean soft socks/);
  assert.doesNotMatch(entry, /books|2 min/);
});

test("sock update is in sitemap once without creating a new search URL", () => {
  const sitemap = read("sitemap.xml");
  for (const p of ["cards/sock-ball-roll.html", ...owners, "collections/indoor-activities-for-preschoolers.html"]) {
    assert.equal(sitemap.split(`<loc>https://kidactivitylab.com/${p}</loc>`).length - 1, 1);
    const date = owners.includes(p) || p === "collections/indoor-activities-for-preschoolers.html" ? "2026-10-28" : "2026-10-27";
    assert.ok(sitemap.includes(`<loc>https://kidactivitylab.com/${p}</loc>\n    <lastmod>${date}</lastmod>`), p);
  }
  assert.doesNotMatch(sitemap, /articles\/sock/);
});

test("sock route narrow headings and compact tiles have scoped fit rules", () => {
  assert.match(read(owners[0]), /\.hero h1 \{ font-size: min\(2\.5rem, 48px\); \}/);
  assert.match(read(owners[1]), /\.hero h1 \{ font-size: min\(2\.5rem, 43px\); \}/);
  const css = read("styles.css");
  assert.match(css, /\.sock-roll-card \.card-meta \{\s*grid-template-columns: 1fr;/);
  assert.match(css, /\.sock-roll-card \.step-tile p \{\s*margin: 0;\s*font-size: 1\.15rem;/);
});
