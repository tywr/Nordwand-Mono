build:
	.venv/bin/python -m generate_font
	.venv/bin/python -m scripts.banner
	.venv/bin/python -m scripts.specimen_pdf
	.venv/bin/python -m scripts.samples

build-otf:
	.venv/bin/python -m generate_font --otf

install-mac:
	cp -r fonts/otf/NordwandMono-*.otf ~/Library/Fonts
