from glyphs import Glyph
from draw.rect import draw_rect


class EnDashGlyph(Glyph):
    name = "en_dash"
    unicode = "0x2013"
    offset = 0
    width = 440
    stroke_ratio = 0.85

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=0)
        w = self.width
        s = dc.stroke_x * self.stroke_ratio
        draw_rect(
            pen,
            b.xmid - w / 2,
            dc.x_height / 2 + s / 2,
            b.xmid + w / 2,
            dc.x_height / 2 - s / 2,
        )
