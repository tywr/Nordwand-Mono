from glyphs.cyrillic.lowercase import CyrillicLowercaseGlyph
from draw.rect import draw_rect


class CyrillicLowercaseTseGlyph(CyrillicLowercaseGlyph):
    name = "cyrillic_lowercase_tse"
    unicode = "0x0446"
    offset = 10
    right_offset = 0.12
    width_ratio = 1.12

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
        )
        sx, sy = dc.stroke_x, dc.stroke_y
        descent = self.descent_ratio * dc.descent
        rx = b.x2 - self.right_offset * b.width

        # Upper stems
        draw_rect(pen, b.x1, 0, b.x1 + sx, b.y2)
        draw_rect(pen, b.x1, b.y1, b.x2, b.y1 + sy)
        draw_rect(pen, b.x2 - sx, descent, b.x2, sy)
        draw_rect(pen, rx - sx, 0, rx, b.y2)
