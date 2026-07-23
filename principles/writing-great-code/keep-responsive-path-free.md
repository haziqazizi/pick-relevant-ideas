# keep-responsive-path-free

Do not block a responsive path on uncontrolled-latency work.

Use for UI threads, request handlers, event loops, game frames, CLI progress,
agent loops, browser commands, device sessions, and scheduler ticks.

## Actions

1. Identify the path that owes a response deadline.
2. List waits on network, disk, locks, browser/device sessions, providers, or
   work whose cost scales with input.
3. Move uncontrolled work off the responsive path with async work, background
   job, bounded queue, worker, pending state, or staged command.
4. Make fullness explicit with backpressure rather than an invisible queue.
5. Add a visible pending/error/degraded state.

## Evidence

Leave a trace, metric, timeout, queue bound, UI state, or command output showing
the path does not go dark while waiting.

## Failure Smells

- UI freezes while fetching or parsing.
- Request handler waits inline on a slow provider.
- CLI appears hung with no progress.
- Queue accepts work indefinitely.
- Old expired work is processed before still-useful work.
