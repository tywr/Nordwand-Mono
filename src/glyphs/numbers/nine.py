from math import sin, cos, atan
from glyphs.numbers import NumberGlyph
from draw.loop import draw_loop
from draw.arch import draw_arch
from draw.polygon import draw_polygon


class NineGlyph(NumberGlyph):
    name = "nine"
    unicode = "0x39"
    offset = 0
    vertical_ratio = 0.64
    stroke_ratio = 1.2
    bottom_cut = 0.2
    taper = 0.2
    foot_x = 0.25
    joint_x = 1.4
    hx_ratio = 0.9
    hy_ratio = 0.9

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            overshoot_top=True,
            overshoot_left=True,
            overshoot_right=True,
            width_ratio=self.width_ratio,
            number=True,
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        hx, hy = self.hx_ratio * b.hx, self.hy_ratio * b.hy
        ymid = b.y2 - self.vertical_ratio * b.height

        xf = b.x1 + self.foot_x * b.width
        xj = b.x2 - self.joint_x * sx

        # Upper loop
        params = draw_arch(
            pen,
            sx,
            sy,
            b.x1,
            ymid,
            b.x2,
            b.y2,
            hx,
            hy * self.vertical_ratio,
            taper=self.taper * dc.taper,
            side="right",
            cut="top",
        )

        # Compute the intersection
        (_, y1), (_, y2) = params["outer"].intersection_x(x=xj)
        yj = min(y1, y2)

        delta = self.diag_stroke_dampening(self.stroke_ratio, dc.stroke_x, coef=0.15)
        theta = atan((yj - b.y1) / (xj - xf))

        ihy = params["inner"].hy
        draw_polygon(
            pen,
            points=[
                (xj, yj),
                (xj, yj),
                (b.x2, (b.y2 + ymid) / 2),
                (b.x2 - sx, (b.y2 + ymid) / 2),
                (b.x2 - sx, (b.y2 + b.ymid) / 2 - ihy),
            ],
        )

        lp = ((b.y1 - yj) ** 2 + (xj - xf) ** 2) ** 0.5
        dx = lp * cos(theta)
        dy = lp * sin(theta)
        x1m, y1m = xj + delta - 0.66 * dx, yj - 0.66 * dy
        x2m, y2m = xj + delta - 0.15 * dx, yj - 0.15 * dy
        x3m, y3m = b.x2, yj - (xj + delta - b.x2) * dy / dx

        pen.moveTo((xj, yj))
        pen.lineTo((xf, b.y1))
        pen.lineTo((xf + delta, b.y1))
        pen.lineTo((x1m, y1m))
        pen.curveTo(
            (x2m, y2m),
            (x3m, y3m),
            (b.x2, (b.y2 + ymid) / 2),
        )

        draw_loop(
            pen,
            sx,
            sy,
            b.x1,
            ymid,
            b.x2,
            b.y2,
            hx,
            b.hy * self.vertical_ratio,
            cut="bottom",
        )
