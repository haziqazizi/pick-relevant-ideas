# Subagent dispatch contract

Use this when a skill uses dynamic lenses, reviewers, graders, scouts, or
subagents. This is host-neutral: if the current agent runtime has subagents,
spawn them; if not, run the same rows inline and label the evidence limit.

The point is to make delegation explicit and auditable, not to force a persona
panel. The parent agent owns scope, synthesis, and final judgment.

## Dispatch plan

Write this table before running lenses for non-trivial work.

| Stage | Topology | Scope signal | Lens | Run? | Reason / skip reason | Agent ref | Mode | Required context | Output |
|---|---|---|---|---|---|---|---|---|---|
| review | fan-out-and-synthesize | auth files changed | security | yes | authz surface touched | `security-reviewer` (fresh-context security lens) | subagent/inline | diff + evidence + no-fire list | findings |

For worker-tree dispatches, add these fields to the table or a sibling table:
`depends_on`, `paths_allowed`, `paths_forbidden`, `handoff_path`,
`verification_quality`, and `retry_policy`. They are optional for read-only
lenses but required when branches edit files, publish artifacts, or feed later
workers.

Allowed `Mode` values:

- `subagent` — host supports fresh-context delegation.
- `inline` — parent runs the lens separately and labels it inline.
- `external-agent` — a repo-approved external runner/tool supplies the result.
- `skipped` — surface absent or out of scope; record one-line rationale.

## Dispatch rules

- Scope-gate first from concrete signals: diff paths, actors, data boundaries,
  auth/permissions, UI visibility, money, migrations, deployment, docs, and
  external integrations.
- Dispatch the smallest set of lenses that can catch realistic failure modes.
- Do not dispatch a fixed panel unless the skill has an always-on reason.
- Give each branch only the context it needs: task, relevant files/artifacts,
  rubric/no-fire list, and required output schema.
- Keep write scopes disjoint when using worker subagents. Branches must not write
  the same artifact, branch, state file, checklist, or output path unless a
  structural single-writer phase or lock is part of the plan. Reviewer/validator
  branches are read-only by default.
- Worker siblings do not coordinate directly. A branch returns dependencies,
  blockers, and discovered scope to the parent; the parent relays approved
  context into later branches through declared handoff paths.
- For external writes, the coordinator is
  the external writer by default; child agents prepare drafts or payloads unless
  the dispatch plan gives them explicit immutable coordinates, allowed
  operations, and post-write verification.
- For candidate-generation lanes, use the same task contract and rubric for each
  candidate so differences are attributable to approach/model judgment, not
  prompt drift. Give each candidate its own output path and require a short
  rationale naming alternatives considered and rejected.
- When the host supports model routing, record the intended `Model role`, the
  resolved model/tool if visible, and any fallback reason in the branch output.
  Treat role routing as an auditable capability choice, not as hidden magic.
- Parent agents verify delegated artifacts directly. Subagent summaries are
  hints; evidence is the diff, file, command output, screenshot, trace, report,
  or other artifact the parent inspected.
- When subagents are unavailable, run the same lenses inline as separate passes;
  do not silently skip rigor.
- Single-level dispatch: a worker subagent does not itself fan out. Recursive
  delegation multiplies context (parent × child × grandchild) and hides scope
  from the owner. A branch that discovers it needs sub-delegation returns that
  to the parent to plan, rather than spawning its own workers.

## Result ledger

After lenses return, write a result ledger before deciding.

| Lens | Mode | Status | Findings | Evidence | Residual / next route |
|---|---|---|---|---|---|
| security | subagent | pass/fail/blocked | `N` or `NO FINDINGS` | artifact/path | fix / residual / none |

Worker-tree ledgers also record path ownership, handoff path, verification
quality (`ground-truth`, `LLM-judge`, `unverified`, or `blocked`), and retry
policy so the parent can resume or stop without reading private branch context.

Findings use grader discipline: severity, confidence, location,
category, summary, evidence/fix direction, and stable fingerprint.

## Synthesis block

Every dynamic dispatch reports:

```text
Topology:
Why this topology:
Dispatch plan path or table:
Branches/lenses run:
Branches/lenses skipped:
Result ledger:
Synthesis decision:
Residuals:
```

Do not hide this in chat reasoning. It belongs in the skill artifact or final
report so a future grader can understand what was and was not checked.

## Cost per task

Dispatch is where cost is decided: the model-price spread is ~20x and agents
burn 5-30x single-turn tokens, so route by need, not habit:

- **Cheapest capable tier per sub-task** — search/extraction/formatting on a
  small model; reserve frontier tiers for the hard reasoning or judging step.
- **Cache-friendly prompts** — reuse stable context blocks verbatim across
  dispatches instead of re-deriving or re-phrasing them; cache hit rate is a
  ~5x cost lever.
- **Verify cheap before retrying expensive** — a small-model or command-level
  check on a candidate beats re-running the full expensive generation.
- **Hard budgets are enforced by the harness, never trusted to the agent.**
  A stated-but-unenforced call/time budget is a no-op for a weak model
  (measured: told 3 tool calls, spent 9, reported nothing). Enforce with
  structure — timeouts, call caps, kill-at-N — and treat the agent's own
  budget accounting as a report to verify against harness ground truth
  (session logs), not as the control.
- **Report cost with results** when the harness exposes it: tokens or $ per
  resolved task is a first-class outcome, not overhead trivia.
