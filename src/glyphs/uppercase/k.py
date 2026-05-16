from glyphs.uppercase import UppercaseGlyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm


class UppercaseKGlyph(UppercaseGlyph):
    name = "uppercase_k"
    unicode = "0x4B"
    offset = 38
    width_ratio = 1.16
    branch_ratio = 0.65
    mid_ratio = 0.52
    upper_branch_offset = 0.05
    branch_stroke_ratio = 1.3
    branch_overlap = 0.5

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
            overshoot_right=True,
            overshoot_left=True,
            height="cap"
        )
        xb = b.x1 + self.branch_overlap * dc.stroke_x
        sx = self.branch_stroke_ratio * dc.stroke_x
        xtop = b.x2 - self.upper_branch_offset * b.width
        ymid = b.y1 + self.mid_ratio * b.height

        # Left ascender stem
        draw_rect(pen, b.x1, 0, b.x1 + dc.stroke_x, dc.cap)

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
