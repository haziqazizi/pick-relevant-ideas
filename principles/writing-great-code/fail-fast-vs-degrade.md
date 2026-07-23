# fail-fast-vs-degrade

Choose deliberately between stopping and reduced service.

Use when errors, dependency failures, invalid data, missing config, browser
failures, or device failures occur.

## Fail Fast When

- continuing risks corruption
- auth/security state is unclear
- money, deletion, or irreversible action is involved
- the system cannot prove what state it is in

## Degrade When

- reduced behavior is useful and safe
- the user/operator can see the degraded mode
- recovery is defined
- correctness is not silently weakened

## Evidence

Name the mode, user/operator signal, and recovery condition.
