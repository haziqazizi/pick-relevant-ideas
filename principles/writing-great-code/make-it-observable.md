# make-it-observable

Emit the signals that prove important invariants hold in the running system.

Use for services, queues, browser/iOS daemons, migrations, QA runs, external
providers, background jobs, and degraded modes.

## Actions

1. Name the invariant or failure mode.
2. Decide which signal would reveal it: log, metric, trace, status, artifact,
   health check, counter, event, screenshot, or state dump. Match signal to
   question — a log answers *why one event happened*, a metric answers *how
   often or how much* (durations as percentiles, never an average), a trace
   answers *where in the flow*.
3. Instrument the failure mode, not only the happy path.
4. Bound and redact observability output. Bound label/field cardinality too:
   route templates and enum states, never per-user IDs, emails, or raw URLs.
5. Make alerts/action items specific enough to act on. Alert on symptoms
   consumers actually feel; route causes to diagnosis surfaces. If the
   accepted response to an alert is "ignore it, it self-heals", delete the
   alert.
6. Verify the telemetry itself: force the failure in a safe environment and
   confirm the signal fires and is findable. Instrumentation is code and
   carries the same proof obligation.

## Evidence

Leave metric/log names, trace IDs, artifact paths, dashboard links, or explicit
"not observable" residuals.

## Failure Smells

- "We would see it in logs" but no log line exists.
- Silent fallback.
- Queue depth, retry count, deadline budget, or drift is invisible.
- Telemetry logs secrets or grows without bound.
- An alert whose accepted answer has ever been "ignore it".
- Instrumentation shipped without ever having been seen to fire.
