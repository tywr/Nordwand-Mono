import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from draw.loop import draw_loop
from draw.rect import draw_rect
from glyphs.lowercase.round import RoundLowercaseGlyph


class LowercaseCGlyph(RoundLowercaseGlyph):
    name = "lowercase_c"
    unicode = "0x63"
    offset = 5
    opening1 = 0.31
    opening2 = 0.685
    width_ratio = 0.99
    right_hx_ratio = 1.2

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
        ec = self.extra_cut(dc)
        yc1 = b.y1 + b.height * self.opening1 + ec
        yc2 = b.y1 + b.height * self.opening2 - ec

        draw_loop(pen, sx, sy, b.x1, b.y1, b.x2, b.y2, b.hx, b.hy, cut="right")

        glyph = ufoLib2.objects.Glyph()
        draw_loop(
            glyph.getPen(),
            sx,
            sy,
            b.x1,
            b.y1,
            b.x2,
            b.y2,
            b.hx * self.right_hx_ratio,
            b.hy,
            cut="left",
        )
        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            b.xmid,
            yc1,
            b.x2 + 10,
            yc2,
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)
