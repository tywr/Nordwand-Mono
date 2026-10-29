from glyphs import Glyph
from draw.loop import draw_loop
from draw.rect import draw_rect


class GreekLowercaseThetaGlyph(Glyph):
    name = "greek_lowercase_theta"
    unicode = "0x3B8"
    offset = 0
    width_ratio = 1.02
    stroke_x_ratio = 1.01
    stroke_y_ratio = 1.00

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            overshoot_bottom=True,
            overshoot_top=True,
            width_ratio=self.width_ratio,
            uppercase=True,
        )
        draw_loop(
            pen,
            dc.stroke_x * self.stroke_x_ratio,
            dc.stroke_y * self.stroke_y_ratio,
            b.x1,
            b.y1,
            b.x2,
            b.y2,
            b.hx,
            b.hy,
        )
        draw_rect(
            pen,
            b.x1 + dc.stroke_x / 2,
            b.ymid - dc.stroke_y / 2,
            b.x2 - dc.stroke_x / 2,
            b.ymid + dc.stroke_y / 2,
        )
