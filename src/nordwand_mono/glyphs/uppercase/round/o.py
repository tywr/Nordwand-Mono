from nordwand_mono.glyphs.uppercase.round import RoundUppercaseGlyph
from nordwand_mono.draw.loop import draw_loop


class UppercaseOGlyph(RoundUppercaseGlyph):
    name = "uppercase_o"
    unicode = "0x4F"
    offset = 0

    def draw(self, pen, dc):
        b = self.body(dc)
        sx, sy = self.get_strokes(dc)
        draw_loop(
            pen,
            sx,
            sy,
            b.x1,
            b.y1,
            b.x2,
            b.y2,
            b.hx,
            b.hy,
        )
