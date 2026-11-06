from fontTools.misc.transform import Transform
from fontTools.pens.reverseContourPen import ReverseContourPen
from fontTools.pens.transformPen import TransformPen
from glyphs.lowercase.v import LowercaseVGlyph


class LowercaseTurnedVGlyph(LowercaseVGlyph):
    """The v upside down. The italic keeps this pointed shape, as the round
    italic v would turn into an n-like arch."""

    name = "lowercase_turned_v"
    unicode = "0x28C"

    def draw(self, pen, dc):
        # The flip reverses the contours' direction, so wind them back
        flip = Transform(1, 0, 0, -1, 0, dc.x_height)
        super().draw(TransformPen(ReverseContourPen(pen), flip), dc)
