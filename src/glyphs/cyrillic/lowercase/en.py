from glyphs import Glyph
from draw.rect import draw_rect


class CyrillicLowercaseEnGlyph(Glyph):
    name = "cyrillic_lowercase_en"
    unicode = "0x43D"
    offset = 0
    bar_height = 0.518
    width_ratio = 0.99

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset, width_ratio=self.width_ratio)
        sx, sy = dc.stroke_x, dc.stroke_y
        yb = self.bar_height * b.height

        # Left stem
        draw_rect(pen, b.x1, b.y1, b.x1 + sx, b.y2)
        # Right stem
        draw_rect(pen, b.x2 - sx, b.y1, b.x2, b.y2)
        # Middle bar
        draw_rect(pen, b.x1, yb - sy / 2, b.x2, yb + sy / 2)
