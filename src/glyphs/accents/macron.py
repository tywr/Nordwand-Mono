from glyphs.accents import Accent
from draw.rect import draw_rect


class Macron(Accent):
    name = "macron"
    unicode = "0xAF"
    width = 0.95
    stroke_ratio = 1.3

    def draw_at(self, pen, dc, x, y):
        w = self.width * dc.width
        t = self.stroke_ratio * dc.stroke_alt
        draw_rect(pen, x - w / 2, y - t / 2, x + w / 2, y + t / 2)
