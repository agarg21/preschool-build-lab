import assert from "node:assert/strict";
import fs from "node:fs";
import test from "node:test";

function responsiveOffset(css, rootSize) {
  const rule = css.match(/\.contributor-profile h2\s*\{([^}]+)\}/)?.[1];
  assert.ok(rule, "The offset stays scoped to contributor profile headings");
  assert.match(rule, /scroll-margin-top:\s*max\(110px,\s*7rem\);/);
  return Math.max(110, 7 * rootSize);
}

test("contributor fragment offsets clear the measured normal and enlarged headers", () => {
  const css = fs.readFileSync("site/assets/contributors.css", "utf8");
  assert.ok(responsiveOffset(css, 16) > 92.90625);
  assert.ok(responsiveOffset(css, 32) > 142.828125);
  const targets = {
    "site/contributors/riley-hart.html": ["contribution", "review", "publisher", "return"],
    "site/about.html": ["apoorva-garg", "research-process", "evidence-limits"]
  };
  for (const [file, ids] of Object.entries(targets)) {
    const html = fs.readFileSync(file, "utf8");
    assert.match(html, /<main class="contributor-profile">/);
    for (const id of ids) {
      assert.equal([...html.matchAll(new RegExp(`<h2 id="${id}">`, "g"))].length, 1, id);
    }
  }
});

test("fixed-only contributor offsets cannot silently restore the enlarged arrival defect", () => {
  const css = fs.readFileSync("site/assets/contributors.css", "utf8");
  assert.throws(() => responsiveOffset(css.replace(/max\(110px,\s*7rem\)/, "110px"), 32));
});
