from nordwand_mono.glyphs.uppercase.bowl import BowlUppercaseGlyph
from nordwand_mono.draw.loop import draw_loop
from nordwand_mono.draw.rect import draw_rect


class UppercaseDGlyph(BowlUppercaseGlyph):
    name = "uppercase_d"
    unicode = "0x44"
    arch_start = 0.4
    offset = 7
    accent_x_offset = -40

    def draw(self, pen, dc):
        b = self.body(dc)
        sx, sy = self.get_strokes(dc)
        xc = b.x1 + self.arch_start * b.width
        hx, hy = b.hx * self.hx_ratio, b.hy * self.hy_ratio
        w = 2 * (b.x2 - xc)

        # Left stem
        draw_rect(pen, b.x1, 0, b.x1 + sx, dc.cap)

        # Connecting bars
        draw_rect(pen, b.x1, b.y2 - sy, xc, b.y2)
        draw_rect(pen, b.x1, 0, xc, sy)

        draw_loop(
            pen,
            sx,
            sy,
            xc - w / 2,
            b.y1,
            xc + w / 2,
            b.y2,
            hx * w / b.width,
            hy,
            cut="left",
        )
