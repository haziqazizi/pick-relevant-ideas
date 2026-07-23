# Adversarial hardening contract

For long-horizon, high-risk, benchmark-like, security-sensitive, or heavily agent-generated work, plan and execute at least one hardening loop.

## Loop

```text
implement/review/cheat attempt → inspect traces/logs/artifacts → identify shortcut → patch spec/verifier/harness → rerun
```

## Shortcut classes to guard

- no-op or docs-only implementation
- hardcoded fixture/golden answer/judge nonce
- mocked or proxy proof outside scope
- verifier/test weakening, renaming, skipping, or tampering
- source-keyword-only success for behavioral claims
- fake browser proof, stale screenshots, or inferred UI state
- toolchain/test-runner spoofing
- service impersonation or sealed asset bypass

Each planned guard should have an executed result when QA/security execution runs: expected fail signal, command/flow, evidence, and residual risk.
