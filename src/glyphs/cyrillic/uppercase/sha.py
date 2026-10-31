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
        sx = max(0, 0.8 * (sx - dc.default_stroke)) + min(dc.default_stroke, sx)
        six = max(0, 0.5 * (sx - 90)) + min(90, sx)

        # Upper stems
        draw_rect(pen, b.x1, 0, b.x1 + sx, dc.cap)
        draw_rect(pen, b.x2 - sx, 0, b.x2, dc.cap)
        draw_rect(pen, b.xmid - six / 2, 0, b.xmid + six / 2, dc.cap)
        draw_rect(pen, b.x1, b.y1, b.x2, b.y1 + sy)
