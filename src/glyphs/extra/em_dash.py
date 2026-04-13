from glyphs import Glyph
from draw.rect import draw_rect


class EmDashGlyph(Glyph):
    name = "em_dash"
    unicode = "0x2014"
    offset = 0

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height"
        )
        w = dc.window_width
        x1, x2 = b.xmid - w / 2, b.xmid + w / 2
        draw_rect(pen, x1, dc.x_height / 2 + dc.stroke_y / 2, x2, dc.x_height / 2 - dc.stroke_y / 2)
