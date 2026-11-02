from math import cos, sin, pi
from glyphs.numbers import NumberGlyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm
from draw.loop import draw_loop
from utils.pens import NullPen


class TwoGlyph(NumberGlyph):
    name = "two"
    unicode = "0x32"
    offset = 0
    xj_ratio = 0.65
    yj_ratio = 0.40
    internal_radius = 0.22
    diag_stroke_ratio = 1.0
    width_ratio = 1.04
    hx_ratio = 0.9
    hy_ratio = 0.9
    top_opening = 0.5
    loop_x_ratio = 1.0
    loop_y_ratio = 0.62

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            overshoot_top=True,
            width_ratio=self.width_ratio,
            number=True,
        )
        ec = self.extra_cut(dc)
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        s = dc.stroke_x * self.diag_stroke_ratio
        hx, hy = self.hx_ratio * b.hx, self.hy_ratio * b.hy
        xj = b.x1 + self.xj_ratio * b.width + sx / 2
        yj = b.y1 + self.yj_ratio * b.height
        ih = self.internal_radius * b.height

        # Top arch, with the same handles as the top loop of the 3
        xl1, xl2 = b.x1, b.x1 + self.loop_x_ratio * b.width
        yl1, yl2 = b.y2 - self.loop_y_ratio * b.height - ec, b.y2
        yt = (yl1 + yl2) / 2

        params = draw_loop(
            pen,
            sx,
            sy,
            xl1,
            yl1,
            xl2,
            yl2,
            hx * (xl2 - xl1) / b.width,
            hy * (yl2 - yl1) / b.height,
            cut="bottom",
        )
        ishy = params["inner"].hy

        phi, delta = draw_parallelogramm(
            NullPen(),
            s,
            b.x1,
            b.y1 + sy,
            xj,
            yj,
        )

        # Angle of the diagonal from the horizontal
        theta = pi / 2 - phi

        eps = theta
        px, py = delta * sin(eps) * cos(eps), delta * sin(eps) ** 2
        xl = xj - px
        yl = yj - py

        ihx, ihy = ih * cos(theta), ih * sin(theta)
        ehy = (xl2 - xl) * ihy / ihx
        ishy = (xl2 - sx - xj + delta) * ihy / ihx

        pen.moveTo((xl, yl))
        pen.curveTo((xl + ihx, yl + ihy), (xl2, yl + ehy), (xl2, yt))
        pen.lineTo((xl2 - sx, yt))
        pen.curveTo(
            (xl2 - sx, yj + ishy),
            (xj - delta + ihx, yj + ihy),
            (xj - delta, yj),
        )
        pen.lineTo((b.x1, b.y1 + sy))
        pen.lineTo((b.x1 + delta, b.y1 + sy))
        pen.closePath()

        # Bottom bar
        draw_rect(pen, b.x1, 0, b.x2, sy)
