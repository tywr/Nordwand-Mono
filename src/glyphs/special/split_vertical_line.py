from glyphs import Glyph
from draw.rect import draw_rect


class SplitVerticalLineGlyph(Glyph):
    name = "split_vertical_line"
    unicode = "0xA6"
    offset = 0
    width_ratio = 1
    gap_ratio = 0.33

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="ascent", width_ratio=self.width_ratio
        )
        ymid = dc.parenthesis
        y1, y2 = ymid - dc.parenthesis_length / 2, ymid + dc.parenthesis_length / 2
        g = self.gap_ratio * b.height

        draw_rect(
            pen, b.xmid - dc.stroke_x / 2, y1, b.xmid + dc.stroke_x / 2, ymid - g / 2
        )
        draw_rect(
            pen, b.xmid - dc.stroke_x / 2, ymid + g / 2, b.xmid + dc.stroke_x / 2, y2
        )
