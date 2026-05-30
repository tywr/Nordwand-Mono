from draw.loop import draw_loop
from glyphs.lowercase.round import RoundLowercaseGlyph
from draw.rect import draw_rect


class OSlashGlyph(RoundLowercaseGlyph):
    name = "oslash"
    unicode = "0xF8"
    offset = 0
    slash_stroke = 1.2
    slash_length = 1.4

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
        ss = sy * self.slash_length
        sl = self.slash_length * b.width
        draw_loop(pen, sx, sy, b.x1, b.y1, b.x2, b.y2, b.hx, b.hy)
        draw_rect(
            pen,
            b.xmid - sl / 2,
            b.ymid - ss / 2,
            b.xmid + sl / 2,
            b.ymid + ss / 2,
            rotate=45,
        )
