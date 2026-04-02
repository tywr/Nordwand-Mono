from config import FontConfig as fc
from glyph import Glyph
from shapes.superellipse_arch import draw_superellipse_arch
from shapes.rect import draw_rect


class UppercaseBGlyph(Glyph):
    name = "uppercase_b"
    unicode = "0x42"

    def draw(
        self,
        pen,
        stroke: int,
    ):
        offset = 0
        width = 350 + fc.h_overshoot
        ratio = 0.6
        hx = fc.side_hx
        hy = fc.side_hy
        arch_offset = 3 * stroke / 4

        x1 = fc.width / 2 - width / 2 - stroke / 2 + offset
        y1 = 0
        x2 = fc.width / 2 + width / 2 + stroke / 2 + offset + fc.h_overshoot
        y2 = fc.ascent
        ymid = y1 + (y2 - y1) / 2
        w = (x2 - x1) / 2

        # Left ascent
        draw_rect(pen, x1, 0, x1 + stroke, fc.ascent)

        # Upper loop
        draw_superellipse_arch(
            pen,
            stroke,
            x1 + (1 - ratio) * w,
            ymid - stroke / 2,
            x2,
            y2,
            hx,
            hy,
            offset=arch_offset,
            side="bottom",
            cut="left",
        )

        # Bottom loop
        draw_superellipse_arch(
            pen,
            stroke,
            x1 + (1 - ratio) * w,
            0,
            x2,
            ymid + stroke / 2,
            hx,
            hy,
            offset=arch_offset,
            side="top",
            cut="left",
        )

        # Lines to connect
        arch_x1 = x1 + (1 - ratio) * w
        cut_x = (arch_x1 + x2) / 2
        draw_rect(pen, x1, y2 - stroke, cut_x, y2)
        draw_rect(pen, x1, ymid - stroke / 2, cut_x, ymid + stroke / 2)
        draw_rect(pen, x1, y1, cut_x, y1 + stroke)
