import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import test from "node:test";

const html = readFileSync("site/collections/stem-activities-for-preschoolers.html", "utf8");
const generator = readFileSync("scripts/generate_seo_pages.py", "utf8");
const styles = readFileSync("site/styles.css", "utf8");
const sitemap = readFileSync("site/sitemap.xml", "utf8");
const image = readFileSync("site/assets/preschool-stem/preschool-stem-three-ways.webp");

function count(pattern, value = html) {
  return [...value.matchAll(pattern)].length;
}

function section(id) {
  const start = html.indexOf(`id="${id}"`);
  assert.notEqual(start, -1, `missing section ${id}`);
  const end = html.indexOf("</article>", start);
  assert.notEqual(end, -1, `missing closing article for ${id}`);
  return html.slice(start, end);
}

test("preschool STEM keeps one established search owner", () => {
  assert.match(html, /<title>STEM Activities for Preschoolers \| Kid Activity Lab<\/title>/);
  assert.match(html, /<link rel="canonical" href="https:\/\/kidactivitylab\.com\/collections\/stem-activities-for-preschoolers\.html">/);
  assert.equal(count(/<h1>/g), 1);
  assert.match(html, /<h1>STEM activities for preschoolers\.<\/h1>/);
  assert.doesNotMatch(html, /name="robots" content="noindex/);
});

test("the three-way chooser is first and links to three complete starts", () => {
  const chooser = html.indexOf('class="stem-mode-links"');
  const disclosure = html.indexOf('class="stem-disclosure"');
  const visual = html.indexOf('class="stem-visual"');
  const starts = html.indexOf('class="stem-starts"');
  assert.ok(chooser > 0 && chooser < disclosure && disclosure < visual && visual < starts);

  const anchors = ["shadow-change", "paper-bridge-test", "continue-a-pattern"];
  for (const anchor of anchors) {
    assert.equal(count(new RegExp(`href="#${anchor}"`, "g")), 1);
    assert.equal(count(new RegExp(`id="${anchor}"`, "g")), 1);
  }
  assert.equal(count(/<article class="stem-start"/g), 3);
  assert.equal(count(/<nav class="stem-mode-links"[\s\S]*?<a href=/g), 1);
});

test("all three starts expose the frozen planning outputs", () => {
  const expected = {
    "shadow-change": [
      "Shadow Builder",
      "a flashlight, one large opaque block or household object, and a blank wall",
      "follow a one-step stop cue",
      "The adult operates the flashlight",
      "Put the flashlight on a stable surface",
      "Do not aim the light at a face",
      "Stop after the two contrasting shadows",
    ],
    "paper-bridge-test": [
      "Bridge Rescue",
      "one sheet of paper, two broad closed books",
      "release one light object without lifting, climbing on, or striking the books",
      "The adult owns the supports",
      "one book flat on each side of a short floor-level gap",
      "fold it once",
      "Stop after one flat and one folded test",
    ],
    "continue-a-pattern": [
      "Pattern Path",
      "two colors or types of large blocks",
      "match two visibly different pieces",
      "switch to matching two alike pieces",
      "Start an A-B-A-B sequence",
      "appropriate for the youngest child who can reach them",
      "Collect every loose piece at cleanup",
    ],
  };

  for (const [id, phrases] of Object.entries(expected)) {
    const block = section(id);
    for (const phrase of phrases) assert.match(block, new RegExp(phrase.replaceAll("-", "\\-")));
    assert.match(block, /Materials or substitute/);
    assert.match(block, /Substitution:/);
    assert.match(block, /Readiness:/);
    assert.match(block, /Adult setup:/);
    assert.match(block, /Kid mission:/);
    assert.match(block, /Stop and reset/);
  }
  assert.doesNotMatch(section("continue-a-pattern"), /add one more piece|second extension/i);
});

test("evidence limits and the required illustration are explicit", () => {
  assert.match(html, /Kid Activity Lab has not family-tested these setups/);
  assert.match(html, /Timing, mess, comprehension, engagement, enjoyment, learning, repeatability, frustration, and safety outcomes are unknown/);
  assert.match(html, /AI-generated illustration/);
  assert.match(html, /From left: science shadow materials, engineering paper-bridge materials, and math pattern materials/);
  assert.match(html, /not a family-test photo or evidence of measured use or outcomes/);
  assert.match(html, /src="\.\.\/assets\/preschool-stem\/preschool-stem-three-ways\.webp"/);
  assert.match(html, /width="1672" height="941"/);
  assert.match(html, /four alternating blue-and-yellow pieces with one loose blue piece/);
  assert.equal(image.subarray(0, 4).toString("ascii"), "RIFF");
  assert.equal(image.subarray(8, 12).toString("ascii"), "WEBP");
  assert.ok(image.byteLength > 20_000 && image.byteLength < 300_000);
});

test("deeper owners remain distinct and optional routes stay optional", () => {
  for (const route of [
    "../collections/science-experiments-for-4-year-olds.html",
    "../collections/engineering-activities-for-4-year-olds.html",
    "../collections/math-activities-for-4-year-olds-at-home.html",
    "../ages/stem-activities-for-4-year-olds.html",
  ]) {
    assert.match(html, new RegExp(`href="${route}"`));
  }
  const optional = html.slice(html.indexOf("Optional library routes"), html.indexOf("Research sources and limits"));
  assert.match(optional, /original-stem-activities-for-4-year-olds\.html/);
  assert.match(optional, /\.\.\/cards\.html/);
  assert.doesNotMatch(html.slice(0, html.indexOf("Optional library routes")), /original-stem-activities-for-4-year-olds\.html/);
});

test("the former engineering-heavy and search-narration surfaces are gone", () => {
  assert.doesNotMatch(html, /Activity chooser/);
  assert.doesNotMatch(html, /<table>/);
  assert.doesNotMatch(html, /Searches this page is built for/);
  assert.doesNotMatch(html, /Car Ramp Distance Test|Cardboard Car Ramp|Paper Plate Ramp|Cup Tower|Tube Sculpture|Magnetic Tile Builds|LEGO or DUPLO Color Tower/);
  assert.doesNotMatch(html, /let the object do the teaching/);
  assert.doesNotMatch(html, /\b\d+ min\b|low mess|medium mess/);
});

test("the generator and CSS own the custom layout without changing page identity", () => {
  assert.match(generator, /"preschool_stem_layout": True/);
  assert.match(generator, /def preschool_stem_page_html\(page\):/);
  assert.match(generator, /if page\.get\("preschool_stem_layout"\):/);
  assert.match(html, /styles\.css\?v=preschool-stem-front-door-1/);
  assert.match(styles, /\.stem-mode-links/);
  assert.match(styles, /\.stem-start/);
  assert.match(styles, /\.stem-deeper-routes/);
  assert.doesNotMatch(styles, /letter-spacing:\s*-/);
});

test("sitemap advances only the existing target URL", () => {
  const entries = sitemap.match(/<url>[\s\S]*?<\/url>/g) ?? [];
  const target = entries.filter((entry) => entry.includes("/collections/stem-activities-for-preschoolers.html"));
  assert.equal(target.length, 1);
  assert.match(target[0], /<lastmod>2026-09-06<\/lastmod>/);
});
