import assert from "node:assert/strict";
import fs from "node:fs";
import test from "node:test";

const read = (file) => fs.readFileSync(file, "utf8");
const card = read("site/cards/straw-bridge.html");
const library = read("site/cards.html");
const svg = read("site/assets/straw-bridge/straw-deck-start.svg");
const owners = ["building", "engineering"].map((name) =>
  read("site/collections/" + name + "-activities-for-4-year-olds.html"));
const section = (id) => card.match(new RegExp('<section id="' + id + '"[\\s\\S]*?</section>'))?.[0] ?? "";

test("straw card keeps one canonical owner, disclosed evidence and no timed or strength promise", () => {
  assert.equal([...card.matchAll(/<h1>/g)].length, 1);
  assert.match(card, /<h1>Straw Bridge<\/h1>/);
  assert.match(card, /rel="canonical" href="https:\/\/kidactivitylab.com\/cards\/straw-bridge.html"/);
  assert.match(card, /Adult joins; try the span EMPTY first/);
  assert.match(card, /not physically or family-tested/);
  assert.match(card, /Time and mess are not measured/);
  assert.match(card, /AI research contributor/);
  assert.doesNotMatch(card, /8 min|testing strength|<iframe|<form|step-tile|meta-tile/);
});

test("material and attention checks precede the first joint and empty trial", () => {
  assert.match(card, /SIX whole straight paper straws of equal length/);
  assert.match(card, /TWO broad low closed books of matching height/);
  assert.match(card, /Low closed books replace the old cup supports/);
  const checks = section("straw-checks");
  for (const text of ["Skip for mouthing", "uncontrolled younger reach", "damaged materials", "uncertain adult attention",
    "No cutting straws", "bendy, silicone or plastic", "Check owned material and tape directions", "Remove any optional object before any change"]) {
    assert.ok(checks.includes(text), text);
  }
  assert.ok(card.indexOf(checks) < card.indexOf('<section id="straw-start"'));
});

test("first joint wraps the entire flat row twice and both ends of every straw rest on books", () => {
  const start = section("straw-start");
  assert.equal([...start.matchAll(/<li>/g)].length, 4);
  for (const text of ["ends even", "FLAT row, not a round bundle", "BOTH outside edges",
    "joins the tape to itself underneath", "Repeat near the other end", "WHOLE flat row, not individual straws",
    "Do not squeeze or twist", "end if the tape will not hold", "gap shorter than the straws",
    "BOTH ends of EVERY straw", "Do not tape it to the books", "EMPTY span", "Do not push", "ONE empty retry"]) {
    assert.ok(start.includes(text), text);
  }
});

test("rescue and optional object do not turn the default into a load-to-failure task", () => {
  const rescue = section("straw-rescue"), optional = section("straw-optional");
  assert.match(rescue, /lift it off before moving books closer/);
  assert.match(rescue, /DIFFERENT joining-only activity/);
  assert.match(rescue, /that is not a bridge/);
  for (const text of ["Only after an intact, stable empty trial", "ONE owned intact LARGE lightweight flat-base block",
    "wholly on the deck without balancing", "EVERY reachable child", "stay empty or end",
    "No cups, coins, marbles, washers, driving or load-to-failure", "Remove the object before ANY change"]) {
    assert.ok(optional.includes(text), text);
  }
  assert.match(section("straw-cleanup"), /optional object first.*deck off the books.*all tape, straws and loose fragments.*books away/s);
});

test("original diagram has two six-straw top views, two wraps per view and equivalent text", () => {
  assert.match(svg, /viewBox="0 0 800 620"/);
  assert.match(svg, /<title id="title">/);
  assert.match(svg, /<desc id="desc">/);
  assert.equal([...svg.matchAll(/width="460" height="20"/g)].length, 12);
  assert.equal([...svg.matchAll(/<path d="M(?:215|552) (?:68|378)H/g)].length, 4);
  assert.match(card, /width="800" height="620" alt="Top views:/);
  assert.match(card, /not to scale or proof of a working or safe setup/);
  assert.doesNotMatch(svg, /<script|<image|<foreignObject|(?:href|src)=/);
});

test("both existing hub handoffs put checks before the card and remove old cup recipes", () => {
  for (const owner of owners) {
    const target = owner.match(/<article[^>]*id="straw-bridge"[\s\S]*?<\/article>/)?.[0] ?? "";
    assert.match(target, /Join a flat row; try it EMPTY first/);
    assert.match(target, /SIX whole straight paper straws/);
    assert.match(target, /BEFORE handling/);
    assert.ok(target.indexOf("Stop:") < target.indexOf('href="../cards/straw-bridge.html"'));
    assert.match(target, /checked joint, diagram and empty-trial steps/);
    assert.doesNotMatch(target, /<ol|<li>|Set the toy|Handle any cutting|silicone straws/);
    assert.match(owner, /Straw (?:Span|Bridge): empty first<\/a>/);
  }
  assert.match(owners[0], /Straw Span also requires skipping for mouthing/);
  assert.match(owners[1], /adult controls the ball while the child chooses/);
});

test("library finder stays at 36 cards and the straw summary uses the new default", () => {
  assert.equal([...library.matchAll(/class="mini-card"/g)].length, 36);
  const mini = library.match(/<a class="mini-card" href="cards\/straw-bridge.html">[\s\S]*?<\/a>/)?.[0] ?? "";
  assert.match(mini, /Adult joins and stays; EMPTY first/);
  assert.match(mini, /Time not measured/);
  assert.match(mini, /SIX whole straight paper straws/);
  assert.doesNotMatch(mini, /8 min|two cups/);
  assert.match(card, /whole-row wrapping principle only, not cutting, blowing, mouthing or medical guidance/);
  assert.match(card, /not a source-tested preschool setup/);
  assert.match(card, /assembly, adhesion, fit, stability, understanding, timing, mess, enjoyment, repetition, learning and safety outcomes are unknown/);
  assert.equal([...read("site/sitemap.xml").matchAll(/<loc>/g)].length, 65);
});
