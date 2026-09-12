from glyphs.uppercase import UppercaseGlyph
from draw.arch import draw_arch
from draw.rect import draw_rect
from draw.square_corner import draw_square_corner


class CyrillicUppercaseLjeGlyph(UppercaseGlyph):
    name = "cyrillic_uppercase_lje"
    unicode = "0x0409"
    offset = 0
    upper_ratio = 0.85  # Upper loop width as a fraction of the lower loop width
    mid_ratio = 0.54
    xmid_ratio = 0.45
    corner_ratio = 0.25
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
        hx, hy = (
            b.hx * self.hx_ratio * (1 - self.xmid_ratio),
            b.hy * self.hy_ratio * self.mid_ratio,
        )
        ymid = b.y1 + self.mid_ratio * b.height

        lx1 = b.x1 + self.xmid_ratio * b.width
        lx2 = b.x2
        xc = b.x1 + self.corner_ratio * b.width

        # Left stem
        draw_rect(pen, lx1, 0, lx1 + sx, dc.cap)

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

        draw_rect(pen, xc, b.y2 - sy, lx1, b.y2)

        draw_square_corner(pen, sx, sy, xc, b.y2, b.x1, b.y1, orientation="bottom-left")
