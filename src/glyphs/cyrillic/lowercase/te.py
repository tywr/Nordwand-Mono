from glyphs import Glyph
from draw.rect import draw_rect


class CyrillicLowercaseTeGlyph(Glyph):
    name = "cyrillic_lowercase_te"
    unicode = "0x442"
    offset = 0
    width_ratio = 1.1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
            min_margin=dc.min_margin_uppercase,
        )
        sx, sy = dc.stroke_x, dc.stroke_y

        # Vertical stem (centered)
        draw_rect(pen, b.xmid - sx / 2, b.y1, b.xmid + sx / 2, b.y2)

        # Top bar
        draw_rect(pen, b.x1, b.y2 - sy, b.x2, b.y2)
