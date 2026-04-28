---
library: blocks
language: markdown
---

# Blocks

## Literate Snippet Template

Create formatted markdown block with snippet title, description, and prefix.
The snippet code can then be copied and pasted easily.
The markdown block can then be tangled into a .json snippet file using the Makefile.

<!-- md-snippet|snip -->

```md
## ${1:Snippet Title}

${2:description}

<!-- ${3:prefix} -->

$0
```
