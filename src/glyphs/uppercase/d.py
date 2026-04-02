from config import FontConfig as fc
from glyph import Glyph
from shapes.superellipse_loop import draw_superellipse_loop
from shapes.corner import draw_corner
from shapes.rect import draw_rect


class UppercaseBGlyph(Glyph):
    name = "uppercase_d"
    unicode = "0x44"

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

        x1 = fc.width / 2 - width / 2 - stroke / 2 + offset
        y1 = 0
        x2 = fc.width / 2 + width / 2 + stroke / 2 + offset + fc.h_overshoot
        y2 = fc.ascent
        w = (x2 - x1) / 2

        # Left ascent
        draw_rect(pen, x1, 0, x1 + stroke, fc.ascent)

        # Right flat portion
        draw_rect(pen, x2 - stroke, 0.25 * fc.ascent, x2, 0.75 * fc.ascent)

        # Lines to connect
        arch_x1 = x1 + (1 - ratio) * w
        cut_x = (arch_x1 + x2) / 2
        draw_rect(pen, x1, y2 - stroke, cut_x, y2)
        draw_rect(pen, x1, y1, cut_x, y1 + stroke)

        # Corners
        draw_corner(
            pen, stroke, x2, 0.75 * fc.ascent, cut_x, y2, hx, hy, orientation="top-left"
        )
