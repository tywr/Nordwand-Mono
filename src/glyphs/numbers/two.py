from math import cos, sin, hypot

import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph

from glyphs.numbers import NumberGlyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm
from draw.loop import draw_loop


def handle_on_line(x, y, ux, uy, qx, qy, h):
    """Point (x, y) + t * (ux, uy), with t >= 0 and (ux, uy) a unit vector,
    at distance `h` from (qx, qy), on the side of (x, y). Falls back to the
    closest point of the line when `h` is shorter than its distance to it."""
    px, py = x - qx, y - qy
    b = px * ux + py * uy
    disc = b * b - (px * px + py * py) + h * h
    t = max(0, -b - max(disc, 0) ** 0.5)
    return x + t * ux, y + t * uy


class TwoGlyph(NumberGlyph):
    name = "two"
    unicode = "0x32"
    offset = 0
    diag_stroke_ratio = 1.0
    width_ratio = 1.02
    loop_y_left_ratio = 0.7
    loop_y_right_ratio = 0.53
    diag_x_ratio = 0.55
    diag_y_ratio = 0.36
    hy_curve_ratio = 0.85
    hd_curve_ratio = 1
    opening = 0.69

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            overshoot_top=True,
            width_ratio=self.width_ratio,
            number=True,
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        s = dc.stroke_x * self.diag_stroke_ratio
        hx, hy = self.hx_ratio * b.hx, self.hy_ratio * b.hy
        xc = b.x1 + self.diag_x_ratio * b.width
        yc_offset = 0.25 * (dc.stroke_x - dc.default_stroke)
        yc = b.y1 + self.diag_y_ratio * b.height + yc_offset

        # Upper loop, cut at the opening as in the 3
        loop_glyph = ufoLib2.objects.Glyph()
        draw_loop(
            loop_glyph.getPen(),
            sx,
            sy,
            b.x1,
            b.y2 - self.loop_y_left_ratio * b.height,
            b.x2,
            b.y2,
            hx,
            hy * self.loop_y_left_ratio,
            quarter="top-left",
        )
        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            b.x1 - 10,
            b.y1,
            b.xmid,
            b.y1 + self.opening * b.height - self.extra_cut(dc),
        )
        BooleanGlyph(loop_glyph).difference(BooleanGlyph(cut_glyph)).draw(pen)

        # Right part
        params = draw_loop(
            pen,
            sx,
            sy,
            b.x1,
            b.y2 - self.loop_y_right_ratio * b.height,
            b.x2,
            b.y2,
            hx,
            hy * self.loop_y_right_ratio,
            quarter="top-right",
        )

        # Bottom bar
        draw_rect(pen, b.x1, 0, b.x2, sy)

        xd, yd = xc, yc
        for _ in range(10):
            theta, _ = draw_parallelogramm(
                pen, s, b.x1, b.y1 + sy, xd, yd, no_draw=True
            )
            xd, yd = xc + s / 2 * cos(theta), yc - s / 2 * sin(theta)
        theta, delta = draw_parallelogramm(pen, s, b.x1, b.y1 + sy, xd, yd)

        inner, outer = params["inner"], params["outer"]
        xd2, yd2 = xd - delta * cos(theta) ** 2, yd + delta * cos(theta) * sin(theta)

        # Distance between the two control points of each curve: the one
        # below the loop stays vertical, the other one on the diagonal line
        # scaled by the distance between the two control points of the
        # quarter of the outer, and inner, superellipse
        hd = self.hd_curve_ratio * hypot(
            outer.x2 - outer.xmid - outer.hx, outer.y2 - outer.ymid - outer.hy
        )
        hdi = self.hd_curve_ratio * hypot(
            inner.x2 - inner.xmid - inner.hx, inner.y2 - inner.ymid - inner.hy
        )
        yhi = inner.ymid - inner.hy * self.hy_curve_ratio
        yho = outer.ymid - outer.hy * self.hy_curve_ratio
        xci, yci = handle_on_line(xd2, yd2, sin(theta), cos(theta), inner.x2, yhi, hdi)
        xco, yco = handle_on_line(xd, yd, sin(theta), cos(theta), b.x2, yho, hd)

        pen.moveTo((inner.x2, inner.ymid))
        pen.curveTo(
            (inner.x2, yhi),
            (xci, yci),
            (xd2, yd2),
        )
        # Through the top-left corner of the diagonal, to fill the triangle
        # between its flat end and the perpendicular end of the curve
        pen.lineTo((xd - delta, yd))
        pen.lineTo((xd, yd))
        pen.curveTo(
            (xco, yco),
            (b.x2, yho),
            (outer.x2, outer.ymid),
        )
        pen.closePath()
