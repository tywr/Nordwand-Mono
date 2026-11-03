from fontTools.misc.transform import Transform
from fontTools.pens.reverseContourPen import ReverseContourPen
from fontTools.pens.transformPen import TransformPen

from glyphs.cyrillic.uppercase import CyrillicUppercaseGlyph
from glyphs.uppercase.n import UppercaseNGlyph


class CyrillicUppercaseIGlyph(UppercaseNGlyph, CyrillicUppercaseGlyph):
    """The N mirrored."""

    name = "cyrillic_uppercase_i"
    unicode = "0x0418"
    width_ratio = 1.08

    def draw(self, pen, dc):
        b = self.bounds(dc)
        mirror = Transform(-1, 0, 0, 1, b.x1 + b.x2, 0)
        super().draw(ReverseContourPen(TransformPen(pen, mirror)), dc)
