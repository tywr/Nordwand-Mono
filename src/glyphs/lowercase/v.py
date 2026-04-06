from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm


class LowercaseVGlyph(Glyph):
    name = "lowercase_v"
    unicode = "0x76"
    offset = 0
    width_ratio = 1.2
    overlap = 0.3

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset, width_ratio=self.width_ratio)
        ov = self.overlap * dc.stroke_x

        draw_parallelogramm(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.xmid - ov,
            0,
            b.x2,
            b.y2,
        )
        draw_parallelogramm(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.xmid + ov,
            0,
            b.x1,
            b.y2,
            direction="top-left",
        )
