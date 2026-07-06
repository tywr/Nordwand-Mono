from glyphs import Glyph
from draw.rect import draw_rect
from draw.arch import draw_arch
from draw.square_corner import draw_square_corner


class LowercaseW2Glyph(Glyph):
    name = "lowercase_w_2"
    font_feature = {"cv08": 1}
    default_italic = True
    width_ratio = 1.18
    unicode = "0x77"
    offset = 0
    tail_ratio = 0.13
    mid_ratio = 0.45

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
            overshoot_bottom=True,
        )
        xmid = b.x1 + self.mid_ratio * b.width
        sx, sy = dc.stroke_x, dc.stroke_y
        xt = b.x2 - self.tail_ratio * b.width - sx

        draw_rect(
            pen,
            b.x1,
            b.ymid,
            b.x1 + dc.stroke_x,
            b.y2,
        )
        draw_rect(
            pen,
            xmid - sx / 2,
            b.ymid,
            xmid + sx / 2,
            b.y2,
        )
        draw_rect(
            pen,
            xmid - sx / 2,
            b.ymid,
            xmid + sx / 2,
            b.y2,
        )
        draw_arch(
            pen,
            sx,
            sy,
            b.x1,
            b.y1,
            xmid + sx / 2,
            b.y2,
            b.hx * (1 - self.mid_ratio),
            b.hy,
            cut="top",
            taper=0.6,
        )
        draw_arch(
            pen,
            sx,
            sy,
            xmid - sx / 2,
            b.y1,
            b.x2,
            b.y2,
            b.hx * self.mid_ratio,
            b.hy,
            side="left",
            cut="top",
            taper=0.6,
        )
        draw_square_corner(pen, sx, sy, b.x2, b.ymid, xt, b.y2, orientation="top-left")
