from glyphs.lowercase.g_2 import LowercaseG2Glyph


class LowercaseG3Glyph(LowercaseG2Glyph):
    """Same design as lowercase_g_2, in both the regular and the italic."""

    name = "lowercase_g_3"
    font_feature = {"cv04": 2}
    regular_only = False
    alternative_character_comment = "Applies to both regular and italic fonts"
