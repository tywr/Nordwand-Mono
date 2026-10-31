from glyphs import LigatureGlyph
from draw.chevron import draw_chevron
from glyphs.special.greater_than_sign import GreaterThenSignGlyph
from draw.rect import draw_rect


class RightArrowGlyph(LigatureGlyph):
    """Ligature glyph for ->"""

    name = "right_arrow_liga"
    components = ["hyphen_minus", "greater_than_sign"]
    feature_tags = (
        "liga",
        "ss02",
    )
    number_characters = 2
    width_ratio = 0.88
    overlap = 0.6
    side_offset = 0.05
    span = GreaterThenSignGlyph.span
    gap = 0.0
    stroke_ratio = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        ymid = dc.math
        h = dc.parenthesis_length * self.span
        s = dc.stroke_x
        x1 = self.side_offset * dc.window_width
        g = self.gap * dc.window_width
        _, delta = draw_chevron(
            pen,
            self.stroke_ratio * dc.stroke_x,
            b.x2 + dc.window_width,
            b.x1 + dc.window_width,
            ymid,
            h,
        )
        draw_rect(
            pen,
            x1,
            dc.math - s / 2,
            b.x2 + dc.window_width - delta - g,
            dc.math + s / 2,
        )
