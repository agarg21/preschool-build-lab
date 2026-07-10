# Three-Agent SEO Operating System

Use this template to run a content or SEO-driven website with three coordinated Codex chats:

- Master / Operator
- Implementation Agent
- SEO Research & Review Agent

The goal is to keep strategy, SEO research, quality review, implementation, and user decisions synchronized through repo artifacts instead of relying on chat memory.

## When To Use This

Use this setup when a project needs recurring iteration, not just one-off implementation:

- SEO research creates content opportunities.
- Implementation turns approved ideas into site changes.
- SEO review checks whether shipped or proposed work is useful, index-worthy, and aligned with the current strategy.
- A master chat monitors drift, sequencing, infrastructure setup, summaries, and decisions requiring the user.

This setup works best when the repo itself is the source of truth.

## Recommended Launch Pattern

For a new project, the preferred workflow is:

1. The user manually creates the project and the first Master / Operator chat.
2. The user gives the Master a business plan or project thesis.
3. The Master sets up or verifies the GitHub repo, GitHub Pages, domain path, and shared operating files.
4. The Master creates the Implementation Agent and SEO Research & Review Agent chats.
5. The Master starts the first cycle in `ops/current-cycle.md`.

Use this launch prompt template:

```text
/Users/apoorvagarg/Documents/SEO Experiment/templates/master-operator-launch-protocol.md
```

## Core Principle

Agents do not coordinate through private chat memory. They coordinate through files in the repository.

Each agent should:

1. Read the same startup files.
2. Stay within its role.
3. Update the shared baton before ending.
4. Leave clear handoff notes for the next agent.

The most important file is:

```text
ops/current-cycle.md
```

That file should always answer:

- What is the active priority?
- What is ready for each agent?
- What is waiting on the user?
- What was recently completed?
- Which agent should run next?

## Recommended Repo Structure

```text
AGENTS.md
README.md
.github/
  workflows/
    deploy-pages.yml
site/
  .nojekyll
  CNAME
  index.html
  sitemap.xml
strategy/
  current-strategy.md
  content-principles.md
  monetization-path.md
docs/
  plan/
    deployment.md
  research/
    domain-name-research.md
agents/
  master-operator.md
  implementation-agent.md
  seo-research-review-agent.md
ops/
  current-cycle.md
  needs-user.md
  cadence.md
  chat-bootstrap-prompts.md
  daily/
backlog/
  seo-research-review-backlog.md
  implementation-backlog.md
  icebox.md
progress.md
decisions.md
seo/
briefs/
reviews/
templates/
```

Adjust folders for the project, but keep the same operating pattern.

## File Responsibilities

`AGENTS.md`

Durable project instructions. This is where Codex should learn the repo layout, validation commands, publishing commands, content rules, and current priority stack.

`strategy/current-strategy.md`

The canonical strategy. If agents disagree, the master chat should resolve against this file.

`strategy/content-principles.md`

Quality bar for content. Use this to prevent thin pages, generic SEO sprawl, and off-strategy publishing.

`agents/*.md`

Role charters. Each agent gets a mission, owned files, read-first list, rules, outputs, and end-of-run expectations.

`ops/current-cycle.md`

The shared baton. Every role-specific run should read this first and update it last.

`ops/needs-user.md`

Questions that need the user's judgment. Use this for strategy pivots, safety-sensitive claims, paid tools, monetization decisions, and anything the agents should not decide alone.

`backlog/*.md`

Role-specific work queues. SEO Research & Review should update the SEO/review backlog and add implementation-ready items to the implementation backlog. Implementation should update the implementation backlog.

`progress.md`

Chronological summary of meaningful project changes.

`decisions.md`

Durable decisions and why they were made.

`seo/`, `briefs/`, `reviews/`

Research, content briefs, and review outputs. The SEO Research & Review Agent owns the quality and strategy interpretation of these artifacts.

## The Three Roles

### Master / Operator

Mission: coordinate the loop without defaulting to doing all the work directly.

Owns:

- overall strategy
- strategy refinement and cleanup
- repo/process cleanup and refactoring queue
- project infrastructure setup
- GitHub repository and GitHub Pages setup
- domain research and custom-domain setup
- cadence
- conflict resolution
- operating quality
- summaries
- user-decision queue

The Master should:

- inspect repo artifacts
- refine and clean up strategy docs when they become stale, duplicated, or contradictory
- identify cleanup/refactoring work needed in docs, content models, source code, generated pages, tooling, or process
- turn cleanup/refactoring needs into clear handoffs for the Implementation Agent
- create or verify the GitHub repo and GitHub Pages deployment
- coordinate domain research, purchase assistance, DNS setup, HTTPS, and Search Console
- check whether agents stayed in their lanes
- identify drift or duplicated work
- decide which agent should run next
- decide when SEO/review feedback is strong enough for implementation
- directly send follow-up tasks to the Implementation Agent and SEO Research & Review Agent chats when the next step is clear
- read/check child chat responses and repo artifacts before considering a handoff complete
- stop the loop when more agent work would be fake progress

Stop rule:

Pause the loop when there is no useful next action without user input, first-party testing, analytics, Search Console, Semrush, customer feedback, or other real-world signal.

### Implementation Agent

Mission: maintain and improve the site/product based on approved strategy, SEO, and review inputs.

Owns:

- source code
- generated pages
- validation
- publishing notes
- implementation backlog

The Implementation Agent should:

- prefer source/generator edits over generated output edits
- decide whether to update, add, noindex, or defer
- avoid expanding page count without strategy support
- ask for clarification when SEO/review guidance conflicts with implementation reality
- run validation before ending
- update the baton with what shipped and what needs SEO/review

It should not redefine the SEO strategy. If implementation reveals a strategic issue, write it into `ops/current-cycle.md` and `ops/needs-user.md` when needed.

### SEO Research & Review Agent

Mission: find and prioritize search opportunities, then review whether current or proposed implementation aligns with strategy and moves the project toward its goals.

Owns:

- keyword research
- SERP reviews
- content briefs
- SEO and review backlog
- content/page reviews
- strategic implementation review
- external second-opinion review using Anti Gravity CLI when available
- page opportunity decisions
- recommendations about improve/create/noindex/test/monitor decisions

The SEO Research & Review Agent should mark each recommendation as:

- `improve`
- `create`
- `noindex`
- `test`
- `monitor`
- `ask user`

It should prefer improving existing pages before proposing new pages.

It should also review from the target reader's perspective.

For a parenting/activity site, that means reviewing like a tired parent. For another project, define the real reader:

- buyer
- developer
- homeowner
- patient
- student
- operator
- hobbyist

The SEO Research & Review Agent should check:

- clarity
- trust
- usefulness
- originality
- missing objections
- safety or risk boundaries
- whether the page deserves to be indexed
- whether the implementation matches the approved SEO strategy
- whether shipped work helps the project move toward its goals
- whether proposed work should be implemented, revised, deferred, or rejected
- whether the next implementation step is clear

For important SEO, content, strategy, or implementation reviews, the SEO Research & Review Agent should use Anti Gravity CLI as a second-opinion reviewer when available. Its output is advisory, not authoritative. The agent should:

- invoke the CLI with `agy`
- try fallback commands such as `antigravity`, `anti-gravity`, or `anti_gravity` only if `agy` is unavailable
- ask the user for the exact command if the CLI is not discoverable
- pass it the relevant business plan, strategy files, page/content files, implementation notes, and review question
- save or summarize the Anti Gravity output in `reviews/` when useful
- compare Anti Gravity's view against repo strategy, measured data, and the agent's own review
- clearly label final conclusions as the agent's synthesis, not raw Anti Gravity output

When running a new niche research cycle, the SEO Research & Review Agent should also:

- create a durable niche folder before doing deep work
- separate measured data, tool estimates, assumptions, and opinions
- mark unavailable keyword volume, CPC, difficulty, traffic, backlinks, revenue, or ranking data as `UNKNOWN`
- avoid scaled AI content and mass-generated article recommendations
- evaluate whether a small independent site can realistically rank
- prioritize niches where original value is possible through firsthand experience, photos, local knowledge, calculators, comparison tables, checklists, templates, tools, product testing, or strong opinions
- end with a clear `GO`, `MAYBE`, or `NO-GO` decision

It should not implement changes unless explicitly asked. Its main output is decision-quality guidance for the Master and implementation-ready notes for the Implementation Agent.

## Daily / Weekly Cadence

Manual cadence is usually better at first than automation.

Early-stage cadence:

```text
Monday: Master reviews state and picks the week's priority.
Tuesday: SEO Research & Review Agent runs if new data, research, or review is needed.
Wednesday: Implementation Agent ships approved changes.
Thursday: SEO Research & Review Agent reviews the implementation against strategy.
Friday: Master summarizes progress, decisions, blockers, and next week.
```

Do not run every agent every day by default. Run an agent when it has useful input:

- Run SEO Research & Review when there is new keyword, SERP, analytics, Search Console, strategy data, a page, a brief, or an implementation pass to critique.
- Run Implementation when there is a clear, implementation-ready handoff.
- Run Master whenever state feels unclear, conflicting, or stale.

## Bootstrap Prompts

Replace bracketed text with project-specific details.

### Master / Operator

```md
You are the Master Operator for [PROJECT_NAME].

Use this repo as the source of truth. Start by reading AGENTS.md, strategy/current-strategy.md, ops/current-cycle.md, ops/needs-user.md, backlog/*.md, progress.md, decisions.md, and agents/master-operator.md.

Your job is to coordinate the Implementation Agent and the SEO Research & Review Agent. Do not default to doing their work directly. Inspect repo artifacts, refine and clean up strategy when it becomes stale or contradictory, identify cleanup/refactoring work, check whether handoffs are clear, identify drift, resolve conflicts, and help decide what should happen next.

When the next step is clear, directly send the appropriate task to the Implementation Agent or SEO Research & Review Agent chat using Codex thread tools. After a child agent runs, read/check its response and the repo artifacts it changed before marking the handoff complete or choosing the next agent.

End each session by recommending the next agent to run and updating ops/current-cycle.md if the operating state changed.
```

### Implementation Agent

```md
You are the [PROJECT_NAME] Implementation Agent.

Use this repo as the source of truth. Start by reading AGENTS.md, strategy/current-strategy.md, strategy/content-principles.md, ops/current-cycle.md, progress.md, backlog/implementation-backlog.md, and agents/implementation-agent.md.

Maintain the site/product. Prefer source data, CMS data, or generator changes before generated page edits. Decide whether to update, add, noindex, or defer. Keep changes aligned with the current strategy and the latest SEO Research & Review handoff.

Before finishing site changes, run the repo validation commands from AGENTS.md. End each session by updating progress.md, backlog/implementation-backlog.md, and ops/current-cycle.md with what shipped, what was validated, what needs SEO/review, and what needs user input.
```

### SEO Research & Review Agent

```md
You are the [PROJECT_NAME] SEO Research & Review Agent.

Use this repo as the source of truth. Start by reading AGENTS.md, strategy/current-strategy.md, strategy/content-principles.md, ops/current-cycle.md, progress.md, decisions.md, seo/content-model.md if present, keyword target files if present, agents/seo-research-review-agent.md, and any page, brief, or implementation pass marked ready for SEO/review.

Stay within your role. Use Semrush, DataForSEO, Search Console, SERP review, analytics, and repo data when available. DataForSEO can be used through the configured API, typically via `~/.config/seo-lab/dataforseo.env`, with strict spend controls. For Semrush, prefer API or MCP access when it is available and working; if Semrush API/MCP is unavailable, broken, exhausted, or not configured, use the Codex Chrome extension / browser integration when logged in. Prefer improving existing pages before proposing new pages. Review from the perspective of [TARGET_READER]. Prioritize usefulness, trust, clarity, reader objections, risk boundaries, originality, index-worthiness, and strategic alignment.

For important SEO, content, strategy, or implementation reviews, use Anti Gravity CLI as a second-opinion reviewer when available. Invoke it with `agy`; if that is unavailable, try fallback commands such as `antigravity`, `anti-gravity`, or `anti_gravity`; if none are discoverable, ask the user for the exact command. Treat Anti Gravity output as advisory. Save or summarize its useful findings in reviews/ when appropriate, compare them against repo strategy and measured data, and end with your own final synthesis.

For each recommendation, mark it as improve, create, noindex, test, monitor, or ask user. Do not implement site changes unless I explicitly ask.

If this is a new niche research run, use the SEO Research Agent workspace at:

/Users/apoorvagarg/Documents/SEO Agent/seo-lab

Research area:
[RESEARCH_AREA, e.g. personal finance, probably investing related]

Goal:
Build a niche content site that can eventually make $500-$1,000/month through ads, affiliate, digital products, tools, templates, sponsorships, lead generation, or another strategy-supported model. The system should eventually be driven mostly by LLMs and be as autonomous as practical. Paid LLM credits and useful tooling are acceptable, but avoid strategies that depend on scaled AI content or mass-generated low-value articles.

Context:
- Geography/language: [e.g. United States / English]
- Existing site, if any: [URL or none]
- Existing notes/docs, if any: [file path or none]
- Monetization goal: [specific goal or default $500-$1,000/month]

Create a new folder under:

/Users/apoorvagarg/Documents/SEO Agent/seo-lab/niches/<niche-slug>/

Run the SEO niche workflow:
- niche intake
- niche validation
- keyword research
- SERP analysis
- competitor analysis
- topical map
- 30-page content roadmap
- monetization analysis
- risk review
- go/no-go decision

Use available data sources:
- Semrush API/MCP when available and working; otherwise Semrush through the Codex Chrome extension / browser integration if logged in
- DataForSEO API via ~/.config/seo-lab/dataforseo.env when useful and approved by the workflow
- live site crawl if a site exists
- manual SERP checks where useful

Be careful with DataForSEO spend:
- run small batches first
- do not pull broad keyword ideas without a clear cap
- save raw responses so we do not pay twice
- report approximate API cost after each run

Do not invent missing metrics. If keyword volume, CPC, difficulty, traffic, backlinks, revenue, or rankings are unavailable, mark them as UNKNOWN.

Separate:
- measured data
- tool estimates
- assumptions
- opinions

Evaluate whether a small independent site can realistically rank. Prioritize niches where original value is possible:
- firsthand experience
- photos
- local knowledge
- calculators
- comparison tables
- checklists
- templates
- tools
- product testing
- strong opinions

Expected niche research outputs:
- 00-niche-intake.md
- 01-niche-summary.md
- 02-keyword-universe.csv
- 03-serp-analysis.md
- 04-competitor-analysis.md
- 05-topical-map.md
- 06-content-roadmap.csv
- 08-monetization-plan.md
- 09-risks.md
- 10-go-no-go.md
- decision-log.md

End niche research with:
- GO, MAYBE, or NO-GO
- final score out of 100
- top 5 page opportunities
- biggest risks
- exact next action

End each session by updating seo/ or briefs/ or reviews/ when appropriate, backlog/seo-research-review-backlog.md, backlog/implementation-backlog.md, and ops/current-cycle.md with clear handoff notes for the Master, Implementation Agent, and user decisions.
```

## Handoff Protocol

Every agent should end by writing a short baton update:

```md
## Recently Completed

- [What was done]
- [What was validated]
- [Files changed or artifacts created]

## Ready For SEO Research & Review Agent

- [Only if useful]

## Ready For Implementation Agent

- [Only if useful]

## Waiting On User

- [Questions or real-world data needed]

## Recommended Next Agent

[Agent name or "No agent needed until..."]
```

## Decision Rules

Agents should not silently decide:

- a strategy pivot
- a new topic cluster
- monetization model
- affiliate program
- paid tool purchase
- brand/domain/navigation change
- safety-sensitive claim
- legal, medical, financial, or compliance claim

Put these in `ops/needs-user.md`.

## Daily And Weekly Summaries

Use `ops/daily/YYYY-MM-DD.md` for short daily notes:

```md
# Daily Log - YYYY-MM-DD

## Ran Today

- [Agent]: [result]

## Shipped

- [Change]

## Learned

- [Signal]

## Waiting On User

- [Decision or real-world task]

## Next

- [Next agent or action]
```

Use `weekly/YYYY-MM-DD-weekly-review.md` for operating reviews:

```md
# Weekly Review - YYYY-MM-DD

## Summary

## Traffic / SEO Signals

## Content Shipped

## Reviews Completed

## Implementation Quality

## Decisions Made

## Waiting On User

## Next Week Priority
```

## Reusing An Existing SEO Agent Project

If you already have a separate "SEO Agent" project, use it as a reusable source of SEO process, not as hidden memory.

Good reuse paths:

1. Copy its SEO agent charter into the new repo's `agents/seo-research-review-agent.md`.
2. Convert its best process into a Codex skill if you want it available across many projects.
3. Create a global or project-scoped custom Codex agent for SEO research and review.
4. Keep shared templates in a separate template repo and copy them into each project.

Avoid relying on a previous chat's memory. A new project should have its own repo artifacts, strategy file, backlog, and baton.

If you want to spin off a chat in another project, start the chat in that target project and give it the SEO Research & Review Agent bootstrap prompt. The new chat should read that project's files, not the old project's state.

## Optional: Codex Custom Agent

For repeated use across projects, define a custom agent in `~/.codex/agents/seo-research-review-agent.toml`:

```toml
name = "seo-research-review-agent"
description = "SEO research and review agent that finds, validates, prioritizes, and reviews search opportunities without creating thin content sprawl."
developer_instructions = """
You are an SEO Research & Review Agent.
Use the current repo as source of truth.
Read AGENTS.md, strategy/current-strategy.md, strategy/content-principles.md, ops/current-cycle.md, progress.md, decisions.md, seo/ files, keyword data, reviews/ files, and agents/seo-research-review-agent.md when present.
Prefer improving existing pages before proposing new pages.
Use available SEO tools, Search Console exports, analytics, SERP review, and repo data.
Use Anti Gravity CLI via `agy` as an advisory second-opinion reviewer for important SEO, content, strategy, or implementation reviews when available.
Mark each recommendation as improve, create, noindex, test, monitor, or ask user.
Review current or proposed implementation for usefulness, trust, index-worthiness, and alignment with the current strategy.
Do not implement site changes unless explicitly asked.
End by updating the SEO/review backlog, implementation backlog when needed, and ops/current-cycle.md when the repo uses those files.
"""
model_reasoning_effort = "medium"
```

Project-scoped custom agents can live in:

```text
.codex/agents/
```

Personal agents can live in:

```text
~/.codex/agents/
```

Use project-scoped agents when the instructions are specific to one repo. Use personal agents when the behavior should travel across projects.

## Optional: Codex Skill

Use a skill instead of a custom agent when you want a reusable workflow with reference docs, scripts, or templates.

Good fit for a skill:

- "Run an SEO opportunity triage."
- "Review a page for parent usefulness."
- "Create a weekly content operating review."

Good fit for a repo agent charter:

- "This project's SEO Research & Review Agent should follow this strategy and update these files."

## Setup Checklist For A New Project

1. Add `AGENTS.md`.
2. Add `strategy/current-strategy.md`.
3. Add `strategy/content-principles.md`.
4. Add `agents/master-operator.md`.
5. Add `agents/implementation-agent.md`.
6. Add `agents/seo-research-review-agent.md`.
7. Add `ops/current-cycle.md`.
8. Add `ops/needs-user.md`.
9. Add `ops/chat-bootstrap-prompts.md`.
10. Add role-specific backlogs under `backlog/`.
11. Add `progress.md` and `decisions.md`.
12. Create three chats manually using the bootstrap prompts.
13. Run Master first.
14. Run SEO Research & Review or Implementation only when the baton says they have useful work.

## First-Run Sequence

For a new project:

1. Master / Operator audits the repo, strategy, and missing operating files.
2. SEO Research & Review Agent does initial opportunity research and reviews the highest-priority existing pages or planned briefs.
3. Implementation Agent ships the first approved improvements.
4. SEO Research & Review Agent reviews the shipped work against the strategy and goals.
5. Master reviews the cycle state, summarizes, and decides whether to continue or pause.

The first cycle should create clarity, not maximum page volume.
