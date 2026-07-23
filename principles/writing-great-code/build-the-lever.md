# build-the-lever

For repeated, broad, or verification-heavy work, build the smallest rerunnable
tool that does or proves the work.

Use when hand-editing many files, checking generated artifacts, migrating
callers, validating screenshots, auditing routes, or repeating a command by
memory.

## Actions

1. Identify the repeated unit.
2. Decide whether a tiny script/check/codemod is cheaper than manual repetition.
3. Make the tool deterministic and easy to rerun.
4. Print concise output that a reviewer can inspect.
5. Use the tool as evidence.

Do not build a framework when one command or script is enough.
