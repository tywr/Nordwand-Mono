from fontTools.pens.reverseContourPen import ReverseContourPen
from fontTools.pens.transformPen import TransformPen

from glyphs.greek.uppercase.omega import GreekUppercaseOmegaGlyph


class LatinUppercaseUpsilonGlyph(GreekUppercaseOmegaGlyph):
    """Ω turned upside down (Ʊ)."""

    name = "latin_uppercase_upsilon"
    unicode = "0x1B1"

    def draw(self, pen, dc):
        h = getattr(dc, self.body_height)
        # Mirrored around half the height; reversed to keep the contours' direction
        flipped = ReverseContourPen(TransformPen(pen, (1, 0, 0, -1, 0, h)))
        super().draw(flipped, dc)
