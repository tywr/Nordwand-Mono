from glyphs.uppercase import UppercaseGlyph
from draw.square_corner import draw_square_corner


class LatinUppercaseIotaGlyph(UppercaseGlyph):
    """A stem curling to the right at the baseline (Ɩ)."""

    name = "latin_uppercase_iota"
    unicode = "0x196"
    offset = 0
    width_ratio = 0.6

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            uppercase=True,
            width_ratio=self.width_ratio,
        )
        draw_square_corner(
            pen,
            dc.stroke_x * self.stroke_x_ratio,
            dc.stroke_y * self.stroke_y_ratio,
            b.x1,
            b.y2,
            b.x2,
            b.y1,
            orientation="bottom-right",
        )
