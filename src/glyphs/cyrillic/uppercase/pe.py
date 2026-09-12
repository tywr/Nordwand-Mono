from glyphs.cyrillic.uppercase import CyrillicUppercaseGlyph
from draw.rect import draw_rect
from draw.square_corner import draw_square_corner


class CyrillicUppercasePeGlyph(CyrillicUppercaseGlyph):
    name = "cyrillic_uppercase_pe"
    unicode = "0x041F"
    offset = 0
    top_offset = 0.00
    mid_ratio = 0.515
    top_ratio = 0.7
    width_ratio = 1.06

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            uppercase=True,
            width_ratio=self.width_ratio,
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio

        # Upper stems
        draw_rect(pen, b.x2 - sx, 0, b.x2, dc.cap)
        draw_rect(pen, b.x1, 0, b.x1 + sx, dc.cap)
        draw_rect(pen, b.x1, b.y2 - sy, b.x2, b.y2)
