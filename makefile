.PHONY: install build build-font build-otf build-nl-font build-nerd-font install-mac visualize website lab

FONT_VERSION ?= $(shell git describe --tags --abbrev=0 2>/dev/null || echo 1.0.0)

install:
	uv sync

build:
	uv run python -m nordwand_mono.generate_font -j --font-version $(FONT_VERSION) --web-font
	uv run python -m nordwand_mono.scripts.banner
	uv run python -m nordwand_mono.scripts.specimen_pdf
	uv run python -m nordwand_mono.scripts.samples
	uv run python -m nordwand_mono.scripts.alternatives_markdown
	uv run python -m nordwand_mono.scripts.website

build-font:
	uv run python -m nordwand_mono.generate_font -j --font-version $(FONT_VERSION) --web-font

build-otf:
	uv run python -m nordwand_mono.generate_font -j --font-version $(FONT_VERSION) --otf

build-nl-font:
	uv run python -m nordwand_mono.generate_font -j --font-version $(FONT_VERSION) --no-ligatures

build-nerd-font:
	uv run python -m nordwand_mono.scripts.nerd_font

install-mac:
	cp -r fonts/otf/NordwandMono-*.otf ~/Library/Fonts

visualize:
	open -n -a /Library/Frameworks/Python.framework/Versions/3.12/Resources/Python.app \
    --env "__PYVENV_LAUNCHER__=$PWD/.venv/bin/python" \
    --args -m nordwand_mono.visualize lowercase_a

website:
	uv run python -m nordwand_mono.scripts.website
	uv run python -m nordwand_mono.scripts.serve

lab:
	@echo "Lab on http://localhost:8001/lab/"
	uv run python -m nordwand_mono.scripts.serve . 8001
