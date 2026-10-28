import assert from "node:assert/strict";
import fs from "node:fs";
import test from "node:test";

const hub = fs.readFileSync("site/collections/independent-activities-for-preschoolers.html", "utf8");
const card = fs.readFileSync("site/cards/cup-tower.html", "utf8");
const guide = fs.readFileSync("site/articles/paper-cup-tower-kids.html", "utf8");
const cup = [...hub.matchAll(/<article class="seo-activity">[\s\S]*?<\/article>/g)].map(m => m[0]).find(block => block.includes("<h2>Cup Tower</h2>"));

test("independent hub marks the cup exception and checks before action", () => {
  assert.ok(cup);
  for (const marker of ["Adult stays beside setup", "Mess not measured", "matching lightweight paper cups", "skip if you cannot attend", "Stop after mouthing", "not family-tested", "closed bottoms touching", "arrange a row"]) assert.ok(cup.includes(marker), marker);
  const steps = cup.indexOf("<ol");
  assert.ok(steps >= 0);
  for (const marker of ["Stop after", "Full Paper Cup Tower guide"]) {
    const position = cup.indexOf(marker);
    assert.ok(position >= 0 && position < steps, marker);
  }
  assert.doesNotMatch(cup, /1 minute|Low help|knock.*down/i);
  assert.match(hub, /not just a quick demonstration/);
});

test("cup card checks and optional depth precede the unchanged four actions", () => {
  const steps = card.indexOf('class="steps-grid"');
  assert.ok(steps >= 0);
  for (const marker of ["Full Paper Cup Tower guide", "Parent check:", "Stop after mouthing", "Need</strong>"]) {
    const position = card.indexOf(marker);
    assert.ok(position >= 0 && position < steps, marker);
  }
  assert.equal([...card.matchAll(/class="step-number"/g)].length, 4);
  assert.equal([...card.matchAll(/Full Paper Cup Tower guide/g)].length, 1);
  assert.match(card, /Skip if you cannot stay/);
  assert.match(card, /Not measured/);
  assert.match(card, /class="kid-card cup-tower-card"/);
});

test("cup quick and direct guide arrivals expose attendance and stop first", () => {
  for (const section of [guide.match(/<section class="bridge-start-panel"[\s\S]*?<\/section>/)[0], guide.match(/<section id="first-try"[\s\S]*?<\/section>/)[0]]) {
    for (const marker of ["Skip this activity if you cannot attend", "Stop after mouthing", "younger children's reach"]) assert.ok(section.indexOf(marker) >= 0 && section.indexOf(marker) < section.indexOf("<ol"), marker);
  }
  assert.match(guide, /Sources rechecked October 27, 2026/);
  assert.match(guide, /datePublished":"2026-09-17","dateModified":"2026-10-27/);
  assert.match(guide, /not a safety assurance/);
});

test("cup fit and hub exception stay scoped without another indexable route", () => {
  const source = fs.readFileSync("scripts/generate_seo_pages.py", "utf8");
  assert.match(source, /activity\.update\(page\.get\("activity_overrides"/);
  assert.match(source, /"link_before_steps": True/);
  const css = fs.readFileSync("site/styles.css", "utf8");
  assert.match(css, /\.cup-tower-card \.step-tile/);
  assert.match(css, /\.cup-tower-guide #first-try\s*\{\s*scroll-margin-top: 7rem;/);
  const sitemap = fs.readFileSync("site/sitemap.xml", "utf8");
  assert.equal([...sitemap.matchAll(/<loc>/g)].length, 66);
  for (const path of ["cards/cup-tower.html", "articles/paper-cup-tower-kids.html", "collections/independent-activities-for-preschoolers.html"]) {
    const date = path.startsWith("collections/") ? "2026-10-28" : "2026-10-27";
    assert.ok(sitemap.includes(`${path}</loc>\n    <lastmod>${date}</lastmod>`), path);
  }
});
