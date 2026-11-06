from glyphs.uppercase import UppercaseGlyph
from draw.corner import draw_corner
from draw.loop import draw_loop
from draw.rect import draw_rect


class UppercaseDGlyph(UppercaseGlyph):
    name = "uppercase_d"
    unicode = "0x44"
    offset = 20
    arch_start = 0.4
    hx_ratio = 1
    hy_ratio = 1
    width_ratio = 1.02

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            width_ratio=self.width_ratio,
            uppercase=True,
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
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
