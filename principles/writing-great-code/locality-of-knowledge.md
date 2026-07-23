# locality-of-knowledge

Knowledge an agent needs must live where the agent will look — in the repo, next
to the code it governs.

An agent has three inputs: its instructions, the repo, and tool output. It
cannot ask Slack, a ticket, or a person. Knowledge that lives outside the repo
does not exist for it; knowledge buried far from the code it governs is rarely
found in time.

Use when placing architecture notes, constraints, or rationale, and when
onboarding or cleaning a repo (setup/commissioning pass).

## Actions

1. **Place docs next to the code they govern.** A short `ARCHITECTURE.md` or
   `CONSTRAINTS.md` in the module beats a long central doc a reader must know to
   open. The entry file (`AGENTS.md`) routes to them; it does not absorb them.
2. **Write hard rules as constraints, not prose.** For a security/data/API
   boundary, a module-local `CONSTRAINTS.md` in MUST / MUST NOT language is
   discoverable and checkable; a paragraph three files away is neither.
3. **Get external knowledge into the repo.** If a decision lives only in a chat
   or someone's head, capture the durable part in the repo before it is lost.
4. **Treat stale docs as worse than none.** A confidently-wrong doc misdirects;
   pair every durable doc with how staleness is caught (`one-source-of-truth.md`)
   or retire it.

## Failure smells

- A rule that only exists in conversation history or a reviewer's memory.
- Central docs no reader opens because nothing points to them from the code.
- A constraint stated as prose the agent skims past, not a MUST it must satisfy.
- A doc that drifted from the code and now misleads.
