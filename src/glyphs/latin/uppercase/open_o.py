from fontTools.misc.transform import Transform
from fontTools.pens.reverseContourPen import ReverseContourPen
from fontTools.pens.transformPen import TransformPen
from glyphs.uppercase.round.c import UppercaseCGlyph


class UppercaseOpenOGlyph(UppercaseCGlyph):
    """The C mirrored horizontally"""

    name = "uppercase_open_o"
    unicode = "0x186"

    def draw(self, pen, dc):
        # Mirroring reverses the contours' direction, so wind them back
        mirror = Transform(-1, 0, 0, 1, dc.window_width, 0)
        super().draw(TransformPen(ReverseContourPen(pen), mirror), dc)
