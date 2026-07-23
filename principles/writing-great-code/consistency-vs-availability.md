# consistency-vs-availability

Choose consistency or availability explicitly when partitions, stale reads,
queues, caches, offline clients, or retries are involved.

## Prefer Consistency When

- auth, permissions, money, inventory, deletion, safety, or legal state is at stake
- stale data would create an irreversible or hard-to-repair action

## Prefer Availability When

- stale data is acceptable
- the UI/API labels uncertainty
- reconciliation exists
- duplicate or delayed work is idempotent

## Evidence

Record the chosen side, stale-data tolerance, reconciliation path, and user or
operator signal.
