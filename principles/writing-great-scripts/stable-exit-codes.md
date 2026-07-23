# stable-exit-codes

Exit codes are part of the interface.

Use for scripts called by agents, CI, hooks, or other scripts.

## Actions

1. Exit `0` for success.
2. Exit nonzero for failed checks, invalid input, or tool failure.
3. Keep meanings stable across releases.
4. Document special codes if more than `0` and `1` matter.
5. Avoid printing PASS while exiting nonzero, or FAIL while exiting zero.
