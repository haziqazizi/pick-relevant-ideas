# idempotent-commands

Commands should be safe to retry.

Use for setup, install, generated files, migrations, cleanup, daemon start,
route creation, and any command agents may rerun.

## Actions

1. Check existing state first.
2. Converge to desired state.
3. Avoid duplicate records, routes, symlinks, jobs, or generated blocks.
4. Treat already-done as success when safe.
5. Print what changed versus what already existed.
