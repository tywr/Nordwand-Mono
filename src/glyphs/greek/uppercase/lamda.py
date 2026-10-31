from glyphs.uppercase.a import UppercaseAGlyph


class GreekUppercaseLamdaGlyph(UppercaseAGlyph):
    """The A without its crossbar"""

    name = "greek_uppercase_lamda"
    unicode = "0x39B"

    def draw(self, pen, dc):
        self.draw_branches(pen, dc, self.body(dc))
