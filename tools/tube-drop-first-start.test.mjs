import assert from "node:assert/strict";
import fs from "node:fs";
import {execFileSync} from "node:child_process";
import test from "node:test";

const slugs = ["paper-roll-drop", "pom-pom-drop"];
const titles = ["Paper Roll Drop", "Pom Pom Drop"];
const read = p => fs.readFileSync("site/" + p, "utf8");
const required = ["EVERY reachable child", "CLEAR ABOVE", "FREELY", "WITHOUT pushing or squeezing", "ONLY after landing", "not family-tested by Kid Activity Lab"];

test("Both legacy drop cards use one checked adult-held default before child action", () => {
  for (const [i, slug] of slugs.entries()) {
    const h = read("cards/" + slug + ".html");
    assert.ok(h.includes("<h1>" + titles[i] + "</h1>"));
    assert.ok(h.includes('canonical" href="https://kidactivitylab.com/cards/' + slug + '.html"'));
    assert.doesNotMatch(h, /<iframe|2 minutes|3 minutes|low mess|adapted from a creator video and simplified/);
    for (const s of required) assert.ok(h.includes(s), slug + ": " + s);
    const steps = h.indexOf('class="tube-drop-steps"');
    for (const s of ["Fit or decline:", "Trial before child access:", "Stop:", "Adult model:"]) assert.ok(h.indexOf(s) > 0 && h.indexOf(s) < steps, slug + ": " + s);
    assert.ok(h.indexOf("Sources and testing status") > steps);
    assert.match(h, /same free passage is plainly restored/);
    assert.match(h, /Account for the ONE pom, tube and receiver/);
    assert.match(h, /Paper Roll Drop and Pom Pom Drop use this SAME default/);
    assert.doesNotMatch(h, /name="robots"/);
  }
});

test("Tube drop actual CSV dispatcher and canonical hub renderer reproduce published bytes", () => {
  const code = `import sys,json,csv
sys.path.insert(0,'scripts')
import generate_card_pages as c,generate_seo_pages as s
from contributor_pages import with_contributor_credit
rows={r['source_id']:r for r in csv.DictReader(open('data/video_activity_sources.csv'))}
out={'cards.html':c.cards_index()}
for slug in ['paper-roll-drop','pom-pom-drop']:
 row=rows['yt-'+slug]
 assert row['kid_step_1'].startswith('Tape')
 assert slug not in c.QUICK_CARD_SLUGS and slug not in c.QUICK_CARD_OVERRIDES
 out['cards/'+slug+'.html']=c.page(row,slug)
for p in s.PAGES:
 if any(k in p.get('activities',[]) for k in ['paper-roll-drop','pom-pom-drop']):
  assert not any(k in p.get('activity_overrides',{}) for k in ['paper-roll-drop','pom-pom-drop'])
  out[p['path']]=s.page_html(p)
print(json.dumps({p:with_contributor_credit(h,p) for p,h in out.items()}))`;
  const out = JSON.parse(execFileSync("python3", ["-B", "-c", code], {encoding: "utf8", maxBuffer: 16 * 1024 * 1024}));
  assert.equal(Object.keys(out).length, 7);
  for (const [p, h] of Object.entries(out)) assert.equal(h, read(p), p);
});

test("All five compact drop forms carry the same fit, trial, role and end branches", () => {
  let count = 0;
  for (const p of ["ages/activities-for-3-year-olds-at-home.html", "collections/no-prep-activities-for-preschoolers.html", "collections/independent-activities-for-preschoolers.html", "collections/fine-motor-activities-for-preschoolers.html"]) {
    for (const h of [...read(p).matchAll(/<article\b[\s\S]*?<\/article>/g)].map(m => m[0]).filter(h => titles.some(t => h.includes("<h2>" + t + "</h2>")))) {
      count++;
      const steps = h.indexOf('<ol class="card-steps">');
      for (const s of required) assert.ok(h.includes(s), p + ": " + s);
      assert.ok(h.indexOf("Trial before child access:") < steps && h.indexOf("Stop:") < steps);
      assert.doesNotMatch(h, /2 min|3 min|low mess|Use large items if younger siblings|<li>Catch|<li>Sort|<li>Try another color/);
      assert.match(h, /Adult holds throughout/);
      assert.match(h, /otherwise end, not smaller filler/);
    }
  }
  assert.equal(count, 5);
  assert.match(read("collections/independent-activities-for-preschoolers.html"), /Paper Roll Drop is adult-held throughout, not hands-off play/);
});

test("Drop discovery labels and sitemap preserve existing owners and counts", () => {
  for (const p of ["cards.html", "materials/cardboard.html"]) {
    for (const slug of slugs) {
      const h = [...read(p).matchAll(/<a class="mini-card"[\s\S]*?<\/a>/g)].map(m => m[0]).find(h => h.includes("cards/" + slug + ".html"));
      assert.ok(h, p + slug);
      assert.match(h, /Same held-tube default/);
      assert.match(h, /adult holds throughout/);
      assert.doesNotMatch(h, /2 min|3 min|parent check/);
      assert.ok(read("sitemap.xml").includes("https://kidactivitylab.com/cards/" + slug + ".html"));
    }
  }
  assert.equal((read("cards.html").match(/class="mini-card"/g) || []).length, 36);
  assert.equal((read("sitemap.xml").match(/<loc>/g) || []).length, 65);
  assert.match(read("materials/cardboard.html"), /name="robots" content="noindex,follow"/);
});
