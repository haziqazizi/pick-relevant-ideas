# explicit-confirmation-bypass

Automation needs explicit confirmation flags instead of prompts.

Use when a command normally asks a human to confirm.

## Actions

1. Add `--yes`, `--force`, or a specific confirmation flag.
2. Make the flag name match the risk.
3. Require target identifiers for destructive operations.
4. Do not infer confirmation from non-TTY alone.
5. Log that confirmation was bypassed.
