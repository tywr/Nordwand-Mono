from glyphs.uppercase import UppercaseGlyph
from draw.parallelogramm import draw_parallelogramm_legacy
from draw.rect import draw_rect


class GreekUppercaseLamdaGlyph(UppercaseGlyph):
    name = "greek_uppercase_lamda"
    unicode = "0x39B"
    offset = 0
    bar_height = 0.38
    overlap = 0.5
    stroke_x_ratio = 1.02
    width_ratio = 1.2

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="cap", width_ratio=self.width_ratio
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio

        ov = self.overlap * sx

        # Left branch
        draw_parallelogramm_legacy(
            pen,
            sx,
            sy,
            b.x2,
            b.y1,
            b.xmid - ov,
            b.y2,
            direction="top-left",
        )
        # Right branch
        theta, delta = draw_parallelogramm_legacy(pen, sx, sy, b.x1, b.y1, b.xmid + ov, b.y2)
