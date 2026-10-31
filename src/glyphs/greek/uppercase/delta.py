from glyphs.uppercase.a import UppercaseAGlyph
from draw.rect import draw_rect


class GreekUppercaseDeltaGlyph(UppercaseAGlyph):
    """The A with a bar along the baseline instead of its crossbar"""

    name = "greek_uppercase_delta"
    unicode = "0x394"

    def draw(self, pen, dc):
        b = self.body(dc)
        sy = dc.stroke_y * self.stroke_y_ratio
        _, delta = self.draw_branches(pen, dc, b)

        # Bar, its ends on the branches' centerlines
        draw_rect(pen, b.x1 + delta / 2, b.y1, b.x2 - delta / 2, b.y1 + sy)
