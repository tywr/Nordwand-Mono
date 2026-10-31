.PHONY: install build build-font build-otf build-nerd-font install-mac visualize website

FONT_VERSION ?= $(shell git describe --tags --abbrev=0 2>/dev/null || echo 1.0.0)

install:
	uv sync

build:
	uv run python -m generate_font --font-version $(FONT_VERSION) --web-font
	uv run python -m scripts.banner
	uv run python -m scripts.specimen_pdf
	uv run python -m scripts.samples
	uv run python -m scripts.alternatives_markdown

build-font:
	uv run python -m generate_font --font-version $(FONT_VERSION) --web-font

build-otf:
	uv run python -m generate_font --font-version $(FONT_VERSION) --otf

build-nerd-font:
	uv run python -m scripts.nerd_font

install-mac:
	cp -r fonts/otf/NordwandMono-*.otf ~/Library/Fonts

visualize:
	open -n -a /Library/Frameworks/Python.framework/Versions/3.12/Resources/Python.app \
    --env "__PYVENV_LAUNCHER__=$PWD/.venv/bin/python" \
    --args -m visualize lowercase_a

website:
	mkdir -p docs/fonts
	cp fonts/woff2/*.woff2 docs/fonts/
	uv run python -m scripts.serve
