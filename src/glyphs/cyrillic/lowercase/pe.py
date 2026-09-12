from glyphs import Glyph
from draw.rect import draw_rect


class CyrillicLowercasePeGlyph(Glyph):
    name = "cyrillic_lowercase_pe"
    unicode = "0x043F"
    offset = 0
    top_offset = 0.00
    mid_ratio = 0.515
    top_ratio = 0.7
    width_ratio = 0.99

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
        )
        sx, sy = dc.stroke_x, dc.stroke_y

        # Upper stems
        draw_rect(pen, b.x2 - sx, 0, b.x2, b.y2)
        draw_rect(pen, b.x1, 0, b.x1 + sx, b.y2)
        draw_rect(pen, b.x1, b.y2 - sy, b.x2, b.y2)
