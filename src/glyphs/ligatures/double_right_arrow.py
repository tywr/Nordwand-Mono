from math import tan
from glyphs import LigatureGlyph
from draw.parallelogramm import draw_parallelogramm
from draw.dented_rect import draw_dented_rect


class DoubleRightArrowGlyph(LigatureGlyph):
    """Ligature glyph for =>"""

    name = "double_right_arrow_liga"
    components = ["equals_sign", "greater_than_sign"]
    number_characters = 2
    width_ratio = 1
    overlap = 0.6
    gap = 0.4
    span = 0.85
    stroke_ratio = 0.92
    stroke_ratio_2 = 1.2

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        s = self.stroke_ratio * dc.stroke_x
        s2 = self.stroke_ratio_2 * dc.stroke_x
        ymid = dc.math
        h = dc.parenthesis_length * self.span
        theta, delta = draw_parallelogramm(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x2 + dc.window_width,
            ymid,
            b.x1 + dc.window_width,
            ymid + h / 2,
            direction="top-left",
            delta=s2,
        )
        draw_parallelogramm(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x1 + dc.window_width,
            ymid - h / 2,
            b.x2 + dc.window_width,
            ymid,
            direction="top-right",
            delta=s2,
        )

        g = self.gap * b.height
        draw_dented_rect(
            pen,
            b.x1,
            dc.math + g / 2 - s / 2,
            b.x2 + dc.window_width - 0.75 * g / tan(theta),
            dc.math + g / 2 + s / 2,
            side="right",
        )
        draw_dented_rect(
            pen,
            b.x1,
            dc.math - g / 2 - s / 2,
            b.x2 + dc.window_width - 0.75 * g / tan(theta),
            dc.math - g / 2 + s / 2,
            side="right",
        )
