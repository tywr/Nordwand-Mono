"""Composed glyphs with the dieresis stacked with a second accent."""

from config import FontConfig as fc
from glyphs.composed import ComposedGlyph
from glyphs.lowercase.square.u import LowercaseUGlyph
from glyphs.uppercase.u import UppercaseUGlyph
from glyphs.accents.dieresis_stacked import (
    DieresisMacron,
    DieresisAcute,
    DieresisCaron,
    DieresisGrave,
)

# Raised so the dots clear the x-height
_lc_accent = fc.accent + 0.1 * fc.x_height
_uc_accent = fc.accent_cap


class UppercaseUDieresisMacronGlyph(ComposedGlyph):
    name = "uppercase_udieresismacron"
    unicode = "0x1D5"
    base_glyph_class = UppercaseUGlyph
    accent_class = DieresisMacron
    accent_y = _uc_accent


class UppercaseUDieresisAcuteGlyph(ComposedGlyph):
    name = "uppercase_udieresisacute"
    unicode = "0x1D7"
    base_glyph_class = UppercaseUGlyph
    accent_class = DieresisAcute
    accent_y = _uc_accent


class UppercaseUDieresisCaronGlyph(ComposedGlyph):
    name = "uppercase_udieresiscaron"
    unicode = "0x1D9"
    base_glyph_class = UppercaseUGlyph
    accent_class = DieresisCaron
    accent_y = _uc_accent


class UppercaseUDieresisGraveGlyph(ComposedGlyph):
    name = "uppercase_udieresisgrave"
    unicode = "0x1DB"
    base_glyph_class = UppercaseUGlyph
    accent_class = DieresisGrave
    accent_y = _uc_accent


class LowercaseUDieresisMacronGlyph(ComposedGlyph):
    name = "lowercase_udieresismacron"
    unicode = "0x1D6"
    base_glyph_class = LowercaseUGlyph
    accent_class = DieresisMacron
    accent_y = _lc_accent


class LowercaseUDieresisAcuteGlyph(ComposedGlyph):
    name = "lowercase_udieresisacute"
    unicode = "0x1D8"
    base_glyph_class = LowercaseUGlyph
    accent_class = DieresisAcute
    accent_y = _lc_accent


class LowercaseUDieresisCaronGlyph(ComposedGlyph):
    name = "lowercase_udieresiscaron"
    unicode = "0x1DA"
    base_glyph_class = LowercaseUGlyph
    accent_class = DieresisCaron
    accent_y = _lc_accent


class LowercaseUDieresisGraveGlyph(ComposedGlyph):
    name = "lowercase_udieresisgrave"
    unicode = "0x1DC"
    base_glyph_class = LowercaseUGlyph
    accent_class = DieresisGrave
    accent_y = _lc_accent
