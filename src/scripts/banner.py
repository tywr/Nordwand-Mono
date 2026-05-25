#!/usr/bin/env python3
"""Generate a banner image for the GitHub README.

Overlays "NORDWAND MONO" in white at the center of assets/banner-raw.jpg.

Usage: python -m scripts.banner [path/to/font.ttf]
"""

import argparse
from PIL import Image, ImageDraw, ImageFont


TEXT = "NORDWAND MONO"
TAGLINE = "A monospace font for coders and adventurers"
FG = "#ffffff"
FONT_SIZE = 260
TAGLINE_SIZE = 64
TAGLINE_GAP = 80
INPUT = "assets/banner-raw.jpg"


def render_banner(font_path, output="assets/banner.png"):
    import os
    os.makedirs(os.path.dirname(output), exist_ok=True)

    img = Image.open(INPUT).convert("RGB")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, FONT_SIZE)
    light_path = font_path.replace("-Regular", "-Light")
    tagline_font = ImageFont.truetype(
        light_path if os.path.exists(light_path) else font_path, TAGLINE_SIZE
    )

    bbox = draw.textbbox((0, 0), TEXT, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    tbbox = draw.textbbox((0, 0), TAGLINE, font=tagline_font)
    tag_w = tbbox[2] - tbbox[0]
    tag_h = tbbox[3] - tbbox[1]

    block_h = text_h + TAGLINE_GAP + tag_h
    top = (img.height - block_h) / 2

    x = (img.width - text_w) / 2 - bbox[0]
    y = top - bbox[1]
    draw.text((x, y), TEXT, font=font, fill=FG)

    tx = (img.width - tag_w) / 2 - tbbox[0]
    ty = top + text_h + TAGLINE_GAP - tbbox[1]
    draw.text((tx, ty), TAGLINE, font=tagline_font, fill=FG)

    img.save(output)
    print(f"Saved {output} ({img.width}x{img.height})")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Nordwand Mono banner")
    parser.add_argument("font", nargs="?", default="fonts/ttf/NordwandMono-Regular.ttf", help="Path to font file")
    parser.add_argument("-o", "--output", default="assets/banner.png", help="Output filename")
    args = parser.parse_args()
    render_banner(args.font, args.output)
