from glyphs import Glyph
from draw.rect import draw_rect


class EmDashGlyph(Glyph):
    name = "em_dash"
    unicode = "0x2014"
    offset = 0
    stroke_ratio = 0.85

    def draw(self, pen, dc):
        s = dc.stroke_x * self.stroke_ratio
        draw_rect(
            pen, 0, dc.x_height / 2 + s / 2, dc.window_width, dc.x_height / 2 - s / 2
        )
