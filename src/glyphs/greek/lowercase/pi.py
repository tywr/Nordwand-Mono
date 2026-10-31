from glyphs import Glyph
from draw.rect import draw_rect
from draw.square_corner import draw_square_corner


class GreekLowercasePiGlyph(Glyph):
    name = "greek_lowercase_pi"
    unicode = "0x3C0"
    offset = 0
    width_ratio = 1.14
    left_offset = 0.15
    right_offset = 0.2

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset, width_ratio=self.width_ratio)
        sx, sy = dc.stroke_x, dc.stroke_y
        xl = b.x1 + self.left_offset * b.width
        xr = b.x2 - self.right_offset * b.width
        draw_rect(
            pen,
            b.x1,
            b.y2 - sy,
            b.x2,
            b.y2,
        )
        draw_rect(
            pen,
            xl,
            b.y1,
            xl + sx,
            b.y2,
        )
        draw_square_corner(
            pen,
            sx,
            sy,
            xr - sx,
            b.y2,
            b.x2,
            b.y1,
            orientation="bottom-right"
        )
