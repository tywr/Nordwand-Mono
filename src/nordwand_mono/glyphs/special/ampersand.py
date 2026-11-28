import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from bisect import bisect
from math import atan, cos, sin, dist
from nordwand_mono.utils.pens import NullPen
from nordwand_mono.glyphs import Glyph
from nordwand_mono.draw.loop import draw_loop
from nordwand_mono.draw.rect import draw_rect
from nordwand_mono.draw.arch import draw_arch
from nordwand_mono.draw.parallelogramm import draw_parallelogramm


class AmpersandGlyph(Glyph):
    name = "ampersand"
    unicode = "0x26"
    offset = 70
    width_ratio = 1.2
    top_loop_x_ratio = 0.7
    top_loop_y_left_ratio = 0.4
    top_loop_y_right_ratio = 0.55
    joint_x = 1.4
    control_coef_1 = 0.66
    control_coef_2 = 0.15
    junction_ratio = 0.85
    bottom_loop_x_ratio = 0.55
    bottom_right_offset = 0.2
    opening1 = 0.5
    opening2 = 0.75
    stroke_x_dampening = 0.7
    stroke_y_dampening = 0.8

    def draw_hook(self, pen, b, sx, sy):
        """Top half-loop blending into the branch going down to the bottom
        right. Returns the middle of the stroke of the branch, sampled from
        the left of the half-loop to the bottom."""

        # Top half of the loop
        xl = b.x1 + self.top_loop_x_ratio * b.width
        yl = b.y2 - self.top_loop_y_left_ratio * b.height
        yr = b.y2 - self.top_loop_y_right_ratio * b.height
        ymid = (yl + b.y2) / 2
        params = draw_loop(
            pen,
            sx,
            sy,
            b.x1,
            yl,
            xl,
            b.y2,
            b.hx * self.top_loop_x_ratio,
            b.hy * self.top_loop_y_left_ratio,
            quarter="top-left",
        )
        draw_loop(
            pen,
            sx,
            sy,
            b.x1,
            yr,
            xl,
            b.y2,
            b.hx * self.top_loop_x_ratio,
            b.hy * self.top_loop_y_right_ratio,
            quarter="top-right",
        )

        # Junction of the diagonal with the bottom of the loop
        xj = b.x1 + self.joint_x * sx
        (_, y1), (_, y2) = params["outer"].intersection_x(x=xj)
        yj = min(y1, y2)

        # Diagonal from the left of the loop down to the bottom right, mirror
        # of the branch of the 6
        _, delta = draw_parallelogramm(
            NullPen(), sx, b.x1, ymid, b.x2, 0, direction="bottom-right"
        )
        theta = atan((-yj) / (b.x2 - xj))

        lp = ((yj) ** 2 + (b.x2 - xj) ** 2) ** 0.5
        dx = lp * cos(theta)
        dy = lp * sin(theta)
        dx1m, dy1m = self.control_coef_1 * dx, self.control_coef_1 * dy
        dx2m, dy2m = self.control_coef_2 * dx, self.control_coef_2 * dy

        # exterior points
        x1m, y1m = xj - delta + dx1m, yj + dy1m
        x2m, y2m = xj - delta + dx2m, yj + dy2m
        x3m, y3m = b.x1, yj + (b.x1 + delta - xj) * dy / dx

        # interior points: the exterior curve on the inner edge of the branch,
        # moved by delta, up to sx inside the left of the loop
        x1i, y1i = x1m + delta, y1m
        x2i, y2i = x2m + delta, y2m
        x3i, y3i = x3m + sx, y3m

        pen.moveTo((b.x1, ymid))
        pen.curveTo(
            (x3m, y3m),
            (x2m, y2m),
            (x1m, y1m),
        )
        pen.lineTo((b.x2 - delta, 0))
        pen.lineTo((b.x2, 0))
        pen.lineTo((x1i, y1i))
        pen.curveTo(
            (x2i, y2i),
            (x3i, y3i),
            (b.x1 + sx, ymid),
        )
        pen.closePath()

        # Middle of the stroke of the branch: the average of its exterior and
        # interior edges, a curve then a line down to the bottom
        p0, p1 = (b.x1 + sx / 2, ymid), (x3m + sx / 2, y3m)
        p2, p3 = (x2m + delta / 2, y2m), (x1m + delta / 2, y1m)
        p4 = (b.x2 - delta / 2, 0)
        # ponytail: curve sampled in 64 segments, more if t needs to be finer
        spine = [
            tuple(
                (1 - u) ** 3 * a
                + 3 * (1 - u) ** 2 * u * b_
                + 3 * (1 - u) * u**2 * c
                + u**3 * d
                for a, b_, c, d in zip(p0, p1, p2, p3)
            )
            for u in (i / 64 for i in range(65))
        ] + [p4]
        return (b.x1 + xl) / 2, spine

    def branch_point(self, b, sx, sy, t):
        """(x, y) on the middle of the branch, t going from 0 at the left of
        the half-loop to 1 at the bottom, proportionally to the length
        travelled along it."""
        _, spine = self.draw_hook(NullPen(), b, sx, sy)
        lengths = [0]
        for q1, q2 in zip(spine, spine[1:]):
            lengths.append(lengths[-1] + dist(q1, q2))
        target = t * lengths[-1]
        i = min(max(bisect(lengths, target), 1), len(lengths) - 1)
        r = (target - lengths[i - 1]) / (lengths[i] - lengths[i - 1])
        (xa, ya), (xb, yb) = spine[i - 1], spine[i]
        return xa + r * (xb - xa), ya + r * (yb - ya)

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            overshoot_top=True,
            overshoot_bottom=True,
            width_ratio=self.width_ratio,
            uppercase=True,
        )
        sx, sy = self.get_strokes(dc)
        ec = self.extra_cut(dc)
        yc1 = b.y1 + self.opening1 * b.height + ec
        yc2 = b.y1 + self.opening2 * b.height - ec

        glyph = ufoLib2.objects.Glyph()
        # Draw the top hook and compute the junction
        xm, _ = self.draw_hook(glyph.getPen(), b, sx, sy)
        (xj, yj) = self.branch_point(b, sx, sy, 1 - self.junction_ratio)

        # Bottom loop
        w = self.bottom_loop_x_ratio * b.width
        x1, x2 = xj - w / 2, xj + w / 2
        x2r = b.x2 - self.bottom_right_offset * b.width
        draw_arch(
            glyph.getPen(),
            sx,
            sy,
            x1,
            b.y1,
            x2,
            yj,
            b.hx * w / b.width,
            b.hy * (yj - b.y1) / b.height,
            taper=0.75,
            quarter="top-left",
            side="top",
        )
        draw_loop(
            glyph.getPen(),
            sx,
            sy,
            x1,
            b.y1,
            x2r,
            yj,
            b.hx * (x2r - x1) / b.width,
            b.hy * (yj - b.y1) / b.height,
            cut="top",
        )
        draw_rect(
            glyph.getPen(),
            x2r - sx,
            (b.y1 + yj) / 2,
            x2r,
            yc2,
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
