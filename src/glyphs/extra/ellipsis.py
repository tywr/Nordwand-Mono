from glyphs import Glyph
from draw.rect import draw_rect


class EllipsisGlyph(Glyph):
    name = "ellipsis"
    unicode = "0x2026"
    offset = 0
    width = 440
    stroke_ratio = 1.5
    side_offset = 0.05
    max_stroke = 130

    def draw(self, pen, dc):
        s = min(self.stroke_ratio * dc.stroke_x, self.max_stroke)
        g = (dc.window_width - 3 * s) / 3
        x1, x2 = g / 2, dc.window_width - g / 2
        xmid = (x1 + x2) / 2
        draw_rect(pen, x1, 0, x1 + s, s)
        draw_rect(pen, x2 - s, 0, x2, s)
        draw_rect(pen, xmid - s / 2, 0, xmid + s / 2, s)
