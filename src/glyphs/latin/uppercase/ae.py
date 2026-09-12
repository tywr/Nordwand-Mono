from draw.parallelogramm import draw_parallelogramm
from draw.rect import draw_rect
from glyphs.uppercase import UppercaseGlyph
from math import cos


class UppercaseAeGlyph(UppercaseGlyph):
    # Placeholder: plots the same as uppercase 'A' for the moment.
    name = "uppercase_ae"
    unicode = "0xC6"
    offset = 0
    bar_height = 0.35
    overlap = 0.25
    stroke_x_ratio = 1.02
    width_ratio = 1.2
    mid_ratio = 0.52
    xmid_ratio = 0.55

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="cap", width_ratio=self.width_ratio
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio

        half_width = b.width / 2 - sx / 2
        ov = self.overlap * sx
        hb = self.bar_height * b.height
        ymid = b.y1 + self.mid_ratio * b.height
        xmid = b.x1 + self.xmid_ratio * b.width

        # Left branch
        theta, delta = draw_parallelogramm(pen, sx, sy, b.x1, b.y1, xmid - ov, b.y2)

        # Crossbar
        draw_rect(
            pen,
            xmid - half_width + (hb - sy) * cos(theta),
            hb - sy,
            xmid,
            hb,
        )
        draw_rect(pen, xmid - sx / 2, b.y1, xmid + sx / 2, b.y2)

        # Vertical stem
        draw_rect(pen, xmid, ymid - sy / 2, b.x2, ymid + sy / 2)

        # Top bar
        draw_rect(pen, xmid, b.y2 - sy, b.x2, b.y2)

        # Middle bar
        draw_rect(
            pen,
            xmid,
            b.y1,
            b.x2,
            b.y1 + sy,
        )
