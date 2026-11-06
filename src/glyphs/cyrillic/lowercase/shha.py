from glyphs import Glyph
from draw.rect import draw_rect
from draw.square_corner import draw_square_corner


class CyrillicLowercaseShhaGlyph(Glyph):
    """ч turned by 180°, its stem going up to the ascent."""

    name = "cyrillic_lowercase_shha"
    unicode = "0x04BB"
    offset = 20
    width_ratio = 0.99
    mid_ratio = 0  # Shoulder, down from the x-height

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
        )
        sx, sy = dc.stroke_x, dc.stroke_y
        ymid = b.y2 - self.mid_ratio * b.height

        draw_rect(pen, b.x1, 0, b.x1 + sx, dc.ascent)
        draw_square_corner(
            pen, sx, sy, b.x2, b.y1, b.x1, ymid, orientation="top-left"
        )
