import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs.uppercase import UppercaseGlyph
from draw.rect import draw_rect
from draw.arch import draw_arch
from draw.corner import draw_corner
from draw.loop import draw_loop


class UppercaseGGlyph(UppercaseGlyph):
    name = "uppercase_g"
    unicode = "0x47"
    offset = 10
    opening = 140
    bot_offset = 0.015
    stroke_x_ratio = UppercaseGlyph.stroke_x_ratio * 1.00
    stroke_y_ratio = UppercaseGlyph.stroke_y_ratio * 1.00
    right_hy_ratio = 1.0
    right_hx_ratio = 1.15
    right_bot_hx_ratio = 1
    right_bot_hy_ratio = 0.8

    opening1 = 0.51
    opening2 = 0.69
    hy_ratio = 1
    hx_ratio = 1
    width_ratio = 1.15
    thinning = 1.0

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            overshoot_bottom=True,
            overshoot_top=True,
            overshoot_left=True,
            overshoot_right=True,
            width_ratio=self.width_ratio,
            uppercase=True,
            height="cap",
        )
        sx, sy = self.stroke_x_ratio * dc.stroke_x, self.stroke_y_ratio * dc.stroke_y
        hx, hy = self.hx_ratio * b.hx, self.hy_ratio * b.hy
        rhx, rhy = self.right_hx_ratio * b.hx, self.right_hy_ratio * b.hy
        rbhx, rbhy = self.right_bot_hx_ratio * b.hx, self.right_bot_hy_ratio * b.hy
        yc1 = b.y1 + b.height * self.opening1
        yc2 = b.y1 + b.height * self.opening2
        ymid = b.y1 + self.opening1 * b.height
        xb = b.x2 - self.bot_offset * b.width


        glyph = ufoLib2.objects.Glyph()
        draw_loop(pen, sx, sy, b.x1, b.y1, b.x2, b.y2, b.hx, b.hy, cut="right")

        draw_corner(
            glyph.getPen(),
            sx * self.thinning,
            sy,
            b.x2,
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
            xb,
            yc1 - sy,
            b.xmid,
            b.y1,
            rbhx,
            rbhy,
            orientation="bottom-left",
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
            xb,
            ymid,
        )
