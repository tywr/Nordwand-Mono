from math import cos, sin, atan
from fontTools.pens.reverseContourPen import ReverseContourPen
from glyphs import Glyph
from draw.loop import draw_loop
from draw.arch import draw_arch
from draw.rect import draw_rect


class GreekLowercaseDeltaGlyph(Glyph):
    """Like the 6, mirrored: the stroke leaves the loop towards the top-left"""

    name = "greek_lowercase_delta"
    unicode = "0x3B4"
    offset = 0
    width_ratio = 1
    height_ratio = 0.76
    stroke_x_ratio = 1
    stroke_y_ratio = 1
    taper = 0.2
    cap_x = 0.9
    loop_ratio = 0.9
    joint_x = 1.4
    hx_ratio = 1
    hy_ratio = 1
    stroke_ratio = 1.5

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            overshoot_bottom=True,
            overshoot_top=True,
            overshoot_left=True,
            overshoot_right=True,
            width_ratio=self.width_ratio,
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        loop_ratio = self.loop_ratio
        hx, hy = self.hx_ratio * b.hx, self.hy_ratio * b.hy * loop_ratio

        ymid = b.y1 + loop_ratio * b.height
        yq = (b.y1 + ymid) / 2
        xc = b.x2 - self.cap_x * b.width
        xc2 = b.x1 + self.cap_x * b.width
        xj = b.x2 - self.joint_x * sx
        yt2 = dc.ascent - dc.stroke_y

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
            hy,
            taper=self.taper * dc.taper,
            side="right",
            cut="bottom",
        )

        # Compute the intersection
        (_, y1), (_, y2) = params["outer"].intersection_x(x=xj)
        yj = max(y1, y2)

        delta = self.diag_stroke_dampening(self.stroke_ratio, dc.stroke_x, coef=0.15)
        theta = atan((yt2 - yj) / (xj - xc))

        # Mirrored contours wind the other way round, reverse them back
        rpen = ReverseContourPen(pen)

        lp = ((yt2 - yj) ** 2 + (xj - xc) ** 2) ** 0.5
        dx = lp * cos(theta)
        dy = lp * sin(theta)
        x1m, y1m = xj + delta - 0.66 * dx, yj + 0.66 * dy
        x2m, y2m = xj + delta - 0.15 * dx, yj + 0.15 * dy
        y3m = yj + (xj + delta - b.x2) * dy / dx

        rpen.moveTo((xj, yj))
        rpen.lineTo((xc, yt2))
        rpen.lineTo((xc + delta, yt2))
        rpen.lineTo((x1m, y1m))
        rpen.curveTo((x2m, y2m), (b.x2, y3m), (b.x2, yq))
        # Back up along the loop's outer edge, so the stroke only adds outside
        # the loop: no hole at the joint and no cut into the counter, whatever
        # the weight and taper
        n = 12
        for i in range(n):
            y = yq + (yj - yq) * i / n
            (x1, _), (x2, _) = params["outer"].intersection_y(y=y)
            rpen.lineTo((max(x1, x2), y))
        rpen.closePath()

        draw_loop(pen, sx, sy, b.x1, b.y1, b.x2, ymid, hx, hy, cut="top")

        draw_rect(
            pen,
            xc,
            dc.ascent - sy,
            xc2,
            dc.ascent,
        )
