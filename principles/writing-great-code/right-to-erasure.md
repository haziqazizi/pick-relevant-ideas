# right-to-erasure

Privacy and deletion duties can outrank reversibility.

Use when handling user data deletion, logs, analytics, backups, exported
artifacts, screenshots, browser state, device state, or generated reports.

## Actions

1. Identify data that must be deleted or redacted.
2. Identify derived copies: logs, caches, screenshots, artifacts, backups.
3. Delete or redact source and derived copies where required.
4. Do not preserve rollback data that violates the deletion duty.
5. Leave an audit record that proves deletion without retaining the deleted data.

## Tension

If this conflicts with `optimize-for-reversibility.md`, deletion/privacy wins
when policy, law, or user promise requires it.
