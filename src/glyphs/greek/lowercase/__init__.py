from abc import ABC
from glyphs import Glyph
from draw.loop import draw_loop


class TailedGreekLowercaseGlyph(Glyph, ABC):
    """Lowercase glyphs (ς, ζ, ξ) whose bottom stroke goes down into the
    descender and ends with a terminal going back to the left"""

    stroke_x_ratio = 1.01
    stroke_y_ratio = 1.00
    hx_ratio = 1
    hy_ratio = 1
    tail_depth = 0.85
    tail_terminal = 0.1
    tail_height_ratio = 0.4

    def draw_tail(self, pen, dc, b, sx, sy):
        """Right half of a loop hanging below the bottom stroke of `b`; the
        glyph has to bring its own bottom stroke to `b.xmid`"""
        y1 = self.tail_depth * dc.descent
        y2 = sy
        yl2 = self.tail_height_ratio * dc.x_height * 2

        # Bottom left curve, going into the tail
        draw_loop(
            pen,
            sx,
            sy,
            b.x1,
            0,
            b.x2,
            yl2,
            self.hx_ratio * dc.hx,
            self.hy_ratio * dc.hy * self.tail_height_ratio * 2,
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
            self.hx_ratio * dc.hx,
            self.hy_ratio * dc.hy * (y2 - y1) / dc.x_height,
            cut="left",
        )
