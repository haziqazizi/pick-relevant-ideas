# single-purpose-checks

Checks should answer one question clearly.

Use for lint-like scripts, stale generated checks, doctor checks, CI gates, and
artifact validators.

## Actions

1. Name the invariant being checked.
2. Keep output focused on failures and repair command.
3. Exit nonzero on failure.
4. Avoid bundling unrelated checks unless it is a top-level aggregator.
5. Provide a fix/render command when possible.
