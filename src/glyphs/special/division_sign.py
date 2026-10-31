from glyphs import Glyph
from draw.rect import draw_rect
from draw.dot import dot_size, draw_dot


class DivisionSignGlyph(Glyph):
    name = "division_sign"
    unicode = "0xF7"
    offset = 0
    side_offset = 0.05
    width_ratio = 1.0
    stroke_ratio = 0.92
    gap_ratio = 0.2
    dot_ratio = 1.5

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=0, width_ratio=self.width_ratio)
        s = self.stroke_ratio * dc.stroke_x
        gap = self.gap_ratio * b.height
        _, h = dot_size(dc, self.dot_ratio)

        draw_rect(
            pen,
            b.x1,
            dc.math + s / 2,
            b.x2,
            dc.math - s / 2,
        )

        dy = s / 2 + gap + h / 2
        draw_dot(pen, dc, b.xmid, dc.math + dy, self.dot_ratio)
        draw_dot(pen, dc, b.xmid, dc.math - dy, self.dot_ratio)
