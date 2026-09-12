from glyphs.cyrillic.uppercase import CyrillicUppercaseGlyph
from draw.rect import draw_rect
from draw.loop import draw_loop


class CyrillicUppercaseEfGlyph(CyrillicUppercaseGlyph):
    name = "cyrillic_uppercase_ef"
    unicode = "0x0424"
    offset = 0
    vertical_ratio = 0.9
    vertical_overflow = 0.05
    width_ratio = 1.24

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            uppercase=True,
            width_ratio=self.width_ratio,
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        y1 = b.y1 + (1 - self.vertical_ratio) * b.height / 2
        y2 = b.y2 - (1 - self.vertical_ratio) * b.height / 2
        of = self.vertical_overflow * b.height

        draw_loop(
            pen,
            sx,
            sy,
            b.x1,
            y1,
            b.x2,
            y2,
            b.hx,
            b.hy,
        )
        draw_rect(
            pen,
            b.xmid - sx / 2,
            b.y1 - of,
            b.xmid + sx / 2,
            b.y2 + of,
        )
