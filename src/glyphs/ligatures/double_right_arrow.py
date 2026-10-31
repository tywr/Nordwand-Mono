from glyphs import LigatureGlyph
from draw.chevron import draw_chevron
from draw.polygon import draw_polygon
from glyphs.special.greater_than_sign import GreaterThenSignGlyph


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
    span = GreaterThenSignGlyph.span
    gap = 0.4
    rect_stroke_ratio = 0.92
    stroke_ratio = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        ymid = dc.math
        h = dc.parenthesis_length * self.span
        s = dc.stroke_x * self.rect_stroke_ratio
        g = self.gap * dc.window_width
        so = self.side_offset * dc.window_width
        x1 = so
        x_tip = b.x2 + dc.window_width
        x_back = b.x1 + dc.window_width
        _, delta = draw_chevron(
            pen, self.stroke_ratio * dc.stroke_x, x_tip, x_back, ymid, h
        )

        def x_end(y):
            # Middle of the chevron stroke at height y, so the bar end stays
            # inside the stroke whatever the chevron angle.
            t = abs(y - ymid) / (h / 2)
            return x_tip - t * (x_tip - x_back - delta) - delta / 2

        for yc in (ymid + g / 2, ymid - g / 2):
            y1, y2 = yc - s / 2, yc + s / 2
            draw_polygon(
                pen, points=[(x1, y1), (x_end(y1), y1), (x_end(y2), y2), (x1, y2)]
            )
