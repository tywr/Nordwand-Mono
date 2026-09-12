from glyphs import Glyph
from draw.rect import draw_rect


class CyrillicLowercaseGheUpturnGlyph(Glyph):
    name = "cyrillic_lowercase_ghe_upturn"
    unicode = "0x0491"
    offset = 20
    width_ratio = 0.95
    hx_ratio = 1
    hy_ratio = 1
    upturn_ratio = 0.2

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            uppercase=True,
            width_ratio=self.width_ratio,
        )
        sx, sy = dc.stroke_x, dc.stroke_y
        ul = self.upturn_ratio * b.height

        draw_rect(pen, b.x1, 0, b.x1 + sx, b.y2)
        draw_rect(pen, b.x1, b.y2 - sy, b.x2, b.y2)
        draw_rect(pen, b.x2 - sx, b.y2, b.x2, b.y2 + ul)
