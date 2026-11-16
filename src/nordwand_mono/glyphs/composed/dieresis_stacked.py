"""Composed glyphs with the dieresis stacked with a second accent."""

from nordwand_mono.config import FontConfig as fc
from nordwand_mono.glyphs.composed import ComposedGlyph
from nordwand_mono.glyphs.lowercase.square.u import LowercaseUGlyph
from nordwand_mono.glyphs.uppercase.u import UppercaseUGlyph
from nordwand_mono.glyphs.accents.dieresis_stacked_lowercase import (
    LowercaseDieresisMacron,
    LowercaseDieresisAcute,
    LowercaseDieresisCaron,
    LowercaseDieresisGrave,
)
from nordwand_mono.glyphs.accents.dieresis_stacked_uppercase import (
    UppercaseDieresisMacron,
    UppercaseDieresisAcute,
    UppercaseDieresisCaron,
    UppercaseDieresisGrave,
)

# Raised so the dots clear the x-height
_lc_accent = fc.accent + 0.1 * fc.x_height
_uc_accent = fc.accent_cap


class UppercaseUDieresisMacronGlyph(ComposedGlyph):
    name = "uppercase_udieresismacron"
    unicode = "0x1D5"
    base_glyph_class = UppercaseUGlyph
    accent_class = UppercaseDieresisMacron
    accent_y = _uc_accent


class UppercaseUDieresisAcuteGlyph(ComposedGlyph):
    name = "uppercase_udieresisacute"
    unicode = "0x1D7"
    base_glyph_class = UppercaseUGlyph
    accent_class = UppercaseDieresisAcute
    accent_y = _uc_accent


class UppercaseUDieresisCaronGlyph(ComposedGlyph):
    name = "uppercase_udieresiscaron"
    unicode = "0x1D9"
    base_glyph_class = UppercaseUGlyph
    accent_class = UppercaseDieresisCaron
    accent_y = _uc_accent


class UppercaseUDieresisGraveGlyph(ComposedGlyph):
    name = "uppercase_udieresisgrave"
    unicode = "0x1DB"
    base_glyph_class = UppercaseUGlyph
    accent_class = UppercaseDieresisGrave
    accent_y = _uc_accent


class LowercaseUDieresisMacronGlyph(ComposedGlyph):
    name = "lowercase_udieresismacron"
    unicode = "0x1D6"
    base_glyph_class = LowercaseUGlyph
    accent_class = LowercaseDieresisMacron
    accent_y = _lc_accent


class LowercaseUDieresisAcuteGlyph(ComposedGlyph):
    name = "lowercase_udieresisacute"
    unicode = "0x1D8"
    base_glyph_class = LowercaseUGlyph
    accent_class = LowercaseDieresisAcute
    accent_y = _lc_accent


class LowercaseUDieresisCaronGlyph(ComposedGlyph):
    name = "lowercase_udieresiscaron"
    unicode = "0x1DA"
    base_glyph_class = LowercaseUGlyph
    accent_class = LowercaseDieresisCaron
    accent_y = _lc_accent


class LowercaseUDieresisGraveGlyph(ComposedGlyph):
    name = "lowercase_udieresisgrave"
    unicode = "0x1DC"
    base_glyph_class = LowercaseUGlyph
    accent_class = LowercaseDieresisGrave
    accent_y = _lc_accent
