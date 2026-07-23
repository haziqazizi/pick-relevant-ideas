# progress-and-timeouts

Long-running commands need progress, deadlines, and a way to stop.

Use for builds, tests, browser/iOS sessions, network polling, deploy watchers,
generators, and migrations.

## Actions

1. Print progress to stderr.
2. Add a timeout or document why none is safe.
3. Handle interruption cleanly.
4. Leave partial output in a known state.
5. Print where logs/artifacts are located.
