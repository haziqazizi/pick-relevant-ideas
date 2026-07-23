---
name: pick-relevant-ideas
description: "Select the few great ideas relevant to this task and bind each to how the approach should change. Use when about to start non-trivial work and doctrine must govern it. Do NOT use when implementing, reviewing, or choosing which workflow to run."
version: 2
---

# pick-relevant-ideas

## Purpose

Identify the few **great ideas** (engineering principles) that are about *this*
task, retrieve neighbors that commonly fire with them, and bind each survivor
to a concrete change in approach.

Self-contained pack: graph, facets, and principle bodies all live in this
skill directory.

Does **not** implement, review, or route workflows. Relevance means: taking
the idea seriously would change how you approach or judge the work.

## Paths (all relative to this skill root)

| Need | Path |
|---|---|
| Facet → seeds | `references/facet-seeds.yaml` |
| Co-apply graph | `references/graph.yaml` |
| Algorithm depth | `references/details.md` |
| Conflict resolver | `references/through-line.md` |
| Principle bodies | `principles/**/{id}.md` (see `principles/INDEX.md`) |
| Basket log | `history/baskets.jsonl` |

## Workflow

1. **Task anatomy.** One-line task. Check only live facets from
   `references/facet-seeds.yaml`. Seed **1–4** entry principle ids total.
2. **Expand (graph).** Load `references/graph.yaml`. Walk **1 hop** on
   `strong`/`med` edges: `co-applies`, `complements`, `requires`.
   Optional **2nd hop**: `strong` only **and** independent facet match.
   Never auto-expand `tension`. Never auto-add a whole named cluster.
3. **Score.** Prefer seed hit, strong edges from the seed set, facet match,
   approach-changing leverage. Dampen hubs (`prove-it-works`,
   `one-source-of-truth`, `make-it-observable`, `simplicity-budget`).
   Fold `requires` into the same bind when possible.
4. **Read bodies.** For candidates that might survive, read
   `principles/**/{id}.md` (resolve via `principles/INDEX.md`). Do not read
   the whole corpus.
5. **Relevance gate.** Keep only if taking it seriously **changes approach
   on this task**. Resolve each live `tension` by picking one side (see
   `references/through-line.md`) — never average.
6. **Cap and bind.** At most **7** ideas. Each → one action, check, artifact,
   or stop. No bind → drop.
7. **Anti-anchor.** Bare major facet? Add ≤2 or note gap. Idea with no
   facet/seed path? Drop.
8. **Emit and stop.** Optional: append selected ids to `history/baskets.jsonl`.
   Do not implement.

## Output

```text
Task: <one line>
Facets: <live facets>
Seeds: <1–4 ids>

Selected:
- <id> → because <facet/neighbor>; bind: <I will …>
  (body: principles/<family>/<id>.md)

Tensions resolved:
- <a> vs <b> → chose <side> because <…>

Rejected near-misses:
- <id> → <why not>

Gaps: <facet with no idea, or none>
```

## Done

- Every kept row would change approach; ≤7 binds; tensions decided
- Bodies for selected ids were read from this pack (or gap noted)
- Stopped without implementing or reviewing

## Hard stops

- Do not implement, edit product code, or open a PR under this skill
- Do not depend on paths outside this skill directory for doctrine
- Do not browse the full principle tree — select via graph, then read
- Do not treat “sounds wise” as enough without approach change on *this* task
