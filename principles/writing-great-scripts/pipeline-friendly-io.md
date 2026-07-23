# pipeline-friendly-io

Scripts should compose with files, stdin, stdout, and stderr.

Use for checks, formatters, generators, codemods, and data transforms.

## Actions

1. Accept input from paths and stdin when practical.
2. Write machine-readable result to stdout.
3. Write diagnostics/progress to stderr.
4. Support explicit output paths for generated files.
5. Avoid mixing logs into data output.
