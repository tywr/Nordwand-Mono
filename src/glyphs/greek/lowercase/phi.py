import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph

from glyphs import Glyph
from draw.rect import draw_rect
from draw.loop import draw_loop


class GreekLowercasePhiGlyph(Glyph):
    name = "greek_lowercase_phi"
    unicode = "0x3C6"
    offset = 0
    width_ratio = 1.1
    stroke_x_ratio = 1.01
    stroke_y_ratio = 1.0
    left_opening = 0.28
    inner_stroke_ratio = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            overshoot_bottom=True,
            overshoot_top=True,
            overshoot_left=True,
            overshoot_right=True,
            width_ratio=self.width_ratio,
        )
        ec = self.extra_cut(dc)
        sx, sy = self.stroke_x_ratio * dc.stroke_x, self.stroke_y_ratio * dc.stroke_y
        six = self.inner_stroke_ratio * dc.stroke_alt
        xo = b.x1 + self.left_opening * b.width

        glyph = ufoLib2.objects.Glyph()
        draw_loop(glyph.getPen(), sx, sy, b.x1, b.y1, b.x2, b.y2, b.hx, b.hy)

        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            xo + ec,
            b.ymid,
            b.xmid,
            b.y2 + 10,
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)

        draw_rect(
            pen,
            b.xmid - six / 2,
            b.y1,
            b.xmid + six / 2,
            b.y2,
        )
        draw_rect(
            pen,
            b.xmid - dc.stroke_x / 2,
            dc.descent,
            b.xmid + dc.stroke_x / 2,
            0,
        )
