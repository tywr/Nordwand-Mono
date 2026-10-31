from glyphs import Glyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm


class CyrillicLowercaseKaGlyph(Glyph):
    name = "cyrillic_lowercase_ka"
    unicode = "0x043A"
    offset = 34
    width_ratio = 1.00
    branch_ratio = 0.75
    mid_ratio = 0.57
    upper_branch_offset = 0.055
    lower_stroke_ratio = 1.0
    branch_overlap = 0.8

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
            overshoot_right=True,
            overshoot_left=True,
        )
        xb = b.x1 + self.branch_overlap * dc.stroke_x
        xtop = b.x2 - self.upper_branch_offset * b.width
        ymid = b.y1 + self.mid_ratio * b.height

        # Left ascender stem
        draw_rect(pen, b.x1, 0, b.x1 + dc.stroke_x, b.y2)

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
