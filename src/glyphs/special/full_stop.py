from glyphs import Glyph
from draw.dot import dot_size, draw_dot


class FullStopGlyph(Glyph):
    name = "full_stop"
    unicode = "0x2E"
    offset = 0
    width_ratio = 1
    taper = 0.5
    dot_ratio = 1.5

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        _, h = dot_size(dc, self.dot_ratio)
        draw_dot(pen, dc, b.xmid, h / 2, self.dot_ratio)
