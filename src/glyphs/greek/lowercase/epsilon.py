from fontTools.pens.reverseContourPen import ReverseContourPen
from fontTools.pens.transformPen import TransformPen
from glyphs.cyrillic.lowercase.ze import CyrillicLowercaseZeGlyph


class GreekLowercaseEpsilonGlyph(CyrillicLowercaseZeGlyph):
    """The cyrillic ze mirrored horizontally"""

    name = "greek_lowercase_epsilon"
    unicode = "0x3B5"

    def draw(self, pen, dc):
        # Mirroring flips the contours direction, reverse them back
        mirror = (-1, 0, 0, 1, dc.window_width, 0)
        super().draw(TransformPen(ReverseContourPen(pen), mirror), dc)
