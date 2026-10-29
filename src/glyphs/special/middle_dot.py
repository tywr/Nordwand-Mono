from glyphs import Glyph
from draw.rect import draw_rect


class MiddleDotGlyph(Glyph):
    name = "middle_dot"
    unicode = "0xB7"
    offset = 0
    width_ratio = 1
    stroke_ratio = 1.8

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        s = self.stroke_ratio * dc.stroke_x
        y = dc.math
        draw_rect(pen, b.xmid - s / 2, y - s / 2, b.xmid + s / 2, y + s / 2)


class GreekAnoTeleiaGlyph(MiddleDotGlyph):
    name = "greek_ano_teleia"
    unicode = "0x0387"
