# Self-improvement loop

Use this with `self-improvement-boundaries.md`. This file is the lifecycle;
that file is the doctrine and anti-sprawl gate for edits to the loop's own
machinery.

When repo-local agent session evidence exists, treat it as mining input:
raw transcripts stay native/gitignored by default, while redacted summaries
and indexes expose friction, slow commands, user steering, and improvement
candidates.

## Loop

1. **Notice** — user steering, missing setup, missing diagnostics, late CI/QA
   failure, workaround temptation, unclear docs, flaky/slow command, session
   evidence, or artifact sprawl.
2. **Classify** — one-off, recurring/high-impact, obvious small fix, reusable
   learning, missing setup/diagnostic/check, or sprawl/duplication.
3. **Act** — prefer delete/consolidate, then edit existing canonical surface,
   then add to existing setup/doctor/ci/lint/test/review path. Add a new surface
   only if `self-improvement-boundaries.md`'s constraints and the ablation
   gate below pass.
4. **Prove** — capture trigger, changed surface, discovery path, command/check,
   anti-sprawl decision, and residual.
5. **Recall** — route reusable lessons to a lessons store; route harness gaps to
   the repo's work queue (`docs/work/queue.md` when present, otherwise
   `docs/agent-friction.md`) or the owning canonical surface.
6. **Prune** — repo-setup/cleanup passes periodically close stale friction entries,
   merges duplicates, deletes or archives stale docs, and consolidates one-off
   harness artifacts.

## Ablation before you keep it

A harness component (a rule, a check, a doc, a wrapper) earns its place by
paying its way, not by having once seemed useful. When a component's value is
unclear, ablate it: remove or disable it, re-run the representative tasks or
benchmark, and keep the removal if nothing degrades. This is the honest test for
both directions — before adding a component, and before trusting one that is
already there. Periodically ablate the harness rather than only ever adding to
it; monotonic addition is how instruction files and check suites bloat into
sediment. agent-ergonomics optimization passes are a natural place to run this against
real fresh-agent probes.

## Routing table

| Signal | Route |
|---|---|
| Missing repo setup / doctor / config | repo setup / commissioning pass |
| Missing diagnostic, test, linter, docs, or script in current scope | build-with-proof pass |
| QA uncovered missing fixture/evidence/setup | QA pass, then build or setup |
| CI caught what local gates missed | PR/publish pass routes a local-gate improvement |
| Release friction or missing smoke/rollback/observe | land/release pass routes harness improvement |
| Review finding should be prevented mechanically | review pass routes prevention, not only a finding |
| Reusable lesson from solved work or mined session evidence | lessons store / compound pass |
| Sprawl, duplicated docs/scripts/flags | setup/cleanup pass (sprawl lens) |

## Completion invariant

Every non-trivial run should end with one of:

- durable improvement made and proven;
- reusable lesson compounded;
- friction residual filed with owner/surface;
- explicit `nothing to compound/improve` rationale.
