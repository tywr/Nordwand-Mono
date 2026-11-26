from nordwand_mono.glyphs.accents import Accent
from nordwand_mono.glyphs.accents.acute import draw_slant


class Grave(Accent):
    name = "grave"
    unicode = "0x60"
    height = 0.32
    width = 0.56
    stroke_ratio = 0.9
    taper = 0.7  # Width of the base, relative to the top
    x_offset = 0.1

    def draw_at(self, pen, dc, x, y):
        h = self.height * dc.x_height
        s = self.stroke_ratio * dc.stroke_x
        xo = self.x_offset * s
        w = self.width * dc.width + xo
        draw_slant(pen, s, x + xo, y, w, h, self.taper, side=-1)
