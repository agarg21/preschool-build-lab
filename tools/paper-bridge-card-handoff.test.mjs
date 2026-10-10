import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import test from "node:test";

const root = process.cwd();
const card = fs.readFileSync(path.join(root, "site/cards/paper-bridge.html"), "utf8");
const styles = fs.readFileSync(path.join(root, "site/styles.css"), "utf8");

test("Paper Bridge card makes the guide and stop decision before executable steps", () => {
  const decision = card.indexOf('class="bridge-card-decision"');
  const guide = card.indexOf('>Full Paper Bridge guide</a>');
  const parentCheck = card.indexOf('aria-label="Parent check"');
  const steps = card.indexOf('aria-label="Steps"');
  assert.ok(decision > 0 && decision < guide && guide < parentCheck && parentCheck < steps);
  assert.equal([...card.matchAll(/Full Paper Bridge guide/g)].length, 1);
  assert.match(card, /Research-backed; not family-tested by Kid Activity Lab/);
  assert.match(card, /If a younger child mouths materials[^<]*, skip\./);
  assert.match(card, /Stop if books slide, the object is thrown, paper goes in a mouth or tears/);
  assert.match(card, /Remove loose paper pieces before continuing/);
});

test("Paper Bridge card preserves the adult setup and optional comparison", () => {
  assert.match(card, /Adult sets two books low\./);
  assert.match(card, /Lay one paper sheet across\./);
  assert.match(card, /Place one large object gently\./);
  assert.match(card, /Optional: fold the paper and compare\./);
  assert.match(card, /<link rel="canonical" href="https:\/\/kidactivitylab\.com\/cards\/paper-bridge\.html">/);
  assert.match(card, /class="kid-card bridge-card"/);
  assert.match(styles, /\.bridge-card-decision\s*\{/);
  assert.match(styles, /\.bridge-card \.step-tile\s*\{/);
  assert.match(styles, /\.bridge-start-panel h2\s*\{\s*scroll-margin-top: max\(104px, 6rem\)/);
});

test("related routes do not repeat the guide handoff", () => {
  const related = card.match(/<section class="parent-strip" aria-label="Related activity pages">([\s\S]*?)<\/section>/)?.[1] ?? "";
  assert.equal([...related.matchAll(/<a /g)].length, 2);
  assert.doesNotMatch(related, /paper-bridge-challenge-kids/);
});
