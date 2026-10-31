import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph

from draw.corner import draw_corner
from draw.loop import draw_loop
from draw.rect import draw_rect
from glyphs.greek.lowercase import TailedGreekLowercaseGlyph


class GreekLowercaseFinalSigmaGlyph(TailedGreekLowercaseGlyph):
    """The top and left part of the c, ending with the tail"""

    name = "greek_lowercase_final_sigma"
    unicode = "0x3C2"
    offset = 5
    width_ratio = 0.99
    opening = 0.685
    right_hx_ratio = 1.2
    right_hy_ratio = 1

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
        yc = b.y1 + b.height * self.opening - self.extra_cut(dc)
        ymid = self.tail_height_ratio * dc.x_height

        draw_rect(pen, b.x1, ymid, b.x1 + sx, b.ymid)

        glyph = ufoLib2.objects.Glyph()
        draw_loop(glyph.getPen(), sx, sy, b.x1, b.y1, b.x2, b.y2, hx, hy, cut="bottom")
        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(cut_glyph.getPen(), b.xmid, b.ymid - 10, b.x2 + 10, yc)
        BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph)).draw(pen)

        self.draw_tail(pen, dc, b, sx, sy)
