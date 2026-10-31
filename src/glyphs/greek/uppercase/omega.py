import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph

from glyphs.uppercase import UppercaseGlyph
from draw.arch import draw_arch
from draw.rect import draw_rect


class GreekUppercaseOmegaGlyph(UppercaseGlyph):
    name = "greek_uppercase_omega"
    unicode = "0x3A9"
    offset = 0
    taper = 0.75
    cut_width = 0.2
    stroke_x_ratio = UppercaseGlyph.stroke_x_ratio * 1.00
    stroke_y_ratio = UppercaseGlyph.stroke_y_ratio * 1.00
    width_ratio = 1.14
    loop_ratio = 0.92

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            overshoot_top=True,
            width_ratio=self.width_ratio,
            uppercase=True,
        )
        wl = self.loop_ratio * b.width
        x1, x2 = b.xmid - wl / 2, b.xmid + wl / 2
        sy = dc.stroke_y * self.stroke_y_ratio
        wc = self.cut_width * b.width
        glyph = ufoLib2.objects.Glyph()
        draw_arch(
            glyph.getPen(),
            dc.stroke_x * self.stroke_x_ratio,
            sy,
            x1,
            b.y1,
            x2,
            b.y2,
            b.hx * self.loop_ratio,
            b.hy,
            side="bottom",
            taper=dc.taper * self.taper,
        )
        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(cut_glyph.getPen(), b.xmid - wc / 2, b.y1, b.xmid + wc / 2, b.ymid)
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)

        draw_rect(
            pen,
            b.xmid + wc / 2,
            b.y1,
            b.x2,
            b.y1 + sy,
        )
        draw_rect(
            pen,
            b.x1,
            b.y1,
            b.xmid - wc / 2,
            b.y1 + sy,
        )
