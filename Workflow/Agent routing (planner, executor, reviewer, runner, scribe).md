---
type: "infra"
tags: ["workflow"]
aliases: ["agent routing", "planner-fable"]
as_of: "2026-10-05"
---
# Agent routing (planner, executor, reviewer, runner, scribe)

**Plain words.** Different AI models get different jobs, matched to cost and difficulty (su2qc-skqd `prompts/ROUTING.md`):

| role | model | effort | job |
|---|---|---|---|
| planner-fable | Claude Fable 5.1 | high (max for blocked gates) | physics decisions, writes the next numbered prompt |
| executor-opus | Claude Opus 5.5 | high | implements the prompt |
| reviewer-opus | Opus | medium | audits JSON ↔ report ↔ code before a push |
| runner-sonnet | Sonnet | low | runs gates and tests, never edits source |
| scribe-haiku | Haiku | low | updates status tables, never changes numbers |

Fallbacks when quotas run out: NIM open models for running, Codex for executing; the planner has no substitute.
