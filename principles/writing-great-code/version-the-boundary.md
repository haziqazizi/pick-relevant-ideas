# version-the-boundary

Name and version contracts that callers depend on.

Use for APIs, CLIs, schemas, events, generated artifacts, config files, browser
protocols, and mobile bridge payloads.

Breaking a boundary without naming the version is a hidden migration.

Hyrum's Law sets the bar: with enough consumers, every observable behavior of
the boundary — documented or not, including error text, ordering, and timing —
becomes a contract someone depends on. Passing tests do not prove a change is
non-breaking: tests cover the documented contract, consumers depend on the
observed one. A "patch" that changes behavior consumers relied on is a major
version wearing a disguise. When unsure whether a change breaks the boundary,
assume it does.

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
