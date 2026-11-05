"""Composed glyphs with the hook above."""

from config import FontConfig as fc
from glyphs.composed import ComposedGlyph
from glyphs.lowercase.a import LowercaseAGlyph
from glyphs.accents.hook_above import HookAbove

_lc_accent = fc.accent


class LowercaseAHookAboveGlyph(ComposedGlyph):
    name = "lowercase_ahookabove"
    unicode = "0x1EA3"
    base_glyph_class = LowercaseAGlyph
    accent_class = HookAbove
    accent_y = _lc_accent
