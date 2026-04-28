#!/usr/bin/env python3
"""
Generate Zed extension files from package.json.
"""

import json
import os
import shutil
from pathlib import Path


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)

    os.chdir(parent_dir)

    with open("package.json", "r") as f:
        pkg = json.load(f)

    name = pkg.get("name", "snippets")
    version = pkg.get("version", "0.0.1")
    schema_version = 1
    description = pkg.get("description", "")
    repository = pkg.get("repository", {}).get("url", "")

    extension_dir = Path("zed-extension")
    snippets_dir = extension_dir / "snippets"

    if extension_dir.exists():
        shutil.rmtree(extension_dir)
    extension_dir.mkdir(parents=True, exist_ok=True)

    extension_toml = extension_dir / "extension.toml"
    with open(extension_toml, "w") as f:
        f.write(f'id = "{name}"\n')
        f.write(f'name = "{name}"\n')
        f.write(f'version = "{version}"\n')
        f.write(f'schema_version = {schema_version}\n')
        f.write(f'description = "{description}"\n')
        if repository:
            f.write(f'repository = "{repository}"\n')
        f.write("\n")
        f.write('snippets = ["./snippets/*/*.json"]')

    languages = set()
    for json_file in Path("snippets").rglob("*.json"):
        lang = json_file.parent.name
        languages.add(lang)

    for lang in sorted(languages):
        lang_dir = snippets_dir / lang
        lang_dir.mkdir(parents=True, exist_ok=True)

        for json_file in sorted(Path("snippets", lang).glob("*.json")):
            target = lang_dir / json_file.name
            os.symlink(json_file, target)

    print(f"Generated {extension_dir}/ with {len(languages)} languages")


if __name__ == "__main__":
    main()
