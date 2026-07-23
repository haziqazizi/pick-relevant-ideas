# simplicity-budget

Simplicity is the budget that funds the necessary complexity.

Use when adding options, abstractions, flags, modes, config, generated files,
workflow steps, or dependencies.

## Actions

1. Delete dead states, flags, branches, or files before adding a new mechanism.
2. Prefer fewer states over more guards.
3. Add complexity only where it buys bounded blast radius, proof, or user value.
4. Treat every new option as a future cognitive load.
5. Record why necessary complexity earns its place.
6. Challenge casts, optionality, fallback paths, and generic wrappers that hide
   a simpler invariant.

## Evidence

Leave a deletion, simplification, rejected abstraction, or explicit complexity
budget note.

## Failure Smells

- Config DSL for a small finite problem.
- Permanent temporary flags.
- Abstraction for a future that has no second concrete use.
- More code to manage states that could be removed.
- File or markdown surface grows past the point where ownership and flow are
  still easy to scan.
- Refactor moves branches around but does not delete a concept.
