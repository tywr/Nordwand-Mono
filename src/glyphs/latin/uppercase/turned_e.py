from fontTools.misc.transform import Transform
from fontTools.pens.reverseContourPen import ReverseContourPen
from fontTools.pens.transformPen import TransformPen
from glyphs.uppercase.e import UppercaseEGlyph


class UppercaseTurnedEGlyph(UppercaseEGlyph):
    """The E mirrored horizontally"""

    name = "uppercase_turned_e"
    unicode = "0x18E"

    def draw(self, pen, dc):
        # The flip reverses the contours' direction, so wind them back
        flip = Transform(-1, 0, 0, 1, dc.window_width, 0)
        super().draw(TransformPen(ReverseContourPen(pen), flip), dc)
