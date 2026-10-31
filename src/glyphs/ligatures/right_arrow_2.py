from glyphs.ligatures.right_arrow import RightArrowGlyph
from glyphs.special.greater_than_sign_2 import GreaterThenSign2Glyph


class RightArrow2Glyph(RightArrowGlyph):
    """Ligature glyph for -> with the wide `ss03` arrow head"""

    name = "right_arrow_liga_2"
    components = ["hyphen_minus", "greater_than_sign_2"]
    span = GreaterThenSign2Glyph.span
    stroke_ratio = 1.0
