"""Composed glyphs with the tilde."""

from config import FontConfig as fc
from glyphs.composed import ComposedGlyph
from glyphs.lowercase.a import LowercaseAGlyph
from glyphs.lowercase.round.o import LowercaseOGlyph
from glyphs.lowercase.square.u import LowercaseUGlyph
from glyphs.lowercase.square.n import LowercaseNGlyph
from glyphs.lowercase.dotted.i import LowercaseIGlyph
from glyphs.uppercase.a import UppercaseAGlyph
from glyphs.uppercase.i import UppercaseIGlyph
from glyphs.uppercase.o import UppercaseOGlyph
from glyphs.uppercase.u import UppercaseUGlyph
from glyphs.uppercase.n import UppercaseNGlyph
from glyphs.accents.tilde import Tilde

_lc_accent = fc.accent
_uc_accent = fc.accent_cap


class LowercaseATildeGlyph(ComposedGlyph):
    name = "lowercase_atilde"
    unicode = "0xE3"
    base_glyph_class = LowercaseAGlyph
    accent_class = Tilde
    accent_y = _lc_accent


class LowercaseNTildeGlyph(ComposedGlyph):
    name = "lowercase_ntilde"
    unicode = "0xF1"
    base_glyph_class = LowercaseNGlyph
    accent_class = Tilde
    accent_y = _lc_accent


class LowercaseOTildeGlyph(ComposedGlyph):
    name = "lowercase_otilde"
    unicode = "0xF5"
    base_glyph_class = LowercaseOGlyph
    accent_class = Tilde
    accent_y = _lc_accent


class UppercaseATildeGlyph(ComposedGlyph):
    name = "uppercase_atilde"
    unicode = "0xC3"
    base_glyph_class = UppercaseAGlyph
    accent_class = Tilde
    accent_y = _uc_accent


class UppercaseNTildeGlyph(ComposedGlyph):
    name = "uppercase_ntilde"
    unicode = "0xD1"
    base_glyph_class = UppercaseNGlyph
    accent_class = Tilde
    accent_y = _uc_accent


class UppercaseOTildeGlyph(ComposedGlyph):
    name = "uppercase_otilde"
    unicode = "0xD5"
    base_glyph_class = UppercaseOGlyph
    accent_class = Tilde
    accent_y = _uc_accent


class LowercaseITildeGlyph(ComposedGlyph):
    name = "lowercase_itilde"
    unicode = "0x129"
    base_glyph_class = LowercaseIGlyph
    accent_class = Tilde
    accent_y = _lc_accent


class UppercaseITildeGlyph(ComposedGlyph):
    name = "uppercase_itilde"
    unicode = "0x128"
    base_glyph_class = UppercaseIGlyph
    accent_class = Tilde
    accent_y = _uc_accent


class LowercaseUTildeGlyph(ComposedGlyph):
    name = "lowercase_utilde"
    unicode = "0x169"
    base_glyph_class = LowercaseUGlyph
    accent_class = Tilde
    accent_y = _lc_accent


class UppercaseUTildeGlyph(ComposedGlyph):
    name = "uppercase_utilde"
    unicode = "0x168"
    base_glyph_class = UppercaseUGlyph
    accent_class = Tilde
    accent_y = _uc_accent
