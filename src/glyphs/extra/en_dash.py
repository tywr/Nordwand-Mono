from glyphs import Glyph
from draw.rect import draw_rect


class EnDashGlyph(Glyph):
    name = "en_dash"
    unicode = "0x2013"
    offset = 0
    width = 440

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=0)
        w = self.width
        draw_rect(
            pen,
            b.xmid - w / 2,
            dc.x_height / 2 + dc.stroke_y / 2,
            b.xmid + w / 2,
            dc.x_height / 2 - dc.stroke_y / 2,
        )
