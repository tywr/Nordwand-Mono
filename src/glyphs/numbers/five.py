import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph

from glyphs.numbers import NumberGlyph
from draw.arch import draw_arch
from draw.parallelogramm import draw_parallelogramm
from draw.rect import draw_rect
from draw.corner import draw_corner
from utils.pens import NullPen


class FiveGlyph(NumberGlyph):
    name = "five"
    offset = 0
    unicode = "0x35"
    width_ratio = 1.07
    stroke_ratio = 0.88
    loop_ratio = 0.66
    junction_ratio = 0.43
    cap_offset = 0.08
    tilt = 0.24
    taper = 0.6
    ending_offset = 0.00
    thinning = 0.9
    overshoot_bottom = True
    hx_ratio = 0.9
    hy_ratio = 0.9

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="cap", width_ratio=self.width_ratio
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        sd = self.diag_stroke_dampening(self.stroke_ratio, dc.stroke_x, coef=0.05)
        yj = b.y1 + b.height * self.junction_ratio
        ew = 0.3 * max(dc.stroke_x - 90, 0)
        oj = self.tilt * b.width + ew
        xc = b.x2 - self.cap_offset * b.width
        xe = b.x1 + self.ending_offset * b.width + ew
        hx, hy = self.hx_ratio * b.hx, self.hy_ratio * b.hy

        base_glyph = ufoLib2.objects.Glyph()

        # Bottom loop
        draw_corner(
            pen,
            sx,
            sy,
            b.x2,
            (b.y1 + b.height * self.loop_ratio) / 2,
            b.xmid,
            b.y1,
            hx,
            hy * self.loop_ratio,
            orientation="bottom-left",
        )
        draw_corner(
            base_glyph.getPen(),
            sx * self.thinning,
            sy,
            xe,
            (b.y1 + b.height * self.loop_ratio) / 2,
            b.xmid,
            b.y1,
            hx,
            hy * self.loop_ratio,
            orientation="bottom-right",
        )
        params = draw_arch(
            base_glyph.getPen(),
            sx,
            sy,
            b.x1,
            b.y1,
            b.x2,
            b.y1 + b.height * self.loop_ratio,
            hx,
            hy * self.loop_ratio,
            taper=self.taper * dc.taper,
            side="left",
            cut="bottom",
        )

        (x1, _), (x2, _) = params["inner"].intersection_y(y=yj)
        xj = min(x1, x2)

        # Remove the left-middle part
        cut_glyph = ufoLib2.objects.Glyph()
        ymid = b.y1 + b.height * self.loop_ratio / 2
        draw_rect(
            cut_glyph.getPen(),
            b.x1 - 10,
            2 * ymid - yj,
            b.xmid,
            yj,
        )

        result = BooleanGlyph(base_glyph).difference(BooleanGlyph(cut_glyph))
        result.draw(pen)

        theta, delta = draw_parallelogramm(
            NullPen(), sx, sy, xj, yj, xj + oj, b.y2, delta=sd
        )
        draw_parallelogramm(
            pen, sx, sy, xj - delta, yj, xj + oj - delta, b.y2, delta=sd
        )
        draw_rect(pen, xj + oj - 2 * delta, b.y2 - sy, xc, b.y2)
