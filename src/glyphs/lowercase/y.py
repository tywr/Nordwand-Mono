from math import tan
from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm


class LowercaseYGlyph(Glyph):
    name = "lowercase_y"
    unicode = "0x79"
    offset = 0
    width_ratio = 1.15
    stroke_ratio = 0.96
    overlap = 0.5
    dent_ratio = 00

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset, width_ratio=self.width_ratio)
        dent_height = self.dent_ratio * b.height
        ov = self.overlap * dc.stroke_x
        sx = self.diag_stroke_dampening(self.stroke_ratio, dc.stroke_x, coef=0.0)

        draw_parallelogramm(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.xmid + ov,
            dent_height,
            b.x1,
            b.y2,
            delta=sx,
            direction="top-left",
        )
        theta, delta = draw_parallelogramm(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.xmid - ov,
            dent_height,
            b.x2,
            b.y2,
            delta=sx,
        )
        w2 = b.x2 - (b.xmid - ov)
        h2 = b.y2 - b.y1
        dx_tail = -(w2 - sx) * abs(dc.descent) / h2
        draw_parallelogramm(
            pen,
            sx,
            sx,
            b.xmid - ov + delta,
            b.y1,
            b.xmid - ov + dx_tail,
            dc.descent,
            direction="bottom-left",
            delta=sx,
        )
