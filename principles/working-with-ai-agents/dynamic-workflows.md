# Dynamic workflow contract

Use this shared contract when a skill needs more than one straightforward pass. The
point is not to apply personas by default; it is to choose the smallest workflow
topology that can satisfy the outcome and expose the evidence.

When a topology dispatches lenses, reviewers, graders, scouts, or subagents, use
`subagent-dispatch.md` for the DispatchPlan and result ledger. If subagents are
unavailable, run the same rows inline and label the evidence limit.

## Topology ladder

Pick one topology up front, state the trigger, and record skipped heavier modes
with one-line rationale when the work is non-trivial.

| Topology | Use when | Gate |
|---|---|---|
| Inline | tiny, mechanical, low-blast-radius work | deterministic proof or self-check passes |
| Single reviewer | small work where one fresh context can catch likely misses | reviewer returns PASS or only residualized findings |
| Classify-and-act | inputs need routing before work begins | classifier names route, confidence, and skipped routes |
| Fan-out-and-synthesize | many independent surfaces or lenses need coverage | all branches return structured outputs; synthesis dedups and routes findings |
| Generate-and-filter | ideation/design/naming needs options and a rubric | candidates are deduped; winners explain rubric fit |
| Tournament | several plausible approaches compete on the same problem | judge chooses a winner against explicit criteria |
| Arena synthesis | several plausible artifacts or designs could each be valid | parent picks one base, grafts only the strongest rejected ideas, and verifies the synthesized result |
| Adversarial verification | high-stakes claims need refutation | verifier/skeptic cannot disprove required evidence |
| Loop-until-done | pass/fail feedback can drive bounded iteration | `max_iterations` or `retry_cap` reached; no infinite loops |

## Selection rules

- Start with the cheapest topology that can catch realistic failure modes.
- State the workflow mode before planning substantial work: `existing-code`
  (start from caller behavior and current seams), `greenfield` (domain terms +
  thin production-shaped tracer bullet), or `complex-existing-codebase` (map
  ownership, entrypoints, callers, and verification before refactoring).
- Use dynamic dispatch predicates from the task surface: diff paths, actors,
  data boundaries, auth/permissions, UI visibility, money, deployment, docs, and
  external integrations.
- Fixed persona panels require an always-on gate and a written reason. Otherwise
  dispatch only lenses whose scope is present.
- For fan-out, tournament, adversarial, and reviewer modes, write a
  `subagent-dispatch.md` DispatchPlan before running lenses and a result ledger
  before synthesis.
- For arena-style lanes, give every candidate the same task contract and rubric,
  require separate output paths, run the judge only after candidate outputs are
  complete, then record the base choice, grafts, rejections, dropouts, and
  verification result. If candidates diverge wildly, reframe instead of
  averaging incompatible designs.
- Keep branch outputs structured enough to synthesize: findings need `severity`,
  `confidence`, `location`, `category`, `summary`, `evidence`, and `fingerprint`
  per grader-discipline norms.
- High-stakes lanes are security, data integrity, money, privacy, migrations,
  launch/release gates, and irreversible operations. These require independent
  grading and, when appropriate, an adversarial skeptic.
- When subagents are unavailable, run the chosen lenses inline, keep notes
  separated by lens, and label the evidence limit.

## Loop discipline

- `retry_cap` bounds stage retries and fix attempts.
- `max_iterations` bounds outcome/grader loops; the default is 7 and the hard cap
  is 20 unless a repo config sets stricter limits.
- From iteration 1 onward, delta re-grade failed criteria fully and regression
  scan passed criteria unless the artifact was restructured.
- If two consecutive passes fail the same criterion for the same reason, stop and
  fix the rubric/feedback or file a residual. More loops are waste.

## Output discipline

Every dynamic workflow reports:

```text
Topology:
Why this topology:
Caps: retry_cap=<n>, max_iterations=<n if relevant>
Branches/lenses run:
Branches/lenses skipped:
Synthesis decision:
Residuals:
```

Do not hide the topology inside chat reasoning; it is part of the artifact a
future grader needs to understand the run.
