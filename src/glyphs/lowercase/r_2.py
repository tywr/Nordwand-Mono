from glyphs import Glyph
from draw.loop import draw_loop
from draw.rect import draw_rect


class LowercaseR2Glyph(Glyph):
    name = "lowercase_r_2"
    unicode = "0x72"
    font_feature = {"cv06": 1}
    offset = 50
    loop_y_ratio = 0.75
    loop_x_ratio = 1
    stroke_y_ratio = 1.12
    hx_ratio = 1.00
    hy_ratio = 1.00
    taper = 0.65
    width_ratio = 0.78

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
        )
        sx, sy = dc.stroke_x, dc.stroke_y * self.stroke_y_ratio
        stx = sx * min(1, dc.taper * self.taper)
        hx, hy = b.hx * self.hx_ratio, b.hy * self.hy_ratio
        ys = b.y2 - self.loop_y_ratio * b.height
        x1, x2 = b.x1 + sx - stx, b.x1 + sx - stx + self.loop_x_ratio * b.width

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
        draw_rect(pen, b.x1, 0, b.x1 + dc.stroke_x, dc.x_height)
