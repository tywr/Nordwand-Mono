from math import cos, sin, tan, hypot
import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph

from glyphs import Glyph
from glyphs.numbers.three import ThreeGlyph
from draw.loop import draw_loop
from draw.arch import draw_arch
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm
from glyphs.numbers.two import handle_on_line


class AmpersandGlyph(Glyph):
    name = "ampersand"
    unicode = "0x26"
    offset = -50
    width_ratio = 1.08
    upper_width = 0.8
    upper_height = 0.4
    lower_width = 1
    hook_ratio = 0.12
    hook_below_baseline = 0
    hook_outside_cell = 0.24
    end_height_ratio = 0.5
    diag_stroke_ratio = 1
    # Center of the top end of the diagonal, relative to the body
    diag_x_ratio = 0.65
    diag_y_ratio = 0.35
    hy_curve_ratio = 0.85
    hd_curve_ratio = 1.0

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            overshoot_top=True,
            overshoot_bottom=True,
            width_ratio=self.width_ratio,
            uppercase=True,
        )

        ec = self.extra_cut(dc)
        ox = self.hook_outside_cell * b.width
        h = self.upper_height * b.height
        w = self.upper_width * b.width
        xu1, xu2 = b.xmid - w / 2, b.xmid + w / 2
        yu1, yu2 = b.y2 - h, b.y2

        # Same handles as the top loop of the 3, the loop being drawn lower for
        # bolder weights while the junction stays where it was
        loop = ThreeGlyph().top_loop(dc).resize(xu1, yu1, xu2, yu2)
        xj = xu1 + self.hook_ratio * w
        (_, y1), (_, y2) = loop.intersection_x(x=xj)
        yj = min(y1, y2)

        yu1 -= 2 * ec
        loop = loop.resize(xu1, yu1, xu2, yu2)
        params = draw_loop(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            xu1,
            yu1,
            xu2,
            yu2,
            loop.hx,
            loop.hy,
            cut="bottom",
        )

        # Diagonal to the bottom right, its top end centered on (xc, yc), the
        # center sitting higher for bolder weights, like the 2. Mirror of the 2: the top end, across the stroke from the
        # outer corner (xd, yd) to the facing point (xd2, yd2) of the inner
        # edge, is s long and perpendicular to the diagonal, theta being its
        # angle from vertical, so (xd, yd) = (xc, yc) + s / 2 * (-cos, -sin).
        # Theta depends on the corner, so iterate
        s = self.diag_stroke_ratio * dc.stroke_x
        dhy = self.hook_below_baseline * b.height
        yc_offset = -0.25 * (dc.stroke_y - dc.default_stroke)
        yc = b.y1 + self.diag_y_ratio * b.height + yc_offset
        xc = b.x1 + self.diag_x_ratio * b.width
        xd, yd = xc, yc
        for _ in range(10):
            theta, _ = draw_parallelogramm(
                pen, s, b.x2 + ox, -dhy, xd, yd, direction="top-left", no_draw=True
            )
            xd, yd = xc - s / 2 * cos(theta), yc - s / 2 * sin(theta)
        theta, delta = draw_parallelogramm(
            pen, s, b.x2 + ox, -dhy, xd, yd, direction="top-left"
        )
        xd2, yd2 = xd + delta * cos(theta) ** 2, yd + delta * cos(theta) * sin(theta)

        # Curves from the left of the loop to the diagonal, like the 2: the
        # control point below the loop stays vertical, the other one on the
        # diagonal line, their distance scaled by the distance between the two
        # control points of the quarter of the outer, and inner, superellipse
        inner, outer = params["inner"], params["outer"]
        hd = self.hd_curve_ratio * hypot(
            outer.xmid - outer.hx - outer.x1, outer.y2 - outer.ymid - outer.hy
        )
        hdi = self.hd_curve_ratio * hypot(
            inner.xmid - inner.hx - inner.x1, inner.y2 - inner.ymid - inner.hy
        )
        yhi = inner.ymid - inner.hy * self.hy_curve_ratio
        yho = outer.ymid - outer.hy * self.hy_curve_ratio
        xci, yci = handle_on_line(xd2, yd2, -sin(theta), cos(theta), inner.x1, yhi, hdi)
        xco, yco = handle_on_line(xd, yd, -sin(theta), cos(theta), outer.x1, yho, hd)

        pen.moveTo((outer.x1, outer.ymid))
        pen.curveTo(
            (outer.x1, yho),
            (xco, yco),
            (xd, yd),
        )
        # Through the top-right corner of the diagonal, to fill the triangle
        # between its flat end and the perpendicular end of the curve
        pen.lineTo((xd + delta, yd))
        pen.lineTo((xd2, yd2))
        pen.curveTo(
            (xci, yci),
            (inner.x1, yhi),
            (inner.x1, inner.ymid),
        )
        pen.closePath()

        # Draw the lower bowl
        xbm = b.xmid
        lw = self.lower_width * b.width
        lh = yj - b.y1

        draw_arch(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            xbm - lw / 2,
            b.y1,
            xbm + lw / 2,
            yj,
            b.hx * lw / b.width,
            b.hy * lh / b.height,
            cut="top",
            side="top",
            taper=0.5,
        )

        loop_glyph = ufoLib2.objects.Glyph()
        draw_arch(
            loop_glyph.getPen(),
            dc.stroke_x,
            dc.stroke_y,
            xbm - lw / 2,
            b.y1,
            xbm + lw / 2,
            yj,
            b.hx * lw / b.width,
            b.hy * lh / b.height,
            cut="right",
            side="top",
            taper=0.5,
        )

        # Where the inner edge of the diagonal crosses the top of the bowl
        xcut = xd + delta - (yj - yd) * tan(theta)
        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(cut_glyph.getPen(), xcut, 0.5 * b.y1 + 0.5 * yj, b.x2, b.y2)
        result = BooleanGlyph(loop_glyph).difference(BooleanGlyph(cut_glyph))
        result.draw(pen)

        # Draw the height extension
        eh = self.end_height_ratio * b.height
        draw_rect(
            pen, xbm + lw / 2 - dc.stroke_x, 0.5 * b.y1 + 0.5 * yj, xbm + lw / 2, eh + ec
        )
