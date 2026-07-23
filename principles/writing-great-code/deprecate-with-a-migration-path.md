# deprecate-with-a-migration-path

Whoever removes a surface owns its consumers' path off it.

Use for removing APIs, flags, schemas, endpoints, modules, or behavior that
anything else still consumes.

Before deprecating, answer: does it still provide value; who still consumes it
(count them); does a replacement exist; what does migration cost each
consumer; what does keeping it cost.

Rules:

- Default to advisory deprecation. Force migration only when maintenance cost
  or risk justifies it — and a forced migration ships with a working
  replacement, migration steps, and support, not just a deadline.
- The owner migrates the consumers, or ships a backward-compatible update that
  needs no migration. Announcing deprecation and walking away is abandonment,
  not deprecation.
- Unowned-but-consumed code gets an owner or a removal plan — never limbo.
  Detect it against the repo's own baseline: dormant relative to normal commit
  cadence, failing tests nobody fixes, dependencies nobody updates.
- Prefer incremental migration shapes — strangler (the new path grows around
  the old), adapter (the old interface over the new implementation), or
  flag-gated switchover — per `incremental-over-revolutionary.md`. The old
  path dies last, after evidence the new path carries the load.

## How To Use This Principle

Use this file after `selection.md` selects it for the task. Do not
apply it as a slogan. Convert it into specific work.

1. **Name the trigger.** State what in the current task made this principle relevant.
2. **Name the risk.** Describe the failure this principle is preventing.
3. **Choose a concrete move.** Add a check, boundary, artifact, refactor, timeout,
   proof, cleanup, diagram, or stop gate.
4. **Apply before acting.** Use the principle to shape the plan or implementation,
   not only the final report.
5. **Verify the result.** Show the command, artifact, screenshot, trace, diff, or
   review finding that proves the move happened.
6. **Report only if material.** Mention this principle in the final report only
   when it changed a concrete decision.

## Evidence To Leave

Leave at least one of these when the principle affects the task:

- changed file path and rationale
- command output or test name
- browser/device artifact path
- generated report or checklist row
- explicit skip reason
- named residual risk

## Failure Smells

The principle was not really applied if:

- it appears only as a decorative final-report bullet
- no action, check, artifact, or stop gate changed
- the same risk remains hidden in the system
- a future agent would need to rediscover the same fact from scratch
