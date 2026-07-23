# validation-hierarchy

Green at a cheap surface does not prove the expensive one.

Use when declaring an acceptance criterion, review finding, or QA check done,
especially when a change touches more than one surface class
(`classify-verification-surfaces.md`).

## The layers

1. **Static** — typecheck, lint, build, unit tests with mocked dependencies.
   Proves shape and isolated logic. Blind to interface mismatch, state
   propagation, resource lifecycle, and environment dependency.
2. **Runtime** — the code actually executes against real dependencies: the
   service starts, the function runs, the query hits a real store.
3. **End-to-end** — the user-facing route works through the real seams the user
   crosses.

## Actions

1. Climb the layers in order, and treat a failing layer as a **stop, not a
   label**: do not push on to runtime or end-to-end work while a lower layer is
   red — fix it and re-pass it first. A failure at a lower layer is cheaper to
   find, so pay for it before building on top of it. (Marking the higher layer
   `not verified` is disclosure; it is not permission to keep going past the
   break.)
2. Mark a claim `verified` only at the **highest layer available for its class**.
   A static-only green never certifies runtime or user-visible behavior; say
   `not verified` for the layers you did not reach.
3. When a change crosses more than one surface class, an end-to-end layer is
   mandatory — unit greens on each side do not prove the seam between them.
4. When the repo exposes a `smoke`, `dev`, or `run` command, invoke it at least
   once for any user-visible or service-level claim before marking it verified.

## Cross-boundary defect classes

The defects a static layer cannot see, and that an end-to-end layer exists to
catch — name the one you are hunting when a change "worked in isolation but broke
integrated":

- **Interface mismatch** — two components agree in mocks, disagree in reality
  (shape, type, contract, order).
- **State propagation** — a value set in one place never reaches, or arrives
  stale at, another.
- **Resource lifecycle** — connections, handles, locks, timers, or subscriptions
  opened and not closed, or used after close.
- **Environment dependency** — passes against fakes, fails against the real
  runtime (config, clock, filesystem, network, versions).

## Failure smells

- "Tests pass" offered as proof the feature works, when the tests mock the exact
  boundary that would break.
- A cross-component change verified only by per-file commands.
- Declaring done on a criterion whose running system was never started.
