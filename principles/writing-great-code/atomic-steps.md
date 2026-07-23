# atomic-steps

Split work into steps that either complete cleanly or leave a known recoverable
state.

Use for migrations, installers, generated files, bulk edits, deploy prep,
browser/iOS daemon setup, and external writes.

## Actions

1. Name each step and its before/after state.
2. Make each step idempotent where practical.
3. Write output to a temp path before replacing durable files.
4. Verify after each step when failure would be costly.
5. Record how to resume or roll back.

Atomic does not mean tiny. It means the system is never left mysterious.
