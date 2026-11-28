from nordwand_mono.glyphs.uppercase.bowl import BowlUppercaseGlyph
from nordwand_mono.draw.loop import draw_loop
from nordwand_mono.draw.rect import draw_rect
from nordwand_mono.draw.parallelogramm import draw_parallelogramm


class UppercaseRGlyph(BowlUppercaseGlyph):
    name = "uppercase_r"
    unicode = "0x52"
    loop_ratio = 0.605
    loop_width = 0.96
    branch_start = 0.46
    hy_ratio = 1
    accent_x_offset = -40
    stroke_y_dampening = 0.8
    leg_stroke_dampening = 0.8

    def draw(self, pen, dc):
        b = self.body(dc)
        sx, sy = self.get_strokes(dc)
        xo = -0.5 * (sx - dc.default_stroke)
        yo = 0.5 * (dc.stroke_x - dc.default_stroke)
        ymid = b.y1 + (1 - self.loop_ratio) * b.height - yo
        xb = b.x1 + self.branch_start * b.width + xo
        w = self.loop_width * b.width
        s = max(0, self.leg_stroke_dampening * (sx - dc.default_stroke)) + min(
            dc.default_stroke, sx
        )

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
            b.hx,
            b.hy * self.hy_ratio * (b.y2 - ymid) / b.height,
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
            s,
            b.x2,
            0,
            xb,
            ymid + sy / 2,
            direction="top-left",
        )
