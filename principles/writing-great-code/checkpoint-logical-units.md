# checkpoint-logical-units

Before long runs or fragile context, preserve completed verified units.

Use for multi-hour work, broad migrations, generated artifacts, browser/iOS QA,
subagent arenas, and work likely to survive interruption.

## Actions

1. Divide work into logical units and reserve deadline/context budget for proof,
   cleanup, and handoff.
2. Verify each unit before moving on.
3. Record unit/criterion state, proof paths, classified scope discoveries, and
   active resources with cleanup state.
4. Stage or commit only when the user/workflow permits.
5. On interruption, stop dispatch, preserve the partial unit without claiming it
   complete, and record exact resume conditions, replay gate, and first action.

The next agent should know what is done, what is live, and what remains.
