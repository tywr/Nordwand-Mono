from glyphs import Glyph
from draw.loop import draw_loop
from shapes.superellipse import Superellipse


class TildeGlyph(Glyph):
    name = "tilde"
    unicode = "0x7E"
    offset = 0
    width_ratio = 1.2
    stroke_x_ratio = 1
    stroke_y_ratio = 1.2
    height_ratio = 0.25
    end_width_ratio = 0.3
    curve_ratio = 1.35
    curve_thinning = 0.1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        h = self.height_ratio * b.height
        y1 = dc.math - h / 2 - sy / 2
        y2 = dc.math + h / 2 + sy / 2

        # Each end is a quarter of a loop spanning the whole height: going up
        # from y1 then right on the left, going right then up to y2 on the right
        qw = self.end_width_ratio * b.width
        qh = y2 - y1
        loop = Superellipse(b.x1, b.y1, b.x2, b.y2, b.hx, b.hy)
        ends = (
            (loop.resize(b.x1, y2 - 2 * qh, b.x1 + 2 * qw, y2), "top-left"),
            (loop.resize(b.x2 - 2 * qw, y1, b.x2, y1 + 2 * qh), "bottom-right"),
        )
        left, right = (
            draw_loop(
                pen, sx, sy, se.x1, se.y1, se.x2, se.y2, se.hx, se.hy, quarter=quarter
            )
            for se, quarter in ends
        )

        # Mid curve, from the top of the left end to the bottom of the right one
        xa, xb = b.x1 + qw, b.x2 - qw
        lhx, lihx = left["outer"].hx, left["inner"].hx
        rhx, rihx = right["outer"].hx, right["inner"].hx
        th = self.curve_thinning * dc.stroke_x
        r = self.curve_ratio
        pen.moveTo((xa, y2 - sy))
        pen.curveTo((xa + r * lihx + th, y2 - sy), (xb - r * rhx + th, y1), (xb, y1))
        pen.lineTo((xb, y1 + sy))
        pen.curveTo((xb - r * rihx - th, y1 + sy), (xa + r * lhx - th, y2), (xa, y2))
        pen.closePath()

