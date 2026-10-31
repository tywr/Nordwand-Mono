import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph

from glyphs.numbers import NumberGlyph
from draw.arch import draw_arch
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm_legacy


class ThreeGlyph(NumberGlyph):
    name = "three_2"
    unicode = "0x33"
    font_feature = {"cv19": 1}
    offset = 0
    loop_width_ratio = 0.92
    mid_ratio = 0.55
    taper = 1.5
    len_mid = 0.7
    hx_ratio = 0.9
    hy_ratio = 0.9
    width_ratio = 1.08

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            overshoot_bottom=True,
            overshoot_right=True,
            width_ratio=self.width_ratio,
            number=True,
        )
        ec = self.extra_cut(dc)
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        hx, hy = b.hx * self.hx_ratio, b.hy * self.hy_ratio

        ymid = b.y1 + self.mid_ratio * b.height
        xl = b.x1 + (1 - self.loop_width_ratio) * b.width / 2
        xr = b.x2 - (1 - self.loop_width_ratio) * b.width / 2
        base_glyph = ufoLib2.objects.Glyph()
        ry = (b.y2 - b.ymid + sy / 2) / b.height

        # Top loop
        taper = max(self.taper * dc.taper, 0.65)

        draw_rect(pen, xl, b.y2 - dc.stroke_y, xr, b.y2)
        draw_parallelogramm_legacy(
            pen,
            sx,
            sy,
            b.xmid - sx,
            ymid - sy / 2,
            xr,
            b.y2 - dc.stroke_y,
            direction="top-right",
        )

        # Bottom loop
        draw_arch(
            base_glyph.getPen(),
            sx,
            sy,
            b.x1,
            b.y1,
            b.x2,
            ymid + sy / 2,
            hx,
            hy * ry * 2 * self.mid_ratio,
            taper=1,
            side="top",
        )

        # Remove the left-middle part
        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            b.x1,
            ymid - b.height / 4 + ec,
            b.x1 + b.width / 2,
            ymid + b.height / 4 - ec,
        )

        result = BooleanGlyph(base_glyph).difference(BooleanGlyph(cut_glyph))
        result.draw(pen)

        # Extension of the middle bar
        # draw_rect(
        #     pen,
        #     b.x1 + (1 - self.len_mid) * b.width,
        #     ymid - sy / 2,
        #     b.xmid,
        #     ymid + sy / 2,
        # )
