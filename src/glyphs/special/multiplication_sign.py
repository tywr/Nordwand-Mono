from glyphs import Glyph
from draw.rect import draw_rect


class MultipliationSignGlyph(Glyph):
    name = "multiplication_sign"
    unicode = "0xD7"
    offset = 0
    width_ratio = 1.31
    stroke_ratio = 1.2

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        s = dc.stroke_alt * self.stroke_ratio
        ymid = dc.math
        draw_rect(
            pen,
            b.x1,
            ymid - s / 2,
            b.x2,
            ymid + s / 2,
            rotate=45,
        )
        draw_rect(
            pen,
            b.x1,
            ymid - s / 2,
            b.x2,
            ymid + s / 2,
            rotate=-45,
        )
