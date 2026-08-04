import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import test from "node:test";

const ROOT = process.cwd();
const PAGE_PATH = path.join(
  ROOT,
  "site",
  "collections",
  "building-activities-for-4-year-olds.html",
);
const IMAGE_PATH = path.join(
  ROOT,
  "site",
  "assets",
  "preschool-building",
  "building-material-chooser.webp",
);
const html = fs.readFileSync(PAGE_PATH, "utf8");
const css = fs.readFileSync(path.join(ROOT, "site", "styles.css"), "utf8");

const buildSlugs = [
  "magnetic-tile-house",
  "magnetic-tile-ideas",
  "block-tower",
  "cup-tower",
  "paper-bridge",
  "straw-bridge",
  "tube-sculpture",
  "wind-tower-test",
  "blanket-river",
];

function webpDimensions(file) {
  const bytes = fs.readFileSync(file);
  assert.equal(bytes.subarray(0, 4).toString(), "RIFF");
  assert.equal(bytes.subarray(8, 12).toString(), "WEBP");

  const chunk = bytes.subarray(12, 16).toString();
  if (chunk === "VP8 ") {
    assert.equal(bytes.subarray(23, 26).toString("hex"), "9d012a");
    return {
      width: bytes.readUInt16LE(26) & 0x3fff,
      height: bytes.readUInt16LE(28) & 0x3fff,
    };
  }
  if (chunk === "VP8X") {
    return {
      width: bytes.readUIntLE(24, 3) + 1,
      height: bytes.readUIntLE(27, 3) + 1,
    };
  }
  throw new Error(`Unsupported WebP chunk ${chunk}`);
}

test("preschool building page keeps its established URL and broadens its target", () => {
  assert.match(html, /<title>Building Activities for Preschoolers \| Kid Activity Lab<\/title>/);
  assert.match(html, /<link rel="canonical" href="https:\/\/kidactivitylab\.com\/collections\/building-activities-for-4-year-olds\.html">/);
  assert.deepEqual(
    [...html.matchAll(/<h1>(.*?)<\/h1>/g)].map((match) => match[1]),
    ["Building activities for preschoolers."],
  );

  const targetRow = fs
    .readFileSync(path.join(ROOT, "data", "seo_keyword_targets.csv"), "utf8")
    .split("\n")
    .find((line) => line.startsWith("/collections/building-activities-for-4-year-olds.html,"));
  assert.ok(targetRow);
  assert.match(targetRow, /,building activities for preschoolers,/);
  assert.match(targetRow, /building activities for 4 year olds/);
  assert.match(targetRow, /UNKNOWN; the existing URL has no public-safe GSC page baseline/);
});

test("page states evidence limits before the illustration and chooser", () => {
  const note = html.match(/<div class="building-disclosure"[\s\S]*?<\/div>/)?.[0] ?? "";
  assert.match(note, /not family-tested/);
  assert.match(note, /timing, mess, engagement, learning, repeatability, and safety outcomes are unknown/);
  const openingOrder = [
    'class="callout"',
    'class="building-disclosure"',
    'class="building-readiness"',
    'class="building-visual"',
    'class="chooser"',
  ].map((marker) => html.indexOf(marker));
  assert.ok(openingOrder.every((position) => position >= 0));
  assert.deepEqual(openingOrder, [...openingOrder].sort((a, b) => a - b));
  assert.doesNotMatch(html, /tested by (?:our|Kid Activity Lab) (?:family|parents?|children)/i);
  assert.doesNotMatch(html, /<span class="tag">[^<]*(?:minutes?|mess)<\/span>/i);
  assert.doesNotMatch(html, /Searches this page is built for/i);
  const readiness = html.match(/<div class="building-readiness"[\s\S]*?<\/div>/)?.[0] ?? "";
  assert.match(readiness, /youngest child who can reach the build/);
  assert.match(readiness, /Remove cracked or damaged materials and any piece with an exposed magnet/);
  assert.match(readiness, /If any child may mouth materials, stay within reach and watch continuously/);
  assert.match(readiness, /skip straws, loose tape, and other loose pieces and use larger solid blocks instead/);
});

test("material chooser, support steps, and architecture boundary are complete", () => {
  const chooser = html.match(/<section class="chooser"[\s\S]*?<\/section>/)?.[0] ?? "";
  assert.equal([...chooser.matchAll(/<tr>/g)].length, 6);
  for (const label of ["What is ready", "Build job", "Adult role"]) {
    assert.equal([...chooser.matchAll(new RegExp(`data-label="${label}"`, "g"))].length, 5);
  }
  assert.deepEqual(
    [...chooser.matchAll(/<a href="([^"]+)">([^<]+)<\/a>/g)].map((match) => [match[2], match[1]]),
    [
      ["Toy Home", "#magnetic-tile-house"],
      ["Wide-Base Tower", "#block-tower"],
      ["Cup Doorway", "#cup-tower"],
      ["Paper Path", "#paper-bridge"],
      ["Straw Span", "#straw-bridge"],
      ["Tube Sculpture", "#tube-sculpture"],
      ["Blanket Crossing", "#blanket-river"],
    ],
  );

  const support = html.match(/<section class="building-support[\s\S]*?<\/section>/)?.[0] ?? "";
  assert.deepEqual(
    [...support.matchAll(/<li><strong>(.*?)<\/strong>/g)].map((match) => match[1]),
    ["Name the job", "Offer a small set", "Ask about space", "Protect the child&#x27;s design"],
  );

  const boundary = html.match(/<section class="building-boundary[\s\S]*?<\/section>/)?.[0] ?? "";
  assert.match(boundary, /open-ended structures and spaces/);
  assert.match(boundary, /a problem, visible test, and one redesign/);
  assert.match(boundary, /does not promise that curriculum/);
  assert.match(css, /\.building-build \{\s+scroll-margin-top: 112px;/);
  assert.doesNotMatch(html, /canonical owner/);
  assert.match(html, /neighboring pages support different activity goals/);
});

test("all nine builds expose mission, setup, rescue, stop, and parent checks", () => {
  const builds = [...html.matchAll(/<article class="seo-activity building-build" id="([^"]+)">([\s\S]*?)<\/article>/g)];
  assert.deepEqual(builds.map((match) => match[1]), buildSlugs);
  for (const [slug, body] of builds.map((match) => [match[1], match[2]])) {
    for (const label of ["Kid mission:", "Need", "Adult setup:", "If the build stalls", "Stop:", "Parent check:"]) {
      assert.ok(body.includes(label), `${slug} is missing ${label}`);
    }
    assert.equal([...body.matchAll(/<li>/g)].length, 3, `${slug} must have three short steps`);
    assert.match(body, /Open (?:the base activity card|the test-and-redesign version)/);
  }
  const tower = builds.find((match) => match[1] === "block-tower")?.[2] ?? "";
  assert.match(tower, /Keep the tower low and away from faces, overhead areas, walkways, pets, and breakable objects/);
  assert.doesNotMatch(tower, /without a climbing or overhead hazard/);
});

test("visual, adjacent routes, and six sources are explicit and bounded", () => {
  const imageSize = fs.statSync(IMAGE_PATH).size;
  assert.ok(imageSize > 50_000 && imageSize < 300_000, imageSize);
  assert.deepEqual(webpDimensions(IMAGE_PATH), { width: 1672, height: 941 });
  assert.match(html, /<img src="\.\.\/assets\/preschool-building\/building-material-chooser\.webp"[^>]*width="1672" height="941">/);
  assert.match(html, /not a Kid Activity Lab family-test photo or a product recommendation/);

  const related = html.match(/<div class="related-routes">([\s\S]*?)<\/div>/)?.[1] ?? "";
  assert.deepEqual(
    [...related.matchAll(/href="([^"]+)"/g)].map((match) => match[1]),
    [
      "../collections/engineering-activities-for-4-year-olds.html",
      "../collections/stem-activities-for-preschoolers.html",
      "../collections/indoor-activities-for-preschoolers.html",
    ],
  );

  const sources = html.match(/<section class="related building-sources"[\s\S]*?<\/section>/)?.[0] ?? "";
  assert.equal([...sources.matchAll(/<li><a href=/g)].length, 6);
  for (const domain of [
    "extension.msstate.edu",
    "scienceinprek.si.edu",
    "preschoolmath.stanford.edu",
    "extension.psu.edu",
    "extension.sdstate.edu",
  ]) {
    assert.match(sources, new RegExp(domain.replaceAll(".", "\\.")));
  }
  assert.match(sources, /do not establish that Kid Activity Lab ran these setups/);
});

test("legacy activity cards retain the age-four building route label", () => {
  let buildingRoutes = 0;
  for (const slug of buildSlugs) {
    const card = fs.readFileSync(path.join(ROOT, "site", "cards", `${slug}.html`), "utf8");
    assert.doesNotMatch(card, /Building activities for preschoolers/);
    if (card.includes('href="../collections/building-activities-for-4-year-olds.html"')) {
      buildingRoutes += 1;
      assert.match(
        card,
        /href="\.\.\/collections\/building-activities-for-4-year-olds\.html">Building activities for 4 year olds<\/a>/,
      );
    }
  }
  assert.equal(buildingRoutes, 6);
});
