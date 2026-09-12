from glyphs.cyrillic.uppercase import CyrillicUppercaseGlyph
from draw.rect import draw_rect


class CyrillicUppercaseShaGlyph(CyrillicUppercaseGlyph):
    name = "cyrillic_uppercase_sha"
    unicode = "0x0428"
    offset = 0
    width_ratio = 1.2

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            uppercase=True,
            width_ratio=self.width_ratio,
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio

        # Upper stems
        draw_rect(pen, b.x1, 0, b.x1 + sx, dc.cap)
        draw_rect(pen, b.x2 - sx, 0, b.x2, dc.cap)
        draw_rect(pen, b.xmid - sx / 2, 0, b.xmid + sx / 2, dc.cap)
        draw_rect(pen, b.x1, b.y1, b.x2, b.y1 + sy)
