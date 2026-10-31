from glyphs import Glyph
from draw.chevron import draw_chevron
from draw.rect import draw_rect


class RightArrowGlyph(Glyph):
    name = "right_arrow"
    unicode = "0x2192"
    offset = 0
    side_offset_left = 0.05
    side_offset_right = 0.02
    width_ratio = 1.33
    overlap = 0.6
    span = 0.4
    arrow_width = 0.5
    stroke_ratio = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        ymid = dc.math
        h = dc.parenthesis_length * self.span
        s = dc.stroke_x * self.stroke_ratio
        sy = dc.stroke_x
        x1 = self.side_offset_left * dc.window_width
        x2 = dc.window_width - self.side_offset_right * dc.window_width
        px1 = (1 - self.arrow_width) * dc.window_width
        _, delta = draw_chevron(pen, s, x2, px1, ymid, h)
        draw_rect(
            pen,
            x1,
            ymid - sy / 2,
            x2 - delta / 2,
            ymid + sy / 2,
        )
