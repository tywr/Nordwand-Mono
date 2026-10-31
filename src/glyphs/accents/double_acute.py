from glyphs.accents.acute import Acute
from draw.parallelogramm import parallelogramm_delta


class DoubleAcute(Acute):
    """Two narrower acutes side by side, as in Hungarian ő and ű."""

    name = "double_acute"
    unicode = "0x2DD"
    width = 0.45
    # Thinner than the acute, so the narrower strokes still read as slanted
    stroke_ratio = 1
    # Distance between the two acutes' bases, relative to the extent of one
    separation = 0.75

    def draw_at(self, pen, dc, x, y):
        w = self.width * dc.width
        h = self.height * dc.x_height
        d = parallelogramm_delta(self.stroke_ratio * dc.stroke_x, 0, 0, w, h)
        sep = self.separation * (w + d)
        for bx in (x - sep / 2, x + sep / 2):
            super().draw_at(pen, dc, x=bx, y=y)
