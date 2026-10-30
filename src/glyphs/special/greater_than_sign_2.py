from glyphs.special.greater_than_sign import GreaterThenSignGlyph


class GreaterThenSign2Glyph(GreaterThenSignGlyph):
    name = "greater_than_sign_2"
    font_feature = {"ss03": 1}
    alternative_character_comment = "Also changes the `->` and `=>` arrows"
    span = 0.85
    stroke_ratio = 1.25
