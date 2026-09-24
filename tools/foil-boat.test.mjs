import assert from "node:assert/strict";
import fs from "node:fs";
import test from "node:test";

const html = fs.readFileSync("site/cards/foil-boat-test.html", "utf8");
const engineering = fs.readFileSync("site/collections/engineering-activities-for-4-year-olds.html", "utf8");
const original = fs.readFileSync("site/collections/original-stem-activities-for-4-year-olds.html", "utf8");
const module = (page, id) => page.match(new RegExp(`<article[^>]*id="${id}"[\\s\\S]*?</article>`))?.[0] ?? "";

test("foil boat preserves its existing owner and no new URL", () => {
  assert.equal([...html.matchAll(/<h1>/g)].length, 1);
  assert.match(html, /rel="canonical" href="https:\/\/kidactivitylab.com\/cards\/foil-boat-test.html"/);
  assert.equal(fs.readFileSync("site/sitemap.xml", "utf8").split("/cards/foil-boat-test.html").length - 1, 1);
  assert.ok(!fs.existsSync("site/articles/foil-boat.html"));
});

test("folded hull and empty clearance instructions precede the diagram", () => {
  const start = html.slice(0, html.indexOf("<figure>"));
  for (const text of ["20 cm (8 inches) square", "all four edges upward", "not a tested best fit", "neighboring raised edges", "against the outside", "Do not cut the corners", "top open", "rim roughly even", "bottom and sides", "do not switch to a deeper vessel"]) assert.ok(start.includes(text), text);
});

test("boat controls and recovery do not promise cargo fit or safe depth", () => {
  for (const text of ["No coins, blocks or other cargo", "not a load-carrying challenge", "continuous adult supervision", "before leaving", "older child is not a substitute", "drains it over the tray", "Replace torn foil or stop", "not a guarantee against leaks", "Age alone does not decide fit", "not family-tested", "outcomes remain unknown"]) assert.ok(html.includes(text), text);
  assert.doesNotMatch(html, /\b8 min\b|one inch of water|two large cargo|too large to swallow|high engagement/i);
});

test("boat participation and phone help have direct routes and text alternatives", () => {
  for (const text of ['href="#rescue"', 'id="rescue"', 'href="#take-part"', 'id="take-part"', 'href="paper-chain-test.html"', "watch without touching", "cannot attend to everyone", "Sources and what we haven't tested"]) assert.ok(html.includes(text), text);
  assert.match(html, /engineering-activities-for-4-year-olds.html#foil-boat-test/);
});

test("existing boat modules agree on no-cargo default and preserve old anchors", () => {
  for (const part of [module(engineering, "foil-boat-test"), module(original, "tiny-boat-cargo-test")]) {
    assert.ok(part);
    for (const text of ["Empty Foil Boat", "no cargo", "towel", "without cutting", "bottom and sides", "before leaving", "deeper vessel", "foil-boat-test.html"]) assert.ok(part.toLowerCase().includes(text.toLowerCase()), text);
    assert.doesNotMatch(part, /two large|wooden blocks|one inch|DUPLO|counting bears|large cargo|6-10 minutes/i);
  }
  const age = fs.readFileSync("site/ages/stem-activities-for-4-year-olds.html", "utf8");
  assert.doesNotMatch(age, /Tiny Boat Cargo Test|High engagement|one inch of water|large cargo/i);
  assert.match(age, /Open the empty-boat steps and diagram/);
  assert.match(age, /class="tag">Mess: not measured<\/span>/);
  assert.match(age, /class="tag">Adult stays throughout<\/span>/);
  assert.doesNotMatch(age, /Not measured mess|Adult stays throughout help/);
  assert.match(fs.readFileSync("site/cards.html", "utf8"), /foil-boat-test.html"><strong>Empty Foil Boat<\/strong><span>Open-ended/);
});

test("foil map is a stable original explanatory bitmap, not a cutting template", () => {
  const png = fs.readFileSync("site/assets/foil-boat/empty-hull.png");
  assert.equal(png.subarray(1, 4).toString(), "PNG");
  assert.equal(png.readUInt32BE(16), 900);
  assert.equal(png.readUInt32BE(20), 1000);
  assert.match(html, /width="900" height="1000"/);
  assert.match(html, /alt="Three stages:[^"]+No cargo goes inside/);
  assert.match(html, /not a cutting template or proof of flotation/);
});

test("boat source boundaries distinguish original empty start from source cargo trials", () => {
  for (const domain of ["sciencebuddies.org", "discoveryworld.org", "discovere.org", "cpsc.gov"]) assert.ok(html.includes(domain));
  assert.match(html, /September 24, 2026/);
  assert.match(html, /Their cargo experiments are not this simpler empty-boat version/);
  assert.match(html, /KAL editorial choices/);
});
