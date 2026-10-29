import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import fs from "node:fs";
import test from "node:test";

const icon = fs.readFileSync("site/favicon.ico");

test("fallback ICO has one bounded transparent DIB entry", () => {
  assert.equal(icon.length, 70);
  assert.deepEqual([...icon.subarray(0, 6)], [0, 0, 1, 0, 1, 0]);
  assert.deepEqual([...icon.subarray(6, 10)], [1, 1, 0, 0]);
  assert.equal(icon.readUInt16LE(10), 1);
  assert.equal(icon.readUInt16LE(12), 32);
  assert.equal(icon.readUInt32LE(14), 48);
  assert.equal(icon.readUInt32LE(18), 22);
  assert.equal(icon.readUInt32LE(22), 40);
  assert.equal(icon.readInt32LE(26), 1);
  assert.equal(icon.readInt32LE(30), 2);
  assert.equal(icon.readUInt16LE(34), 1);
  assert.equal(icon.readUInt16LE(36), 32);
  assert.equal(icon.readUInt32LE(38), 0);
  assert.equal(icon.readUInt32LE(42), 4);
  assert.deepEqual([...icon.subarray(46, 62)], Array(16).fill(0));
  assert.deepEqual([...icon.subarray(62)], [0, 0, 0, 0, 128, 0, 0, 0]);
});

test("neutral fallback bytes reproduce without a generator write", () => {
  const output = execFileSync("python3", ["-c", "import scripts.generate_favicon as g; import sys; a=g.favicon_bytes(); assert a==g.favicon_bytes(); sys.stdout.buffer.write(a)"], { env: { ...process.env, PYTHONDONTWRITEBYTECODE: "1" } });
  assert.deepEqual(output, icon);
});

test("fallback stays outside content inventory and preserves explicit blank icons", () => {
  assert.ok(!fs.readFileSync("site/sitemap.xml", "utf8").includes("favicon.ico"));
  for (const name of ["cardboard-ball-maze-kids", "paper-helicopter-kids", "paper-cup-tower-kids", "paper-straw-rocket", "painter-tape-road-kids", "paper-bridge-challenge-kids"]) {
    assert.match(fs.readFileSync(`site/articles/${name}.html`, "utf8"), /<link rel="icon" href="data:,">/);
  }
});
