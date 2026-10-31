from glyphs.uppercase import UppercaseGlyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm


class UppercaseKGlyph(UppercaseGlyph):
    name = "uppercase_k"
    unicode = "0x4B"
    offset = 50
    width_ratio = 1.02
    branch_ratio = 0.65
    mid_ratio = 0.55
    upper_branch_offset = 0.05
    lower_stroke_ratio = 1.0
    branch_overlap = 0.8

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
            overshoot_right=True,
            overshoot_left=True,
            height="cap",
        )
        xb = b.x1 + self.branch_overlap * dc.stroke_x
        xtop = b.x2 - self.upper_branch_offset * b.width
        ymid = b.y1 + self.mid_ratio * b.height

        # Left ascender stem
        draw_rect(pen, b.x1, 0, b.x1 + dc.stroke_x, dc.cap)

        # Lower branch
        _, d = draw_parallelogramm(
            pen,
            self.lower_stroke_ratio * dc.stroke_x,
            xb,
            ymid,
            b.x2,
            b.y1,
            direction="bottom-right",
        )

        # Upper branch
        draw_parallelogramm(
            pen,
            0,
            xb,
            ymid,
            xtop,
            b.y2,
            overwrite_section=d,
        )
