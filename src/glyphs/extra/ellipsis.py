from glyphs import Glyph
from draw.dot import dot_size, draw_dot


class EllipsisGlyph(Glyph):
    name = "ellipsis"
    unicode = "0x2026"
    offset = 0
    width = 440
    dot_ratio = 1.5
    side_offset = 0.05

    def draw(self, pen, dc):
        w, h = dot_size(dc, self.dot_ratio)
        g = (dc.window_width - 3 * w) / 3
        for i in range(3):
            draw_dot(pen, dc, g / 2 + w / 2 + i * (w + g), h / 2, self.dot_ratio)
