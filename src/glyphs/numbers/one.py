from glyphs.numbers import NumberGlyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm_vertical


class OneGlyph(NumberGlyph):
    name = "one"
    unicode = "0x31"
    offset = 20
    branch_height = 0.29
    branch_offset = 0.04
    width_ratio = 1.08
    rl_ratio = 0.51
    diag_stroke_ratio = 0.95

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="cap", width_ratio=self.width_ratio, number=True
        )
        sx = dc.stroke_x * self.stroke_x_ratio
        xb = b.x1 + self.branch_offset * b.width
        xmid = b.x1 + self.rl_ratio * b.width
        yo = -0.75 * (sx - dc.default_stroke)

        # Vertical stem (centered)
        draw_rect(pen, xmid - sx / 2, b.y1, xmid + sx / 2, b.y2)

        # Horizontal stem
        draw_rect(pen, b.x1, b.y1, b.x2, b.y1 + dc.stroke_y)

        draw_parallelogramm_vertical(
            pen,
            self.diag_stroke_ratio * dc.stroke_x,
            xb,
            b.y1 + b.height * (1 - self.branch_height) + yo,
            xmid - sx / 2,
            b.y2,
        )
