from nordwand_mono.glyphs.accents import Accent
from nordwand_mono.glyphs.accents.acute import Acute
from nordwand_mono.glyphs.accents.dieresis import Dieresis


class DialytikaTonos(Accent):
    """Greek dialytika with a tonos between its two dots"""

    name = "dialytika_tonos"
    unicode = "0x0385"
    gap = 0.62
    tonos_scale = 1.0
    tonos_extra_y = 0.24
    x_offset_tonos = -0.25

    def draw_at(self, pen, dc, x, y):
        dieresis = Dieresis()
        dieresis.gap = self.gap
        dieresis.draw_at(pen, dc, x, y)

        # The acute starts half a stroke left of x and leans to the right
        acute = Acute().scaled(dc, self.tonos_scale)
        ox = self.x_offset_tonos * self.gap
        acute.stroke_ratio = 0.75
        acute.width = 0.4
        ey = dc.x_height * self.tonos_extra_y
        acute.draw_at(pen, dc, x + ox, y + ey)
