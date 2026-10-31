from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm


class LowercaseXGlyph(Glyph):
    name = "lowercase_x"
    unicode = "0x78"
    offset = 0
    width_ratio = 1.1
    stroke_ratio = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset, width_ratio=self.width_ratio)
        s = self.stroke_ratio * dc.stroke_x
        draw_parallelogramm(pen, s, b.x1, b.y1, b.x2, b.y2)
        draw_parallelogramm(pen, s, b.x2, b.y1, b.x1, b.y2, direction="top-left")
