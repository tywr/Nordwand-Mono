from glyphs.cyrillic.lowercase import CyrillicLowercaseGlyph
from draw.rect import draw_rect


class CyrillicLowercaseShchaGlyph(CyrillicLowercaseGlyph):
    name = "cyrillic_lowercase_shcha"
    unicode = "0x0449"
    offset = 10
    right_offset = 0.12
    width_ratio = 1.26

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
        )
        sx, sy = dc.stroke_x, dc.stroke_y
        descent = self.descent_ratio * dc.descent
        rx = b.x2 - self.right_offset * b.width
        xmid = (b.x1 + rx) / 2

        # Upper stems
        draw_rect(pen, b.x1, 0, b.x1 + sx, b.y2)
        draw_rect(pen, rx - sx, 0, rx, b.y2)
        draw_rect(pen, xmid - sx / 2, 0, xmid + sx / 2, b.y2)
        draw_rect(pen, b.x1, b.y1, b.x2, b.y1 + sy)
        draw_rect(pen, b.x2 - sx, descent, b.x2, sy)
