# process-is-structure

When code cannot enforce a property, make the process explicit and auditable.

Use checklists, generated artifacts, scripts, dry-runs, or review gates for
properties that live outside code.

Do not rely on invisible discipline when a lightweight structure would hold.

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
