from glyphs.uppercase import UppercaseGlyph
from draw.loop import draw_loop
from draw.rect import draw_rect


class UppercaseUGlyph(UppercaseGlyph):
    name = "uppercase_u"
    unicode = "0x55"
    offset = 0
    hx_ratio = 1.0
    hy_ratio = 1.0
    width_ratio = 1.03
    loop_ratio = 0.66

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            overshoot_bottom=True,
            width_ratio=self.width_ratio,
            uppercase=True,
        )
        y2 = self.loop_ratio * b.height
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        hx, hy = self.hx_ratio * b.hx, self.hy_ratio * b.hy * self.loop_ratio

        draw_loop(pen, sx, sy, b.x1, b.y1, b.x2, y2, hx, hy, cut="top")

        draw_rect(pen, b.x1, (b.y1 + y2) / 2, b.x1 + sx, b.y2)
        draw_rect(pen, b.x2 - sx, (b.y1 + y2) / 2, b.x2, b.y2)
