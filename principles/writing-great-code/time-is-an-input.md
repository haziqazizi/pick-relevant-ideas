# time-is-an-input

Wall-clock time can lie. Measure durations with a monotonic clock and order
distributed events with logical or fenced ordering.

Use for deadlines, retries, leases, TTLs, token expiry, ordering, analytics,
browser/device waits, and distributed workflows.

## Actions

1. Classify the use: duration, deadline, timestamp display, expiry, or ordering.
2. Use monotonic time for durations and deadlines.
3. Do not infer distributed causality from wall-clock timestamps.
4. Use logical clocks, sequence numbers, versions, or fenced leases for ordering.
5. Treat client-supplied or remote timestamps as untrusted input.

## Evidence

Leave the chosen clock, sequence, version, or ordering rule in code or notes.

## Failure Smells

- Timeout measured against wall clock.
- Ordering by `created_at` across hosts.
- Lease/expiry can be extended or shortened by clock skew.
- Test depends on real current time with no override seam.
