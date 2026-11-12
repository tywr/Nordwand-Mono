from glyphs.lowercase.f import LowercaseF2Glyph


class FlorinSignGlyph(LowercaseF2Glyph):
    """The descending italic f, used in both the upright and italic fonts, with
    the crossbar centered between the descender and the x-height."""

    name = "florin_sign"
    unicode = "0x192"
    default_italic = False

    def cross_bar_top(self, dc):
        return (dc.x_height - dc.descent) / 2 + dc.stroke_y / 2
