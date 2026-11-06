from glyphs.latin.lowercase.gamma import draw_gamma
from glyphs.uppercase import UppercaseGlyph


class LatinUppercaseGammaGlyph(UppercaseGlyph):
    """V whose branches cross and close in a loop below the baseline (Ɣ)."""

    name = "latin_uppercase_gamma"
    unicode = "0x194"
    offset = 0
    width_ratio = 1.2
    branch_stroke_ratio = 1
    loop_width = 0.75  # Relative to the body width
    loop_depth = 1  # Relative to the descent

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, width_ratio=self.width_ratio, height="cap"
        )
        draw_gamma(
            pen,
            dc,
            b,
            self.branch_stroke_ratio * dc.stroke_x,
            dc.stroke_x * self.stroke_x_ratio,
            dc.stroke_y * self.stroke_y_ratio,
            self.loop_width,
            self.loop_depth * dc.descent,
        )
