from glyphs import Glyph
from draw.rect import draw_rect
from draw.loop import draw_loop
from draw.corner import draw_corner


class LowercaseK2Glyph(Glyph):
    name = "lowercase_k_2"
    default_italic = True
    unicode = "0x6B"
    offset = 16
    width_ratio = 1
    branch_ratio = 0.75
    mid_ratio = 0.43
    branch_x_ratio = 0.33
    upper_branch_offset = 0.055
    branch_stroke_ratio = 1.25
    branch_overlap = 0.8
    loop_ratio = 0.85

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
            overshoot_right=True,
            overshoot_left=True,
        )
        ymid = b.y1 + self.mid_ratio * b.height
        xl = b.xmid + (self.loop_ratio * b.width) / 2
        xbl = b.xmid - dc.stroke_x * 0.66

        # Left ascender stem
        draw_rect(pen, b.x1, 0, b.x1 + dc.stroke_x, dc.ascent)

        draw_rect(pen, b.x1, b.y2 - dc.stroke_y, b.xmid, b.y2)
        # draw_rect(pen, b.x1, ymid, b.xmid, ymid + dc.stroke_y)
        draw_loop(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x1,
            ymid,
            xl,
            b.y2,
            b.hx * (xl - b.x1) / b.width,
            b.hy * (b.y2 - ymid) / b.height,
            cut="left",
        )

        draw_corner(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            xbl,
            ymid + dc.stroke_y,
            b.x2,
            0,
            b.hx * 2 * (b.x2 - xbl) / b.width,
            b.hy * 2 * (ymid + dc.stroke_y) / b.height,
            orientation="bottom-right",
        )
