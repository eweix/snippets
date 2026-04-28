#!/usr/bin/env python3
"""
Extract snippets from markdown files to JSON format.
"""

import json
from pathlib import Path

def md_to_json(md_path: Path) -> dict:
    content = md_path.read_text()
    lines = content.split("\n")

    data = {}
    current_snippet = None
    current_description = None
    current_prefix = None
    current_body_lines = []
    in_code_block = False

    i = 0
    while i < len(lines):
        line = lines[i]

        if line.startswith("## "):
            if current_snippet and current_prefix is not None:
                body = "\n".join(current_body_lines).strip() if current_body_lines else ""
                data[current_snippet] = {
                    "prefix": current_prefix,
                    "description": current_description or "",
                    "body": body
                }

            current_snippet = line[3:].strip()
            current_description = None
            current_prefix = None
            current_body_lines = []
            in_code_block = False

        elif line.strip().startswith("<!--") and line.strip().endswith("-->"):
            prefix_str = line.strip()[4:-3].strip()
            current_prefix = prefix_str.split("|")

        elif line.strip().startswith("```"):
            in_code_block = True

        elif in_code_block and line.strip() == "```":
            in_code_block = False

        elif in_code_block:
            current_body_lines.append(line)

        elif current_description is None and line.strip():
            current_description = line.strip()

        i += 1

    if current_snippet and current_prefix is not None:
        body = "\n".join(current_body_lines).strip() if current_body_lines else ""
        data[current_snippet] = {
            "prefix": current_prefix,
            "description": current_description or "",
            "body": body
        }

    return data

def main():
    docs_dir = Path("sources/python")
    json_dir = Path("snippets/python")

    for md_file in sorted(docs_dir.glob("*.md")):
        print(f"Extracting {md_file.name}...")
        snippets = md_to_json(md_file)
        json_file = json_dir / md_file.name.replace(".md", ".json")

        with open(json_file, "w") as f:
            json.dump(snippets, f, indent=2)

        print(f"  -> {json_file.name}")

    print("Done!")

if __name__ == "__main__":
    main()