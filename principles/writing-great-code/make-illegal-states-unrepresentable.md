# make-illegal-states-unrepresentable

Represent valid states directly.

Use when designing data structures, status fields, workflow state, config,
schemas, forms, API payloads, or generated artifacts.

Prefer:

- enums over free strings
- tagged unions over nullable field bundles
- explicit lifecycle states over booleans
- branded IDs over interchangeable strings
- parsed/validated data over raw payloads
- required fields for required concepts

## Actions

1. List valid states.
2. List impossible or forbidden states.
3. Choose the smallest representation that cannot express the forbidden states.
4. Put parsing/validation at the boundary.
5. Add a test or schema check for rejected invalid states.

## Tradeoff

In dynamic languages, you may not fully enforce this in types. Use runtime
schemas, constructors, assertions, or focused tests where the value crosses a
boundary.
