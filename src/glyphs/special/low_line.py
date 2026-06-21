from glyphs import Glyph
from draw.rect import draw_rect


class LowLineGlyph(Glyph):
    name = "low_line"
    unicode = "0x5F"
    offset = 0
    side_offset = 0.05
    stroke_ratio = 0.92
    width_ratio = 1

    def draw(self, pen, dc):
        # b = dc.body_bounds(
        #     offset=self.offset, height="x_height", width_ratio=self.width_ratio
        # )
        s = self.stroke_ratio * dc.stroke_x
        so = self.side_offset * dc.window_width
        x1, x2 = so, dc.window_width - so
        draw_rect(pen, x1, -s, x2, 0)
