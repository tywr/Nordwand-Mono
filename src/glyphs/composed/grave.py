"""Composed glyphs with the grave."""

from config import FontConfig as fc
from glyphs.composed import ComposedGlyph
from glyphs.lowercase.a import LowercaseAGlyph
from glyphs.lowercase.round.e import LowercaseEGlyph
from glyphs.lowercase.round.o import LowercaseOGlyph
from glyphs.lowercase.square.u import LowercaseUGlyph
from glyphs.lowercase.dotted.i import LowercaseIGlyph
from glyphs.lowercase.y import LowercaseYGlyph
from glyphs.lowercase.w import LowercaseWGlyph
from glyphs.uppercase.a import UppercaseAGlyph
from glyphs.uppercase.e import UppercaseEGlyph
from glyphs.uppercase.i import UppercaseIGlyph
from glyphs.uppercase.o import UppercaseOGlyph
from glyphs.uppercase.u import UppercaseUGlyph
from glyphs.uppercase.y import UppercaseYGlyph
from glyphs.uppercase.w import UppercaseWGlyph
from glyphs.accents.grave import Grave

_lc_accent = fc.accent
_uc_accent = fc.accent_cap


class LowercaseAGraveGlyph(ComposedGlyph):
    name = "lowercase_agrave"
    unicode = "0xE0"
    base_glyph_class = LowercaseAGlyph
    accent_class = Grave
    accent_y = _lc_accent


class LowercaseEGraveGlyph(ComposedGlyph):
    name = "lowercase_egrave"
    unicode = "0xE8"
    base_glyph_class = LowercaseEGlyph
    accent_class = Grave
    accent_y = _lc_accent


class LowercaseIGraveGlyph(ComposedGlyph):
    name = "lowercase_igrave"
    unicode = "0xEC"
    base_glyph_class = LowercaseIGlyph
    accent_class = Grave
    accent_y = _lc_accent


class LowercaseOGraveGlyph(ComposedGlyph):
    name = "lowercase_ograve"
    unicode = "0xF2"
    base_glyph_class = LowercaseOGlyph
    accent_class = Grave
    accent_y = _lc_accent


class LowercaseUGraveGlyph(ComposedGlyph):
    name = "lowercase_ugrave"
    unicode = "0xF9"
    base_glyph_class = LowercaseUGlyph
    accent_class = Grave
    accent_y = _lc_accent


class UppercaseAGraveGlyph(ComposedGlyph):
    name = "uppercase_agrave"
    unicode = "0xC0"
    base_glyph_class = UppercaseAGlyph
    accent_class = Grave
    accent_y = _uc_accent


class UppercaseEGraveGlyph(ComposedGlyph):
    name = "uppercase_egrave"
    unicode = "0xC8"
    base_glyph_class = UppercaseEGlyph
    accent_class = Grave
    accent_y = _uc_accent


class UppercaseIGraveGlyph(ComposedGlyph):
    name = "uppercase_igrave"
    unicode = "0xCC"
    base_glyph_class = UppercaseIGlyph
    accent_class = Grave
    accent_y = _uc_accent


class UppercaseOGraveGlyph(ComposedGlyph):
    name = "uppercase_ograve"
    unicode = "0xD2"
    base_glyph_class = UppercaseOGlyph
    accent_class = Grave
    accent_y = _uc_accent


class UppercaseUGraveGlyph(ComposedGlyph):
    name = "uppercase_ugrave"
    unicode = "0xD9"
    base_glyph_class = UppercaseUGlyph
    accent_class = Grave
    accent_y = _uc_accent


class LowercaseWGraveGlyph(ComposedGlyph):
    name = "lowercase_wgrave"
    unicode = "0x1E81"
    base_glyph_class = LowercaseWGlyph
    accent_class = Grave
    accent_y = _lc_accent


class UppercaseWGraveGlyph(ComposedGlyph):
    name = "uppercase_wgrave"
    unicode = "0x1E80"
    base_glyph_class = UppercaseWGlyph
    accent_class = Grave
    accent_y = _uc_accent


class LowercaseYGraveGlyph(ComposedGlyph):
    name = "lowercase_ygrave"
    unicode = "0x1EF3"
    base_glyph_class = LowercaseYGlyph
    accent_class = Grave
    accent_y = _lc_accent


class UppercaseYGraveGlyph(ComposedGlyph):
    name = "uppercase_ygrave"
    unicode = "0x1EF2"
    base_glyph_class = UppercaseYGlyph
    accent_class = Grave
    accent_y = _uc_accent
