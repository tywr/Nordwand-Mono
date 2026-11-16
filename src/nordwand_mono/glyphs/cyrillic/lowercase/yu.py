from nordwand_mono.glyphs import Glyph
from nordwand_mono.draw.rect import draw_rect
from nordwand_mono.draw.loop import draw_loop


class CyrillicLowercaseYuGlyph(Glyph):
    name = "cyrillic_lowercase_yu"
    unicode = "0x044E"
    offset = 8
    width_ratio = 1.18
    mid_ratio = 0.33
    ymid_ratio = 0.518
    stroke_dampening = 0.8

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
            overshoot_bottom=True,
            overshoot_top=True,
        )
        sx, sy = dc.stroke_x, dc.stroke_y
        sx = max(0, self.stroke_dampening * (sx - dc.default_stroke)) + min(
            dc.default_stroke, sx
        )
        lx1 = b.x1 + self.mid_ratio * b.width
        hx = (1 - self.mid_ratio) * b.hx
        ymid = b.y1 + self.ymid_ratio * b.height

        draw_loop(
            pen,
            sx,
            sy,
            lx1,
            b.y1,
            b.x2,
            b.y2,
            hx,
            b.hy,
        )

        draw_rect(
            pen,
            b.x1,
            0,
            b.x1 + sx,
            b.y2,
        )
        draw_rect(
            pen,
            b.x1,
            ymid - sy / 2,
            lx1 + sx / 2,
            ymid + sy / 2,
        )
