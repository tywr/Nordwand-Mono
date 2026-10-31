from fontTools.misc.transform import Transform
from fontTools.pens.reverseContourPen import ReverseContourPen
from fontTools.pens.transformPen import TransformPen
from glyphs.lowercase.y import LowercaseYGlyph


class GreekLowercaseLamdaGlyph(LowercaseYGlyph):
    """The y upside down: the legs stand on the baseline and the right one
    goes on up to the ascender"""

    name = "greek_lowercase_lamda"
    unicode = "0x3BB"

    def tail_end(self, dc):
        # Flipped around the middle of the x-height, this lands on the ascent
        return dc.x_height - dc.ascent

    def draw(self, pen, dc):
        # The flip reverses the contours' direction, so wind them back
        flip = Transform(1, 0, 0, -1, 0, dc.x_height)
        super().draw(TransformPen(ReverseContourPen(pen), flip), dc)
