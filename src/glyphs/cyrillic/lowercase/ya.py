from glyphs.cyrillic.lowercase import CyrillicLowercaseGlyph
from draw.loop import draw_loop
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm


class CyrillicLowercaseYaGlyph(CyrillicLowercaseGlyph):
    name = "cyrillic_lowercase_ya"
    unicode = "0x044F"
    offset = -20
    loop_ratio = 0.605
    loop_width = 0.96
    branch_start = 0.72
    width_ratio = 1.02

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            overshoot_right=True,
            width_ratio=self.width_ratio,
        )
        sx, sy = dc.stroke_x, dc.stroke_y
        hx, hy = b.hx * self.loop_width, b.hy * self.loop_ratio
        ymid = b.y1 + (1 - self.loop_ratio) * b.height
        xb = self.branch_start * b.width
        w = self.loop_width * b.width

        # Left stem
        draw_rect(pen, b.x2 - sx, 0, b.x2, b.y2)

        # Upper loop (narrower, displaced left)
        draw_loop(
            pen,
            sx,
            sy,
            b.x2 - w,
            ymid,
            b.x2,
            b.y2,
            hx,
            hy,
            cut="right",
        )

        # Connecting bars
        draw_rect(pen, b.x1 + b.width / 2, b.y2 - sy, b.x2, b.y2)
        draw_rect(
            pen,
            b.x1 + b.width / 2,
            ymid,
            b.x2,
            ymid + sy,
        )
        #
        # # Right stem
        draw_parallelogramm(
            pen,
            sx,
            sy,
            b.x1,
            0,
            xb,
            ymid + sy / 2,
            direction="top-right",
        )
