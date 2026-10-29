from glyphs.uppercase import UppercaseGlyph
from draw.rect import draw_rect


class GreekUppercaseGammaGlyph(UppercaseGlyph):
    name = "greek_uppercase_gamma"
    unicode = "0x393"
    offset = 30
    width_ratio = 0.96

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            uppercase=True,
            width_ratio=self.width_ratio,
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        draw_rect(pen, b.x1, b.y1, b.x1 + sx, b.y2)
        draw_rect(pen, b.x1, b.y2 - sy, b.x2, b.y2)
