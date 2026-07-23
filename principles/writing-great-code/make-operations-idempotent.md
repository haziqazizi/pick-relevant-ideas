# make-operations-idempotent

Operations should converge if run twice or resumed after interruption.

Use for installers, setup, generated files, migrations, browser/iOS daemon
startup, cleanup, retries, PR prep, and deploy-adjacent steps.

## Actions

1. Define the desired end state.
2. Check current state before writing.
3. Make repeated execution harmless.
4. Use temp files or atomic replacement for durable outputs.
5. Record how to recover after partial completion.

Idempotency reduces what a future agent must remember about what already ran.
