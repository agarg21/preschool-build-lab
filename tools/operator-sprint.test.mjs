import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { createHash } from "node:crypto";
import test from "node:test";
import { sprintDecision } from "./sprint-mode.mjs";

const operator = JSON.parse(readFileSync(new URL("../ops/operator.json", import.meta.url), "utf8"));
const active = { ...operator, active_sprint: { ...operator.active_sprint, status: "active" } };
const start = active.active_sprint.starts_at;
const decide = (now, count = 0, runStartedAt = start, state = active) => sprintDecision(state, { now, runStartedAt, completedTransactions: count });

test("sprint admits sequential selections only within actual-run time and count limits", () => {
  assert.equal(decide(start).can_start, true);
  assert.equal(decide("2026-10-27T12:43:32Z", 2).can_start, true);
  assert.equal(decide("2026-10-27T12:43:33Z", 2).can_start, false);
  assert.equal(decide(start, 3).can_start, false);
  assert.equal(decide(start, -1).mode, "blocked");
  assert.equal(sprintDecision(active, { now: start }).mode, "blocked");
  assert.equal(sprintDecision(active, { now: start, runStartedAt: start }).mode, "blocked");
  assert.equal(decide(start, 0, "2026-10-27T11:59:00Z").mode, "blocked");
});

test("late wakeups restore at exact expiry and cannot restart the sprint clock", () => {
  assert.equal(decide("2026-10-30T11:58:32Z", 0, "2026-10-30T11:58:00Z").can_start, true);
  assert.equal(decide("2026-10-30T11:58:33Z").mode, "restore_only");
  assert.equal(decide("2026-10-31T12:00:00Z", 0, "2026-10-31T12:00:00Z").mode, "restore_only");
  assert.equal(decide("2026-10-27T11:58:32Z").mode, "recurring");
  assert.equal(decide("2026-11-03T22:00:00Z").mode, "ended");
});

test("restoration and unconfirmed activation cannot authorize sprint work", () => {
  for (const status of ["restoring", "stop_requested"]) assert.equal(decide(start, 0, start, { ...active, active_sprint: { ...active.active_sprint, status } }).mode, "restore_only");
  assert.equal(decide(start, 0, start, { ...active, active_sprint: { ...active.active_sprint, status: "pending_activation" } }).can_start, false);
  assert.equal(decide(start, 0, start, { ...active, active_sprint: { ...active.active_sprint, status: "restored" } }).mode, "recurring");
  assert.equal(decide("bad-clock").mode, "blocked");
});

test("72-hour override preserves exact normal prompt, identity, cutoff and notification baseline", () => {
  const baseline = JSON.parse(readFileSync(new URL("../ops/sprint-normal-baseline-2026-10-27.json", import.meta.url), "utf8"));
  const prompt = readFileSync(new URL("../ops/autopilot-prompt.md", import.meta.url), "utf8");
  const normal = prompt.split("## Normal Cycle Instructions\n\n")[1].trimEnd();
  assert.equal(normal, baseline.prompt);
  assert.equal(createHash("sha256").update(normal).digest("hex"), active.active_sprint.normal_prompt_sha256);
  assert.equal(Date.parse(active.active_sprint.ends_at) - Date.parse(start), 72 * 60 * 60_000);
  assert.equal(baseline.id, active.active_sprint.automation_id);
  assert.equal(baseline.kind, "heartbeat");
  assert.equal(baseline.target_thread_id, "019f7334-5c9c-7dd0-9993-79318cc00db5");
  assert.equal(baseline.status, "ACTIVE");
  assert.equal(Object.hasOwn(baseline, "notification_policy"), false);
  assert.match(baseline.rrule, /BYHOUR=9,17/);
  assert.match(active.active_sprint.hourly_rrule, /FREQ=HOURLY;INTERVAL=1/);
  assert.ok(active.active_sprint.hourly_rrule.endsWith("UNTIL=20261103T220000Z"));
  assert.ok(baseline.rrule.endsWith("UNTIL=20261103T220000Z"));
});
