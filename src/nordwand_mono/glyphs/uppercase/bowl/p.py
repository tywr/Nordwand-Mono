from nordwand_mono.glyphs.uppercase.bowl import BowlUppercaseGlyph
from nordwand_mono.draw.loop import draw_loop
from nordwand_mono.draw.rect import draw_rect


class UppercasePGlyph(BowlUppercaseGlyph):
    name = "uppercase_p"
    unicode = "0x50"
    offset = 17
    loop_ratio = 0.645
    hy_ratio = 1

    def draw(self, pen, dc):
        b = self.body(dc)
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        yo = 0.5 * (dc.stroke_x - dc.default_stroke)
        ymid = b.y1 + (1 - self.loop_ratio) * b.height - yo

        # Left stem
        draw_rect(pen, b.x1, 0, b.x1 + sx, dc.cap)

        # Upper loop (narrower, displaced left)
        draw_loop(
            pen,
            sx,
            sy,
            b.x1,
            ymid,
            b.x2,
            b.y2,
            b.hx,
            b.hy * (b.y2 - ymid) / b.height * self.hy_ratio,
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
