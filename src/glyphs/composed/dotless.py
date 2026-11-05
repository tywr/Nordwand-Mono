"""Composed glyphs with the dotless letters."""

from glyphs.lowercase.dotted.i import LowercaseIGlyph
from glyphs.lowercase.dotted.i_2 import LowercaseI2Glyph


class LowercaseDotlessIGlyph(LowercaseIGlyph):
    name = "lowercase_dotlessi"
    unicode = "0x131"

    def draw(self, pen, dc):
        self.draw_base(pen, dc)


class LowercaseDotlessI2Glyph(LowercaseI2Glyph):
    name = "lowercase_dotlessi_2"
    unicode = "0x131"

    def draw(self, pen, dc):
        self.draw_base(pen, dc)
