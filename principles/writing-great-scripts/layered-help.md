# layered-help

Help should reveal detail in layers.

Use for multi-command CLIs and scripts with modes.

## Actions

1. Top-level help lists commands and common examples.
2. Subcommand help explains flags, defaults, and examples for that command.
3. Avoid dumping the entire manual for every error.
4. Include where outputs are written.
5. Include whether command is read-only or writes state.

Agents need fast discovery without flooding context.
