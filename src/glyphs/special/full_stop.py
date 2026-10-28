from glyphs import Glyph
from draw.rect import draw_rect


class FullStopGlyph(Glyph):
    name = "full_stop"
    unicode = "0x2E"
    offset = 0
    width_ratio = 1
    taper = 0.5
    stroke_ratio = 1.5
    dampening = 0.3

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        # Above regular, the dot only grows by a fraction of the stroke growth
        extra = max(0, dc.stroke_x - dc.default_stroke)
        s = self.stroke_ratio * (dc.stroke_x - self.dampening * extra)
        draw_rect(pen, b.xmid - s / 2, 0, b.xmid + s / 2, s)
