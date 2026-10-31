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
        sx = max(0, 0.8 * (sx - dc.default_stroke)) + min(dc.default_stroke, sx)
        six = max(0, 0.5 * (sx - 90)) + min(90, sx)
        draw_loop(pen, sx, sy, b.x1, b.y1, b.x2, b.y2, b.hx, b.hy)
        draw_rect(pen, b.xmid - six / 2, dc.descent, b.xmid + six / 2, dc.cap)
