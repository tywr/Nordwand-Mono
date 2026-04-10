from glyphs import Glyph
from draw.rect import draw_rect


class VerticalLineGlyph(Glyph):
    name = "vertical_line"
    unicode = "0x7C"
    offset = 0
    width_ratio = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="ascent", width_ratio=self.width_ratio
        )
        ymid = dc.parenthesis
        y1, y2 = ymid - dc.parenthesis_length / 2, ymid + dc.parenthesis_length / 2
        draw_rect(pen, b.xmid - dc.stroke_x/2, y1, b.xmid + dc.stroke_x / 2, y2)
