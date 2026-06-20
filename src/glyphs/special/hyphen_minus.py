from glyphs import Glyph
from draw.rect import draw_rect


class HyphenMinusGlyph(Glyph):
    name = "hyphen_minus"
    unicode = "0x2D"
    offset = 0
    side_offset = 0.05
    width_ratio = 1
    stroke_ratio = 0.92

    def draw(self, pen, dc):
        # b = dc.body_bounds(offset=0, width_ratio=self.width_ratio)
        s = self.stroke_ratio * dc.stroke_x
        so = self.side_offset * dc.window_width
        x1, x2 = so, dc.window_width - so
        draw_rect(
            pen,
            x1,
            dc.math + s / 2,
            x2,
            dc.math - s / 2,
        )
