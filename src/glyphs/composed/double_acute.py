"""Composed glyphs with the double acute."""

from config import FontConfig as fc
from glyphs.composed import ComposedGlyph
from glyphs.lowercase.round.o import LowercaseOGlyph
from glyphs.lowercase.square.u import LowercaseUGlyph
from glyphs.uppercase.round.o import UppercaseOGlyph
from glyphs.uppercase.u import UppercaseUGlyph
from glyphs.accents.double_acute import DoubleAcute

_lc_accent = fc.accent
_uc_accent = fc.accent_cap


class LowercaseODoubleAcuteGlyph(ComposedGlyph):
    name = "lowercase_ohungarumlaut"
    unicode = "0x151"
    base_glyph_class = LowercaseOGlyph
    accent_class = DoubleAcute
    accent_y = _lc_accent


class UppercaseODoubleAcuteGlyph(ComposedGlyph):
    name = "uppercase_ohungarumlaut"
    unicode = "0x150"
    base_glyph_class = UppercaseOGlyph
    accent_class = DoubleAcute
    accent_y = _uc_accent


class LowercaseUDoubleAcuteGlyph(ComposedGlyph):
    name = "lowercase_uhungarumlaut"
    unicode = "0x171"
    base_glyph_class = LowercaseUGlyph
    accent_class = DoubleAcute
    accent_y = _lc_accent


class UppercaseUDoubleAcuteGlyph(ComposedGlyph):
    name = "uppercase_uhungarumlaut"
    unicode = "0x170"
    base_glyph_class = UppercaseUGlyph
    accent_class = DoubleAcute
    accent_y = _uc_accent
