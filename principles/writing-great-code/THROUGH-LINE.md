# Principle Through-Line

Every principle is one move wearing different clothes:

Push correctness out of human vigilance and into the structure of the system.

Use types, schemas, ownership, boundaries, atomic steps, deadlines, tests,
reproducible runs, and explicit process where code runs out. The wrong thing
should be hard to express:

- the illegal state cannot be built
- the hostile input cannot get in
- the irreversible act cannot fire untested
- the clock cannot lie without being caught
- the promise does not go unkept because someone remembered

## The Objective

When principles pull against each other, return to this objective:

Cut down what a tired engineer or bounded-context model must hold in mind while
keeping a bounded blast radius around whatever an attacker, caller, page,
provider, queue, clock, or unlucky operator controls.

If the blast radius is wide and the input belongs to someone else, pay the cost
now. If the blast radius is contained and the input is yours, you may defer, but
write down why.

## Common Tensions

No slogan settles these. Choose by objective, blast radius, ownership, and
reversibility.

| Tension | Choose the stricter side when | Choose the lighter side when |
|---|---|---|
| Bound everything vs YAGNI | caller-controlled input, cost, security, queue, or fan-out can grow | local trusted input and failure is cheap |
| Unrepresentable states vs dynamic-language reality | data crosses modules, persistence, or external contracts | throwaway local transform with narrow proof |
| Locality vs one source of truth | duplicated truth would drift silently | single authority would create unreadable distance |
| Strict parse vs tolerant read | accepting bad input creates ambiguity, security risk, or data corruption | compatibility requires reading old/foreign data safely |
| Fail fast vs degrade | continuing hides corruption or unsafe state | users/operators benefit from reduced mode and clear signal |
| Consistency vs availability | money, auth, deletion, safety, or invariants are at stake | stale/partial data is acceptable and visible |
| Reversibility vs duty to forget | rollback is needed for safety and does not retain forbidden data | erasure/privacy/legal duty dominates rollback convenience |
| Seams vs simplicity | tests, adapters, or provider isolation need a seam | seam would only add indirection |

## 2am Reader Rule

Write for the person reading at 2am with a pager going off, who knows less than
you know now.

Make the right thing easy. Make the wrong thing hard to express. Never make them
hold in their head what the code, artifact, test, boundary, or process could
have held for them.

## Lineage

This doctrine follows the broad engineering lineage named in Shape of the
System: programs written for people to read, complexity as cognitive load,
essential versus accidental complexity, correctness in system shape rather than
vigilance, values expressed as tradeoffs, pit of success, least privilege, trust
boundaries, CAP, fail-fast, YAGNI, tolerant-read/strict-write traditions, DRY,
illegal states unrepresentable, and the duty to forget.
