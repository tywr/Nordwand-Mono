from abc import ABC
from glyphs import Glyph
from draw.loop import draw_loop
from draw.rect import draw_rect


class TailedGreekLowercaseGlyph(Glyph, ABC):
    """Lowercase glyphs (ς, ζ, ξ) whose bottom stroke goes down into the
    descender and ends with a terminal going back to the left"""

    stroke_x_ratio = 1.01
    stroke_y_ratio = 1.00
    hx_ratio = 1
    hy_ratio = 1
    tail_depth = 0.85
    tail_terminal = 0.1

    def draw_tail(self, pen, dc, b, sx, sy):
        """Right half of a loop hanging below the bottom stroke of `b`; the
        glyph has to bring its own bottom stroke to `b.xmid`"""
        y1 = self.tail_depth * dc.descent
        y2 = b.y1 + sy
        # Bottom left curve, going into the tail
        draw_loop(
            pen,
            sx,
            sy,
            b.x1,
            b.y1,
            b.x2,
            b.y2,
            self.hx_ratio * b.hx,
            self.hy_ratio * b.hy,
            quarter="bottom-left",
        )
        draw_loop(
            pen,
            sx,
            sy,
            b.x1,
            y1,
            b.x2,
            y2,
            self.hx_ratio * b.hx,
            self.hy_ratio * b.hy * (y2 - y1) / b.height,
            cut="left",
        )
