from glyphs import Glyph
from draw.chevron import draw_chevron


class SingleRightPointingAngleQuotationMarkGlyph(Glyph):
    name = "single_right_pointing_angle_quotation_mark"
    unicode = "0x203A"
    offset = 0
    width_ratio = 0.55
    span = 0.6
    stroke_ratio = 1

    def chevrons(self, b):
        """(x_tip, x_back) of each chevron, given the body bounds."""
        return [(b.x2, b.x1)]

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        h = dc.x_height * self.span
        s = dc.stroke_x * self.stroke_ratio
        for x_tip, x_back in self.chevrons(b):
            draw_chevron(pen, s, x_tip, x_back, dc.x_height / 2, h)
