"""Composed glyphs with the Polish diagonal stroke (ł Ł)."""

from config import FontConfig as fc
from glyphs.composed import ComposedGlyph
from glyphs.lowercase.l import LowercaseLGlyph
from glyphs.uppercase.l import UppercaseLGlyph
from glyphs.accents.stroke import Stroke, UppercaseStroke


class LowercaseLStrokeGlyph(ComposedGlyph):
    name = "lowercase_lslash"
    unicode = "0x142"
    base_glyph_class = LowercaseLGlyph
    accent_class = Stroke
    accent_y = 0.55 * fc.ascent

    def accent_x(self, dc, base, b):
        return base.stem_center(dc)


class UppercaseLStrokeGlyph(ComposedGlyph):
    name = "uppercase_lslash"
    unicode = "0x141"
    base_glyph_class = UppercaseLGlyph
    accent_class = UppercaseStroke
    accent_y = 0.45 * fc.cap

    def accent_x(self, dc, base, b):
        return base.stem_center(dc)
