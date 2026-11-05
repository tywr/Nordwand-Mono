"""Composed glyphs with the circumflex stacked with a second accent."""

from config import FontConfig as fc
from glyphs.composed import ComposedGlyph
from glyphs.lowercase.a import LowercaseAGlyph
from glyphs.accents.circumflex_stacked import (
    CircumflexAcute,
    CircumflexGrave,
    CircumflexHookAbove,
    CircumflexTilde,
    CircumflexDotBelow,
)

_lc_accent = fc.accent


class LowercaseACircumflexAcuteGlyph(ComposedGlyph):
    name = "lowercase_acircumflexacute"
    unicode = "0x1EA5"
    base_glyph_class = LowercaseAGlyph
    accent_class = CircumflexAcute
    accent_y = _lc_accent


class LowercaseACircumflexGraveGlyph(ComposedGlyph):
    name = "lowercase_acircumflexgrave"
    unicode = "0x1EA7"
    base_glyph_class = LowercaseAGlyph
    accent_class = CircumflexGrave
    accent_y = _lc_accent


class LowercaseACircumflexHookAboveGlyph(ComposedGlyph):
    name = "lowercase_acircumflexhookabove"
    unicode = "0x1EA9"
    base_glyph_class = LowercaseAGlyph
    accent_class = CircumflexHookAbove
    accent_y = _lc_accent


class LowercaseACircumflexTildeGlyph(ComposedGlyph):
    name = "lowercase_acircumflextilde"
    unicode = "0x1EAB"
    base_glyph_class = LowercaseAGlyph
    accent_class = CircumflexTilde
    accent_y = _lc_accent


class LowercaseACircumflexDotBelowGlyph(ComposedGlyph):
    name = "lowercase_acircumflexdotbelow"
    unicode = "0x1EAD"
    base_glyph_class = LowercaseAGlyph
    accent_class = CircumflexDotBelow
    accent_y = _lc_accent
