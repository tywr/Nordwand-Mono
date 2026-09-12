from glyphs.uppercase import UppercaseGlyph
from draw.arch import draw_arch
from draw.rect import draw_rect


class CyrillicUppercaseYeruGlyph(UppercaseGlyph):
    name = "cyrillic_uppercase_yeru"
    unicode = "0x042B"
    offset = 0
    upper_ratio = 0.85  # Upper loop width as a fraction of the lower loop width
    mid_ratio = 0.54
    xmid_ratio = 0.7
    width_ratio = 1.16
    hx_ratio = 1
    hy_ratio = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            uppercase=True,
            width_ratio=self.width_ratio,
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        hx, hy = b.hx * self.hx_ratio * self.xmid_ratio, b.hy * self.hy_ratio
        ymid = b.y1 + self.mid_ratio * b.height

        lower_x1 = b.x1
        lower_x2 = b.x1 + self.xmid_ratio * b.width
        lower_width = lower_x2 - lower_x1

        # Left stem
        draw_rect(pen, b.x1, 0, b.x1 + sx, dc.cap)

        # Lower loop (full width)
        draw_arch(
            pen,
            sx,
            sy,
            lower_x1,
            0,
            lower_x2,
            ymid + sy / 2,
            hx,
            hy * self.mid_ratio,
            taper=1,
            side="top",
            cut="left",
        )

        # Connecting bars
        draw_rect(pen, b.x1, 0, (lower_x1 + lower_x2) / 2, sy)
        draw_rect(
            pen,
            b.x1,
            ymid - sy / 2,
            (lower_x1 + lower_x2) / 2,
            ymid + sy / 2,
        )

        # Right stroke
        draw_rect(
            pen,
            b.x2 - sx,
            b.y1,
            b.x2,
            b.y2
        )
