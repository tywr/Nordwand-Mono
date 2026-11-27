from nordwand_mono.glyphs.uppercase import UppercaseGlyph
from nordwand_mono.draw.rect import draw_rect


class UppercaseHGlyph(UppercaseGlyph):
    name = "uppercase_h"
    unicode = "0x48"
    offset = 0
    bar_height = 0.51
    width_ratio = 1.0
    height = "cap"
    mid_shift_coef = -0.04

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height=self.height, width_ratio=self.width_ratio, uppercase=True
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        yo = self.mid_shift_coef * (dc.stroke_x - dc.default_stroke)
        yb = self.bar_height * b.height + yo

        # Left stem
        draw_rect(pen, b.x1, b.y1, b.x1 + sx, b.y2)
        # Right stem
        draw_rect(pen, b.x2 - sx, b.y1, b.x2, b.y2)
        # Middle bar
        draw_rect(pen, b.x1, yb - sy / 2, b.x2, yb + sy / 2)
