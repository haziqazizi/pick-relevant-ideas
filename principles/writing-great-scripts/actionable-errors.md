# actionable-errors

Errors should tell the caller what to do next.

Use for all scripts and CLIs.

## Actions

1. Fail fast when required inputs are missing.
2. State the missing fact or invalid value.
3. Include a corrected example command when possible.
4. Separate user errors from tool/internal errors.
5. Do not print stack traces by default for expected user mistakes.

Good error messages reduce retries and context churn.
