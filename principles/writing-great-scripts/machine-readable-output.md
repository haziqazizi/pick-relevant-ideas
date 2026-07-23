# machine-readable-output

Return data that tools can consume.

Use when output may feed another command, CI, an agent, or an artifact.

## Actions

1. Provide `--json` for structured output when useful.
2. Keep human logs out of JSON.
3. Print stable fields: status, paths, IDs, URLs, durations, counts.
4. Avoid decorative output in machine mode.
5. Redact secrets in every output mode.
