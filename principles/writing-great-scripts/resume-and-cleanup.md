# resume-and-cleanup

A script should leave a recoverable state after interruption.

Use for commands that create temp files, locks, sessions, tunnels, background
processes, generated artifacts, or external resources.

## Actions

1. Track created resources.
2. Clean up on success and failure.
3. Use stable state files for resumable work.
4. Provide a cleanup command when automatic cleanup is unsafe.
5. Print resume instructions when stopping early.
