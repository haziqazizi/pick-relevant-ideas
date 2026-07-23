# non-interactive-first

Every script input should be expressible through flags, args, stdin, or config.

Interactive prompts are allowed only as convenience fallback.

## Actions

1. List required inputs.
2. Add flags or positional args for each.
3. Support environment/config only for stable defaults, not hidden required input.
4. Add `--yes` or equivalent only for explicit confirmation bypass.
5. Make CI/agent mode refuse prompts.

## Failure Smells

- Script hangs waiting for input.
- Prompt text is the only documentation.
- Agent has to echo into stdin to answer questions.
