# systems-over-heroes

Design for a tired on-call human at 3am, not the best engineer on their best
day.

Use when reviewing or designing operational surfaces: alerts, runbooks,
recovery paths, failure handling, or anything someone must operate under
stress.

## Actions

1. Ask of every operational path: could a competent stranger, tired and under
   pressure, execute this correctly from what is written down?
2. Replace steps that require heroics (tribal knowledge, judgment calls at
   2am, remembering an incantation) with a script, a runbook line, or a
   safer default.
3. Make the recovery path more obvious than the failure was.
4. Knowledge that lives in one person's head is a defect in the system, not a
   virtue of the person.

## Evidence

The runbook/script/default that removes the hero dependency, or the finding
naming it.

## Failure Smells

- A recovery procedure that only its author has ever run.
- Alerts that require interpretation before action.
- "Ask X" as a step in any operational path.
