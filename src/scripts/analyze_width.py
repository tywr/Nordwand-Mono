#!/usr/bin/env python3
"""Analyze alphanumeric character widths relative to lowercase 'o'.

Usage: python scripts/analyze_width.py path/to/font.ttf
"""

import argparse
import string

from fontTools.ttLib import TTFont
from fontTools.pens.boundsPen import BoundsPen


def get_x_bounds(font, glyph_name):
    """Return (x_min, x_max) for a glyph, or None if empty."""
    glyph_set = font.getGlyphSet()
    if glyph_name not in glyph_set:
        return None
    pen = BoundsPen(glyph_set)
    glyph_set[glyph_name].draw(pen)
    if pen.bounds is None:
        return None
    return pen.bounds[0], pen.bounds[2]


def main():
    parser = argparse.ArgumentParser(description="Analyze glyph widths relative to lowercase 'o'")
    parser.add_argument("font", help="Path to a TTF font file")
    args = parser.parse_args()

    font = TTFont(args.font)
    cmap = font.getBestCmap()

    # Baseline: lowercase 'o'
    o_code = ord("o")
    if o_code not in cmap:
        print("Error: font has no lowercase 'o'")
        return
    o_bounds = get_x_bounds(font, cmap[o_code])
    if o_bounds is None:
        print("Error: lowercase 'o' has no outlines")
        return
    o_width = o_bounds[1] - o_bounds[0]
    print(f"Baseline 'o': x_min={o_bounds[0]:.0f}  x_max={o_bounds[1]:.0f}  width={o_width:.0f}\n")

    chars = string.ascii_letters + string.digits
    results = []
    for ch in chars:
        code = ord(ch)
        if code not in cmap:
            continue
        bounds = get_x_bounds(font, cmap[code])
        if bounds is None:
            continue
        width = bounds[1] - bounds[0]
        pct = (width - o_width) / o_width * 100
        results.append((ch, bounds[0], bounds[1], width, pct))

    # Print sorted by character
    print(f"{'Char':>4}  {'x_min':>6}  {'x_max':>6}  {'width':>6}  {'shift':>7}")
    print(f"{'----':>4}  {'-----':>6}  {'-----':>6}  {'-----':>6}  {'------':>7}")
    for ch, x_min, x_max, width, pct in results:
        print(f"{ch:>4}  {x_min:>6.0f}  {x_max:>6.0f}  {width:>6.0f}  {pct:>+6.1f}%")

    font.close()


if __name__ == "__main__":
    main()
