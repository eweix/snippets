.PHONY: all zed-extension

all: package.json

zed-extension: package.json
	python3 scripts/generate_zed_extension.py

clean:
	rm -rf snippets

package.json: $(patsubst sources/%.md, snippets/%.json, $(wildcard sources/*/*.md))
	python3 scripts/update_package.py

snippets:
	mkdir snippets
	mkdir -p $@

snippets/%.json: sources/%.md
	python3 scripts/extract_md_to_json.py $<
