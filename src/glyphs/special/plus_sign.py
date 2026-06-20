from glyphs import Glyph
from draw.rect import draw_rect


class PlusSignGlyph(Glyph):
    name = "plus_sign"
    unicode = "0x2B"
    offset = 0
    width_ratio = 1
    side_offset = 0.05
    stroke_ratio = 0.92

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="cap", width_ratio=self.width_ratio
        )
        s = dc.stroke_x * self.stroke_ratio
        so = self.side_offset * dc.window_width
        x1, x2 = so, dc.window_width - so

        draw_rect(pen, x1, dc.math - s / 2, x2, dc.math + s / 2)
        draw_rect(
            pen,
            b.xmid - s / 2,
            dc.math - b.width / 2,
            b.xmid + s / 2,
            dc.math + b.width / 2,
        )
