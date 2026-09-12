from glyphs import Glyph
from draw.loop import draw_loop
from draw.arch import draw_arch
from draw.square_corner import draw_square_corner


class CyrillicLowercaseBeGlyph(Glyph):
    name = "cyrillic_lowercase_be"
    unicode = "0x0431"
    offset = 0
    width_ratio = 1.0
    loop_ratio = 0.92
    top_ratio = 0.9
    taper = 1
    cap_x = 0.75
    joint_x = 1.4
    hx_ratio = 0.9
    hy_ratio = 0.9
    stroke_ratio = 1.2

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            overshoot_bottom=True,
            overshoot_left=True,
            overshoot_right=True,
            width_ratio=self.width_ratio,
            number=True,
        )
        sx, sy = dc.stroke_x, dc.stroke_y
        hx, hy = self.hx_ratio * b.hx, self.hy_ratio * b.hy
        xt = b.x1 + self.top_ratio * b.width

        ymid = b.y1 + self.loop_ratio * b.height

        # Bottom loop
        draw_arch(
            pen,
            sx,
            sy,
            b.x1,
            b.y1,
            b.x2,
            ymid,
            hx,
            hy * self.loop_ratio,
            taper=self.taper * dc.taper,
            side="left",
            cut="bottom",
        )

        draw_loop(
            pen,
            sx,
            sy,
            b.x1,
            b.y1,
            b.x2,
            ymid,
            hx,
            hy * self.loop_ratio,
            cut="top",
        )

        draw_square_corner(
            pen, sx, sy, b.x1, (b.y1 + ymid) / 2, xt, dc.cap, orientation="top-right"
        )
