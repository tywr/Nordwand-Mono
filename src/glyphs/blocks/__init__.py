"""Block elements (U+2580–U+259F).

Every glyph fills parts of the whole cell. Each family has its own base class
holding its settings:

- BlockGlyph: the bleed into neighbouring cells, shared by every family
- RectBlockGlyph (rects.py): eighths, halves and quadrants
- ShadeBlockGlyph (shades.py): the size of the dots of ░ ▒ ▓
"""

import unicodedata

from config import FontConfig as fc
from glyphs import Glyph


class BlockGlyph(Glyph):
    offset = 0
    italic_skew = False
    # Units a shape touching the cell edge reaches into the neighbouring
    # cell, so no seam shows between cells
    bleed = 20

    @staticmethod
    def cell(dc):
        """Cell bounds (x1, y1, x2, y2)."""
        return 0, fc.window_descent, dc.window_width, fc.window_ascent


def block_glyph(base, code, **attrs):
    """Subclass of `base` for the character `code`, named after its Unicode
    name, e.g. 0x2588 -> block_full_block."""
    name = "block_" + unicodedata.name(chr(code)).lower().replace(" ", "_")
    cls_name = "".join(part.title() for part in name.split("_")) + "Glyph"
    return type(cls_name, (base,), {"name": name, "unicode": f"0x{code:04X}", **attrs})
