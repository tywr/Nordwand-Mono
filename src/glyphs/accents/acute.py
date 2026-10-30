from config import FontConfig as fc
from glyphs.accents import Accent
from draw.parallelogramm import draw_parallelogramm


class Acute(Accent):
    name = "acute"
    unicode = "0xB4"
    height = 0.35
    width = 0.55
    stroke_ratio = 1.1

    def scaled(self, dc, k):
        """Same slant, its height and its slanted part scaled by `k`"""
        d = self.stroke_ratio * dc.stroke_x
        self.width = (d + k * (self.width * dc.width - d)) / dc.width
        self.height *= k
        return self

    def draw_at(self, pen, dc, x, y, stroke_ratio=None):
        h = self.height * dc.x_height
        w = self.width * dc.width
        d = self.stroke_ratio * dc.stroke_x
        draw_parallelogramm(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            x - d / 2,
            y - h / 2,
            x + w - d / 2,
            y + h / 2,
            delta=d,
        )


class Tonos(Acute):
    name = "tonos"
    unicode = "0x0384"


class CombiningAcute(Acute):
    name = "combining_acute"
    unicode = "0x0301"
    number_characters = 0

    def draw(self, pen, dc):
        # Fallback placement when shaping does not apply the ccmp glyph.
        self.draw_at(pen, dc, x=-fc.window_width / 2, y=fc.accent_cap)
