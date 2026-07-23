# name-to-reveal

Name things to reveal the load-bearing fact a reader would otherwise miss.

Use for functions, variables, files, states, generated artifacts, commands,
metrics, tests, and reports.

## Actions

1. Identify the one fact a reader is likely to get wrong.
2. Encode units, ordering, side effects, idempotency, authority, or lifecycle in
   the name when the type or schema does not already carry it.
3. Avoid vague names like `data`, `handle`, `process`, and `result` when a domain
   name exists.
4. Avoid names so long they become summaries of the implementation.
5. Rename when behavior changes and the old name becomes false.

## Evidence

Leave renamed symbols/files or a note explaining the chosen name.

## Failure Smells

- `amount` without unit.
- `doThing` hiding a side effect.
- Name claims idempotency or safety that no longer exists.
- Reader must open the body to learn the basic caveat.
