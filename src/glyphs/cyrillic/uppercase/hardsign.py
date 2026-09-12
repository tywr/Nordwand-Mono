from glyphs.cyrillic.uppercase import CyrillicUppercaseGlyph
from draw.rect import draw_rect
from draw.arch import draw_arch


class CyrillicUppercaseHardsignGlyph(CyrillicUppercaseGlyph):
    name = "cyrillic_uppercase_hardsign"
    unicode = "0x042A"
    offset = -20
    upper_ratio = 0.85  # Upper loop width as a fraction of the lower loop width
    mid_ratio = 0.54
    left_ratio = 0.2
    width_ratio = 1.32
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
        ymid = b.y1 + self.mid_ratio * b.height
        x1 = b.x1 + self.left_ratio * b.width

        lower_x1 = x1
        lower_x2 = b.x2
        lower_width = lower_x2 - lower_x1
        hx, hy = b.hx * self.hx_ratio * lower_width / b.width, b.hy * self.hy_ratio

        # Left stem
        draw_rect(pen, x1, 0, x1 + sx, dc.cap)

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
        draw_rect(pen, x1, 0, b.x2 - lower_width / 2, sy)
        draw_rect(
            pen,
            x1,
            ymid - sy / 2,
            (x1 + b.x2) / 2,
            ymid + sy / 2,
        )

        draw_rect(
            pen,
            0,
            b.y2 - sy,
            x1,
            b.y2,
        )
