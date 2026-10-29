from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm


class GreekLowercaseLamdaGlyph(Glyph):
    """The y upside down: the legs stand on the baseline and the right one
    goes on up to the ascender"""

    name = "greek_lowercase_lamda"
    unicode = "0x3BB"
    offset = 0
    width_ratio = 1.15
    stroke_ratio = 0.96
    junction_ratio = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset, width_ratio=self.width_ratio)
        yj = dc.x_height
        sx = self.diag_stroke_dampening(self.stroke_ratio, dc.stroke_x, coef=0.0)
        ov = sx / 2

        draw_parallelogramm(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.xmid + ov,
            yj,
            b.x1,
            0,
            delta=sx,
            direction="bottom-left",
        )
        theta, delta = draw_parallelogramm(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.xmid - ov,
            yj,
            b.x2,
            0,
            delta=sx,
            direction="bottom-right",
        )
        w2 = b.x2 - (b.xmid - ov)
        dx_tail = -(w2 - sx) * (dc.ascent - yj) / yj
        draw_parallelogramm(
            pen,
            sx,
            sx,
            b.xmid - ov + delta,
            yj,
            b.xmid - ov + dx_tail,
            dc.ascent,
            direction="top-left",
            delta=sx,
        )
