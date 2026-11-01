"""Box drawing characters (U+2500–U+257F).

Every glyph spans the whole cell so lines join seamlessly with their
neighbours. Each family has its own base class holding its settings:

- BoxGlyph: light and heavy stroke weights, shared by every family
- LineBoxGlyph / DoubleLineBoxGlyph (lines.py): straight lines and junctions,
  the double ones also set the stroke and gap of their two lines
- DashedBoxGlyph (dashed.py): the gap between dashes
- ArcBoxGlyph (arcs.py): the radius of the rounded corners
- DiagonalBoxGlyph (diagonals.py)
"""

import unicodedata

from config import FontConfig as fc
from glyphs import Glyph


class BoxGlyph(Glyph):
    offset = 0
    italic_skew = False
    # Line thicknesses in units, the same for every weight. Lines are as thick
    # horizontally as vertically, so the grid looks even
    light = 76
    heavy = 152
    # Units a line reaches into the neighbouring cell it connects to, so no
    # seam shows between cells
    bleed = 20

    def stroke(self, weight):
        return {"light": self.light, "heavy": self.heavy}[weight]

    @staticmethod
    def cell(dc):
        """Cell bounds (x1, y1, x2, y2) and its centre (cx, cy)."""
        x1, y1, x2, y2 = 0, fc.window_descent, dc.window_width, fc.window_ascent
        return (x1, y1, x2, y2), ((x1 + x2) / 2, (y1 + y2) / 2)


def box_glyph(base, code, **attrs):
    """Subclass of `base` for the character `code`, named after its Unicode
    name, e.g. 0x2500 -> box_light_horizontal."""
    name = unicodedata.name(chr(code)).lower().replace("box drawings ", "box ")
    name = name.replace(" ", "_")
    cls_name = "".join(part.title() for part in name.split("_")) + "Glyph"
    return type(cls_name, (base,), {"name": name, "unicode": f"0x{code:04X}", **attrs})
