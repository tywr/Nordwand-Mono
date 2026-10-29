from glyphs import Glyph

from draw.loop import draw_loop
from draw.arch import draw_arch
from draw.rect import draw_rect


class LowercaseG2Glyph(Glyph):
    name = "lowercase_g_2"
    unicode = "0x67"
    font_feature = {"cv04": 1}
    offset = 0
    width_ratio = 1.05

    taper = 0.75
    bowl_y_ratio = 0.68
    bowl_x_ratio = 0.85
    bridge_hy_ratio = 3.0
    bridge_x_offset = 0.075
    bottom_loop_top = 0.065
    terminal_offset = 0.1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            width_ratio=self.width_ratio,
            offset=self.offset,
            # overshoot_top=True,
        )
        sx, sy = dc.stroke_x, dc.stroke_y
        yb1, yb2 = b.y1 + (1 - self.bowl_y_ratio) * b.height, b.y2
        xb1, xb2 = b.x1, b.x1 + b.width * self.bowl_x_ratio
        xbmid = (xb1 + xb2) / 2
        lb = b.x2 - xbmid
        lb2 = xbmid - b.x1
        bo = self.bridge_x_offset * b.width
        ybt = self.bottom_loop_top * b.height
        xt = b.x2 - self.terminal_offset * b.width

        draw_loop(
            pen,
            sx,
            sy,
            xb1,
            yb1,
            xb2,
            yb2,
            b.hx * self.bowl_x_ratio,
            b.hy * self.bowl_y_ratio,
            cut="right",
        )
        draw_arch(
            pen,
            sx,
            sy,
            xb1,
            yb1,
            xb2,
            yb2,
            b.hx * self.bowl_x_ratio,
            b.hy * self.bowl_y_ratio,
            taper=dc.taper * self.taper,
            cut="left",
            side="top",
        )
        draw_rect(
            pen,
            (xb1 + xb2) / 2,
            yb2 - sy,
            xt,
            yb2,
        )
        # Half bottom loop
        draw_loop(
            pen,
            sx,
            sy,
            xbmid - lb,
            dc.descent - dc.v_overshoot,
            xbmid + lb,
            ybt + sy,
            b.hx * 2 * lb / b.width,
            b.hy * abs(dc.descent - dc.v_overshoot - sy - ybt) / b.height,
            cut="left",
        )
        # Bridge between the two loops
        draw_arch(
            pen,
            sx,
            sy,
            xb1 + bo,
            ybt,
            xb2 - bo,
            yb1 + sy,
            b.hx * (xb2 - xb1 - 2 * bo) / b.width,
            b.hy * (yb1 - sy - ybt) / b.height * self.bridge_hy_ratio,
            taper=dc.taper * self.taper,
            cut="right",
            side="top",
        )
        # End of bottom loop
        draw_arch(
            pen,
            sx,
            sy,
            xbmid - lb2,
            dc.descent - dc.v_overshoot,
            xbmid + lb2,
            ybt + sy,
            b.hx * 2 * lb2 / b.width,
            b.hy * abs(dc.descent - dc.v_overshoot - sy - ybt) / b.height,
            taper=dc.taper * self.taper,
            cut="right",
            side="top",
        )
