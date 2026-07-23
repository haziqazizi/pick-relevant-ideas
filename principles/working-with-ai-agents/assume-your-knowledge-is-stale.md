# assume-your-knowledge-is-stale

An agent's built-in knowledge has a cutoff; the ecosystem does not. For
anything version-sensitive or fast-moving, confirm before relying on it.

Use when work depends on: a library/framework/tool API, CLI flags, pricing or
limits, provider behavior, a spec or protocol, "best practice" in a space that
moves, or any fact where being a year stale produces confidently wrong output.

## Actions

1. Bounded web search to confirm the load-bearing fact — current version,
   current API shape, current recommendation — before building on it. Rank
   sources: official docs/changelog/the repo itself > standards references >
   aggregated posts; forum answers, blog summaries, and the agent's own memory
   are never primary. Fetch the specific reference page (deep link with an
   anchor survives doc restructuring), not a homepage or a generic search.
2. When the subject is OSS and the docs are thin or doubtful: **clone the
   repo into a scratch/tmp directory and read the actual source** — the code
   is the current truth; ten minutes in the source beats an hour of stale
   guessing.
3. Version-pin the understanding: note which version/date the confirmed fact
   belongs to, so the next reader knows when it expires.
4. Scale to risk: a stable stdlib call needs no search; a provider SDK
   released last quarter always does. When search is unavailable, say the
   knowledge is unverified-from-memory rather than presenting it as current.

## Evidence

The confirmed fact carries its source (URL, repo path + commit, doc version)
in the output or artifact. When a non-obvious API choice lands in code, the
code carries the citation too (a short `Source: <url>#<anchor>` comment) so
the next reader does not re-derive it.

## Failure Smells

- Confident API usage from memory that 404s or takes deprecated flags.
- Designing against a library's year-old architecture.
- "Best practice" asserted without a date attached.
- Answering a question about a tool the agent has never actually opened.
