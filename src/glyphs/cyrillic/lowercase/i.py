from glyphs.cyrillic.uppercase.i import CyrillicUppercaseIGlyph


class CyrillicLowercaseIGlyph(CyrillicUppercaseIGlyph):
    """The mirrored N of the uppercase, at the x-height."""

    name = "cyrillic_lowercase_i"
    unicode = "0x0438"
    width_ratio = 1.0
    height = "x_height"
