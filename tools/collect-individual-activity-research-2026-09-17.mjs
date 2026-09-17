import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

// One dated, explicitly authorized batch. Refuse reruns of paid calls.
const root = fileURLToPath(new URL('../', import.meta.url));
const output = path.join(root, 'data/individual-activity-serps-2026-09-17.json');
const csvOutput = path.join(root, 'data/individual-activity-opportunities-2026-09-17.csv');
const families = [
  ['paper-helicopter', 'paper helicopter', 'paper helicopter experiment'],
  ['straw-rocket', 'straw rocket', 'straw rocket for kids'],
  ['foil-boat', 'aluminum foil boat experiment', 'foil boat challenge'],
  ['paper-spinner', 'paper spinner', 'paper spinner toy'],
  ['paper-chain', 'paper chain challenge', 'longest paper chain challenge'],
  ['balloon-rocket', 'balloon rocket experiment', 'balloon rocket activity'],
];
const serpQueries = families.map((row) => row[2]);
serpQueries[2] = 'aluminum foil boat experiment';
serpQueries[4] = 'paper chain challenge';
const batch = {
  action_id: 'KAL-RES-013',
  collected_at: new Date().toISOString(),
  provider: 'DataForSEO',
  market: { location_code: 2840, location: 'United States', language_code: 'en' },
  budget: { authorized_usd: 5, published_expected_usd: 0.102, reported_usd: 0, calls: 0, max_calls: 7, automatic_retries: false },
  volume: null,
  serps: [],
  completed: false,
};

function save() {
  fs.writeFileSync(output, JSON.stringify(batch, null, 2) + '\n', { mode: 0o600 });
}

async function post(endpoint, payload, expectedCost, auth) {
  if (batch.budget.calls >= 7 || batch.budget.reported_usd + expectedCost > 5) throw new Error('Budget guard stopped batch');
  batch.budget.calls += 1;
  save();
  const response = await fetch(`https://api.dataforseo.com/v3/${endpoint}`, {
    method: 'POST',
    headers: { Authorization: `Basic ${auth}`, 'Content-Type': 'application/json' },
    body: JSON.stringify([payload]),
    signal: AbortSignal.timeout(120000),
  });
  const json = await response.json();
  const cost = Number(json.cost);
  if (!Number.isFinite(cost) || cost < 0) throw new Error('Missing response charge; stop without retry');
  batch.budget.reported_usd = Number((batch.budget.reported_usd + cost).toFixed(6));
  save();
  const task = json.tasks?.[0];
  if (!response.ok || json.status_code !== 20000 || task?.status_code !== 20000) {
    throw new Error(`Provider failure HTTP ${response.status}, task ${task?.status_code ?? 'absent'}; no retry`);
  }
  return { task, response_cost: cost };
}

async function main() {
  if (fs.existsSync(output) || fs.existsSync(csvOutput)) throw new Error('Dated batch already exists; paid rerun prohibited');
  if (!process.argv.includes('--execute-authorized-batch')) throw new Error('Explicit execution flag required');
  if (new Date().toISOString().slice(0, 10) !== '2026-09-17') throw new Error('Dated authorization requires a new action on another date');
  const env = fs.readFileSync(path.join(process.env.HOME, '.config/seo-lab/dataforseo.env'), 'utf8');
  const values = {};
  for (const line of env.split(/\r?\n/)) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) continue;
    const index = trimmed.indexOf('=');
    if (index < 0) continue;
    values[trimmed.slice(0, index)] = trimmed.slice(index + 1).replace(/^['"]|['"]$/g, '');
  }
  const auth = process.env.DATAFORSEO_AUTH_B64 || values.DATAFORSEO_AUTH_B64;
  if (!auth) throw new Error('Configured authentication unavailable');
  const keywords = families.flatMap((row) => row.slice(1));
  const volume = await post('keywords_data/google_ads/search_volume/live', {
    location_code: 2840, language_code: 'en', search_partners: false, keywords,
  }, 0.09, auth);
  batch.volume = {
    endpoint: 'keywords_data/google_ads/search_volume/live',
    task_id: volume.task.id, status_code: volume.task.status_code, cost_usd: volume.response_cost,
    requested_keywords: keywords,
    interpretation: 'TOOL_ESTIMATE; approximate Google Ads monthly averages, not unique users. Competition is advertising competition, not organic difficulty. Null means unavailable, not zero; variants must not be summed.',
    rows: (volume.task.result ?? []).map((row) => ({
      keyword: row.keyword, search_volume: row.search_volume ?? null,
      competition: row.competition ?? null, competition_index: row.competition_index ?? null,
      monthly_searches: row.monthly_searches ?? null,
    })),
  };
  save();
  for (const [index, keyword] of serpQueries.entries()) {
    const response = await post('serp/google/organic/live/advanced', {
      keyword, location_code: 2840, language_code: 'en', device: 'desktop', os: 'windows', depth: 10,
    }, 0.002, auth);
    const result = response.task.result?.[0];
    if (!result) throw new Error('SERP result absent; stop without retry');
    const organic = (result.items ?? []).filter((row) => row.type === 'organic');
    batch.serps.push({
      family: families[index][0], keyword, task_id: response.task.id,
      endpoint: 'serp/google/organic/live/advanced', status_code: response.task.status_code,
      cost_usd: response.response_cost, device: 'desktop', os: 'windows', requested_depth: 10,
      datetime: result.datetime ?? null, check_url: result.check_url ?? null,
      item_types: result.item_types ?? [], items_count: result.items_count ?? null,
      organic_count: organic.length,
      completeness: organic.length >= 10 ? 'at-least-ten-organic-rows-returned; not full-SERP-or-market coverage' : 'fewer-than-ten-organic-rows; incomplete organic sample',
      organic: organic.map((row) => ({
        rank_group: row.rank_group, rank_absolute: row.rank_absolute,
        url: row.url, domain: row.domain, title: row.title,
      })),
    });
    save();
  }
  const headers = ['family', 'keyword', 'collected_at', 'provider', 'location_code', 'language_code', 'search_partners', 'search_volume', 'volume_availability', 'ads_competition', 'ads_competition_index', 'organic_difficulty', 'volume_task_id'];
  const escape = (value) => `"${String(value ?? '').replaceAll('"', '""')}"`;
  const rows = families.flatMap(([family, ...keywords]) => keywords.map((keyword) => {
    const match = batch.volume.rows.find((row) => row.keyword === keyword);
    return [family, keyword, batch.collected_at, 'DataForSEO Google Ads', 2840, 'en', false,
      match?.search_volume ?? '', match?.search_volume == null ? 'UNKNOWN' : 'TOOL_ESTIMATE',
      match?.competition ?? '', match?.competition_index ?? '', 'UNKNOWN', batch.volume.task_id];
  }));
  fs.writeFileSync(csvOutput, [headers, ...rows].map((row) => row.map(escape).join(',')).join('\n') + '\n');
  batch.completed = true;
  save();
  console.log(JSON.stringify({ completed: true, volume_rows: batch.volume.rows.length, serps: batch.serps.length, budget: batch.budget }));
}

main().catch((error) => { console.error(error.message); process.exitCode = 1; });
