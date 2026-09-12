from glyphs.cyrillic.lowercase import CyrillicLowercaseGlyph
from draw.rect import draw_rect


class CyrillicLowercaseDzheGlyph(CyrillicLowercaseGlyph):
    name = "cyrillic_lowercase_dzhe"
    unicode = "0x045F"
    offset = 0
    width_ratio = 0.99
    middle_stroke_ratio = 0.84
    overlap = 0.3

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
            min_margin=dc.min_margin_lowercase,
        )
        sx, sy = dc.stroke_x, dc.stroke_y
        descent = dc.descent * self.descent_ratio

        # Vertical stems
        draw_rect(pen, b.x1, b.y1, b.x1 + sx, b.y2)
        draw_rect(pen, b.x2 - sx, b.y1, b.x2, b.y2)
        draw_rect(pen, b.x1, b.y1, b.x2, b.y1 + sy)
        draw_rect(pen, b.xmid - sx / 2, descent, b.xmid + sx / 2, b.y1)
