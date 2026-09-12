import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from draw.loop import draw_loop
from draw.rect import draw_rect
from draw.corner import draw_corner
from glyphs.lowercase.round import RoundLowercaseGlyph


class CyrillicLowercaseEGlyph(RoundLowercaseGlyph):
    name = "cyrillic_lowercase_e"
    unicode = "0x044d"
    offset = -5
    opening1 = 0.31
    opening2 = 0.685
    width_ratio = 0.99
    thinning = 1
    top_offset = 0.00
    right_hx_ratio = 1.2
    right_hy_ratio = 1
    mid_branch_ratio = 0.35
    mid_branch_y_ratio = 0.518

    def draw(self, pen, dc):

        b = dc.body_bounds(
            offset=self.offset,
            overshoot_bottom=True,
            overshoot_top=True,
            overshoot_left=True,
            overshoot_right=True,
            width_ratio=self.width_ratio,
        )
        sx, sy = self.stroke_x_ratio * dc.stroke_x, self.stroke_y_ratio * dc.stroke_y
        hx, hy = self.hx_ratio * b.hx, self.hy_ratio * b.hy
        rhx, rhy = self.right_hx_ratio * b.hx, self.right_hy_ratio * b.hy
        ec = self.extra_cut(dc)
        yc1 = b.y1 + b.height * self.opening1 + ec
        yc2 = b.y1 + b.height * self.opening2 - ec
        xt = b.x1 + self.top_offset * b.width
        xb = b.x1 + self.mid_branch_ratio * b.width
        yb = b.y1 + self.mid_branch_y_ratio * b.height

        draw_loop(pen, sx, sy, b.x1, b.y1, b.x2, b.y2, hx, hy, cut="left")

        glyph = ufoLib2.objects.Glyph()
        draw_corner(
            glyph.getPen(),
            sx * self.thinning,
            sy,
            xt,
            b.ymid,
            b.xmid,
            b.y2,
            rhx,
            rhy,
            orientation="top-right",
        )
        draw_corner(
            glyph.getPen(),
            sx * self.thinning,
            sy,
            b.x1,
            b.ymid,
            b.xmid,
            b.y1,
            rhx,
            rhy,
            orientation="bottom-right",
        )
        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            b.x1 - 10,
            yc1,
            b.xmid,
            yc2,
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)

        draw_rect(
            pen,
            xb,
            yb - sy / 2,
            b.x2 - sx / 2,
            yb + sy / 2,
        )
