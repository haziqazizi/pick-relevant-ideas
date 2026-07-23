# atomic-or-serialized-shared-state

Check-then-act on shared state is a race unless the act is atomic, serialized,
or harmless to repeat.

Use for database writes, file claims, locks, leases, queues, cron jobs, browser
sessions, generated files, and any state multiple actors can touch.

## Actions

1. Ask whether two actors can run between the read and the write.
2. Prefer one atomic operation: unique constraint, upsert, compare-and-swap,
   atomic rename, fenced lease, or row-count checked update.
3. If atomicity is not available, serialize with one owner or a clear lock order.
4. If neither is practical, make the operation idempotent or commutative.
5. Test or demonstrate the duplicate/overlap case when risk is real.

## Evidence

Leave the atomic operation, lock owner, idempotency key, test, or rationale.

## Failure Smells

- `SELECT` then `INSERT` where `INSERT ... ON CONFLICT` would work.
- "Check flag then claim work" without atomic claim.
- Lease used without fencing.
- Double-click or retry can duplicate an effect.
