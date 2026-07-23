# dry-run-before-effects

Dangerous commands need a preview path.

Use for deletes, migrations, writes, network changes, deploys, pushes, PRs,
token changes, and generated overwrites.

## Actions

1. Add `--dry-run` or `check` mode.
2. Show what would change.
3. Include counts and paths.
4. Make dry-run safe and side-effect free.
5. Keep dry-run logic close to real execution so it does not drift.
