from glyphs.uppercase import UppercaseGlyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm


class GreekUppercaseSigmaGlyph(UppercaseGlyph):
    name = "greek_uppercase_sigma"
    unicode = "0x3A3"
    offset = 0
    x_mid_ratio = 0.77
    diag_stroke_ratio = 0.944  # Perpendicular thickness of the diagonals

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset, height="cap", uppercase=True)
        sy = dc.stroke_y * self.stroke_y_ratio
        xmid = b.x1 + self.x_mid_ratio * b.width

        draw_rect(pen, b.x1, b.y2 - sy, b.x2, b.y2)
        draw_rect(pen, b.x1, b.y1, b.x2, b.y1 + sy)

        s = self.diag_stroke_ratio * dc.stroke_x
        draw_parallelogramm(
            pen, s, b.x1, b.y1 + sy, xmid, b.ymid, direction="top-right"
        )
        draw_parallelogramm(
            pen, s, b.x1, b.y2 - sy, xmid, b.ymid, direction="bottom-right"
        )
