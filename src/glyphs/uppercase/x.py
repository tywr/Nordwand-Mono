from glyphs.uppercase import UppercaseGlyph
from draw.parallelogramm import draw_parallelogramm


class UppercaseXGlyph(UppercaseGlyph):
    name = "uppercase_x"
    unicode = "0x58"
    offset = 0
    width_ratio = 1.25

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, width_ratio=self.width_ratio, height="cap"
        )
        draw_parallelogramm(pen, dc.stroke_x, dc.stroke_y, b.x1, b.y1, b.x2, b.y2)
        draw_parallelogramm(
            pen, dc.stroke_x, dc.stroke_y, b.x2, b.y1, b.x1, b.y2, direction="top-left"
        )
