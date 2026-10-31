from glyphs import Glyph
from draw.dot import draw_dot


class MiddleDotGlyph(Glyph):
    name = "middle_dot"
    unicode = "0xB7"
    offset = 0
    width_ratio = 1
    dot_ratio = 1.8

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        draw_dot(pen, dc, b.xmid, dc.math, self.dot_ratio)


class GreekAnoTeleiaGlyph(MiddleDotGlyph):
    name = "greek_ano_teleia"
    unicode = "0x0387"
