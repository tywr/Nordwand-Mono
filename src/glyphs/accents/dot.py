from glyphs.accents import Accent
from draw.dot import draw_dot


class DotAbove(Accent):
    name = "dotaccent"
    unicode = "0x2D9"
    dot_ratio = 1.3

    def draw_at(self, pen, dc, x, y):
        draw_dot(pen, dc, x, y, self.dot_ratio)
