import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph

from nordwand_mono.glyphs.numbers import NumberGlyph
from nordwand_mono.draw.arch import draw_arch
from nordwand_mono.draw.parallelogramm import draw_parallelogramm
from nordwand_mono.draw.loop import draw_loop
from nordwand_mono.draw.rect import draw_rect
from nordwand_mono.draw.corner import draw_corner
from nordwand_mono.utils.pens import NullPen


class FiveGlyph(NumberGlyph):
    name = "five"
    offset = -9
    unicode = "0x35"
    width_ratio = 1.06
    stroke_ratio = 0.88
    loop_ratio = 0.67
    junction_ratio = 0.45
    cap_offset = 0.07
    tilt = 0.22
    taper = 0.8
    hx_ratio = 0.9
    hy_ratio = 0.9
    opening = 0.27
    top_loop_offset = 0

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            width_ratio=self.width_ratio,
            overshoot_bottom=True,
            overshoot_left=True,
            overshoot_right=True,
            number=True,
        )
        sx, sy = self.get_strokes(dc)
        ec = self.extra_cut(dc)
        sd = self.stroke_ratio * dc.stroke_x
        yc = b.y1 + self.opening * b.height + ec
        yj = b.y1 + b.height * self.junction_ratio
        xo = 0.6 * (sx - dc.default_stroke)
        xlo = -0.4 * (sx - dc.default_stroke)
        oj = self.tilt * b.width + xo
        xc = b.x2 - self.cap_offset * b.width
        xt1 = b.x1 + self.top_loop_offset * b.width + xlo
        hx, hy = self.hx_ratio * b.hx, self.hy_ratio * b.hy
        taper = min(1, self.taper * dc.taper)

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
        params = draw_loop(
            base_glyph.getPen(),
            sx,
            sy,
            b.x1,
            b.y1,
            b.x2,
            b.y1 + b.height * self.loop_ratio,
            hx,
            hy * self.loop_ratio,
            cut="top",
        )
        params = draw_arch(
            base_glyph.getPen(),
            sx,
            sy,
            xt1,
            b.y1,
            b.x2,
            b.y1 + b.height * self.loop_ratio,
            hx,
            hy * self.loop_ratio,
            taper=taper,
            side="left",
            cut="bottom",
        )

        (x1, _), (x2, _) = params["inner"].intersection_y(y=yj)
        xj = min(x1, x2)

        # Remove the left-middle part
        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            xt1 - 100,
            yc,
            b.xmid,
            yj,
        )

        result = BooleanGlyph(base_glyph).difference(BooleanGlyph(cut_glyph))
        result.draw(pen)

        _, delta = draw_parallelogramm(NullPen(), sd, xj, yj, xj + oj, b.y2)

        draw_parallelogramm(pen, sd, xj - delta, yj, xj + oj - delta, b.y2)
        draw_rect(pen, xj + oj - 2 * delta, b.y2 - sy, xc, b.y2)
