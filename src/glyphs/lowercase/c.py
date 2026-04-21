from glyphs import Glyph
from draw.superellipse_loop import draw_superellipse_loop
from draw.parallelogramm import draw_smooth_parallelogramm_vertical


class LowercaseCGlyph(Glyph):
    name = "lowercase_c"
    unicode = "0x63"
    offset = 12
    stroke_x_ratio = 1.0
    tail_offset = 0.08
    hy_ratio = 1
    hx_ratio = 1
    overshoot_reduction = 0

    def draw(self, pen, dc):

        b = dc.body_bounds(
            offset=self.offset,
            overshoot_bottom=True,
            overshoot_top=True,
            overshoot_left=True,
        )
        xmid = b.xmid + dc.h_overshoot
        v_overshoot = self.overshoot_reduction * dc.v_overshoot
        b.reduce_v_overshoot(v_overshoot)
        sx, sy = self.stroke_x_ratio * dc.stroke_x, dc.stroke_y
        hx, hy = self.hx_ratio * b.hx, self.hy_ratio * b.hy
        yt_top = dc.x_height - sy - dc.v_overshoot
        yt_bot = sy + dc.v_overshoot
        xt = b.x2 - self.tail_offset * b.width

        draw_superellipse_loop(pen, sx, sy, b.x1, b.y1, b.x2 + 2 * dc.h_overshoot, b.y2, hx, hy, cut="right")

        draw_smooth_parallelogramm_vertical(
            pen, sy, xmid, b.y2, xt, yt_top, direction="bottom-right"
        )
        draw_smooth_parallelogramm_vertical(
            pen, sy, xmid, b.y1, xt, yt_bot, direction="top-right"
        )
