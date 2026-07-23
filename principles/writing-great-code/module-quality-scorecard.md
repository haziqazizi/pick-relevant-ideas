# module-quality-scorecard

A per-module quality grade that persists across sessions, so "which part is
weakest, and are we getting better or worse" is answerable from the repo — not
re-derived each run.

Use when a repo is large enough to have distinct modules/domains and work spans
many sessions (continuous improvement or setup readiness).
Skip for a single small surface — one run's scoring is enough there.

Per-run scoring (e.g. deep-sweep prioritization) ranks
*this* batch; it is ephemeral. The scorecard is the **standing, trended**
counterpart: a durable artifact updated over time whose job is to point the next
session at the lowest-graded module first.

## The artifact

A durable file (e.g. `docs/quality-score.md`), one row per module/domain/layer,
each graded **A–D** on:

- **Verification status** — how much of the module is proven by executable
  checks vs unverified.
- **Agent legibility** — can a fresh agent understand and safely change it from
  repo contents alone?
- **Test stability** — flaky/absent vs reliable.
- **Boundary enforcement** — are its interfaces and invariants mechanically held?
- **Key gaps** — the one or two things dragging the grade down.

## Actions

1. Grade each module A–D on the dimensions above; record the date/commit so
   grades are comparable across runs.
2. Prioritize the lowest-graded module for the next improvement pass.
3. Re-grade after a change; a grade that dropped is a regression to surface, not
   bury (`fix-loop-self-regulation.md` close-out).
4. Keep it honest and coarse — letter grades, not false-precision numbers.

## Failure smells

- Every module graded the same (the scorecard is decorative, not measured).
- Grades never change run to run (nobody is re-grading; it has gone stale).
- A high grade next to a module with no executable verification.
