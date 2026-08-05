import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import test from "node:test";

const ROOT = process.cwd();
const INDOOR_PATH = path.join(
  ROOT,
  "site",
  "collections",
  "indoor-activities-for-preschoolers.html",
);
const RAINY_PATH = path.join(
  ROOT,
  "site",
  "collections",
  "rainy-day-activities-for-preschoolers.html",
);
const IMAGE_PATH = path.join(
  ROOT,
  "site",
  "assets",
  "preschool-indoor",
  "indoor-moment-chooser.webp",
);
const indoor = fs.readFileSync(INDOOR_PATH, "utf8");
const rainy = fs.readFileSync(RAINY_PATH, "utf8");
const css = fs.readFileSync(path.join(ROOT, "site", "styles.css"), "utf8");

const startSlugs = [
  "sock-target-roll",
  "paper-puddle-path",
  "tape-road-delivery",
  "low-car-ramp",
  "make-a-toy-place",
  "blanket-toy-crossing",
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

test("the indoor URL is the single indexable owner", () => {
  assert.match(
    indoor,
    /<title>Indoor Activities for Preschoolers: Choose by Moment \| Kid Activity Lab<\/title>/,
  );
  assert.match(
    indoor,
    /<link rel="canonical" href="https:\/\/kidactivitylab\.com\/collections\/indoor-activities-for-preschoolers\.html">/,
  );
  assert.deepEqual(
    [...indoor.matchAll(/<h1>(.*?)<\/h1>/g)].map((match) => match[1]),
    ["Indoor activities for preschoolers."],
  );

  const targets = fs.readFileSync(
    path.join(ROOT, "data", "seo_keyword_targets.csv"),
    "utf8",
  );
  const indoorRow = targets
    .split("\n")
    .find((line) => line.startsWith("/collections/indoor-activities-for-preschoolers.html,"));
  assert.ok(indoorRow);
  assert.match(indoorRow, /,indoor activities for preschoolers,/);
  assert.match(indoorRow, /rainy day activities for preschoolers/);
  assert.match(indoorRow, /Complete GSC queries and both candidate page rows remain unavailable/);
  assert.doesNotMatch(targets, /^\/collections\/rainy-day-activities-for-preschoolers\.html,/m);
});

test("opening decision surface is honest and ordered", () => {
  const openingOrder = [
    'class="callout"',
    'class="indoor-disclosure"',
    'class="indoor-readiness"',
    'class="indoor-visual"',
    'class="chooser"',
  ].map((marker) => indoor.indexOf(marker));
  assert.ok(openingOrder.every((position) => position >= 0));
  assert.deepEqual(openingOrder, [...openingOrder].sort((a, b) => a - b));

  const disclosure = indoor.match(/<div class="indoor-disclosure"[\s\S]*?<\/div>/)?.[0] ?? "";
  assert.match(disclosure, /Kid Activity Lab has not family-tested these setups/);
  assert.match(disclosure, /timing, mess, engagement, enjoyment, learning, repeatability, and safety outcomes are unknown/);
  assert.doesNotMatch(indoor, /tested by (?:our|Kid Activity Lab) (?:family|parents?|children)/i);
  assert.doesNotMatch(indoor, /<span class="tag">[^<]*(?:minutes?|mess|help)<\/span>/i);
  assert.doesNotMatch(indoor, /Searches this page is built for/i);

  const readiness = indoor.match(/<div class="indoor-readiness"[\s\S]*?<\/div>/)?.[0] ?? "";
  assert.match(readiness, /every child who can reach the setup/);
  assert.match(readiness, /away from stairs, doors, pets, breakable objects, and active walkways/);
  assert.match(readiness, /If any child may mouth a piece, use larger solid materials, stay within reach, and watch continuously/);
});

test("moment chooser names seven exact routes and adult roles", () => {
  const chooser = indoor.match(/<section class="chooser"[\s\S]*?<\/section>/)?.[0] ?? "";
  assert.equal([...chooser.matchAll(/<tr>/g)].length, 8);
  for (const label of ["Moment", "Start with", "Space and materials", "Adult role"]) {
    assert.equal(
      [...chooser.matchAll(new RegExp(`data-label="${label}"`, "g"))].length,
      7,
    );
  }
  assert.deepEqual(
    [...chooser.matchAll(/<a href="([^"]+)">([^<]+)<\/a>/g)].map((match) => [match[2], match[1]]),
    [
      ["Soft-Sock Target Roll", "#sock-target-roll"],
      ["Paper Puddle Path", "#paper-puddle-path"],
      ["Tape Road Delivery", "#tape-road-delivery"],
      ["Low Car Ramp", "#low-car-ramp"],
      ["Make a Toy Place", "#make-a-toy-place"],
      ["Blanket Toy Crossing", "#blanket-toy-crossing"],
      ["Standard-Deck Card Game Chooser", "../collections/card-games-for-kids.html"],
    ],
  );
  assert.match(css, /\.indoor-start \{\s+scroll-margin-top: 112px;/);
  assert.match(css, /\.indoor-page \.chooser td::before/);
});

test("six starts expose setup, rescue, stop, and local parent checks", () => {
  const starts = [
    ...indoor.matchAll(
      /<article class="seo-activity indoor-start" id="([^"]+)">([\s\S]*?)<\/article>/g,
    ),
  ];
  assert.deepEqual(starts.map((match) => match[1]), startSlugs);
  for (const [slug, body] of starts.map((match) => [match[1], match[2]])) {
    for (const label of ["Kid idea:", "Need", "Adult setup:", "If it stalls", "Stop:", "Parent check:"]) {
      assert.ok(body.includes(label), `${slug} is missing ${label}`);
    }
    assert.equal([...body.matchAll(/<li>/g)].length, 3, `${slug} must have three short steps`);
    assert.match(body, /class="small-link"/);
  }
  const movement = starts.find((match) => match[1] === "paper-puddle-path")?.[2] ?? "";
  assert.match(movement, /Stop if paper or tape lifts, the path slides, running starts/);
  const blanket = starts.find((match) => match[1] === "blanket-toy-crossing")?.[2] ?? "";
  assert.match(blanket, /the route is for the toy, not for feet/);
  assert.match(blanket, /Move the toy along or between the supports/);
  assert.doesNotMatch(blanket, /step between the supports/i);
});

test("rain context, deeper routes, visual, and source limits are explicit", () => {
  const rain = indoor.match(/<section class="indoor-rain[\s\S]*?<\/section>/)?.[0] ?? "";
  assert.match(rain, /Rainy day is a context/);
  assert.match(rain, /Rain-themed crafts and weather learning are separate jobs and are not promised here/);
  assert.equal([...rain.matchAll(/<div class="indoor-rotation">[\s\S]*?<\/div>/g)].length, 1);
  assert.equal([...rain.matchAll(/<a href=/g)].length, 3);

  const related = indoor.match(/<div class="related-routes">([\s\S]*?)<\/div>/)?.[1] ?? "";
  assert.deepEqual(
    [...related.matchAll(/href="([^"]+)"/g)].map((match) => match[1]),
    [
      "../collections/building-activities-for-4-year-olds.html",
      "../collections/card-games-for-kids.html",
      "../collections/no-prep-activities-for-preschoolers.html",
    ],
  );

  const imageSize = fs.statSync(IMAGE_PATH).size;
  assert.ok(imageSize > 50_000 && imageSize < 500_000, imageSize);
  assert.deepEqual(webpDimensions(IMAGE_PATH), { width: 1672, height: 941 });
  assert.match(
    indoor,
    /<img src="\.\.\/assets\/preschool-indoor\/indoor-moment-chooser\.webp"[^>]*width="1672" height="941">/,
  );
  assert.match(indoor, /It is not a family-test photo and does not show measured use/);

  const sources = indoor.match(/<section class="related indoor-sources"[\s\S]*?<\/section>/)?.[0] ?? "";
  assert.equal([...sources.matchAll(/<li>/g)].length, 6);
  for (const domain of [
    "parentmap.com",
    "mybrightwheel.com",
    "pre-kpages.com",
    "extension.psu.edu",
    "reachallreaders.com",
    "pbs.org",
  ]) {
    assert.match(sources, new RegExp(domain.replaceAll(".", "\\.")));
  }
  assert.equal([...sources.matchAll(/<li>[\s\S]*?<span>/g)].length, 6);
  assert.match(sources, /do not establish that Kid Activity Lab ran these setups/);
});

test("rainy URL is an accessible legacy redirect, not an indexable second owner", () => {
  assert.match(
    rainy,
    /<meta http-equiv="refresh" content="0; url=indoor-activities-for-preschoolers\.html">/,
  );
  assert.match(
    rainy,
    /<link rel="canonical" href="https:\/\/kidactivitylab\.com\/collections\/indoor-activities-for-preschoolers\.html">/,
  );
  assert.match(
    rainy,
    /<a href="indoor-activities-for-preschoolers\.html">Open the indoor activities chooser<\/a>/,
  );
  assert.doesNotMatch(rainy, /name="robots" content="noindex/i);

  const sitemap = fs.readFileSync(path.join(ROOT, "site", "sitemap.xml"), "utf8");
  assert.doesNotMatch(sitemap, /rainy-day-activities-for-preschoolers\.html/);
  assert.equal(
    [...sitemap.matchAll(/indoor-activities-for-preschoolers\.html/g)].length,
    1,
  );

  const homepage = fs.readFileSync(path.join(ROOT, "site", "index.html"), "utf8");
  assert.doesNotMatch(homepage, /rainy-day-activities-for-preschoolers\.html/);
  assert.match(homepage, /including rainy days/);

  for (const file of fs.readdirSync(path.join(ROOT, "site", "cards"))) {
    if (!file.endsWith(".html")) continue;
    const card = fs.readFileSync(path.join(ROOT, "site", "cards", file), "utf8");
    assert.doesNotMatch(card, /href="\.\.\/collections\/rainy-day-activities-for-preschoolers\.html"/);
  }
});
