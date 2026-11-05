from glyphs import Glyph
from draw.square_corner import draw_square_corner


class LatinLowercaseIotaGlyph(Glyph):
    """A stem curling to the right at the baseline (ɩ)."""

    name = "latin_lowercase_iota"
    unicode = "0x269"
    offset = 0
    width_ratio = 0.6

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset, width_ratio=self.width_ratio)
        draw_square_corner(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x1,
            b.y2,
            b.x2,
            b.y1,
            orientation="bottom-right",
        )
