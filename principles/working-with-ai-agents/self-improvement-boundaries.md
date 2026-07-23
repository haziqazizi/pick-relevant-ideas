# Self-Improvement Boundaries

Use this with `self-improvement-loop.md` and `verification-and-autonomy.md`.
The first is the notice→prune lifecycle; the second owns the evidence
hierarchy and autonomy tiers, and this file repeats neither. It owns one
question they leave open: when a loop improves the thing that does the
improving — a rubric, a grader prompt, a gate, a judge-facing skill — what may
change and what must not.

Read it before sharpening graders, editing a judge-facing skill, or letting a
campaign fold learnings back into its own machinery.

## 1. The judge stays outside the modification boundary

A self-improving loop may change how it searches and probes: lenses, prompts,
prompt overlays, gates, telemetry requirements, probe order, batch selection.
It may never change what counts as passing: acceptance criteria, the evidence
hierarchy, autonomy tier gates, held-out sets, or the keep/revert rule of the
very run doing the modifying.

The published self-improvement systems split exactly on this line: the ones
that compound (Bilevel Autoresearch, HyperAgents/DGM) freeze the judge and
let everything else evolve; the one that let the agent rewrite its own
acceptance logic (Gödel Agent) is the cautionary tale — maximal
self-reference, weakest control against self-dealing. Before the first
self-edit, state the boundary explicitly in the ledger or contract: name what
is mutable and what is frozen.

## 2. Protected constraints

Harness and grader evolution may only strengthen evidence integrity. A change
whose effect is to raise pass rates, soften a bar, skip a probe, or polish the
appearance of compliance is self-dealing, not improvement — the meta-layer
sibling of the verifier tampering that `adversarial-hardening.md` teaches
graders to catch in workers. If a proposed grader change would make the
current batch pass where it failed, that change is Tier 3 by definition: stop
for a human.

## 3. Three depths of self-modification

Name the depth before making the change; each depth binds to a gate that
already exists. Do not invent new gates.

| Depth | Example | Gate |
|---|---|---|
| Artifact change | a campaign batch edits product code | the loop's own keep/revert rule (`verification-and-autonomy.md` §3) |
| Mechanism tuning | reweighting a rubric, adding a lens, widening a probe catalog | calibration capture (`verification-and-autonomy.md` §4): the tune must trace to an observed override, miss, or stall — never to taste |
| Mechanism rewrite | editing a grader/judge-facing skill or a gate's logic | full blind re-eval of ALL golden cases before the rewrite ships |

Depth resolves upward on doubt, like autonomy tiers: a "tuning" change that
alters which artifacts pass is a rewrite, and a "rewrite" that alters what
counts as passing crosses section 1 and stops for a human.

## 4. Hold out part of the bar

Across repeated grading cycles, hold out or rotate part of the bar per the
operational rule for grader discipline (Finding
contract, rule 13) — that rule, not this file, carries the mechanics.

## 5. Predict before you run

A loop that only ratchets — keep what scored better — learns nothing from its
wins. Before an improvement runs, record the predicted outcome: direction and
rough size. Afterward, compare. A miss is a calibration asset even when the
change was kept: it means the loop's model of the repo is wrong somewhere,
and that belongs in a durable lessons store. Prediction error
never gates keep/revert — outcomes decide what ships; predictions decide what
the loop learns.

## The one rule

Improve the search, never the scoreboard: declare what is frozen before
editing your own machinery, resolve depth upward on doubt, hold out part of
the bar, predict before you run — and treat any self-edit that flips a
failure into a pass as a stop, not a win.
