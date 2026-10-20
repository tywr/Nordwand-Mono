.PHONY: install build build-otf build-nerd install-mac install-nerd-mac

install:
	uv sync

build:
	uv run python -m generate_font --web-font
	uv run python -m scripts.banner
	uv run python -m scripts.specimen_pdf
	uv run python -m scripts.samples
	uv run python -m scripts.alternatives_markdown

build-font:
	uv run python -m generate_font --web-font

build-otf:
	uv run python -m generate_font --otf

NERD_FONTS_VERSION := 3.5.1
PATCHER_DIR := ext-fonts/nerd-fonts-patcher-$(NERD_FONTS_VERSION)

$(PATCHER_DIR)/font-patcher:
	mkdir -p $(PATCHER_DIR)
	curl -fsSL -o $(PATCHER_DIR)/FontPatcher.zip \
		https://github.com/ryanoasis/nerd-fonts/releases/download/v$(NERD_FONTS_VERSION)/FontPatcher.zip
	unzip -q -o $(PATCHER_DIR)/FontPatcher.zip -d $(PATCHER_DIR)

build-nerd: build-otf $(PATCHER_DIR)/font-patcher
	mkdir -p fonts/nerd
	ls fonts/otf/*.otf | xargs -P 4 -I{} \
		fontforge -script $(PATCHER_DIR)/font-patcher --complete --mono --quiet -out fonts/nerd {}

install-mac:
	cp -r fonts/otf/NordwandMono-*.otf ~/Library/Fonts

install-nerd-mac:
	cp fonts/nerd/NordwandMonoNerdFontMono-*.otf ~/Library/Fonts

visualize:
	open -n -a /Library/Frameworks/Python.framework/Versions/3.12/Resources/Python.app \
    --env "__PYVENV_LAUNCHER__=$PWD/.venv/bin/python" \
    --args -m visualize lowercase_a
