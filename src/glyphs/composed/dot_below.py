"""Composed glyphs with the dot below."""

from glyphs.composed import ComposedGlyph
from glyphs.lowercase.a import LowercaseAGlyph
from glyphs.accents.dot_below import DotBelow


class LowercaseADotBelowGlyph(ComposedGlyph):
    name = "lowercase_adotbelow"
    unicode = "0x1EA1"
    base_glyph_class = LowercaseAGlyph
    accent_class = DotBelow
    accent_y = 0
