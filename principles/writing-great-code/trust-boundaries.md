# trust-boundaries

Draw a hard line between trusted internal state and untrusted external input.

Use when data crosses from users, browsers, devices, files, webhooks, MCP tools,
LLM output, third-party APIs, queues, databases, or environment variables.

## Actions

1. Name each boundary.
2. Parse and validate on entry.
3. Sanitize or encode before crossing output boundaries.
4. Avoid passing raw external payloads deep into business logic.
5. Log boundary failures without leaking secrets.

## Evidence

Leave a schema, parser, guard, adapter test, or explicit review note showing
where trust changes.
