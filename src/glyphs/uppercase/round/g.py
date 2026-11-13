import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs.uppercase.round import RoundUppercaseGlyph
from draw.rect import draw_rect
from draw.loop import draw_loop


class UppercaseGGlyph(RoundUppercaseGlyph):
    name = "uppercase_g"
    unicode = "0x47"
    offset = 10
    opening1 = 0.51

    def draw(self, pen, dc):
        b = self.body(dc)
        sx, sy = self.stroke_x_ratio * dc.stroke_x, self.stroke_y_ratio * dc.stroke_y
        rhx, rhy = self.right_hx_ratio * b.hx, b.hy
        yc1 = b.y1 + b.height * self.opening1
        yc2 = b.y1 + b.height * self.opening2 - self.extra_cut(dc)
        ymid = b.y1 + self.opening1 * b.height

        glyph = ufoLib2.objects.Glyph()
        draw_loop(pen, sx, sy, b.x1, b.y1, b.x2, b.y2, b.hx, b.hy, cut="right")

        draw_loop(
            glyph.getPen(),
            sx,
            sy,
            b.x1,
            b.y1,
            b.x2,
            b.y2,
            rhx,
            rhy,
            cut="left"
        )

        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            b.xmid,
            yc1 - sy,
            b.x2 + 10,
            yc2,
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)

        draw_rect(
            pen,
            b.xmid,
            ymid - sy,
            b.x2,
            ymid,
        )
