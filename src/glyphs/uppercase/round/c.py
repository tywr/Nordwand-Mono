from glyphs.uppercase.round import RoundUppercaseGlyph
from draw.loop import draw_loop
from draw.rect import draw_rect
import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph


class UppercaseCGlyph(RoundUppercaseGlyph):
    name = "uppercase_c"
    unicode = "0x43"
    offset = 6
    opening1 = 0.29
    width_ratio = 0.99

    def draw(self, pen, dc):
        b = self.body(dc)
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
