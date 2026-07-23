# incremental-over-revolutionary

Strangler fig, not big bang. Make the change easy, then make the easy change.

Use when a plan proposes a rewrite, a large refactor, a migration, or any
change whose diff cannot land in reviewable increments.

## Actions

1. Prefer refactor over rewrite unless the foundation is genuinely broken —
   and when it is, say "scrap it and do this instead" plainly rather than
   hedging.
2. Slice revolutions into increments that each land, prove, and revert
   independently (new path grows alongside old; traffic moves gradually;
   old path dies last).
3. Never travel structural and behavioral changes in the same step: first the
   refactor that makes the change easy, then the easy change.
4. If an increment cannot be verified on its own, it is sliced wrong.

## Evidence

The plan shows the increment sequence and what proves each step, or records
why a true big-bang was unavoidable.

## Failure Smells

- A migration whose first verifiable checkpoint is "everything is moved."
- Refactor and feature change in one commit/PR.
- A rewrite justified by discomfort rather than a named broken invariant.
