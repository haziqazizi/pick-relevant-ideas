# classify-verification-surfaces

Different claims need different proof surfaces.

Use before declaring plan items, review findings, QA checks, or ship readiness
done.

## Capability Classification

Classify what the claim must let a verifier do, not which framework or software
category it resembles. Capability identifiers are extensible; typical needs are
prepare, execute, observe, assert, capture, reproduce, cleanup, resume, and
present. The repo maps those needs to its own named proof adapters.

## Actions

1. Name each important claim and required capabilities.
2. Select the closest faithful repo-declared adapter and verify it provides them.
3. Record invocation, target/identity, artifacts, result, cleanup, and limits.
4. Mark missing capability coverage as residual, not verified, or blocked.
