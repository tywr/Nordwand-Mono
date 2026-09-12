from glyphs import Glyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm


class CyrillicLowercaseZheGlyph(Glyph):
    name = "cyrillic_lowercase_zhe"
    unicode = "0x0436"
    offset = 0
    neck_ratio = 0.1
    top_ratio = 0.96
    width_ratio = 1.35

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
        )
        sx, sy = dc.stroke_x, dc.stroke_y
        ymid = (b.y1 + b.y2) / 2
        dn = self.neck_ratio * b.width
        tx1 = b.x1 + (1 - self.top_ratio) * b.width / 2
        tx2 = b.x2 - (1 - self.top_ratio) * b.width / 2

        draw_rect(pen, b.xmid - sx / 2, 0, b.xmid + sx / 2, b.y2)

        theta, delta = draw_parallelogramm(
            pen, sx, sy, tx1, b.y2, b.xmid - dn, ymid, direction="bottom-right"
        )
        draw_parallelogramm(
            pen, sx, sy, b.x1, 0, b.xmid - dn, ymid, direction="top-right"
        )
        draw_parallelogramm(
            pen, sx, sy, tx2, b.y2, b.xmid + dn, ymid, direction="bottom-left"
        )
        draw_parallelogramm(
            pen, sx, sy, b.x2, 0, b.xmid + dn, ymid, direction="top-left"
        )

        draw_rect(
            pen, b.xmid - dn - delta, ymid - sy / 2, b.xmid + dn + delta, ymid + sy / 2
        )
