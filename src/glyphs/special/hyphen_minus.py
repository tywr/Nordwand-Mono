from glyphs import Glyph
from draw.rect import draw_rect


class HyphenMinusGlyph(Glyph):
    name = "hyphen_minus"
    unicode = "0x2D"
    offset = 0
    width_ratio = 0.88

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=0, width_ratio=self.width_ratio)
        draw_rect(
            pen,
            b.x1,
            dc.math + dc.stroke_x / 2,
            b.x2,
            dc.math - dc.stroke_x / 2,
        )
