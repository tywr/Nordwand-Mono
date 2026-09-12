from draw.loop import draw_loop
from draw.rect import draw_rect
from glyphs.lowercase.round import RoundLowercaseGlyph


class CyrillicLowercaseEfGlyph(RoundLowercaseGlyph):
    name = "cyrillic_lowercase_ef"
    unicode = "0x0444"
    offset = 0

    def draw(
        self,
        pen,
        dc,
    ):
        b = dc.body_bounds(
            offset=self.offset,
            overshoot_bottom=True,
            overshoot_top=True,
            overshoot_left=True,
            overshoot_right=True,
        )
        sx, sy = self.stroke_x_ratio * dc.stroke_x, self.stroke_y_ratio * dc.stroke_y
        draw_loop(pen, sx, sy, b.x1, b.y1, b.x2, b.y2, b.hx, b.hy)
        draw_rect(pen, b.xmid - sx / 2, dc.descent, b.xmid + sx / 2, dc.cap)
