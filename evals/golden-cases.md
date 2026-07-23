# pick-relevant-ideas — golden cases

Standalone pack: all principle bodies must resolve under `principles/` in this
repo. Two-part bars: **Coverage** (must include) and **Verification / no-fire**.

## Case 1 — auth middleware (graph neighborhood)

Input:

```text
Pick relevant ideas before we change JWT middleware that verifies tokens
and attaches a principal to the request. Don't implement.
```

Coverage:

- Facets include something like `auth` and/or `external-input`
- Seeds include at least one of: `trust-boundaries`, `least-privilege-access`, `structural-safety-boundaries`
- Expanded/selected set includes boundary-domain ideas (e.g. `boundary-discipline`, `data-shape-discipline`, `make-illegal-states-unrepresentable`) when gate passes — not necessarily the whole cluster
- Every selected id has a concrete approach bind
- ≤7 selected; no implementation

Verification / no-fire:

- Does not ship code or a full security audit verdict
- Does not auto-select entire `boundary-to-valid-domain` cluster without gate
- Does not treat tension edges as “take both”

## Case 2 — new check script (CLI cluster)

Input:

```text
Which great ideas apply before I add a repo check script wired into npm test?
Principles only — no code.
```

Coverage:

- Facets include `cli-script` and/or `repeated-work` / `generated-artifacts`
- Seeds touch `agent-friendly-cli` or `non-interactive-first` or `single-purpose-checks`
- Binds mention non-interactive, actionable errors, stable exits/paths, or reproducibility as approach changes
- ≤7 binds

Verification / no-fire:

- Does not dump all of `automation-cli`
- Does not pivot into implementing the script
- Does not force auth/security cluster

## Case 3 — open API design (design, not disaster)

Input:

```text
We're choosing the shape of a new public API. Pick relevant ideas only —
no endpoint list yet.
```

Coverage:

- Facets include `open-design` (and maybe `schema-lifecycle`)
- Seeds/selection can include `exhaust-design-space`, `version-the-boundary`, `pit-of-success`, `simplicity-budget` or neighbors via graph
- Framing is relevance/approach, not only “what could go wrong”
- Tensions (e.g. exhaust vs prefer-existing) resolved with a side + reason if both appear

Verification / no-fire:

- Does not produce the API design itself as DONE
- Does not select only hazard/auth ideas unless user mentioned them

## Case 4 — near-miss: wants a review verdict

Input:

```text
Review this auth diff and tell me if it's safe. Mention principles if useful.
```

Coverage:

- Should **not** treat pick-relevant-ideas as the owning deliverable
- May briefly note ideas a review should use, subordinate to “this is a review request”
- No standalone principle-pass claimed as DONE

Verification / no-fire:

- No fabricated safety verdict from this skill alone
- No full graph expand presented as the answer to “is it safe?”

## Case 5 — rename private helper (thin selection)

Input:

```text
Pick relevant ideas for renaming a private helper for clarity. Tiny change.
```

Coverage:

- Few or even zero principles is OK
- If any: naming/reader-load cluster (`name-to-reveal`, `minimize-reader-load`) — not auth/time/proof dumps

Verification / no-fire:

- Fails if ≥5 ideas selected for a rename
- Fails if security or migration clusters appear without cause

## Trigger probes

Should trigger:

- “Principles first for the webhook adapter; don’t plan yet.”
- “Which ideas should govern this refactor?”
- “Pick relevant ideas before we start.”

Should not trigger as owner:

- “Fix the failing test.”
- “Implement the middleware.”
- “Is this PR safe?” (review)
- “What should we build?” (product direction without doctrine ask)
