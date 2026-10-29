import assert from "node:assert/strict";
import fs from "node:fs";
import { execFileSync } from "node:child_process";
import test from "node:test";

const read = path => fs.readFileSync(`site/${path}`, "utf8");
const card = read("cards/box-garage.html");
const article = (path, title) => [...read(path).matchAll(/<article\b[\s\S]*?<\/article>/g)]
  .map(m => m[0]).find(s => s.includes(`<h2>${title}</h2>`));
const basic = [
  ["card", card],
  ["age4", article("ages/activities-for-4-year-olds-at-home.html", "Box Garage")],
  ["age6", article("ages/activities-for-6-year-olds-at-home.html", "Box Garage")],
  ["independent", article("collections/independent-activities-for-preschoolers.html", "Box Garage")],
];
const extension = article("collections/engineering-activities-for-4-year-olds.html", "Two-Car Box Garage");
const before = (html, control, action) => {
  const a = html.indexOf(control), b = html.indexOf(action);
  assert.ok(a >= 0 && b >= 0 && a < b, control);
};

test("Box Garage readiness groups conserve the shared cue and stay expanded before action", () => {
  const script = `import json, sys
sys.path.insert(0, 'scripts')
from generate_seo_pages import ACTIVITIES
a = ACTIVITIES['box-garage']
print(json.dumps({k: a[k] for k in ['readiness_groups', 'fit_cue', 'start_cue', 'stop']}))`;
  const a = JSON.parse(execFileSync("python3", ["-B", "-c", script], { encoding: "utf8" }));
  assert.deepEqual(a.readiness_groups.map(([label]) => label), ["Box and car", "Space", "Adult and child", "Evidence"]);
  assert.equal(a.readiness_groups.map(([, text]) => text).join(" "), a.fit_cue);
  assert.equal(`${a.fit_cue} Stop: ${a.stop}`, a.start_cue);
  const readiness = card.match(/<section class="parent-strip box-garage-readiness"[\s\S]*?<\/section>/)?.[0];
  assert.ok(readiness);
  assert.doesNotMatch(readiness, /<details|hidden|aria-hidden/);
  const escape = s => s.replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;").replaceAll('"', "&quot;").replaceAll("'", "&#x27;");
  for (const [label, text] of [...a.readiness_groups, ["Stop", a.stop]]) {
    assert.ok(readiness.includes(`<p><strong>${label}:</strong> ${escape(text)}</p>`), label);
    before(card, `<strong>${label}:</strong>`, 'class="steps-grid"');
  }
  before(card, '<strong>Need:</strong>', 'aria-label="Before starting"');
  assert.match(card, /Open-ended; duration and mess not measured/);
  assert.doesNotMatch(card, /class="meta-tile"/);
  assert.match(card, /styles\.css\?v=box-garage-card-2/);
});

test("Box Garage base owners expose the same ready one-car start and early adult controls", () => {
  for (const [name, html] of basic) {
    assert.ok(html, name);
    const marker = name === "card" ? 'class="steps-grid"' : '<ol class="card-steps">';
    for (const s of ["Stay beside every reachable child", "Skip if fit, space or attention do not match", "Stop:", "not family-tested by Kid Activity Lab", "without staples"]) before(html, s, marker);
    for (const s of ["1 already-open small cardboard box", "1 large lightweight toy car", "opening facing the player", "without catching, force or lifting the box", "No cutting or tape is needed", "Drive the car through the ready opening", "park beside the box instead", "Adult puts away the box and car", "Duration and mess have not been measured"]) assert.ok(html.includes(s), `${name}: ${s}`);
    assert.equal((html.match(name === "card" ? /class="step-tile"/g : /<li>/g) || []).length, 3);
    assert.doesNotMatch(html, /Make spaces\.|5 min|low mess|<p>Open a box\.<\/p>/);
  }
});

test("engineering keeps its distinct two-car clearance extension with early controls and simpler handoff", () => {
  assert.ok(extension);
  before(extension, "Stay beside every reachable child", "Kid mission:");
  before(extension, "Stop:", '<ol class="card-steps">');
  assert.equal((extension.match(/<li>/g) || []).length, 3);
  for (const s of ["2 appropriate large lightweight toy cars", "optional extension", "Adult tests and places the short bay tape", "adult-prepared bays", "Do both cars fit, and can one leave without hitting the other?", "Never force an exit or cut during play", "one-car no-cut start", "PBS: parking-line spacing principle", "not tested geometry or tape performance"]) assert.ok(extension.includes(s), s);
  assert.doesNotMatch(extension, /Move one tape line or widen the exit/);
});

test("actual quick-card, library and four entry renderers match generated contributor-credited files", () => {
  const script = `import json, sys
from pathlib import Path
sys.path.insert(0, str(Path('scripts').resolve()))
import generate_card_pages as cards
import generate_seo_pages as seo
from contributor_pages import with_contributor_credit
assert 'box-garage' in cards.QUICK_CARD_SLUGS
out = {'cards/box-garage.html': cards.quick_page('box-garage'), 'cards.html': cards.cards_index()}
for page in seo.PAGES:
    if 'box-garage' in page['activities']:
        out[page['path']] = seo.page_html(page)
print(json.dumps({p: with_contributor_credit(s, p) for p, s in out.items()}))`;
  const output = JSON.parse(execFileSync("python3", ["-B", "-c", script], { encoding: "utf8", maxBuffer: 8 * 1024 * 1024 }));
  assert.equal(Object.keys(output).length, 6);
  for (const [path, html] of Object.entries(output)) assert.equal(html, read(path), path);
});

test("library inventory, independent exception, scoped fit and dated routes remain explicit", () => {
  const library = read("cards.html");
  assert.equal((library.match(/class="mini-card"/g) || []).length, 36);
  const row = library.match(/<a class="mini-card" href="cards\/box-garage.html">[\s\S]*?<\/a>/)?.[0];
  assert.match(row, /One-car no-cut start, adult stays beside/);
  assert.match(row, /Open-ended/);
  assert.match(read("collections/independent-activities-for-preschoolers.html"), /Box Garage also requires an adult to stay beside every reachable child/);
  for (const age of [4, 6]) assert.match(read(`ages/activities-for-${age}-year-olds-at-home.html`), /font-size: min\(2\.5rem, 48px\)/);
  assert.match(card, /class="kid-card box-garage-card"/);
  assert.match(read("styles.css"), /\.box-garage-card \.step-tile \{\s*min-height: 0;/);
  const sitemap = read("sitemap.xml");
  assert.equal((sitemap.match(/<loc>/g) || []).length, 65);
  for (const path of ["cards/box-garage.html", "cards.html", "ages/activities-for-4-year-olds-at-home.html", "ages/activities-for-6-year-olds-at-home.html", "collections/independent-activities-for-preschoolers.html", "collections/engineering-activities-for-4-year-olds.html"]) {
    const date = path === "collections/engineering-activities-for-4-year-olds.html" ? "2026-10-29" : ["cards.html", "ages/activities-for-4-year-olds-at-home.html", "ages/activities-for-6-year-olds-at-home.html", "collections/independent-activities-for-preschoolers.html"].includes(path) ? "2026-10-28" : "2026-10-27";
    assert.ok(sitemap.includes(`${path}</loc>\n    <lastmod>${date}</lastmod>`), path);
  }
});
