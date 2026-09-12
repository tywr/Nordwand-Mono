from glyphs import Glyph
from draw.rect import draw_rect
from draw.square_corner import draw_square_corner


class CyrillicLowercaseElGlyph(Glyph):
    name = "cyrillic_lowercase_el"
    unicode = "0x043B"
    offset = 0
    upper_ratio = 0.94
    top_offset = 0.02
    mid_ratio = 0.515
    top_ratio = 0.7
    width_ratio = 1.24

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
        )
        sx, sy = dc.stroke_x, dc.stroke_y

        offset = self.top_offset * b.width
        upper_x2 = b.x2 - (1 - self.top_ratio) * b.width / 2 + offset
        upper_x1 = b.x1 + (1 - self.top_ratio) * b.width / 2 + offset

        # Upper stems
        draw_square_corner(
            pen,
            sx,
            sy,
            upper_x1 + sx,
            b.y2,
            b.x1,
            0,
            orientation="bottom-left"
        )
        draw_rect(pen, upper_x2 - sx, 0, upper_x2, b.y2)

        # Upper bar
        draw_rect(pen, upper_x1, b.y2 - sy, upper_x2, b.y2)
