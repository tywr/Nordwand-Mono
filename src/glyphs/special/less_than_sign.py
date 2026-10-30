from glyphs import Glyph
from glyphs.special.greater_than_sign import GreaterThenSignGlyph
from draw.chevron import draw_chevron


class LessThenSignGlyph(Glyph):
    name = "less_than_sign"
    unicode = "0x3C"
    offset = 0
    width_ratio = 1
    overlap = 0.6
    span = GreaterThenSignGlyph.span
    stroke_ratio = 1.45

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        h = dc.parenthesis_length * self.span
        s = self.diag_stroke_dampening(self.stroke_ratio, dc.stroke_x, coef=0.2)
        draw_chevron(pen, s, s, b.x1, b.x2, dc.math, h, delta=s)
