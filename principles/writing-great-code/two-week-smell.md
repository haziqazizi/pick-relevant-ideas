# two-week-smell

If a competent newcomer could not ship a small feature in this area within two
weeks, the plan is building on an onboarding problem disguised as
architecture.

Use when reviewing a plan that touches a notoriously hard area, or when
estimating why "simple" changes in a subsystem keep costing multiples.

## Actions

1. Ask the two-week question of the area the plan builds on, honestly.
2. When the answer is no, flag the onboarding debt as its own finding — do
   not price it into the feature and move on.
3. Prefer plans that reduce the smell in passing (a seam, a doc, a deleted
   indirection) over plans that compound it.
4. Distinguish essential domain difficulty (irreducible) from accumulated
   incidental difficulty (the actual smell).

## Evidence

The review names the area, the verdict, and the debt finding when the answer
is no.

## Failure Smells

- Every estimate in one subsystem carries a silent 3x multiplier.
- New capability stacked on a module nobody will refactor because nobody
  fully understands it.
- Onboarding docs that begin "first, ask someone to walk you through it."
