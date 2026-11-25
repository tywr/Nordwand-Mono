from nordwand_mono.glyphs.numbers import NumberGlyph
from nordwand_mono.draw.rect import draw_rect
from nordwand_mono.draw.parallelogramm import draw_parallelogramm


class SevenGlyph(NumberGlyph):
    name = "seven"
    unicode = "0x37"
    offset = -10
    offset_foot = 0.22
    width_ratio = 0.97
    stroke_ratio = 1.00

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="cap", width_ratio=self.width_ratio, number=True
        )
        _, sy = self.get_strokes(dc)
        ox = self.offset_foot * b.width
        s = self.stroke_ratio * dc.stroke_x

        # Top bar
        draw_rect(pen, b.x1, b.y2 - sy, b.x2, b.y2)

        # Diagonal stroke
        draw_parallelogramm(pen, s, b.x1 + ox, b.y1, b.x2, b.y2 - sy)
