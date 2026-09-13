import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs import Glyph
from draw.rect import draw_rect
from draw.circle import draw_circle


class CurrencySignGlyph(Glyph):
    name = "currency_sign"
    unicode = "0xA4"
    offset = 0
    radius_ratio = 0.5
    arm_ratio = 1.4
    width_ratio = 1.08

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="cap", width_ratio=self.width_ratio
        )
        s = dc.stroke_x
        la = self.arm_ratio * b.width
        rd = self.radius_ratio * b.width

        glyph = ufoLib2.objects.Glyph()
        draw_rect(
            glyph.getPen(),
            b.xmid - la / 2,
            b.ymid - s / 2,
            b.xmid + la / 2,
            b.ymid + s / 2,
            rotate=45,
        )
        draw_rect(
            glyph.getPen(),
            b.xmid - la / 2,
            b.ymid - s / 2,
            b.xmid + la / 2,
            b.ymid + s / 2,
            rotate=-45,
        )
        draw_circle(
            glyph.getPen(),
            b.xmid,
            b.ymid,
            rd,
        )
        cut_glyph = ufoLib2.objects.Glyph()
        draw_circle(
            cut_glyph.getPen(),
            b.xmid,
            b.ymid,
            rd - s,
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)
