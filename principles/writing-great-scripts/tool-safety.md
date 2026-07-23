# tool-safety

When designing the tools and permissions an agent may call, the safe default is
closed, and safety is decided per call, not per tool.

Use when building or reviewing an agent's tool registry, permission model, or
command-approval layer.

## Actions

1. **Fail closed by default.** A tool with no explicit safety classification is
   treated as non-concurrent, non-read-only, and requiring approval — never
   auto-allowed. "Allow" is a decision you make, not a default you inherit.
2. **Classify per call, not per tool.** The same tool (a shell, an HTTP client)
   is safe for some arguments and dangerous for others. Decide concurrency and
   permission from the actual call, not a static registration on the tool name.
3. **Keep a bypass-immune list.** Protected paths and commands (`/etc/**`,
   `rm -rf`, `DROP TABLE`, force-push to shared branches, production writes)
   never auto-approve, regardless of mode or prior approvals. No "allow all"
   reaches them.
4. **Do not cache a permission decision across calls.** Approval evaluation is
   stateful (it tracks denials and mode changes); a result that was safe last
   call is not guaranteed safe this call.

## Failure smells

- A new tool is callable without anyone having decided it should be.
- A tool marked safe once runs an unsafe argument freely.
- A blanket "yes to everything" that also swallows destructive commands.
- A cached "allowed" that outlives the context that justified it.
