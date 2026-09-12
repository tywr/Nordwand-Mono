from glyphs import Glyph
from draw.rect import draw_rect


class YenSignGlyph(Glyph):
    name = "yen_sign"
    unicode = "0xA5"
    offset = 0
    width_ratio = 1
    overflow_ratio = 0.2
    gap = 0.1
    bar_height = 0.2

    def draw(self, pen, dc):
        from glyphs.uppercase.y import UppercaseYGlyph

        b = dc.body_bounds(
            offset=self.offset, height="cap", width_ratio=self.width_ratio
        )
        sg = UppercaseYGlyph()
        sg.draw(pen, dc)

        sy = dc.stroke_y
        g = self.gap * b.height
        yb = b.y1 + self.bar_height * b.height

        draw_rect(pen, b.x1, yb, b.x2, yb + sy)
        draw_rect(pen, b.x1, yb + sy + g, b.x2, yb + g + 2 * sy)
