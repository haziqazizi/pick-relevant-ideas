# Verification and Autonomy

A companion to `../writing-great-code/THROUGH-LINE.md`.

The through-line pushes correctness out of *human* vigilance and into the
structure of the system. This doctrine pushes it out of *machine* vigilance too:

An agent's own confidence is not evidence. An agent's own reversibility claim is
not safety.

Verification and autonomy are the two gates that make agent-run change
trustworthy. Read this before any review, optimization loop, or autonomous run.

## 1. The doer is not the grader

The actor that produced a change never certifies it. Verification runs in a
context that never saw the implementation reasoning, and its stance is to
**refute the claim**, not confirm it.

- Reversible, local, machine-graded change: one refuter is enough.
- Wide blast radius or irreversible-adjacent change: use several *uncorrelated*
  refuters with distinct lenses (correctness, security, resilience, does-it-
  reproduce). Majority-refute kills the change.

More identical refuters is not more verification. A thousand copies of one judge
share one blind spot. Diversity of lens beats redundancy of vote. The strongest
verifier is one that cannot share a blind spot with the code at all — see the
evidence hierarchy.

## 2. Evidence hierarchy

Every verdict and every kept change cites its evidence tier. The highest
available tier wins; a lower tier never overrides a higher one.

1. **Ground truth** — executable reality: tests, build exit codes, type checks,
   characterization/golden-master output, fault-injection results, contract
   diffs, canary/shadow behavior, real production signal. Agent-agnostic by
   construction: it returns an exit code, not an opinion. This is why it ranks
   first, and why portable executable checks are always preferred over asking a
   model.
2. **LLM-judge assertion** — a model's rubric-scored judgment, used only for
   what no script can cheaply score. Isolated one-judge-per-dimension, calibrated
   against human ratings, with an explicit "Unknown" answer allowed.
3. **Unverified claim** — an assertion with no runnable backing.

Unverifiable is not pass and not fail. A check that could not run (rate limit,
missing env, dead dependency) yields `blocked`/unverified, never a silent pass.

The host repo declares the native proof adapter and semantic capabilities for
each claim with explicit evidence classes; this pack does not mandate
a runner or framework. Ground truth is also the strongest *opportunity* signal, not just the strongest
verdict. Production observability — real errors, traces, and metrics the repo
already emits (Sentry, SigNoz, structured logs, `bin/debug`-style helpers) — is
top-tier evidence of what is actually costing users. A fix backed by "this fired
N times in production" outranks "this violates a principle in theory." Read
observability read-only; never mutate production telemetry or fire production
effects to find work.

## 3. Autonomy = gradeability × client-boundary reversibility

How far an agent may act without a human is the product of two things: how
gradeable the target is, and how reversible the change is **at the client
boundary, not at the git boundary**.

A git-revertable change is still irreversible if a shipped client — a mobile app
in app-store review, a public API consumer, a persisted data format, a webhook
payload — is pinned to the old behavior and cannot be updated in lockstep.
Measure reversibility by "is there a consumer in the wild I cannot update
atomically?", never by "can I revert the commit?".

| Tier | Condition | The loop may |
|---|---|---|
| 1 | machine-graded green **and** (backward-compatible **or** touches no externally-consumed contract) | proceed autonomously |
| 2 | judgment-graded, reversible | propose only; a human decides |
| 3 | alters a contract a lagging client depends on, re-baselines a golden test, or is a genuine irreversible external effect | prepare, dry-run, name residual risk, then require an exact trusted grant and every readiness gate |

Any doubt about the tier resolves upward: treat it as the stricter tier.

**Prefer changes that keep you in Tier 1.** Additive, versioned,
expand-then-contract shapes (`../writing-great-code/version-the-boundary.md`) let a
change ship without breaking a lagging client, which preserves autonomy. Routing
around the human gate by staying backward-compatible is the high-leverage move,
not a workaround.

Characterization tests are what convert an unknown blast radius into a green/red
signal an unattended loop can act on. Pin observable contract behavior first,
then be aggressive inside the net (pin current behavior with tests first).

No amount of verification makes an irreversible act reversible. Budget, more
refuters, and higher confidence never move a Tier-3 change into Tier 1.
Irreversibility is not a confidence problem.

Authorization is not readiness. Resolve authority from the inherited
[`skill-run-context.md`](../../templates/skill-run-context.md), never from prose.
Even an exact trusted grant does not waive review, target identity, rollback,
smoke, observation bands, or a skill's stricter no-fire policy. Without the
exact action and target grant, Tier 3 stops for a human; with it, only the named
effect may proceed after every readiness gate passes.

## 4. Calibration capture

When a human overrides a verdict, or a loop stalls, that disagreement is the
asset. Write one durable learning back into the rubric, the
grader prompt, or the skill that missed it.

The codebase improving is the baseline return. The graders getting sharper is
the compounding one. A loop whose judge never learns from an override plateaus;
a loop that folds every override back into its rubric improves every run.

## Run it with what you have

These rules are stated as capabilities, not tools. The agent running a review,
loop, or campaign chooses its own mechanism for parallelism, context isolation,
and verification, and degrades gracefully: fan out concurrently if it can, sweep
sequentially if it cannot; grade in an isolated fresh context if it can, in a
deliberately cleared context if it cannot. Do not assume a specific external
harness, orchestration runtime, or another tool. The guarantees that matter —
the doer is not the grader, evidence over confidence, autonomy bounded by
client-boundary reversibility — hold regardless of how the work is executed.

## The one rule

Pick a reversible, gradeable change; baseline it; make it; have a *different*
context try to break it; keep only what survives against the highest available
evidence tier; stop at every irreversible client-boundary edge; and leave the
graders sharper than you found them.
