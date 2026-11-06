"""Composed glyphs with the circumflex stacked with a second accent."""

from config import FontConfig as fc
from glyphs.composed import ComposedGlyph
from glyphs.lowercase.a import LowercaseAGlyph
from glyphs.accents.circumflex_stacked_lowercase import (
    LowercaseCircumflexAcute,
    LowercaseCircumflexGrave,
    LowercaseCircumflexHookAbove,
    LowercaseCircumflexTilde,
    LowercaseCircumflexDotBelow,
)
from glyphs.accents.circumflex_stacked_uppercase import (
    UppercaseCircumflexAcute,
    UppercaseCircumflexGrave,
    UppercaseCircumflexHookAbove,
    UppercaseCircumflexTilde,
    UppercaseCircumflexDotBelow,
)
from glyphs.lowercase.round.e import LowercaseEGlyph
from glyphs.lowercase.round.o import LowercaseOGlyph
from glyphs.uppercase.e import UppercaseEGlyph
from glyphs.uppercase.a import UppercaseAGlyph
from glyphs.uppercase.o import UppercaseOGlyph

_lc_accent = fc.accent
_uc_accent = fc.accent_cap


class LowercaseCircumflexAcuteGlyph(ComposedGlyph):
    accent_class = LowercaseCircumflexAcute
    accent_y = _lc_accent


class LowercaseACircumflexAcuteGlyph(LowercaseCircumflexAcuteGlyph):
    name = "lowercase_acircumflexacute"
    unicode = "0x1EA5"
    base_glyph_class = LowercaseAGlyph


class LowercaseECircumflexAcuteGlyph(LowercaseCircumflexAcuteGlyph):
    name = "lowercase_ecircumflexacute"
    unicode = "0x1EBF"
    base_glyph_class = LowercaseEGlyph


class LowercaseOCircumflexAcuteGlyph(LowercaseCircumflexAcuteGlyph):
    name = "lowercase_ocircumflexacute"
    unicode = "0x1ED1"
    base_glyph_class = LowercaseOGlyph


class UppercaseCircumflexAcuteGlyph(ComposedGlyph):
    accent_class = UppercaseCircumflexAcute
    accent_y = _uc_accent


class UppercaseECircumflexAcuteGlyph(UppercaseCircumflexAcuteGlyph):
    name = "uppercase_ecircumflexacute"
    unicode = "0x1EBE"
    base_glyph_class = UppercaseEGlyph


class UppercaseACircumflexAcuteGlyph(UppercaseCircumflexAcuteGlyph):
    name = "uppercase_acircumflexacute"
    unicode = "0x1EA4"
    base_glyph_class = UppercaseAGlyph


class UppercaseOCircumflexAcuteGlyph(UppercaseCircumflexAcuteGlyph):
    name = "uppercase_ocircumflexacute"
    unicode = "0x1ED0"
    base_glyph_class = UppercaseOGlyph


class LowercaseCircumflexGraveGlyph(ComposedGlyph):
    accent_class = LowercaseCircumflexGrave
    accent_y = _lc_accent


class LowercaseACircumflexGraveGlyph(LowercaseCircumflexGraveGlyph):
    name = "lowercase_acircumflexgrave"
    unicode = "0x1EA7"
    base_glyph_class = LowercaseAGlyph


class LowercaseECircumflexGraveGlyph(LowercaseCircumflexGraveGlyph):
    name = "lowercase_ecircumflexgrave"
    unicode = "0x1EC1"
    base_glyph_class = LowercaseEGlyph


class LowercaseOCircumflexGraveGlyph(LowercaseCircumflexGraveGlyph):
    name = "lowercase_ocircumflexgrave"
    unicode = "0x1ED3"
    base_glyph_class = LowercaseOGlyph


class UppercaseCircumflexGraveGlyph(ComposedGlyph):
    accent_class = UppercaseCircumflexGrave
    accent_y = _uc_accent


class UppercaseECircumflexGraveGlyph(UppercaseCircumflexGraveGlyph):
    name = "uppercase_ecircumflexgrave"
    unicode = "0x1EC0"
    base_glyph_class = UppercaseEGlyph


class UppercaseACircumflexGraveGlyph(UppercaseCircumflexGraveGlyph):
    name = "uppercase_acircumflexgrave"
    unicode = "0x1EA6"
    base_glyph_class = UppercaseAGlyph


class UppercaseOCircumflexGraveGlyph(UppercaseCircumflexGraveGlyph):
    name = "uppercase_ocircumflexgrave"
    unicode = "0x1ED2"
    base_glyph_class = UppercaseOGlyph


class LowercaseCircumflexHookAboveGlyph(ComposedGlyph):
    accent_class = LowercaseCircumflexHookAbove
    accent_y = _lc_accent


class LowercaseACircumflexHookAboveGlyph(LowercaseCircumflexHookAboveGlyph):
    name = "lowercase_acircumflexhookabove"
    unicode = "0x1EA9"
    base_glyph_class = LowercaseAGlyph


class LowercaseECircumflexHookAboveGlyph(LowercaseCircumflexHookAboveGlyph):
    name = "lowercase_ecircumflexhookabove"
    unicode = "0x1EC3"
    base_glyph_class = LowercaseEGlyph


class LowercaseOCircumflexHookAboveGlyph(LowercaseCircumflexHookAboveGlyph):
    name = "lowercase_ocircumflexhookabove"
    unicode = "0x1ED5"
    base_glyph_class = LowercaseOGlyph


class UppercaseCircumflexHookAboveGlyph(ComposedGlyph):
    accent_class = UppercaseCircumflexHookAbove
    accent_y = _uc_accent


class UppercaseECircumflexHookAboveGlyph(UppercaseCircumflexHookAboveGlyph):
    name = "uppercase_ecircumflexhookabove"
    unicode = "0x1EC2"
    base_glyph_class = UppercaseEGlyph


class UppercaseACircumflexHookAboveGlyph(UppercaseCircumflexHookAboveGlyph):
    name = "uppercase_acircumflexhookabove"
    unicode = "0x1EA8"
    base_glyph_class = UppercaseAGlyph


class UppercaseOCircumflexHookAboveGlyph(UppercaseCircumflexHookAboveGlyph):
    name = "uppercase_ocircumflexhookabove"
    unicode = "0x1ED4"
    base_glyph_class = UppercaseOGlyph


class LowercaseCircumflexTildeGlyph(ComposedGlyph):
    accent_class = LowercaseCircumflexTilde
    accent_y = _lc_accent


class LowercaseACircumflexTildeGlyph(LowercaseCircumflexTildeGlyph):
    name = "lowercase_acircumflextilde"
    unicode = "0x1EAB"
    base_glyph_class = LowercaseAGlyph


class LowercaseECircumflexTildeGlyph(LowercaseCircumflexTildeGlyph):
    name = "lowercase_ecircumflextilde"
    unicode = "0x1EC5"
    base_glyph_class = LowercaseEGlyph


class LowercaseOCircumflexTildeGlyph(LowercaseCircumflexTildeGlyph):
    name = "lowercase_ocircumflextilde"
    unicode = "0x1ED7"
    base_glyph_class = LowercaseOGlyph


class UppercaseCircumflexTildeGlyph(ComposedGlyph):
    accent_class = UppercaseCircumflexTilde
    accent_y = _uc_accent


class UppercaseECircumflexTildeGlyph(UppercaseCircumflexTildeGlyph):
    name = "uppercase_ecircumflextilde"
    unicode = "0x1EC4"
    base_glyph_class = UppercaseEGlyph


class UppercaseACircumflexTildeGlyph(UppercaseCircumflexTildeGlyph):
    name = "uppercase_acircumflextilde"
    unicode = "0x1EAA"
    base_glyph_class = UppercaseAGlyph


class UppercaseOCircumflexTildeGlyph(UppercaseCircumflexTildeGlyph):
    name = "uppercase_ocircumflextilde"
    unicode = "0x1ED6"
    base_glyph_class = UppercaseOGlyph


class LowercaseCircumflexDotBelowGlyph(ComposedGlyph):
    accent_class = LowercaseCircumflexDotBelow
    accent_y = _lc_accent


class LowercaseACircumflexDotBelowGlyph(LowercaseCircumflexDotBelowGlyph):
    name = "lowercase_acircumflexdotbelow"
    unicode = "0x1EAD"
    base_glyph_class = LowercaseAGlyph


class LowercaseECircumflexDotBelowGlyph(LowercaseCircumflexDotBelowGlyph):
    name = "lowercase_ecircumflexdotbelow"
    unicode = "0x1EC7"
    base_glyph_class = LowercaseEGlyph


class LowercaseOCircumflexDotBelowGlyph(LowercaseCircumflexDotBelowGlyph):
    name = "lowercase_ocircumflexdotbelow"
    unicode = "0x1ED9"
    base_glyph_class = LowercaseOGlyph


class UppercaseCircumflexDotBelowGlyph(ComposedGlyph):
    accent_class = UppercaseCircumflexDotBelow
    accent_y = _uc_accent


class UppercaseECircumflexDotBelowGlyph(UppercaseCircumflexDotBelowGlyph):
    name = "uppercase_ecircumflexdotbelow"
    unicode = "0x1EC6"
    base_glyph_class = UppercaseEGlyph


class UppercaseACircumflexDotBelowGlyph(UppercaseCircumflexDotBelowGlyph):
    name = "uppercase_acircumflexdotbelow"
    unicode = "0x1EAC"
    base_glyph_class = UppercaseAGlyph


class UppercaseOCircumflexDotBelowGlyph(UppercaseCircumflexDotBelowGlyph):
    name = "uppercase_ocircumflexdotbelow"
    unicode = "0x1ED8"
    base_glyph_class = UppercaseOGlyph
