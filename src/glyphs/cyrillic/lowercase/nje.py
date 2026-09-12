from glyphs import Glyph
from draw.arch import draw_arch
from draw.rect import draw_rect


class CyrillicLowercaseNjeGlyph(Glyph):
    name = "cyrillic_lowercase_nje"
    unicode = "0x045A"
    offset = 8
    upper_ratio = 0.85  # Upper loop width as a fraction of the lower loop width
    mid_ratio = 0.56
    xmid_ratio = 0.45
    corner_ratio = 0.25
    width_ratio = 1.22
    hx_ratio = 1
    hy_ratio = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
        )
        sx, sy = dc.stroke_x, dc.stroke_y
        hx, hy = (
            b.hx * self.hx_ratio * (1 - self.xmid_ratio),
            b.hy * self.hy_ratio * self.mid_ratio,
        )
        ymid = b.y1 + self.mid_ratio * b.height

        lx1 = b.x1 + self.xmid_ratio * b.width
        lx2 = b.x2
        xc = b.x1 + self.corner_ratio * b.width

        # Left stem
        draw_rect(pen, lx1, 0, lx1 + sx, b.y2)

        # Lower loop (full width)
        draw_arch(
            pen,
            sx,
            sy,
            lx1,
            0,
            lx2,
            ymid + sy / 2,
            hx,
            hy,
            taper=1,
            side="top",
            cut="left",
        )

        # Connecting bars
        draw_rect(pen, lx1, 0, (lx1 + lx2) / 2, sy)
        draw_rect(
            pen,
            lx1,
            ymid - sy / 2,
            (lx1 + lx2) / 2,
            ymid + sy / 2,
        )

        draw_rect(pen, b.x1, ymid - sy / 2, lx1, ymid + sy / 2)
        draw_rect(pen, b.x1, b.y1, b.x1 + sx, b.y2)
