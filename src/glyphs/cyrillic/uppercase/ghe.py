from glyphs.cyrillic.uppercase import CyrillicUppercaseGlyph
from draw.rect import draw_rect


class CyrillicUppercaseGheGlyph(CyrillicUppercaseGlyph):
    name = "cyrillic_uppercase_ghe"
    unicode = "0x0413"
    offset = 45
    upper_ratio = 0.85  # Upper loop width as a fraction of the lower loop width
    mid_ratio = 0.515
    top_ratio = 0.92
    width_ratio = 1.06

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            uppercase=True,
            width_ratio=self.width_ratio,
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio

        upper_x2 = b.x1 + self.top_ratio * b.width

        # Left stem
        draw_rect(pen, b.x1, 0, b.x1 + sx, dc.cap)

        # Connecting bars
        draw_rect(pen, b.x1, b.y2 - sy, upper_x2, b.y2)
