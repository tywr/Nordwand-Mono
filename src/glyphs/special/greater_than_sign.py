from glyphs import Glyph
from draw.chevron import draw_chevron


class GreaterThenSignGlyph(Glyph):
    name = "greater_than_sign"
    unicode = "0x3E"
    offset = 0
    width_ratio = 1
    overlap = 0.6
    span = 0.50
    stroke_ratio = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        h = dc.parenthesis_length * self.span
        s = dc.stroke_x * self.stroke_ratio
        draw_chevron(pen, s, b.x2, b.x1, dc.math, h)
