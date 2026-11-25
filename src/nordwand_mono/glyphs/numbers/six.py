from nordwand_mono.utils.pens import NullPen
from math import cos, sin, atan
from nordwand_mono.glyphs.numbers import NumberGlyph
from nordwand_mono.draw.loop import draw_loop
from nordwand_mono.draw.arch import draw_arch
from nordwand_mono.draw.parallelogramm import draw_parallelogramm


class SixGlyph(NumberGlyph):
    name = "six"
    unicode = "0x36"
    offset = 5
    loop_ratio = 0.64
    taper = 0.75
    cap_x = 0.69
    joint_x = 1.4
    hx_ratio = 0.9
    hy_ratio = 0.9
    stroke_ratio = 1.0
    control_coef_1 = 0.66
    control_coef_2 = 0.15

    def body(self, dc):
        return dc.body_bounds(
            offset=self.offset,
            height="cap",
            overshoot_bottom=True,
            overshoot_left=True,
            overshoot_right=True,
            width_ratio=self.width_ratio,
            number=True,
        )

    def draw(self, pen, dc):
        b = self.body(dc)
        sx, sy = self.get_strokes(dc)
        s = self.stroke_ratio * sx
        hx, hy = self.hx_ratio * b.hx, self.hy_ratio * b.hy
        xo = 0.45 * (sx - dc.default_stroke)

        ymid = b.y1 + self.loop_ratio * b.height
        xc = b.x1 + self.cap_x * b.width + xo
        xj = b.x1 + self.joint_x * sx

        # Bottom loop
        params = draw_arch(
            pen,
            sx,
            sy,
            b.x1,
            b.y1,
            b.x2,
            ymid,
            hx,
            hy * self.loop_ratio,
            taper=self.taper * dc.taper,
            side="left",
            cut="bottom",
        )

        # Compute the intersection
        (_, y1), (_, y2) = params["outer"].intersection_x(x=xj)
        yj = max(y1, y2)

        _, delta = draw_parallelogramm(
            NullPen(), s, b.x1, (b.y1 + ymid) / 2, xc, b.y2, direction="top-right"
        )
        theta = atan((yj - b.y2) / (xj - xc))

        ihy = params["inner"].hy
        # draw_polygon(
        #     pen,
        #     points=[
        #         (xj, yj),
        #         (xj - sx / 2, yj),
        #         (b.x1, (b.y1 + ymid) / 2),
        #         (b.x1 + sx, (b.y1 + ymid) / 2),
        #         (b.x1 + sx, (b.y1 + b.ymid) / 2 + ihy),
        #     ],
        # )

        lp = ((b.y2 - yj) ** 2 + (xj - xc) ** 2) ** 0.5
        dx = lp * cos(theta)
        dy = lp * sin(theta)
        dx1m, dy1m = self.control_coef_1 * dx, self.control_coef_1 * dy
        dx2m, dy2m = self.control_coef_2 * dx, self.control_coef_2 * dy

        # exterior points
        x1m, y1m = xj - delta + dx1m, yj + dy1m
        x2m, y2m = xj - delta + dx2m, yj + dy2m
        x3m, y3m = b.x1, yj + (b.x1 + delta - xj) * dy / dx

        # interior points: the exterior curve on the inner edge of the branch,
        # moved by delta, down to sx inside the left of the loop
        x1i, y1i = x1m + delta, y1m
        x2i, y2i = x2m + delta, y2m
        x3i, y3i = x3m + sx, y3m

        pen.moveTo((b.x1 + sx, (b.y1 + ymid) / 2))
        pen.curveTo(
            (x3i, y3i),
            (x2i, y2i),
            (x1i, y1i),
        )
        pen.lineTo((xc, b.y2))
        pen.lineTo((xc - delta, b.y2))
        pen.lineTo((x1m, y1m))
        pen.curveTo(
            (x2m, y2m),
            (x3m, y3m),
            (b.x1, (b.y1 + ymid) / 2),
        )
        pen.closePath()

        draw_loop(
            pen,
            sx,
            sy,
            b.x1,
            b.y1,
            b.x2,
            ymid,
            hx,
            hy * self.loop_ratio,
            cut="top",
        )
