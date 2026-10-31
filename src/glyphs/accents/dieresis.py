from glyphs.accents import Accent
from draw.dot import dot_size, draw_dot


class Dieresis(Accent):
    name = "dieresis"
    unicode = "0xA8"
    gap = 0.38
    dot_ratio = 1.3

    def draw_at(self, pen, dc, x, y):
        w, _ = dot_size(dc, self.dot_ratio)
        g = self.gap * dc.width
        draw_dot(pen, dc, x - g / 2 - w / 4, y, self.dot_ratio)
        draw_dot(pen, dc, x + g / 2 + w / 4, y, self.dot_ratio)
