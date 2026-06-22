from math import cos, sin, atan
from glyphs.numbers import NumberGlyph
from draw.loop import draw_loop
from draw.arch import draw_arch
from draw.polygon import draw_polygon
from draw.parallelogramm import draw_parallelogramm
from utils.pens import NullPen


class SixGlyph(NumberGlyph):
    name = "six"
    unicode = "0x36"
    offset = 0
    stroke_ratio = 1.2
    loop_ratio = 0.64
    top_ratio = 0.4
    taper = 0.2
    cap_x = 0.75
    joint_x = 1.4
    hx_ratio = 0.9
    hy_ratio = 0.9

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            overshoot_bottom=True,
            overshoot_left=True,
            overshoot_right=True,
            width_ratio=self.width_ratio,
            number=True,
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        hx, hy = self.hx_ratio * b.hx, self.hy_ratio * b.hy

        ymid = b.y1 + self.loop_ratio * b.height
        xc = b.x1 + self.cap_x * b.width
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

        delta = self.diag_stroke_dampening(self.stroke_ratio, dc.stroke_x, coef=0.15)
        theta = atan((yj - b.y2) / (xj - xc))

        ihy = params["inner"].hy
        draw_polygon(
            pen,
            points=[
                (xj, yj),
                (xj - delta / 2, yj),
                (b.x1, (b.y1 + ymid) / 2),
                (b.x1 + sx, (b.y1 + ymid) / 2),
                (b.x1 + sx, (b.y1 + b.ymid) / 2 + ihy),
            ],
        )

        lp = ((b.y2 - yj) ** 2 + (xj - xc) ** 2) ** 0.5
        dx = lp * cos(theta)
        dy = lp * sin(theta)
        # xcm, ycm = xj - delta + 0.66 * dx, yj + 0.66 * dy
        # xcp, ycp = xj - delta + 0.33 * dx, yj + 0.33 * dy
        x1m, y1m = xj - delta + 0.66 * dx, yj + 0.66 * dy
        x2m, y2m = xj - delta + 0.15 * dx, yj + 0.15 * dy
        x3m, y3m = b.x1, yj + (b.x1 + delta - xj) * dy / dx

        pen.moveTo((xj, yj))
        pen.lineTo((xc, b.y2))
        pen.lineTo((xc - delta, b.y2))
        pen.lineTo((x1m, y1m))
        pen.curveTo(
            (x2m, y2m),
            (x3m, y3m),
            (b.x1, (b.y1 + ymid) / 2),
        )
        # pen.lineTo((b.x1 + sx / 2, (b.y1 + ymid) / 2))
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
