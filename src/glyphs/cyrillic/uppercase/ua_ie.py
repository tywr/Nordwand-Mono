from glyphs.uppercase import UppercaseGlyph
from draw.loop import draw_loop
from draw.corner import draw_corner
from draw.rect import draw_rect
import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph


class CyrillicUppercaseUaIeGlyph(UppercaseGlyph):
    name = "cyrillic_uppercase_ua_ie"
    unicode = "0x0404"
    offset = 12
    stroke_x_ratio = UppercaseGlyph.stroke_x_ratio * 1.00
    stroke_y_ratio = UppercaseGlyph.stroke_y_ratio * 1.00
    opening1 = 0.29
    opening2 = 0.69
    thinning = 1
    top_offset = 0.00
    right_hx_ratio = 1.2
    right_hy_ratio = 1
    width_ratio = 1.13
    xmid_ratio = 0.68
    ymid_ratio = 0.522

    def draw(self, pen, dc):

        b = dc.body_bounds(
            offset=self.offset,
            overshoot_bottom=True,
            overshoot_top=True,
            height="cap",
            width_ratio=self.width_ratio,
            uppercase=True,
        )
        sx, sy = self.stroke_x_ratio * dc.stroke_x, self.stroke_y_ratio * dc.stroke_y
        rhx, rhy = self.right_hx_ratio * b.hx, self.right_hy_ratio * b.hy
        yc1 = b.y1 + b.height * self.opening1
        yc2 = b.y1 + b.height * self.opening2
        xt = b.x2 - self.top_offset * b.width
        xb = b.x1 + self.xmid_ratio * b.width
        yb = b.y1 + self.ymid_ratio * b.height

        draw_loop(pen, sx, sy, b.x1, b.y1, b.x2, b.y2, b.hx, b.hy, cut="right")

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
            orientation="top-left",
        )
        draw_corner(
            glyph.getPen(),
            sx * self.thinning,
            sy,
            b.x2,
            b.ymid,
            b.xmid,
            b.y1,
            rhx,
            rhy,
            orientation="bottom-left",
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

        draw_rect(
            pen,
            b.x1 + sx / 2,
            yb - sy / 2,
            xb,
            yb + sy / 2,
        )
