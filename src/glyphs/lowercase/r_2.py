from glyphs import Glyph
from draw.loop import draw_loop
from draw.rect import draw_rect


class LowercaseR2Glyph(Glyph):
    name = "lowercase_r_2"
    unicode = "0x72"
    font_feature = {"cv06": 1, "ss01": 1}
    offset = 20
    loop_y_ratio = 0.75
    loop_x_ratio = 1
    stroke_y_ratio = 1.12
    hx_ratio = 1.00
    hy_ratio = 1.00
    taper = 0.65
    width_ratio = 1.1
    rl_ratio = 0.38
    serif_length = 0.88

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
            overshoot_top=True,
        )
        sx, sy = dc.stroke_x, dc.stroke_y * self.stroke_y_ratio
        stx = sx * min(1, dc.taper * self.taper)
        hx, hy = b.hx * self.hx_ratio, b.hy * self.hy_ratio
        ys = b.y2 - self.loop_y_ratio * b.height
        xmid = b.x1 + self.rl_ratio * b.width
        x1, x2 = xmid + 0.5 * sx - stx, xmid + 0.5 * sx - stx + self.loop_x_ratio * b.width
        xl2 = b.x1 + self.serif_length * b.width

        draw_loop(
            pen,
            stx,
            sy,
            x1,
            ys,
            x2,
            b.y2,
            hx * self.loop_x_ratio,
            hy * self.loop_y_ratio,
            quarter="top-left",
        )
        # Top part
        draw_rect(pen, (x1 + x2) / 2, b.y2 - sy, b.x2, b.y2)

        # Left stem
        draw_rect(pen, xmid - sx / 2, 0, xmid + sx / 2, dc.x_height)

        # Hook
        draw_rect(
            pen,
            b.x1,
            dc.x_height - sy,
            xmid,
            dc.x_height,
        )

        # Bottom serif
        draw_rect(
            pen,
            b.x1,
            b.y1,
            xl2,
            b.y1 + sy,
        )
