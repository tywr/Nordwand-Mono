"""Composed glyphs with the ring above."""

from nordwand_mono.config import FontConfig as fc
from nordwand_mono.glyphs.composed import ComposedGlyph
from nordwand_mono.glyphs.lowercase.a import LowercaseAGlyph
from nordwand_mono.glyphs.lowercase.square.u import LowercaseUGlyph
from nordwand_mono.glyphs.uppercase.diagonal.a import UppercaseAGlyph
from nordwand_mono.glyphs.uppercase.u import UppercaseUGlyph
from nordwand_mono.glyphs.accents.ring import Ring

_lc_accent = fc.accent
_uc_accent = fc.accent_cap


class LowercaseARingGlyph(ComposedGlyph):
    name = "lowercase_aring"
    unicode = "0xE5"
    base_glyph_class = LowercaseAGlyph
    accent_class = Ring
    accent_y = _lc_accent


class UppercaseARingGlyph(ComposedGlyph):
    name = "uppercase_aring"
    unicode = "0xC5"
    base_glyph_class = UppercaseAGlyph
    accent_class = Ring
    accent_y = _uc_accent


class LowercaseURingGlyph(ComposedGlyph):
    name = "lowercase_uring"
    unicode = "0x16F"
    base_glyph_class = LowercaseUGlyph
    accent_class = Ring
    accent_y = _lc_accent


class UppercaseURingGlyph(ComposedGlyph):
    name = "uppercase_uring"
    unicode = "0x16E"
    base_glyph_class = UppercaseUGlyph
    accent_class = Ring
    accent_y = _uc_accent
