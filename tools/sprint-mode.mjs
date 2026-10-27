import { readFile } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import { resolve } from "node:path";

export function sprintDecision(operator, { now, runStartedAt, completedTransactions }) {
  const current = Date.parse(now);
  const cutoff = Date.parse(operator.pilot_ends_at);
  const sprint = operator.active_sprint;
  if (!Number.isFinite(current) || !Number.isFinite(cutoff)) return { mode: "blocked", can_start: false, reason: "invalid-clock-or-cutoff" };
  if (current >= cutoff) return { mode: "ended", can_start: false, reason: "pilot-cutoff" };
  if (!sprint || sprint.status === "restored") return { mode: "recurring", can_start: true };
  const start = Date.parse(sprint.starts_at);
  const end = Date.parse(sprint.ends_at);
  if (!Number.isFinite(start) || !Number.isFinite(end) || start >= end || end > cutoff) return { mode: "blocked", can_start: false, reason: "invalid-sprint-window" };
  if (current >= end || sprint.status === "restoring" || sprint.status === "stop_requested") return { mode: "restore_only", can_start: false, baseline: sprint.normal_baseline };
  if (current < start) return { mode: "recurring", can_start: true };
  if (sprint.status !== "active") return { mode: "blocked", can_start: false, reason: "activation-unconfirmed" };
  const runStart = Date.parse(runStartedAt);
  if (!Number.isFinite(runStart) || runStart < start || runStart > current) return { mode: "blocked", can_start: false, reason: "valid-actual-run-start-required" };
  if (!Number.isInteger(completedTransactions) || completedTransactions < 0) return { mode: "blocked", can_start: false, reason: "invalid-transaction-count" };
  const deadline = Math.min(end, runStart + sprint.new_action_start_minutes * 60_000);
  const allowed = current < deadline && completedTransactions < sprint.maximum_transactions_per_run;
  return { mode: "sprint", can_start: allowed, start_deadline: new Date(deadline).toISOString(), transactions_remaining: Math.max(0, sprint.maximum_transactions_per_run - completedTransactions), reason: allowed ? "eligible-selection" : "finish-or-checkpoint-underway-work" };
}

async function main() {
  const root = fileURLToPath(new URL("../", import.meta.url));
  const operator = JSON.parse(await readFile(resolve(root, "ops/operator.json"), "utf8"));
  const args = process.argv.slice(2);
  const value = (name) => args.includes(name) ? args[args.indexOf(name) + 1] : undefined;
  const count = value("--completed-actions");
  const result = sprintDecision(operator, { now: new Date().toISOString(), runStartedAt: value("--run-start"), completedTransactions: count === undefined ? undefined : Number(count) });
  console.log(JSON.stringify(result, null, 2));
  if (result.mode === "blocked") process.exitCode = 1;
}

if (process.argv[1] && fileURLToPath(import.meta.url) === resolve(process.argv[1])) await main();
