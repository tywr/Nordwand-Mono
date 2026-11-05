"""Composed glyphs with the breve stacked with a second accent."""

from config import FontConfig as fc
from glyphs.composed import ComposedGlyph
from glyphs.lowercase.a import LowercaseAGlyph
from glyphs.accents.breve_stacked import (
    BreveAcute,
    BreveGrave,
    BreveHookAbove,
    BreveTilde,
    BreveDotBelow,
)

_lc_accent = fc.accent


class LowercaseABreveAcuteGlyph(ComposedGlyph):
    name = "lowercase_abreveacute"
    unicode = "0x1EAF"
    base_glyph_class = LowercaseAGlyph
    accent_class = BreveAcute
    accent_y = _lc_accent


class LowercaseABreveGraveGlyph(ComposedGlyph):
    name = "lowercase_abrevegrave"
    unicode = "0x1EB1"
    base_glyph_class = LowercaseAGlyph
    accent_class = BreveGrave
    accent_y = _lc_accent


class LowercaseABreveHookAboveGlyph(ComposedGlyph):
    name = "lowercase_abrevehookabove"
    unicode = "0x1EB3"
    base_glyph_class = LowercaseAGlyph
    accent_class = BreveHookAbove
    accent_y = _lc_accent


class LowercaseABreveTildeGlyph(ComposedGlyph):
    name = "lowercase_abrevetilde"
    unicode = "0x1EB5"
    base_glyph_class = LowercaseAGlyph
    accent_class = BreveTilde
    accent_y = _lc_accent


class LowercaseABreveDotBelowGlyph(ComposedGlyph):
    name = "lowercase_abrevedotbelow"
    unicode = "0x1EB7"
    base_glyph_class = LowercaseAGlyph
    accent_class = BreveDotBelow
    accent_y = _lc_accent
