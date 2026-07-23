# Grading Subjective Output

A cross-cutting doctrine, and the concrete method behind
`verification-and-autonomy.md`'s "several uncorrelated refuters with distinct
lenses" when the thing being graded is *subjective* — writing, design, creative,
taste. Read it whenever a grader must judge quality that no exact script can score.

The governing rule from the parent doctrine still holds: **a grader is the
LLM-judge tier; real-world outcome is ground truth.** A subjective grader filters
and prunes; it never certifies an irreversible effect. When the market, a test,
or a human decision is available, it outranks the grader.

## Build the grader from real signal, not adjectives

1. **Mine real accept/reject signal.** Distill "good" from actual decisions
   (upvotes, kept vs discarded, winners vs losers), not from a description of
   taste. Ground it in a corpus via example-mining — the codebook is the
   rubric's backbone.
2. **Make the rubric explicit** — a library of concrete principles plus good/bad
   exemplars, one criterion per line. Freeze and **version** it; verdicts flip on
   equivalent rewordings, so a drifting rubric is not a grader.
3. **One single-purpose judge per axis.** Separate judges for distinct qualities
   (e.g. idea-strength vs execution). Multi-purpose judges degrade.

## Judge pairwise, with evidence

- **Pairwise, not absolute.** "Which of these two is better?" beats a 1-10 score.
  Absolute scores compress (models cluster everything 70-85) and are noise;
  comparative judgment is measurably stronger.
- **Evidence-required.** The judge must quote/point to the exact part of the
  artifact that supports its verdict. No ungrounded scores.
- **Optimize the judge prompt against a held-out labeled set** (e.g. DSPy-style),
  and keep a holdout you never optimize against.

## Calibrate on local data — agreement does not transfer

A grader validated in one domain does NOT carry to another (chat-domain "80%
human agreement" numbers do not transfer to ad or code scoring). Calibrate every
subjective grader against **human ratings on your own artifacts** before trusting
it, and re-calibrate when the domain shifts.

## Vision-judge failure modes (for visual artifacts — design guardrails)

A vision-LLM grader is noisy and biased; wire around these, don't ignore them:

- **Position bias** — judges copy the shown ordering → randomize A/B order and
  average both orderings.
- **Verbosity/length bias** — more text scores higher with no quality change →
  control for copy density.
- **Self-preference** — a judge over-passes its own output (up to ~50% more) →
  **never let the same model both generate and judge.**
- **OCR blindness** — models misread small text and hallucinate plausible-but-
  wrong copy (they may rate an ad highly while misreading the discount,
  disclaimer, or brand name) → OCR with a **dedicated engine** and feed verified
  text to the judge.
- **Motion blindness from stills** — still-frame judges score shuffled frames
  the same → a still judge cannot validly rate hook timing, transitions, or
  pacing; use video-native eval or a human on those axes.
- **Overconfidence / miscalibration** — ignore self-reported confidence;
  calibrate on a labeled holdout of your own artifacts.
- **Modality neglect** — judges sometimes don't really look at the artifact;
  reliability ≠ validity. Spot-check.

## The one rule

Mine real signal → write an explicit, versioned rubric (codebook-backed) → judge
pairwise with required evidence, one axis per judge, generator ≠ judge → calibrate
on your own labeled data → and remember the grader only prunes; the real-world
outcome decides.
