---
library: snippet
language: json
---

# Snippets

## Snippet template

Create a vscode-like snippet in json.
Takes in prefix, description, and body fields.

<!-- js-snippet|snip -->

```json
"${1:Snippet}": {
	"prefix": "${2:prefix}",
	"description": "${3:description}",
	"body":"${4:body}"
},
```
