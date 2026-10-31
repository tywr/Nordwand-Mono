from glyphs.uppercase import UppercaseGlyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm


class UppercaseZGlyph(UppercaseGlyph):
    name = "uppercase_z"
    unicode = "0x5A"
    offset = 0
    right_offset = 0.01
    left_offset = 0.01
    width_ratio = 1.06
    diag_stroke_ratio = 0.961  # Perpendicular thickness of the diagonal

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="cap", width_ratio=self.width_ratio
        )
        sy = dc.stroke_y * self.stroke_y_ratio
        xl = b.x1 + self.left_offset * b.width
        xr = b.x2 - self.right_offset * b.width

        # Top and bottom bars
        draw_rect(pen, xl, b.y2 - sy, xr, b.y2)
        draw_rect(pen, b.x1, 0, b.x2, sy)

        # Diagonal stroke
        draw_parallelogramm(
            pen,
            self.diag_stroke_ratio * dc.stroke_x,
            b.x1,
            b.y1 + sy,
            xr,
            b.y2 - sy,
        )
