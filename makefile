.PHONY: install build build-otf install-mac

install:
	python3 -m venv .venv
	.venv/bin/python -m pip install -e .

build:
	.venv/bin/python -m generate_font --web-font
	.venv/bin/python -m scripts.banner
	.venv/bin/python -m scripts.specimen_pdf
	.venv/bin/python -m scripts.samples

build-font:
	.venv/bin/python -m generate_font --web-font

build-otf:
	.venv/bin/python -m generate_font --otf

install-mac:
	cp -r fonts/otf/NordwandMono-*.otf ~/Library/Fonts
