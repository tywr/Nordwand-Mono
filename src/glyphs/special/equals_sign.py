from glyphs import Glyph
from draw.rect import draw_rect


class EqualsSignGlyph(Glyph):
    name = "equals_sign"
    unicode = "0x3D"
    offset = 0
    side_offset = 0.05
    width_ratio = 1
    gap = 0.4
    stroke_ratio = 0.92

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        s = dc.stroke_x * self.stroke_ratio
        g = self.gap * b.height
        so = self.side_offset * dc.window_width
        x1, x2 = so, dc.window_width - so
        draw_rect(
            pen,
            x1,
            dc.math + g / 2 - s / 2,
            x2,
            dc.math + g / 2 + s / 2,
        )
        draw_rect(
            pen,
            x1,
            dc.math - g / 2 - s / 2,
            x2,
            dc.math - g / 2 + s / 2,
        )
