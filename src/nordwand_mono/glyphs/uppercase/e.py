from nordwand_mono.glyphs.uppercase import UppercaseGlyph
from nordwand_mono.draw.rect import draw_rect


class UppercaseEGlyph(UppercaseGlyph):
    name = "uppercase_e"
    unicode = "0x45"
    offset = 14
    upper_bar_ratio = 1
    mid_bar_ratio = 0.96
    mid_ratio = 0.51
    width_ratio = 0.88
    mid_shift_coef = -0.05
    mid_stroke_dampening = 0.8

    def draw(self, pen, dc):
        b = dc.body_bounds(
            width_ratio=self.width_ratio,
            offset=self.offset,
            height="cap",
            uppercase=True,
        )
        sx, sy = self.get_strokes(dc)
        yo = self.mid_shift_coef * (dc.stroke_x - dc.default_stroke)
        smy = max(0, self.mid_stroke_dampening * (sy - dc.default_stroke)) + min(
            dc.default_stroke, sy
        )
        ymid = self.mid_ratio * b.height + yo

        # Vertical stem
        draw_rect(pen, b.x1, b.y1, b.x1 + sx, b.y2)

        # Top bar
        draw_rect(pen, b.x1, b.y2 - sy, b.x1 + self.upper_bar_ratio * b.width, b.y2)

        # Middle bar
        draw_rect(
            pen,
            b.x1,
            ymid - smy / 2,
            b.x1 + self.mid_bar_ratio * b.width,
            ymid + smy / 2,
        )

        # Bottom bar
        draw_rect(pen, b.x1, b.y1, b.x2, b.y1 + sy)
