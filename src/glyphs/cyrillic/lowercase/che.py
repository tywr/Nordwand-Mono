from glyphs import Glyph
from draw.rect import draw_rect
from draw.square_corner import draw_square_corner


class CyrillicLowercaseCheGlyph(Glyph):
    name = "cyrillic_lowercase_che"
    unicode = "0x0447"
    offset = -20
    width_ratio = 0.99
    mid_ratio = 0.37

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
        )
        sx, sy = dc.stroke_x, dc.stroke_y
        ymid = b.y1 + self.mid_ratio * b.height

        # Upper stems
        draw_rect(pen, b.x2 - sx, 0, b.x2, b.y2)
        draw_square_corner(
            pen, sx, sy, b.x1, b.y2, b.x2, ymid, orientation="bottom-right"
        )
