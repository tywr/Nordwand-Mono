from glyphs.cyrillic.uppercase import CyrillicUppercaseGlyph
from draw.parallelogramm import draw_parallelogramm, parallelogramm_delta


class CyrillicUppercaseUGlyph(CyrillicUppercaseGlyph):
    name = "cyrillic_uppercase_u"
    unicode = "0x0423"
    offset = 0
    width_ratio = 1.15
    stroke_ratio = 0.89
    dent_ratio = 00

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
            uppercase=True,
            height="cap",
        )
        dent_height = self.dent_ratio * b.height + abs(dc.descent)
        s = self.stroke_ratio * dc.stroke_x
        # Both branches start at the same foot, delta wide
        d = parallelogramm_delta(s, b.xmid, dent_height, b.x2, b.y2)
        ov = d / 2

        draw_parallelogramm(
            pen, s, b.xmid + ov, dent_height, b.x1, b.y2, direction="top-left"
        )
        _, delta = draw_parallelogramm(pen, s, b.xmid - ov, dent_height, b.x2, b.y2)
        # Tail continuing the right branch below the baseline: same edges'
        # slope, so the same stroke gives it the same horizontal width
        w2 = b.x2 - (b.xmid - ov)
        h2 = b.height - abs(dc.descent)
        dx_tail = -(w2 - delta) * abs(dc.descent) / h2
        draw_parallelogramm(
            pen,
            s,
            b.xmid - ov + delta,
            b.y1 + abs(dc.descent),
            b.xmid - ov + dx_tail,
            b.y1,
            direction="bottom-left",
        )
