from glyphs.cyrillic.uppercase import CyrillicUppercaseGlyph
from draw.rect import draw_rect
from draw.square_corner import draw_square_corner


class CyrillicUppercaseShhaGlyph(CyrillicUppercaseGlyph):
    """Ч turned by 180°."""

    name = "cyrillic_uppercase_shha"
    unicode = "0x04BA"
    offset = 20
    width_ratio = 1.06
    mid_ratio = 0.37  # Shoulder, down from the top

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            uppercase=True,
            width_ratio=self.width_ratio,
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        ymid = b.y2 - self.mid_ratio * b.height

        draw_rect(pen, b.x1, 0, b.x1 + sx, b.y2)
        draw_square_corner(
            pen,
            sx,
            sy,
            b.x2,
            b.y1,
            b.x1,
            ymid,
            orientation="top-left"
        )
