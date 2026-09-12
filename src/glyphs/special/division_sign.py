from glyphs import Glyph
from draw.rect import draw_rect


class DivisionSignGlyph(Glyph):
    name = "division_sign"
    unicode = "0xF7"
    offset = 0
    side_offset = 0.05
    width_ratio = 1.0
    stroke_ratio = 0.92
    gap_ratio = 0.2
    dot_width = 0.33

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=0, width_ratio=self.width_ratio)
        s = self.stroke_ratio * dc.stroke_x
        gap = self.gap_ratio * b.height
        w = self.dot_width * b.width

        draw_rect(
            pen,
            b.x1,
            dc.math + s / 2,
            b.x2,
            dc.math - s / 2,
        )

        draw_rect(
            pen,
            b.xmid - w / 2,
            dc.math + s / 2 + gap,
            b.xmid + w / 2,
            dc.math + s / 2 + gap + w,
        )
        draw_rect(
            pen,
            b.xmid - w / 2,
            dc.math - s / 2 - gap - w,
            b.xmid + w / 2,
            dc.math - s / 2 - gap,
        )
