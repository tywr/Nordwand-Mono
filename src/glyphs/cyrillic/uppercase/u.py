from glyphs.cyrillic.uppercase import CyrillicUppercaseGlyph
from draw.parallelogramm import draw_parallelogramm


class CyrillicUppercaseUGlyph(CyrillicUppercaseGlyph):
    name = "cyrillic_uppercase_u"
    unicode = "0x0423"
    offset = 0
    width_ratio = 1.15
    stroke_ratio = 0.96
    dent_ratio = 00

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
            uppercase=True,
            height="cap",
        )
        dent_height = self.dent_ratio * b.height + abs(dc.descent)
        sx = self.diag_stroke_dampening(self.stroke_ratio, dc.stroke_x, coef=0.0)
        ov = sx / 2

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
        h2 = b.height - abs(dc.descent)
        dx_tail = -(w2 - sx) * abs(dc.descent) / h2
        draw_parallelogramm(
            pen,
            sx,
            sx,
            b.xmid - ov + delta,
            b.y1 + abs(dc.descent),
            b.xmid - ov + dx_tail,
            b.y1,
            direction="bottom-left",
            delta=sx,
        )
