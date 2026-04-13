from glyphs import Glyph
from draw.rect import draw_rect


class EnDashGlyph(Glyph):
    name = "en_dash"
    unicode = "0x2013"
    offset = 0

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height"
        )
        w = dc.window_width / 2
        x1, x2 = b.xmid - w / 2, b.xmid + w / 2
        draw_rect(pen, x1, dc.x_height / 2 + dc.stroke_y / 2, x2, dc.x_height / 2 - dc.stroke_y / 2)
