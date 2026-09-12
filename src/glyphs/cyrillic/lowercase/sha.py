from glyphs import Glyph
from draw.rect import draw_rect


class CyrillicLowercaseShaGlyph(Glyph):
    name = "cyrillic_lowercase_sha"
    unicode = "0x0448"
    offset = 0
    width_ratio = 1.16

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
        )
        sx, sy = dc.stroke_x, dc.stroke_y

        # Upper stems
        draw_rect(pen, b.x1, 0, b.x1 + sx, b.y2)
        draw_rect(pen, b.x2 - sx, 0, b.x2, b.y2)
        draw_rect(pen, b.xmid - sx / 2, 0, b.xmid + sx / 2, b.y2)
        draw_rect(pen, b.x1, b.y1, b.x2, b.y1 + sy)
