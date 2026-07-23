# Through-line

Every principle is one move wearing different clothes:

> **Push correctness out of human vigilance and into the structure of the system.**

Types, schemas, ownership, boundaries, atomic steps, deadlines, tests,
reproducible runs, and explicit process where code runs out. The wrong thing
should be hard to express.

## When ideas conflict

Do not average. Choose by:

1. **Objective** — what must be true when done  
2. **Input owner** — yours vs caller/attacker/provider/clock/operator  
3. **Blast radius** — how wide if wrong  
4. **Reversibility** — can the client-boundary effect be undone  

If blast is wide and input is foreign, pay cost now.  
If blast is contained and input is yours, you may defer — write down why.

## Common tensions (pick a side when both light up)

| Tension | Stricter when | Lighter when |
|---|---|---|
| Bound everything vs YAGNI | caller-controlled growth, security, cost, fan-out | local trusted input, cheap failure |
| Unrepresentable states vs dynamic reality | crosses modules, persistence, external contracts | throwaway local transform |
| Locality vs one source of truth | duplicated truth would drift | single authority creates unreadable distance |
| Fail fast vs degrade | continuing hides corruption | reduced mode helps users with clear signal |
| Consistency vs availability | money, auth, deletion, safety invariants | stale/partial data OK and visible |
| Reversibility vs duty to forget | rollback needed and allowed | erasure/privacy duty dominates |
| Seams vs simplicity | tests/adapters need a seam | seam is only indirection |

## 2am reader

Write for the person paging at 2am who knows less than you know now.  
Make the right thing easy. Never make them hold what structure could hold.
