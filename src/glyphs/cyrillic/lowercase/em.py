from glyphs.uppercase.m import UppercaseMGlyph


class CyrillicLowercaseEmGlyph(UppercaseMGlyph):
    """The uppercase M at x-height: same diagonals, ink traps and section cut"""

    name = "cyrillic_lowercase_em"
    unicode = "0x043C"
    offset = 0
    width_ratio = 1.08

    def body(self, dc):
        return dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
            min_margin=dc.min_margin_uppercase,
        )
