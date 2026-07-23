# trace-the-shadow-paths

Every data flow has a happy path and three shadow paths: nil input, empty
input, and upstream error. A plan that traces only the happy path is untested
thinking.

Use when reviewing a plan's data flow, designing a new flow, or writing
acceptance criteria for one.

## Actions

1. For each flow, trace all four paths explicitly: happy, nil, empty,
   upstream-error.
2. Name what the user or consumer observes on each shadow path — silence is
   not an answer.
3. Turn each shadow path into an acceptance criterion or test, not a comment.
4. Where a shadow path is genuinely impossible, record why (the type system,
   the schema, the caller contract) instead of skipping it.

## Evidence

The traced paths appear in the plan/review/criteria with their observable
outcomes.

## Failure Smells

- A sequence diagram with no failure arrows.
- Error handling that logs and continues with no user-visible state.
- "That can't happen" without the mechanism that makes it impossible.
