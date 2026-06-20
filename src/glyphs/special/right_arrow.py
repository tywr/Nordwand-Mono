from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm
from draw.rect import draw_rect


class RightArrowGlyph(Glyph):
    name = "right_arrow"
    unicode = "0x2192"
    offset = 0
    side_offset_left = 0.05
    side_offset_right = 0.02
    width_ratio = 1.33
    overlap = 0.6
    span = 0.65
    arrow_width = 0.66
    stroke_ratio = 1.2

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
        draw_parallelogramm(
            pen,
            s,
            s,
            x2,
            ymid,
            px1,
            ymid + h / 2,
            direction="top-left",
            delta=s,
        )
        draw_parallelogramm(
            pen,
            s,
            s,
            px1,
            ymid - h / 2,
            x2,
            ymid,
            direction="top-right",
            delta=s,
        )
        draw_rect(
            pen,
            x1,
            ymid - sy / 2,
            x2 - s / 2,
            ymid + sy / 2,
        )
