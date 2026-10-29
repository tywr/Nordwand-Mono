import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph

from draw.loop import draw_loop
from draw.rect import draw_rect
from glyphs.greek.lowercase import TailedGreekLowercaseGlyph
from draw.arch import draw_arch


class GreekLowercaseXiGlyph(TailedGreekLowercaseGlyph):
    name = "greek_lowercase_xi"
    unicode = "0x3BE"
    offset = 0
    width_ratio = 0.99
    mid_ratio = 0.55
    upper_inset = 0.15
    mid_bar = 0.83
    upper_ratio = 0.9
    cap_height = 0.75

    def draw(self, pen, dc):
        b = dc.body_bounds(
            height="cap",
            offset=self.offset,
            overshoot_bottom=True,
            overshoot_top=True,
            overshoot_left=True,
            width_ratio=self.width_ratio,
            uppercase=True,
        )
        ec = self.extra_cut(dc)
        sx, sy = self.stroke_x_ratio * dc.stroke_x, self.stroke_y_ratio * dc.stroke_y
        hx, hy = self.hx_ratio * b.hx, self.hy_ratio * b.hy
        lh = self.tail_height_ratio * dc.x_height
        uw = self.upper_ratio * b.width
        yc = self.cap_height * b.height

        # # Middle bar
        draw_rect(
            pen,
            b.xmid,
            2 * lh - sy,
            b.x1 + self.mid_bar * b.width,
            2 * lh,
        )

        # Lower bowl, going into the tail
        draw_loop(
            pen,
            sx,
            sy,
            b.x1,
            0,
            b.x2,
            2 * lh,
            hx,
            hy * lh / b.height * 2,
            quarter="top-left",
        )

        # Top bowl, going to the top
        base_glyph = ufoLib2.objects.Glyph()
        draw_arch(
            base_glyph.getPen(),
            sx,
            sy,
            b.x2 - uw,
            2 * lh - sy,
            b.x2,
            b.y2,
            hx * self.upper_ratio,
            hy * uw / b.height,
            side="bottom",
            taper=dc.taper,
        )
        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            b.xmid,
            0,
            b.x2 + 300,
            yc - ec,
        )
        result = BooleanGlyph(base_glyph).difference(BooleanGlyph(cut_glyph))
        result.draw(pen)

        self.draw_tail(pen, dc, b, sx, sy)
