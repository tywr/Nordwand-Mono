"""Composed glyphs with the breve stacked with a second accent."""

from config import FontConfig as fc
from glyphs.composed import ComposedGlyph
from glyphs.lowercase.a import LowercaseAGlyph
from glyphs.uppercase.diagonal.a import UppercaseAGlyph
from glyphs.accents.breve_stacked_lowercase import (
    LowercaseBreveAcute,
    LowercaseBreveGrave,
    LowercaseBreveHookAbove,
    LowercaseBreveTilde,
    LowercaseBreveDotBelow,
)
from glyphs.accents.breve_stacked_uppercase import (
    UppercaseBreveAcute,
    UppercaseBreveGrave,
    UppercaseBreveHookAbove,
    UppercaseBreveTilde,
    UppercaseBreveDotBelow,
)

_lc_accent = fc.accent
_uc_accent = fc.accent_cap


class LowercaseBreveAcuteGlyph(ComposedGlyph):
    accent_class = LowercaseBreveAcute
    accent_y = _lc_accent


class LowercaseABreveAcuteGlyph(LowercaseBreveAcuteGlyph):
    name = "lowercase_abreveacute"
    unicode = "0x1EAF"
    base_glyph_class = LowercaseAGlyph


class UppercaseBreveAcuteGlyph(ComposedGlyph):
    accent_class = UppercaseBreveAcute
    accent_y = _uc_accent


class UppercaseABreveAcuteGlyph(UppercaseBreveAcuteGlyph):
    name = "uppercase_abreveacute"
    unicode = "0x1EAE"
    base_glyph_class = UppercaseAGlyph


class LowercaseBreveGraveGlyph(ComposedGlyph):
    accent_class = LowercaseBreveGrave
    accent_y = _lc_accent


class LowercaseABreveGraveGlyph(LowercaseBreveGraveGlyph):
    name = "lowercase_abrevegrave"
    unicode = "0x1EB1"
    base_glyph_class = LowercaseAGlyph


class UppercaseBreveGraveGlyph(ComposedGlyph):
    accent_class = UppercaseBreveGrave
    accent_y = _uc_accent


class UppercaseABreveGraveGlyph(UppercaseBreveGraveGlyph):
    name = "uppercase_abrevegrave"
    unicode = "0x1EB0"
    base_glyph_class = UppercaseAGlyph


class LowercaseBreveHookAboveGlyph(ComposedGlyph):
    accent_class = LowercaseBreveHookAbove
    accent_y = _lc_accent


class LowercaseABreveHookAboveGlyph(LowercaseBreveHookAboveGlyph):
    name = "lowercase_abrevehookabove"
    unicode = "0x1EB3"
    base_glyph_class = LowercaseAGlyph


class UppercaseBreveHookAboveGlyph(ComposedGlyph):
    accent_class = UppercaseBreveHookAbove
    accent_y = _uc_accent


class UppercaseABreveHookAboveGlyph(UppercaseBreveHookAboveGlyph):
    name = "uppercase_abrevehookabove"
    unicode = "0x1EB2"
    base_glyph_class = UppercaseAGlyph


class LowercaseBreveTildeGlyph(ComposedGlyph):
    accent_class = LowercaseBreveTilde
    accent_y = _lc_accent


class LowercaseABreveTildeGlyph(LowercaseBreveTildeGlyph):
    name = "lowercase_abrevetilde"
    unicode = "0x1EB5"
    base_glyph_class = LowercaseAGlyph


class UppercaseBreveTildeGlyph(ComposedGlyph):
    accent_class = UppercaseBreveTilde
    accent_y = _uc_accent


class UppercaseABreveTildeGlyph(UppercaseBreveTildeGlyph):
    name = "uppercase_abrevetilde"
    unicode = "0x1EB4"
    base_glyph_class = UppercaseAGlyph


class LowercaseBreveDotBelowGlyph(ComposedGlyph):
    accent_class = LowercaseBreveDotBelow
    accent_y = _lc_accent


class LowercaseABreveDotBelowGlyph(LowercaseBreveDotBelowGlyph):
    name = "lowercase_abrevedotbelow"
    unicode = "0x1EB7"
    base_glyph_class = LowercaseAGlyph


class UppercaseBreveDotBelowGlyph(ComposedGlyph):
    accent_class = UppercaseBreveDotBelow
    accent_y = _uc_accent


class UppercaseABreveDotBelowGlyph(UppercaseBreveDotBelowGlyph):
    name = "uppercase_abrevedotbelow"
    unicode = "0x1EB6"
    base_glyph_class = UppercaseAGlyph
