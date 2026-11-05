from fontTools.misc.transform import Transform
from fontTools.pens.reverseContourPen import ReverseContourPen
from fontTools.pens.transformPen import TransformPen
from glyphs.uppercase.v import UppercaseVGlyph


class UppercaseTurnedVGlyph(UppercaseVGlyph):
    """The V upside down"""

    name = "uppercase_turned_v"
    unicode = "0x245"

    def draw(self, pen, dc):
        # The flip reverses the contours' direction, so wind them back
        flip = Transform(1, 0, 0, -1, 0, dc.cap)
        super().draw(TransformPen(ReverseContourPen(pen), flip), dc)
