from glyphs.uppercase.round import RoundUppercaseGlyph
from draw.loop import draw_loop


class UppercaseOGlyph(RoundUppercaseGlyph):
    name = "uppercase_o"
    unicode = "0x4F"
    offset = 0

    def draw(self, pen, dc):
        b = self.body(dc)
        draw_loop(
            pen,
            dc.stroke_x * self.stroke_x_ratio,
            dc.stroke_y * self.stroke_y_ratio,
            b.x1,
            b.y1,
            b.x2,
            b.y2,
            b.hx,
            b.hy,
        )
