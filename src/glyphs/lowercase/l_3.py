from glyphs.lowercase.l_2 import LowercaseL2Glyph


class LowercaseL3Glyph(LowercaseL2Glyph):
    """Same design as lowercase_l_2, in both the regular and the italic."""

    name = "lowercase_l_3"
    font_feature = {"cv03": 2}
    regular_only = False
    alternative_character_comment = "Applies to both regular and italic fonts"
