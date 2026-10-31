from glyphs import Glyph
from draw.dot import dot_size, draw_dot


class ColonGlyph(Glyph):
    name = "colon"
    unicode = "0x3A"
    offset = 0
    width_ratio = 1
    dot_ratio = 1.5
    gap = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        _, h = dot_size(dc, self.dot_ratio)
        g = b.height * self.gap

        draw_dot(pen, dc, b.xmid, b.y1 + h / 2, self.dot_ratio)
        draw_dot(pen, dc, b.xmid, b.y1 + g - h / 2, self.dot_ratio)
