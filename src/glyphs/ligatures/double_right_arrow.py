from math import cos
from glyphs import LigatureGlyph
from draw.parallelogramm import draw_parallelogramm
from draw.rect import draw_rect


class RightArrowGlyph(LigatureGlyph):
    """Ligature glyph for =>"""

    name = "double_right_arrow_liga"
    components = ["equals_sign", "greater_than_sign"]
    feature_tags = (
        "liga",
        "ss02",
    )
    number_characters = 2
    width_ratio = 0.88
    overlap = 0.6
    side_offset = 0.05
    span = 0.85
    gap = 0.4
    rect_stroke_ratio = 0.92
    stroke_ratio = 1.2

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        ymid = dc.math
        h = dc.parenthesis_length * self.span
        s = dc.stroke_x * self.rect_stroke_ratio
        s2 = self.stroke_ratio * dc.stroke_x
        g = self.gap * dc.window_width
        so = self.side_offset * dc.window_width
        x1 = so
        draw_parallelogramm(
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
        theta, delta = draw_parallelogramm(
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
        lb = 0.9 * g * cos(theta)
        draw_rect(
            pen,
            x1,
            dc.math + g / 2 - s / 2,
            b.x2 + dc.window_width - lb,
            dc.math + g / 2 + s / 2,
        )
        draw_rect(
            pen,
            x1,
            dc.math - g / 2 - s / 2,
            b.x2 + dc.window_width - lb,
            dc.math - g / 2 + s / 2,
        )
