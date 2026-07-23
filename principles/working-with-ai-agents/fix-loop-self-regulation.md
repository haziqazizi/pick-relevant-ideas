# Fix-Loop Self-Regulation

Single source of truth for how an iterative fix loop — a run that applies many
small fixes in sequence (polish passes, audit-driven optimization, finding
remediation) — keeps itself honest, reversible, and bounded. A fix loop
without a budget quietly degrades into an unreviewable mega-change.

## Preconditions

- **Clean tree in.** Start from a clean working tree (or an explicitly
  recorded baseline commit) so every fix is separable from pre-existing work.
  If the tree is dirty, stop and resolve it with the user (commit, stash, or
  abort) before the first fix.
- **Baseline out in front.** Capture the baseline state the loop will be
  judged against — scores, screenshots, failing findings — before fix one.

## Loop contract

- **One fix, one commit.** Each finding gets its own atomic commit with the
  finding's identifier in the message. Never bundle fixes; a bundled commit
  cannot be reverted without collateral.
- **Minimal fix.** The smallest change that resolves the finding. No drive-by
  refactors, no "improving" unrelated code mid-loop — a discovered unrelated
  issue becomes a new finding, not a rider.
- **Correctness before performance before style.** Prove functional correctness
  first; only then optimize; touch style last. Reordering — polishing or
  optimizing code whose correctness is not yet proven — shifts the
  verified/unverified boundary and silently breaks paths that were passing.
- **Verify each fix at its surface.** Re-test the affected surface after each
  fix (re-capture the screenshot, re-run the focused check) and classify:
  `verified`, `best-effort` (applied but not fully verifiable — say why), or
  `reverted`.
- **Revert on regression, immediately.** A fix that makes things worse is
  reverted the moment the regression is seen, and its finding is marked
  deferred with the observed failure — not retried in place with a bigger
  patch.

## Risk budget

Track a running risk score and stop to check in when it crosses the line —
the loop self-regulates instead of asking the user to babysit it:

```text
risk starts at 0
+15  each revert
+5   each non-trivial structural/behavioral file change (vs. a safe local fix)
+20  any touch outside the finding's predicted footprint
+1   per fix beyond the tenth
```

- **Over ~20: stop and check in.** Show what was done so far and ask whether
  to continue (interactive), or stop the lane and record the residual
  (autonomous).
- **Hard cap.** Set a maximum fix count for the run (default ~30) and stop
  there regardless of remaining findings — remaining work is handed off as a
  deferred list, not silently continued.

## Close-out

- **Re-audit against the baseline.** After the loop, re-check the surfaces
  against the captured baseline. If the end state is *worse* than the
  baseline on any tracked measure, warn prominently — never bury a net
  regression in a success summary.
- **Deferred findings survive.** Findings not fixed (deferred, reverted,
  out-of-reach) land on the repo's TODO surface or the run's durable
  artifact with enough context to resume — a dropped finding is a silent cap.

## What this does not change

The retry/stop rule in the skill template still binds (the same failure twice
without new information stops the lane). Stop gates and review requirements
are unchanged: a fix loop's commits still go through the normal review and
delivery gates before publication.
