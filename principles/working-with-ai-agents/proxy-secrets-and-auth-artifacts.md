# Proxy secrets and auth artifact policy

Do not give agents raw long-lived secrets when a scoped capability works.

Prefer:

- platform secret stores, SOPS/age/KMS/Vault, or equivalent sealed storage
- short-lived per-task credentials
- HTTP proxies or integration wrappers that inject secrets server-side
- allowlisted network/capability boundaries
- least-privilege staging/test credentials
- redacted logs and evidence artifacts
- explicit rotation/revocation path

Never print raw `.env` values, cookies, tokens, private keys, auth headers, database URLs with credentials, or browser storage state. Do not commit screenshots, HAR files, traces, videos, cookies, or auth-state files if they contain secrets; place them under ignored artifact paths and redact before sharing.
