# minimize-reader-load

Optimize for the next reader's working memory.

Use when code, skills, docs, or generated artifacts require too much chasing.

## Actions

1. Count how many concepts must be held at once.
2. Inline or delete one-caller indirection when it adds no boundary value.
3. Name concepts with domain words.
4. Keep related decision and effect close unless one source of truth would be violated.
5. Prefer tables, schemas, and diagrams over scattered prose for multi-part state.
6. Treat repeated conditionals, wrong-layer feature logic, and cast/optionality
   churn as signs the reader is carrying a missing model.
7. Split or consolidate large files/docs by ownership only when that reduces
   the number of concepts a reader must chase.

The target reader is tired, interrupted, and missing context.
