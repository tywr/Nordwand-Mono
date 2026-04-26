build:
	python -m generate_font
	python -m scripts.banner
	python -m scripts.specimen_pdf
	python -m scripts.specimen_png
	python -m scripts.samples

build-otf:
	python -m generate_font --otf

install-mac:
	cp -r fonts/otf/NordwandMono-*.otf ~/Library/Fonts
