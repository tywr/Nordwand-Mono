from glyphs.cyrillic.uppercase import CyrillicUppercaseGlyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm_vertical


class CyrillicUppercaseDzheGlyph(CyrillicUppercaseGlyph):
    name = "cyrillic_uppercase_dzhe"
    unicode = "0x040F"
    offset = 0
    width_ratio = 1.08
    middle_stroke_ratio = 0.84
    overlap = 0.3

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            width_ratio=self.width_ratio,
            uppercase=True,
            min_margin=dc.min_margin_uppercase,
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        descent = dc.descent * self.descent_ratio

        # Vertical stems
        draw_rect(pen, b.x1, b.y1, b.x1 + sx, b.y2)
        draw_rect(pen, b.x2 - sx, b.y1, b.x2, b.y2)
        draw_rect(pen, b.x1, b.y1, b.x2, b.y1 + sy)
        draw_rect(pen, b.xmid - sx / 2, descent, b.xmid + sx / 2, b.y1)
