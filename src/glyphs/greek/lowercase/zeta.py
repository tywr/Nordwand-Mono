from draw.loop import draw_loop
from draw.polygon import draw_polygon
from draw.rect import draw_rect
from glyphs.greek.lowercase import TailedGreekLowercaseGlyph


class GreekLowercaseZetaGlyph(TailedGreekLowercaseGlyph):
    name = "greek_lowercase_zeta"
    unicode = "0x3B6"
    offset = 0
    width_ratio = 0.99
    top_offset = 0.15
    diagonal_ratio = 1.2

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            overshoot_bottom=True,
            overshoot_left=True,
            width_ratio=self.width_ratio,
        )
        sx, sy = self.stroke_x_ratio * dc.stroke_x, self.stroke_y_ratio * dc.stroke_y

        # Top bar
        draw_rect(
            pen, b.x1 + self.top_offset * b.width, dc.ascent - sy, b.x2, dc.ascent
        )

        self.draw_tail(pen, dc, b, sx, sy)
