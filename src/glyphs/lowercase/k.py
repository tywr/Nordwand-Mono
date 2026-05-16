from glyphs import Glyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm


class LowercaseKGlyph(Glyph):
    name = "lowercase_k"
    unicode = "0x6B"
    offset = 34
    width_ratio = 1.00
    branch_ratio = 0.75
    mid_ratio = 0.52
    upper_branch_offset = 0.055
    branch_stroke_ratio = 1.25
    branch_overlap = 0.5

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
            overshoot_right=True,
            overshoot_left=True,
        )
        xb = b.x1 + self.branch_overlap * dc.stroke_x
        sx = self.branch_stroke_ratio * dc.stroke_x
        xtop = b.x2 - self.upper_branch_offset * b.width
        ymid = b.y1 + self.mid_ratio * b.height

        # Left ascender stem
        draw_rect(pen, b.x1, 0, b.x1 + dc.stroke_x, dc.ascent)

        # Lower branch
        draw_parallelogramm(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            xb,
            ymid,
            b.x2,
            b.y1,
            direction="bottom-right",
            delta=sx,
        )

        # Upper branch
        theta, delta = draw_parallelogramm(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            xb,
            ymid,
            xtop,
            b.y2,
            delta=sx,
        )
