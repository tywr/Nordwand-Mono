from nordwand_mono.glyphs.uppercase import UppercaseGlyph
from nordwand_mono.draw.rect import draw_rect


class UppercaseFGlyph(UppercaseGlyph):
    name = "uppercase_f"
    unicode = "0x46"
    offset = 26
    mid_bar_ratio = 0.93
    mid_ratio = 0.48
    width_ratio=0.88
    mid_shift_coef = -0.15

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="cap", width_ratio=self.width_ratio
        )
        yo = self.mid_shift_coef * (dc.stroke_x - dc.default_stroke)
        sx, sy = self.get_strokes(dc)
        ymid = self.mid_ratio * b.height + yo

        # Vertical stem
        draw_rect(pen, b.x1, b.y1, b.x1 + sx, b.y2)
        # Top bar
        draw_rect(pen, b.x1, b.y2 - sy, b.x2, b.y2)
        # Middle bar
        draw_rect(
            pen,
            b.x1,
            ymid - sy / 2,
            b.x1 + self.mid_bar_ratio * b.width,
            ymid + sy / 2,
        )
