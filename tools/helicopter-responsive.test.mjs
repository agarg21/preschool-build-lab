import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { createHash } from "node:crypto";
import fs from "node:fs";
import test from "node:test";

const path = "site/articles/paper-helicopter-kids.html";
const html = fs.readFileSync(path, "utf8");
const rendered = execFileSync("python3", ["-c", `
import sys
from pathlib import Path
sys.path.insert(0, 'scripts')
source = Path('scripts/generate_seo_pages.py')
namespace = {'__file__': str(source.resolve()), '__name__': 'responsive_review'}
exec(compile(source.read_text(), str(source), 'exec'), namespace)
print(namespace['paper_helicopter_guide_html'](), end='')
`], { encoding: "utf8" });

function verifyResponsiveRules(document) {
  const style = document.match(/<style>([\s\S]*?)<\/style>/)?.[1];
  assert.ok(style, "rendered inline stylesheet must exist");
  assert.match(style, /\.helicopter-guide \.content section\[id\]\s*\{\s*scroll-margin-top:\s*max\(110px, 7rem\);\s*\}/);
  assert.match(style, /@media\s*\(max-width:\s*600px\)\s*\{\s*\.helicopter-guide h1\s*\{\s*font-size:\s*min\(2rem, 56px\);\s*\}\s*\.helicopter-guide \.content h2\s*\{\s*font-size:\s*min\(1\.75rem, 48px\);\s*\}\s*\}/);
}

test("helicopter actual renderer and generated page retain scoped responsive rules", () => {
  verifyResponsiveRules(rendered);
  verifyResponsiveRules(html);
  assert.throws(() => verifyResponsiveRules(html.replace("max(110px, 7rem)", "110px")));
  assert.throws(() => verifyResponsiveRules(html.replace("min(2rem, 56px)", "2rem")));
  assert.throws(() => verifyResponsiveRules(html.replace("min(1.75rem, 48px)", "1.75rem")));
});

test("helicopter responsive repair conserves all non-style bytes and its map", () => {
  const withoutStyle = (document) => document.replace(/<style>[\s\S]*?<\/style>/, "<style></style>");
  // Update only after separately reviewing a content change, not a layout repair.
  assert.equal(createHash("sha256").update(withoutStyle(html)).digest("hex"), "537da6c9a1ae486bdd97015b5d3e1ce286cfb6a6afa134d33236d742282a3513");
  const image = "site/assets/paper-helicopter/cut-fold-map.png";
  assert.equal(createHash("sha256").update(fs.readFileSync(image)).digest("hex"), "1be76e5cda7cbc452684e4ee8c9a8c1b0c43a7f532bcb51ae5989aa185d13675");
});
