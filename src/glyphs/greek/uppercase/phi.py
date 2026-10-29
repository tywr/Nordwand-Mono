from glyphs.uppercase import UppercaseGlyph
from draw.rect import draw_rect


class GreekUppercasePhiGlyph(UppercaseGlyph):
    name = "greek_uppercase_phi"
    unicode = "0x3A6"
    offset = 0

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset, height="cap", uppercase=True)
        draw_rect(pen, b.x1, b.y1, b.x2, b.y2)
