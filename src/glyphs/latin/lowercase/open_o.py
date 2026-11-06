from fontTools.misc.transform import Transform
from fontTools.pens.reverseContourPen import ReverseContourPen
from fontTools.pens.transformPen import TransformPen
from glyphs.lowercase.round.c import LowercaseCGlyph


class LowercaseOpenOGlyph(LowercaseCGlyph):
    """The c mirrored horizontally"""

    name = "lowercase_open_o"
    unicode = "0x254"

    def draw(self, pen, dc):
        # Mirroring reverses the contours' direction, so wind them back
        mirror = Transform(-1, 0, 0, 1, dc.window_width, 0)
        super().draw(TransformPen(ReverseContourPen(pen), mirror), dc)
