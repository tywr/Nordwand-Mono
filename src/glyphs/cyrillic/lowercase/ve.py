from glyphs import Glyph
from draw.arch import draw_arch
from draw.rect import draw_rect


class CyrillicLowercaseVeGlyph(Glyph):
    name = "cyrillic_lowercase_ve"
    unicode = "0x0432"
    offset = 5
    upper_ratio = 0.85  # Upper loop width as a fraction of the lower loop width
    mid_ratio = 0.515
    width_ratio = 1.02
    hx_ratio = 1
    hy_ratio = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            uppercase=True,
            width_ratio=self.width_ratio,
        )
        sx, sy = dc.stroke_x, dc.stroke_y
        hx, hy = b.hx * self.hx_ratio, b.hy * self.hy_ratio
        ymid = b.y1 + self.mid_ratio * b.height

        lower_x1 = b.x1
        lower_x2 = b.x2
        lower_width = lower_x2 - lower_x1
        upper_width = self.upper_ratio * lower_width
        delta = lower_width - upper_width
        upper_x1 = lower_x1 + delta / 2
        upper_x2 = lower_x2 - delta / 2

        # Left stem
        draw_rect(pen, b.x1, 0, b.x1 + sx, b.y2)

        # Upper loop (narrower, displaced left)
        draw_arch(
            pen,
            sx,
            sy,
            upper_x1,
            ymid - sy / 2,
            upper_x2,
            b.y2,
            hx * (upper_x2 - upper_x1) / b.width,
            hy * (1 - self.mid_ratio),
            taper=0.75,
            side="bottom",
            cut="left",
        )
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
            taper=0.75,
            side="top",
            cut="left",
        )

        # Connecting bars
        draw_rect(pen, b.x1, b.y2 - sy, upper_x2 - upper_width / 2, b.y2)
        draw_rect(pen, b.x1, 0, b.x2 - lower_width / 2, sy)
        draw_rect(
            pen,
            b.x1,
            ymid - sy / 2,
            b.xmid,
            ymid + sy / 2,
        )
