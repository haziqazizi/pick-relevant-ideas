# Principle bodies

In-pack corpus. The skill resolves ids to these files after graph selection.

```text
principles/
  INDEX.md
  writing-great-code/
  writing-great-scripts/
  working-with-ai-agents/
```

- Ids in `references/graph.yaml` and `references/facet-seeds.yaml` are filename
  stems (`trust-boundaries` → `writing-great-code/trust-boundaries.md`).
- After selection, **read only the selected bodies** — do not browse the tree.
- `writing-great-code/THROUGH-LINE.md` is the long-form conflict resolver;
  `references/through-line.md` is the short runtime copy.

## Editing

1. Add `principles/{family}/{id}.md`
2. Wire edges in `references/graph.yaml`
3. Add facet seeds if it is an entry node
4. Run `python3 scripts/validate-graph.py`
