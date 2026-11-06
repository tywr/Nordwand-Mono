from draw.rect import draw_rect
from glyphs.numbers.seven import SevenGlyph


class SevenBarredGlyph(SevenGlyph):
    name = "seven_barred"
    font_feature = {"cv18": 1}
    alternative_character_comment = "Continental seven with a crossbar"
    bar_height = 0.52
    bar_length = 0.85

    def draw(self, pen, dc):
        super().draw(pen, dc)
        b = dc.body_bounds(
            offset=self.offset, height="cap", width_ratio=self.width_ratio, number=True
        )
        sy = dc.stroke_y * self.stroke_y_ratio
        x1 = b.x1 + (1 - self.bar_length) * b.width
        y = b.y1 + self.bar_height * b.height

        # Aligns with the right side of the bounds
        draw_rect(pen, x1, y - sy / 2, b.x2, y + sy / 2)
