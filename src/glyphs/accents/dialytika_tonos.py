from glyphs.accents import Accent
from glyphs.accents.acute import Acute
from glyphs.accents.dieresis import Dieresis


class DialytikaTonos(Accent):
    """Greek dialytika with a tonos between its two dots"""

    name = "dialytika_tonos"
    unicode = "0x0385"
    gap = 0.62
    tonos_scale = 0.6

    def draw_at(self, pen, dc, x, y):
        dieresis = Dieresis()
        dieresis.gap = self.gap
        dieresis.draw_at(pen, dc, x, y)

        # The acute starts half a stroke left of x and leans to the right
        acute = Acute().scaled(dc, self.tonos_scale)
        w = acute.width * dc.width
        d = acute.stroke_ratio * dc.stroke_x
        acute.draw_at(pen, dc, x - (w - d) / 2, y)
