from glyphs import Glyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm_vertical


class CyrillicLowercaseIGlyph(Glyph):
    name = "cyrillic_lowercase_i"
    unicode = "0x0438"
    offset = 0
    width_ratio = 1.0
    middle_stroke_ratio = 0.84
    overlap = 0.3

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
            min_margin=dc.min_margin_uppercase,
        )
        sx, sy = dc.stroke_x, dc.stroke_y

        # Vertical stems
        draw_rect(pen, b.x1, b.y1, b.x1 + sx, b.y2)
        draw_rect(pen, b.x2 - sx, b.y1, b.x2, b.y2)

        # Diagonal
        theta, delta = draw_parallelogramm_vertical(
            pen,
            sx * self.middle_stroke_ratio,
            sy * self.middle_stroke_ratio,
            b.x1 + sx,
            b.y1,
            b.x2 - sx,
            b.y2,
            direction="top-right",
        )
