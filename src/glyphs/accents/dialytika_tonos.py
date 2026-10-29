from glyphs.accents import Accent
from glyphs.accents.acute import Acute
from glyphs.accents.dieresis import Dieresis


class DialytikaTonos(Accent):
    """Greek dialytika with a tonos between its two dots"""

    name = "dialytika_tonos"
    unicode = "0x0385"
    gap = 0.62
    tonos_scale = 1.0
    tonos_extra_y = 0.2

    def draw_at(self, pen, dc, x, y):
        dieresis = Dieresis()
        dieresis.gap = self.gap
        dieresis.draw_at(pen, dc, x, y)

        # The acute starts half a stroke left of x and leans to the right
        acute = Acute().scaled(dc, self.tonos_scale)
        ey = dc.x_height * self.tonos_extra_y
        acute.draw_at(pen, dc, x, y + ey)
