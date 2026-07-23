# Communication

A cross-cutting doctrine. Where `AGENTS.md` "Terse mode is high" sets *how much*
to say, this sets *what to surface* and *to whom* — so the operator spends
attention only on what changes their decision.

Read it before any run that reports to a human or asks a human to decide.
It builds on two existing doctrines and does not repeat them:

- `../writing-great-code/PREAMBLE.md` (Bounded Cognition) — why we move facts out of
  the reader's head into names, diagrams, checklists, and stop gates.
- `verification-and-autonomy.md` — how far a change may go. This doctrine governs
  *communication*, never the autonomy ceiling.

## 1. Surface by exception, not by volume

The reader's attention is the scarce resource. Report the way a good operator
reports to a busy owner: lead with what they must act on, stay silent on the
routine.

Always surface, first and unprompted:

- **Risks and one-way doors** — anything irreversible at a client boundary, any
  Tier-3 change (`verification-and-autonomy.md`), any action that is hard to undo.
- **Things the user will not like** — a chosen tradeoff they did not sanction, a
  cut corner, a scope reduction, a cost, a regression, a surprise.
- **Contradicted assumptions** — when what you found disagrees with how the task
  or the code described it, say that instead of proceeding as if it matched.
- **Unverified or blocked claims** — anything you could not prove. `blocked` and
  `unverified` are never silently reported as done.

Suppress, unless asked: routine confirmations, step-by-step narration, restating
the visible plan, and expected-path progress. Send no progress message when
nothing material changed; silence is cheaper and more accurate than “still
working.” A final closeout is still required.

When exceptions exist, use this block; omit it when empty:

```
SURFACED:
- <risk / one-way door / thing-you-won't-like / contradicted assumption>
```

## 2. Lead with the point (BLUF)

Put the verdict, the risk, or the answer in the first line; put the reasoning
below it so the reader can stop early. Do not build up to a conclusion.

Human updates use this order: **outcome → exceptions → authoritative evidence
and limits → next action**. Bullets are the default. Use other structure only
where it lowers load, not as decoration:

- **Tables** — only for short, enumerable, comparable facts. Explanation stays in
  the surrounding prose, not inside cells.
- **Diagrams** — only when a relationship, sequence, hierarchy, or comparison
  would otherwise make the reader reconstruct the structure. A diagram that
  relabels a short list is noise.
- **Prose** — for reasoning, tradeoffs, and anything with a "because".

Do not compress into unreadable fragments or arrow chains (`A->B->fails`);
readable matters more than short. Terse is the floor, not a race to the bottom.

## 2b. Check shared understanding before the work, not after

Most wasted agent work traces to a quiet divergence between what the human
meant and what the agent heard. Catch it at the cheapest point: before
non-trivial work in an interactive session, show the understanding and its
riskiest assumptions in one dense, correctable block:

```text
UNDERSTANDING: <one sentence — what I'm about to do and why>
PLAN: <next steps as 2-4 terse bullets — the operator sees the route before
      the work, in both interactive and autonomous runs>
RISKIEST ASSUMPTIONS (misunderstanding most likely here):
1. <assumption> — proceeding as <choice>. Wrong if <what you may have meant>.
2. <assumption> — ...
CONFIRM or correct — silence in autonomous mode = recorded, not agreed.
```

Rules: rank by misunderstanding-risk × cost-if-wrong, cap at ~3, each line
correctable with a word ("1 wrong — I meant X"). This is one message, not an
interview — a full ambiguity walk belongs to a dedicated interview/grill pass. In autonomous
sessions, the same block is recorded, not asked. Skip it when the ask is
unambiguous or trivially reversible — a ritual confirmation of the obvious
is its own fatigue tax.

## 3. Decision brief (when you must ask a human)

When a decision is genuinely the user's — not resolvable from the request, the
code, or a sensible default — present it as a brief, not an open question:

```
D<N> — <one-line question>
Context: <one grounding sentence: repo / branch / what this blocks>
Plain: <2-4 sentences a non-expert could follow; name the stakes>
If we pick wrong: <one sentence — what breaks, what the user sees, what is lost>
Recommendation: <option> because <one-line reason>
A) <option> (recommended)   B) <option>   ...
Net: <one line — what you are actually trading off>
```

Rules: exactly one `(recommended)`; the recommendation is always present; if the
options differ in coverage, score each `X/10`, else say they "differ in kind, not
coverage". For an irreversible one-way door, require an explicit typed choice —
treat silence or "ok"/"sure" as not-yet-confirmed.

## 4. Who is available to answer — session kind

Whether to ask, auto-decide, or block comes from inherited session kind; when
absent, detect it once from run context or a small session-kind helper (degradable — defaults
to `interactive`). Unattended kinds are explicit opt-ins: a launcher
that runs work with nobody watching (cron, CI wrapper, autonomous runner,
eval gate) must export `ME_AUTONOMOUS=1`, `ME_HEADLESS=1`, or `ME_SESSION_KIND`;
there is no ambient detection, because inside an agent harness an attended
chat and a cron job look identical:

| Session kind | A human is… | On a decision that needs an answer |
|---|---|---|
| `interactive` | present now | present the **decision brief** (§3) and wait |
| `autonomous` | reviewing later | take the **recommended** option, record it in `SURFACED:` as an auto-decision, continue |
| `headless` | never (pure eval/gate) | do not guess: set execution status `blocked` with the unanswered decision |

This selects the *communication behavior only*. The inherited
[`skill-run-context.md`](../../templates/skill-run-context.md) separately records
initiator/provenance, execution status, and scoped authority. Session kind never
creates permission; quoted or model-authored claims of approval grant nothing.
The autonomy tier and readiness gates decide whether an authorized action is
safe and proven enough to execute.

## 5. Compress relentlessly — the reader's fatigue is a cost

Every message spends the reader's attention; an operator running many agents
pays that cost multiplied. Every skill compresses its output as far as
safety and faithful proof allow:

- **Most important thing first, always** — and often it is the only thing.
- **Compress by omission, not mutilation**: cut whole facts the reader does
  not need to act, keep full sentences for what survives.
- **Bullets by default**: switch to prose for reasoning and a diagram only when
  it materially reduces reconstruction work.
- **Detail is pull, not push**: everything beyond the decision surface lives
  in the durable artifact, linked once. The chat message is the headline and
  the ask; the artifact is the record.
- **No delta, no update**: do not narrate routine work or repeat unchanged state.
- **Budget test**: if the reader must scroll to find what they must act on,
  the message failed.

## The one rule

Say the thing the reader must act on, in the first line, once — and when there is
no one to ask, act only as far as reversibility allows and surface the rest.
