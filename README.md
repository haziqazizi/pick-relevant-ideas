# pick-relevant-ideas

Standalone agent skill: pick the few great engineering ideas relevant to a task via a co-application graph, then bind each to how the approach should change.

This is a **selection guide the agent follows**, not a builder, reviewer, or workflow runtime.

```text
task anatomy → seed 1–4 → expand graph → read bodies → gate → ≤7 binds → stop
```

## When to use

You are about to start non-trivial work and want doctrine to govern it:

- "Which ideas should shape this change?"
- "Principles first — don't implement yet"
- Multi-facet work (auth + migration, CLI + long-running, design still open)

## When not to use

| Situation | Do instead |
|---|---|
| You already know the file and the fix | Just do it |
| You need a diff verdict ("is this safe?") | Review skill / human review |
| You need product direction or a full plan | Brainstorm / define-done |
| Work is already mid-implementation | Keep building; don't restart selection |

Rule of thumb: **use this when you can name the kind of work, but not yet which ideas should govern it.**

## One-sentence design law

> Facets seed entry ideas, the graph proposes neighbors that commonly fire together, and only ideas that change the approach survive the cap.

Relevance first. Risk may rank. Catalog tours and disaster theater are failures.

## Install

### Claude Code / Amp / agents that read `SKILL.md`

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/haziqazizi/pick-relevant-ideas.git ~/.agents/skills/pick-relevant-ideas
```

Legacy hosts using `.claude/skills`:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/haziqazizi/pick-relevant-ideas.git ~/.claude/skills/pick-relevant-ideas
```

No API keys or runtime deps. The skill is markdown + YAML + principle essays in-tree.

## How to use

Ask your agent before the work starts:

```text
Pick relevant ideas before we change JWT middleware that verifies tokens
and attaches a principal. Don't implement.
```

```text
Which ideas should govern this new repo check script?
```

```text
Principles first for the public API shape — no endpoints yet.
```

The agent should:

1. Name live **facets**
2. **Seed** 1–4 entry ids from `references/facet-seeds.yaml`
3. **Expand** neighbors via `references/graph.yaml`
4. **Read** only selected bodies under `principles/`
5. **Gate** on “changes approach on this task?”
6. Emit ≤7 **binds** and stop

## Edge types

| Type | Meaning |
|---|---|
| `co-applies` | Often relevant on the same task |
| `complements` | A without B is incomplete |
| `requires` | Soft prerequisite (fold into one bind when possible) |
| `tension` | Tradeoff — pick a side; never auto-take both |

Named **clusters** are diagnostic neighborhoods for evals — never auto-select every member.

## Layout

```text
pick-relevant-ideas/
├── README.md                      # you are here (human-facing)
├── SKILL.md                       # agent runtime kernel
├── LICENSE
├── references/
│   ├── facet-seeds.yaml           # task anatomy → entry nodes
│   ├── graph.yaml                 # 120 co-application edges + clusters
│   ├── through-line.md            # conflict resolver
│   └── details.md                 # full algorithm + anti-patterns
├── principles/
│   ├── INDEX.md                   # id → path
│   ├── writing-great-code/        # design, data, proof, ops, …
│   ├── writing-great-scripts/     # CLIs, checks, automation
│   └── working-with-ai-agents/    # agent conduct, verification, handoff
├── evals/
│   └── golden-cases.md
├── history/
│   └── baskets.jsonl              # optional past selections
└── scripts/
    └── validate-graph.py
```

## Validate

```bash
python3 scripts/validate-graph.py
```

Checks edge shape, facet seeds, cluster membership, and that every graph/seed id has a body under `principles/`.

## Quick smells (before you trust a selection)

- Whole cluster dumped without a relevance gate
- Prestige hubs always selected (`prove-it-works`, `one-source-of-truth`, …) with no facet path
- Tension edge treated as “take both”
- Reading list with no binds
- Implementation or review verdict produced as the deliverable
- More than 7 “governing” ideas for one task

## Learning (optional)

Append one JSON line per good run to `history/baskets.jsonl`, then mine co-occurrence later. Promote new edges into `graph.yaml` by hand — do not auto-write `strong` edges from history alone.

## Related

- Full agent contract: [`SKILL.md`](./SKILL.md)
- Companion design skill: [designing-dynamic-workflows](https://github.com/haziqazizi/designing-dynamic-workflows)

## License

MIT
