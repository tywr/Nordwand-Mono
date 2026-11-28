from nordwand_mono.glyphs.uppercase import UppercaseGlyph
from nordwand_mono.draw.loop import draw_loop
from nordwand_mono.draw.rect import draw_rect


class UppercaseOSlashGlyph(UppercaseGlyph):
    name = "uppercase_oslash"
    unicode = "0xD8"
    offset = 0
    stroke_x_ratio = UppercaseGlyph.stroke_x_ratio * 1.00
    stroke_y_ratio = UppercaseGlyph.stroke_y_ratio * 1.00
    width_ratio = 1.18
    slash_stroke_dampening = 0.5
    slash_length = 1.75

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            overshoot_bottom=True,
            overshoot_top=True,
            width_ratio=self.width_ratio,
            uppercase=True,
        )
        sx, sy = self.get_strokes(dc)
        ss = self.get_thinned_stroke(dc, self.slash_stroke_dampening)
        sl = self.slash_length * b.width
        draw_loop(
            pen,
            sx,
            sy,
            b.x1,
            b.y1,
            b.x2,
            b.y2,
            b.hx,
            b.hy,
        )
        draw_rect(
            pen,
            b.xmid - sl / 2,
            b.ymid - ss / 2,
            b.xmid + sl / 2,
            b.ymid + ss / 2,
            rotate=60,
        )
