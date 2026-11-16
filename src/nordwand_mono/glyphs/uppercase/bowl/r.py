from nordwand_mono.glyphs.uppercase.bowl import BowlUppercaseGlyph
from nordwand_mono.draw.loop import draw_loop
from nordwand_mono.draw.rect import draw_rect
from nordwand_mono.draw.parallelogramm import draw_parallelogramm


class UppercaseRGlyph(BowlUppercaseGlyph):
    name = "uppercase_r"
    unicode = "0x52"
    loop_ratio = 0.605
    loop_width = 0.96
    branch_start = 0.45
    leg_stroke_ratio = 1.0

    def draw(self, pen, dc):
        b = self.body(dc)
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        hx, hy = b.hx * self.loop_width, b.hy * self.loop_ratio
        xo = -0.8 * (sx - dc.default_stroke)
        ymid = b.y1 + (1 - self.loop_ratio) * b.height
        xb = b.x1 + self.branch_start * b.width + xo
        w = self.loop_width * b.width

        # Left stem
        draw_rect(pen, b.x1, b.y1, b.x1 + sx, b.y2)

        # Upper loop (narrower, displaced left)
        draw_loop(
            pen,
            sx,
            sy,
            b.x1,
            ymid,
            b.x1 + w,
            b.y2,
            hx,
            hy,
            cut="left",
        )

        # Connecting bars
        draw_rect(pen, b.x1, b.y2 - sy, b.x2 - b.width / 2, b.y2)
        draw_rect(
            pen,
            b.x1,
            ymid,
            b.x2 - b.width / 2,
            ymid + sy,
        )

        # Right stem
        draw_parallelogramm(
            pen,
            self.leg_stroke_ratio * dc.stroke_x,
            b.x2,
            0,
            xb,
            ymid + sy / 2,
            direction="top-left",
        )
