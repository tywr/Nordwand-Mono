from glyphs.uppercase import UppercaseGlyph
from draw.rect import draw_rect


class GreekUppercaseXiGlyph(UppercaseGlyph):
    name = "greek_uppercase_xi"
    unicode = "0x39E"
    offset = 0
    upper_bar_ratio = 1
    mid_bar_ratio = 0.95
    mid_ratio = 0.51
    width_ratio = 0.95

    def draw(self, pen, dc):
        b = dc.body_bounds(
            width_ratio=self.width_ratio,
            offset=self.offset,
            height="cap",
            uppercase=True,
        )
        sy = dc.stroke_y * self.stroke_y_ratio
        ymid = self.mid_ratio * b.height

        # Top bar
        draw_rect(pen, b.x1, b.y2 - sy, b.x1 + self.upper_bar_ratio * b.width, b.y2)

        # Middle bar
        draw_rect(
            pen,
            b.x1,
            ymid - sy / 2,
            b.x1 + self.mid_bar_ratio * b.width,
            ymid + sy / 2,
        )

        # Bottom bar
        draw_rect(pen, b.x1, b.y1, b.x2, b.y1 + sy)
