# pick-relevant-ideas — details

`SKILL.md` is the runtime kernel. Pull this when selection is ambiguous,
you are editing the graph, or you need cold-start / anti-pattern rules.

## Product frame

**Job:** which great ideas are *about this task*, and how does each change
the approach?

Not: disaster workshop, workflow router, implementation, or catalog tour.

A principle earns a slot only if taking it seriously would change how you
approach or judge the work. Risk/severity may rank or boost; it does not
have to generate the set.

## Through-line (one move)

Push correctness out of human vigilance and into structure: types, schemas,
ownership, boundaries, atomic steps, deadlines, tests, reproducible runs,
explicit process. When ideas conflict, choose by:

1. objective  
2. who owns the input  
3. blast radius  
4. reversibility at the client boundary  

Never average incompatible doctrine.

## Retrieval algorithm (full)

```text
1. TASK ANATOMY
   one-liner + live facets from facet-seeds.yaml
   seeds = union of facet entry nodes, then trim to 1–4 total

2. EXPAND
   hop1: neighbors via co-applies | complements | requires
         weights strong|med
   hop2 (optional): strong only AND independent facet match
   tension: flag only — do not auto-add the other side
   clusters: diagnostic labels only — never select all members

3. SCORE
   + seed hit
   + edge weight from selected/seed set
   + facet match
   + approach-changing leverage on THIS task
   − degree penalty on hubs
   − already covered by a stronger neighbor (merge requires into one bind)

4. RELEVANCE GATE
   keep iff "changes approach on this task"
   drop decorative / prestige / "sounds wise"

5. TENSION RESOLVE
   if both ends score: pick one side via through-line axes
   record the decision; do not emit both as co-applies

6. CAP ≤7 + BIND
   each survivor → one action | check | artifact | stop

7. ANTI-ANCHOR
   bare major facet? add ≤2 or note gap
   idea with no facet/seed path? drop

8. EMIT + optional basket log + STOP
```

## Edge semantics

| Type | Meaning | Expand? |
|---|---|---|
| `co-applies` | Often relevant on the same task | yes (symmetric) |
| `complements` | A without B is incomplete | yes (a→b) |
| `requires` | Soft prerequisite; fold into same bind when possible | yes (a→b) |
| `tension` | Live tradeoff — pick a side | **flag only** |

No authored `weak` edges at cold start. Reserve `weak` for later learned
co-occurrence from `history/baskets.jsonl`.

## Cold-start rules

Load-bearing:

- Keep every `requires` and every `tension` edge when pruning the graph file.
- Keep strong edges whose endpoints share a named cluster.
- Prefer `must_keep_if_pruning` pairs in `graph.yaml` if the graph must shrink.

Optional / damp:

- Treat every `med` edge as optional unless one endpoint is a direct facet seed.
- Do not expand through umbrella doctrine (e.g. broad “agentic engineering”
  hub if added later).
- Do not let `prove-it-works`, `one-source-of-truth`, `make-it-observable`,
  or `simplicity-budget` win on degree alone.

## Anti-patterns

| Name | Avoid | Why |
|---|---|---|
| index-row-clique | Every INDEX row → complete clique | Rows are candidate sets, not proof all pairs co-apply |
| proof-hub | Link prove-it-works to everything | Appears in every basket; prefer specific proof ideas |
| generic-risk-hub | name-residual-risk on every task | Output condition, not idea generator |
| security-clique | Fully connect all auth/secrets nodes | Different anatomy: trust vs scope vs effects vs ambiguity vs credentials |
| observability-everywhere | make-it-observable ↔ everything | Prefer concrete invariant→signal pairs |
| baseline-everywhere | baseline on every change | Use for comparative claims |
| cli-family-clique | agent-friendly-cli ↔ all scripts | Seed the actual surface (I/O, destructive, long-run) |
| tension-means-take-both | Expand tension as co-applies | Tension is a decision, not a bundle |
| transitive-closure | Materialize A–C because A→B→C | Creates dense hubs; keep hop reasons |
| cluster-as-hyperedge | Auto-select all cluster members | Clusters are eval/diagnostic only |

## Principle body texts (required, in-pack)

All doctrine bodies ship under `principles/` in this skill directory:

```text
principles/INDEX.md
principles/writing-great-code/{id}.md
principles/writing-great-scripts/{id}.md
principles/working-with-ai-agents/{id}.md
```

Resolve id → path via `principles/INDEX.md`. After selection, read **only**
selected bodies. A missing body for a selected id is a pack integrity error
(`blocked` or fix the pack) — do not silently fetch outside this directory.

## Basket log (optional learning)

Append one JSON object per successful run to `history/baskets.jsonl`:

```json
{"ts":"2026-07-23","task":"…","facets":["auth"],"seeds":["trust-boundaries"],"selected":["trust-boundaries","boundary-discipline","prove-it-works"]}
```

Later: mine lift/confidence; propose `weak` edges behind the same gate.
Do not auto-promote learned edges to `strong` without human edit of
`graph.yaml`.

## Failure semantics

| Situation | Behavior |
|---|---|
| Task too vague to name facets | Ask one blocking question; do not dump popular hubs |
| `graph.yaml` / `facet-seeds.yaml` missing | `blocked` |
| Selected id has no file under principles/ | `blocked` pack integrity — do not invent body text |
| >7 still seem relevant after gate | Keep highest approach-leverage 7; list rejects |
| User asks to implement next | Hand off; this skill is done |

## Quality smells

- **Premature completion:** ids listed, no binds  
- **No-op:** “be careful with X” with no approach change  
- **Clique dump:** whole cluster selected  
- **Disaster theater:** only hazard language, no design/refactor/proof ideas when those facets are live  
- **Catalog tour:** reading list without seeds/expansion path  
