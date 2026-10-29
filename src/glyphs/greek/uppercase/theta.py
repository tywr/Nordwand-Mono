from glyphs.uppercase import UppercaseGlyph
from draw.rect import draw_rect


class GreekUppercaseThetaGlyph(UppercaseGlyph):
    name = "greek_uppercase_theta"
    unicode = "0x398"
    offset = 0

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset, height="cap", uppercase=True)
        draw_rect(pen, b.x1, b.y1, b.x2, b.y2)
