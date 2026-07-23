# exec-plan

Single source of truth for durable multi-session state: the **ExecPlan**, a
git-tracked file that carries a unit of work across sessions, agents, and context
compaction. The concept is referenced from many skills and templates; this file
is the one definition they all point at.

Context is finite and a long task will span sessions. Compaction keeps the
"what" (the diff) and loses the "why" (the rationale and the rejected paths).
The repo is the system of record: what a fresh session cannot read from the repo
does not exist for it. The ExecPlan is where the "why" and the live "what's left"
survive.

This is the **default, in-repo** continuity mechanism: the lightweight
artifact every skill can write without any runtime installed. Do not build a
second state store when an ExecPlan will do.

External orchestrators may maintain runtime JSON, databases, or task boards for
mechanical state such as agent ids, retries, URLs, and handoff paths. Treat those
as runtime projections unless the host runner explicitly owns a richer authority.
When that happens, the ExecPlan links to the authority and names what it owns;
do not keep two competing live stores for the same decision or acceptance state.

## When to create one

- Work spanning more than one session or agent handoff.
- Multi-hour or multi-file work, or work that is risky or ambiguous.
- Interruptible or delegated work where a fresh agent must resume.
- Whenever the context-budget handoff trigger fires
  (`../writing-great-code/checkpoint-logical-units.md`, the skill template's
  Context Budget And Handoff rule).

Do **not** create one for tiny single-pass work — that is what the chat closeout
is for. One active ExecPlan per unit of work; never two plans for one unit.

## Location and lifecycle

- Live plans: `docs/exec-plans/active/<slug>.md`, git-tracked. Committing the
  plan is the point — it is the durable record, not scratch.
- On land: move to `docs/exec-plans/done/<slug>.md` (or delete if the contract
  and PR already carry the record). A stale active plan is worse than none —
  it misdirects a confident agent — so it is updated on every handoff or retired.
- `docs/exec-plans/active/` **is** the standing index of in-flight work: a fresh
  agent scans it to answer "what is in progress" without a separate project-wide
  status file (a second store would be the duplication this doctrine exists to
  avoid). Orientation passes read it first.
- The Decision Log is append-only and outlives the Progress section. When a plan
  is archived or deleted, its decisions (choice + rejected alternatives + why)
  must survive — fold them into the landed PR, the contract, or a durable lessons store.
  The mutable Progress state may be discarded; the "why" must not.

## Required shape

Keep it lean; deep detail lives in the artifacts it links (the execution
contract, evidence manifest, review verdict). The plan is the index, not a copy.

- **Status** — `active` / `interrupted` / `blocked` / `done`, and the current
  pickup point. `interrupted` means safely checkpointed, not failed or blocked.
- **Acceptance criteria** — the contract's criteria table, or a link to it,
  with each criterion's `not_started | active | blocked | passing` state
  (the gradeable contract). This is the single source of "what's left"; do not
  re-derive it from the conversation.
- **Progress** — Done / In progress / Next, with logical-unit boundaries.
- **Interruption state** — deadline/context signal and handoff reserve; classified
  scope discoveries; active resources with cleanup/owner/status; authoritative
  proof paths; exact resume conditions, stale-sensitive gate, and first action.
- **Decision Log** — `decision | rejected alternatives | why`. This is the part
  compaction destroys; it is the reason the plan exists.
- **Blockers** — open questions and what would unblock each.
- **Validation** — the exact commands and observable acceptance.

## Reads and writes

- Orientation reads the active ExecPlan **first**, before re-deriving state from
  git — a persisted plan turns orientation into a cheap clock-in read.
- Build and end-to-end execution skills write/update it at each checkpoint, deadline
  reserve, and context-budget handoff, so a fresh agent resumes without the
  original conversation.
- The Session Exit Checklist requires the active plan to be current before any
  interrupt or handoff.

## Failure smells

- Two plans, or a contract and a plan, disagreeing about what is left.
- A plan that records what changed but never why — the next agent re-litigates
  settled decisions.
- A plan that went stale because nobody updated it on handoff.
- A skill re-deriving multi-session state from chat because no plan was written.
- “Resume work” with no target/resource validation, stale-sensitive replay gate,
  or exact first action.
