from math import cos, sin, atan
from glyphs import Glyph
from draw.loop import draw_loop
from draw.arch import draw_arch
from draw.polygon import draw_polygon
from draw.parallelogramm import draw_parallelogramm_vertical


class LowercaseEthGlyph(Glyph):
    name = "lowercase_eth"
    unicode = "0xF0"
    offset = 0
    loop_ratio = 0.64
    top_ratio = 0.4
    taper = 0.2
    cap_x = 0.75
    joint_x = 1.4
    hx_ratio = 0.9
    hy_ratio = 0.9
    stroke_ratio = 1.2
    width_ratio = 1.0
    ystroke_ratio = 0.65
    ystroke_width_ratio = 0.8

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
        sx, sy = dc.stroke_x, dc.stroke_y
        hx, hy = self.hx_ratio * b.hx, self.hy_ratio * b.hy

        ymid = b.y1 + self.loop_ratio * b.height
        xc = b.x2 - self.cap_x * b.width
        xj = b.x2 - self.joint_x * sx
        ysmid = b.y1 + self.ystroke_ratio * b.height
        tx1 = b.x1 + (1 - self.ystroke_width_ratio) * b.width / 2
        tx2 = b.x2 - (1 - self.ystroke_width_ratio) * b.width / 2

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
            side="right",
            cut="bottom",
        )

        # Compute the intersection
        (_, y1), (_, y2) = params["outer"].intersection_x(x=xj)
        yj = max(y1, y2)

        delta = self.diag_stroke_dampening(self.stroke_ratio, dc.stroke_x, coef=0.15)
        theta = atan((yj - b.y2) / (xc - xj))

        ihy = params["inner"].hy
        draw_polygon(
            pen,
            points=[
                (b.x2 - sx, (b.y1 + b.ymid) / 2 + ihy),
                (b.x2 - sx, (b.y1 + ymid) / 2),
                (b.x2, (b.y1 + ymid) / 2),
                (xj + delta / 2, yj),
                (xj, yj),
            ],
        )

        lp = ((b.y2 - yj) ** 2 + (xc - xj) ** 2) ** 0.5
        dx = lp * cos(theta)
        dy = lp * sin(theta)
        x1m, y1m = xj + delta - 0.66 * dx, yj + 0.66 * dy
        x2m, y2m = xj + delta - 0.15 * dx, yj + 0.15 * dy
        x3m, y3m = b.x2, yj + (b.x2 - delta - xj) * dy / dx

        pen.moveTo((b.x2, (b.y1 + ymid) / 2))
        pen.curveTo(
            (x3m, y3m),
            (x2m, y2m),
            (x1m, y1m),
        )
        pen.lineTo((xc + delta, b.y2))
        pen.lineTo((xc, b.y2))
        pen.lineTo((xj, yj))
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

        draw_parallelogramm_vertical(
            pen, sx, sy, tx1, ysmid, tx2, b.y2, direction="top-right"
        )
