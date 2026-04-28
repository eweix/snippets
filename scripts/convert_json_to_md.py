#!/usr/bin/env python3
"""
Convert JSON snippet files to markdown format.
"""

import json
import os
from pathlib import Path


def json_to_markdown(json_path: Path) -> str:
    with open(json_path) as f:
        data = json.load(f)

    lang = os.path.basename(os.path.dirname(json_path))

    library_name = json_path.stem
    lines = [
        "---",
        f"library: {library_name}",
        f"language: {lang}",
        "---",
        "",
        f"# {library_name}",
        "",
    ]

    for snippet_name, snippet in data.items():
        prefix = snippet.get("prefix")
        description = snippet.get("description", "")
        body = snippet.get("body", [])

        if isinstance(prefix, list):
            prefix_tag = "|".join(prefix)
        else:
            prefix_tag = prefix

        if isinstance(body, list):
            code_body = body
        else:
            code_body = [body]

        lines.append(f"## {snippet_name}")
        lines.append("")
        lines.append(f"{description}")
        lines.append("")
        lines.append(f"<!-- {prefix_tag} -->")
        lines.append("")
        if code_body:
            lines.append(f"```{lang}")
            lines.extend(code_body)
            lines.append("```")
        else:
            lines.append(f"```{lang}")
            lines.append("```")
        lines.append("")

    return "\n".join(lines)


def main():
    json_dir = Path("snippets")
    docs_dir = Path("docs")
    docs_dir.mkdir(exist_ok=True)

    for json_file in sorted(json_dir.glob("*/*.json")):
        print(f"Converting {json_file.name}...")
        md_content = json_to_markdown(json_file)
        md_file = docs_dir / json_file.name.replace(".json", ".md")
        md_file.write_text(md_content)
        print(f"  -> {md_file.name}")

    print("Done!")


if __name__ == "__main__":
    main()
