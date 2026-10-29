from glyphs import Glyph
from draw.rect import draw_rect
from draw.square_corner import draw_square_corner


class GreekLowercaseTauGlyph(Glyph):
    name = "greek_lowercase_tau"
    unicode = "0x3C4"
    offset = -10
    width_ratio = 1.08
    stem_ratio = 0.45
    stem_foot_offset = 0.05

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset, width_ratio=self.width_ratio)
        sx, sy = dc.stroke_x, dc.stroke_y
        xmid = b.x1 + self.stem_ratio * b.width
        xr = b.x2 - self.stem_foot_offset * b.width
        draw_rect(pen, b.x1, b.y2 - sy, b.x2, b.y2)
        draw_square_corner(
            pen,
            sx,
            sy,
            xmid - sx / 2,
            b.y2,
            xr,
            b.y1,
            orientation="bottom-right"
        )
