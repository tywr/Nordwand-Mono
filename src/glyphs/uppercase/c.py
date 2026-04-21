from glyphs.uppercase import UppercaseGlyph
from draw.superellipse_loop import draw_superellipse_loop
from draw.parallelogramm import draw_parallelogramm_vertical


class UppercaseCGlyph(UppercaseGlyph):
    name = "uppercase_c"
    unicode = "0x43"
    offset = 0
    stroke_x_ratio = UppercaseGlyph.stroke_x_ratio * 1.12
    stroke_y_ratio = UppercaseGlyph.stroke_y_ratio
    tail_offset = 0.08
    hx_ratio = 0.8
    hy_ratio = 0.8

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            overshoot_bottom=True,
            overshoot_top=True,
            overshoot_left=True,
            # overshoot_right=True,
            width_ratio=self.width_ratio,
            uppercase=True,
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        hx, hy = self.hx_ratio * b.hx, self.hy_ratio * b.hy
        yt_top = dc.cap - sy - dc.v_overshoot
        yt_bot = sy + dc.v_overshoot
        xt = b.x2 - self.tail_offset * b.width

        draw_superellipse_loop(
            pen, sx, sy, b.x1, b.y1, b.x2, b.y2, hx, hy, cut="right"
        )
        draw_parallelogramm_vertical(
            pen, sx, sy, b.xmid, b.y2, xt, yt_top, direction="bottom-right", delta=sy
        )
        draw_parallelogramm_vertical(
            pen, sx, sy, b.xmid, b.y1, xt, yt_bot, direction="top-right", delta=sy
        )
