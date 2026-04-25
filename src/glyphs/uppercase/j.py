from glyphs.uppercase import UppercaseGlyph
from draw.rect import draw_rect
from draw.loop import draw_loop
from draw.corner import draw_corner
from draw.parallelogramm import draw_parallelogramm_vertical


class UppercaseJGlyph(UppercaseGlyph):
    name = "uppercase_j"
    unicode = "0x4A"
    offset = -6
    cap_ratio = 1
    hx_ratio = 1
    loop_ratio = 0.56
    tail_len = 0.5

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            overshoot_bottom=True,
            width_ratio=self.width_ratio,
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        xc = self.cap_ratio * b.width
        yl = b.y1 + self.loop_ratio * b.height

        # Vertical stem (centered)
        draw_rect(pen, b.x2 - sx, (b.y1 + yl) / 2, b.x2, b.y2)

        # Top bar
        draw_rect(pen, b.x2 - xc, b.y2 - sy, b.x2, b.y2)

        # Corner to bottom
        draw_loop(
            pen,
            sx,
            sy,
            b.x1,
            b.y1,
            b.x2,
            yl,
            b.hx,
            self.loop_ratio * b.hy,
            cut="top",
        )
