from glyphs.cyrillic.uppercase import CyrillicUppercaseGlyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm


class CyrillicUppercaseZheGlyph(CyrillicUppercaseGlyph):
    name = "cyrillic_uppercase_zhe"
    unicode = "0x0416"
    offset = 0
    neck_ratio = 0.1
    top_ratio = 0.96
    width_ratio = 1.35
    branch_stroke_ratio = 1
    inner_stroke_ratio = 1.25

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            uppercase=True,
            width_ratio=self.width_ratio,
        )
        sy = dc.stroke_y * self.stroke_y_ratio
        sx = self.branch_stroke_ratio * dc.stroke_x
        sx = max(0, 0.8 * (sx - dc.default_stroke)) + min(dc.default_stroke, sx)
        ymid = dc.cap / 2
        dn = self.neck_ratio * b.width
        tx1 = b.x1 + (1 - self.top_ratio) * b.width / 2
        tx2 = b.x2 - (1 - self.top_ratio) * b.width / 2

        draw_rect(pen, b.xmid - sx / 2, 0, b.xmid + sx / 2, dc.cap)

        _, dr = draw_parallelogramm(
            pen, sx, tx1, dc.cap, b.xmid - dn, ymid, direction="bottom-right"
        )
        draw_parallelogramm(
            pen,
            sx,
            b.x1,
            0,
            b.xmid - dn,
            ymid,
            direction="top-right",
            overwrite_section=dr,
        )
        _, dl = draw_parallelogramm(
            pen, sx, tx2, dc.cap, b.xmid + dn, ymid, direction="bottom-left"
        )
        draw_parallelogramm(
            pen,
            sx,
            b.x2,
            0,
            b.xmid + dn,
            ymid,
            direction="top-left",
            overwrite_section=dl,
        )

        draw_rect(pen, b.xmid - dn - dl, ymid - sy / 2, b.xmid + dn + dr, ymid + sy / 2)
