from glyphs.accents import Accent
from draw.parallelogramm import draw_parallelogramm, parallelogramm_delta


class Grave(Accent):
    name = "grave"
    unicode = "0x60"
    height = 0.35
    width = 0.55
    stroke_ratio = 1.0

    def draw_at(self, pen, dc, x, y):
        h = self.height * dc.x_height
        w = self.width * dc.width
        s = self.stroke_ratio * dc.stroke_x
        # Base centered on x
        d = parallelogramm_delta(s, 0, 0, w, h)
        draw_parallelogramm(
            pen, s, x + d / 2, y - h / 2, x + d / 2 - w, y + h / 2, direction="top-left"
        )
