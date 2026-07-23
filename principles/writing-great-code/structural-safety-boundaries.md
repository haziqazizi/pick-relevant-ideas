# structural-safety-boundaries

For risky work, enforce safety mechanically where possible.

Use for destructive commands, broad edits, production-like data, external
writes, device/browser sessions, and generated outputs.

## Actions

1. Identify the risky operation.
2. Add a dry-run, allowlist, prompt, guard, path restriction, or explicit flag.
3. Prefer commands that refuse unsafe defaults.
4. Log or report denied unsafe attempts.
5. Remove or retire the guard only when the risk is gone.

Warnings are weaker than constraints. Use constraints when cheap.
