from nordwand_mono.glyphs.accents import Accent
from nordwand_mono.glyphs.accents.acute import draw_slant


class Grave(Accent):
    name = "grave"
    unicode = "0x60"
    height = 0.33
    width = 0.55
    stroke_x_ratio = 0.9
    stroke_x_dampening = 0.5
    taper = 0.7  # Width of the base, relative to the top
    x_offset = 0.08

    def draw_at(self, pen, dc, x, y):
        h = self.height * dc.x_height
        s, _ = self.get_strokes(dc)
        xo = self.x_offset * s
        w = self.width * dc.accent_width
        draw_slant(pen, s, x + xo, y, w, h, self.taper, side=-1)
