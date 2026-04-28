#!/usr/bin/env python3
import json
import glob
import os

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)

    os.chdir(parent_dir)
    snippets = glob.glob("snippets/**/*.json")

    snippet_entries = []
    for path in sorted(snippets):
        if "python" in path:
            lang = "python"
        elif "json" in path:
            lang = "json"
        else:
            lang = "plaintext"
        snippet_entries.append({
            "language": lang,
            "path": f"./{path}"
        })

    package_path = os.path.join(parent_dir, "package.json")
    with open(package_path, "r") as f:
        package = json.load(f)

    package["contributes"]["snippets"] = snippet_entries

    with open(package_path, "w") as f:
        json.dump(package, f, indent=2)
        f.write("\n")

    print(f"Updated package.json with {len(snippet_entries)} snippet entries")

if __name__ == "__main__":
    main()