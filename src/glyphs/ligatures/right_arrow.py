from glyphs import LigatureGlyph
from draw.parallelogramm import draw_parallelogramm
from draw.rect import draw_rect


class RightArrowGlyph(LigatureGlyph):
    """Ligature glyph for ->"""

    name = "right_arrow_liga"
    components = ["hyphen_minus", "greater_than_sign"]
    number_characters = 2
    width_ratio = 0.88
    overlap = 0.6
    span = 0.85
    stroke_ratio = 1.2

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        o = ((1 - self.width_ratio) * b.width) / 2
        ymid = dc.math
        h = dc.parenthesis_length * self.span
        s = dc.stroke_x
        s2 = self.stroke_ratio * dc.stroke_x
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
        draw_rect(
            pen,
            b.x1 + o,
            dc.math - s / 2,
            b.x2 + dc.window_width - s2 / 2,
            dc.math + s / 2,
        )
