from math import cos, tan, pi
from glyphs.uppercase import UppercaseGlyph
from draw.parallelogramm import draw_parallelogramm
from draw.rect import draw_rect
from draw.dented_rect import draw_dented_rect


class UppercaseAGlyph(UppercaseGlyph):
    name = "uppercase_a"
    unicode = "0x41"
    offset = 0
    bar_height = 0.35
    overlap = 0.25
    stroke_x_ratio = 1.02
    width_ratio = 1.2

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="cap", width_ratio=self.width_ratio
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio

        half_width = b.width / 2 - sx / 2
        ov = self.overlap * sx
        hb = self.bar_height * b.height

        # Left branch
        draw_parallelogramm(
            pen,
            sx,
            sy,
            b.x2,
            b.y1,
            b.xmid - ov,
            b.y2,
            direction="top-left",
        )
        # Right branch
        theta, delta = draw_parallelogramm(pen, sx, sy, b.x1, b.y1, b.xmid + ov, b.y2)

        # Crossbar
        draw_rect(
            pen,
            b.xmid - half_width + (hb - sy) * cos(theta),
            hb - sy,
            b.xmid + half_width - (hb - sy) * cos(theta),
            hb,
        )

        # Fill the gap
        h = dc.gap / (2 * tan(0.5 * pi - theta))
        p = ov * tan(theta)
        draw_rect(
            pen,
            b.xmid - ov,
            b.y2 - p - h,
            b.xmid + ov,
            b.y2,
        )
