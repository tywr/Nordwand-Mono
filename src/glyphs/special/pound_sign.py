from glyphs import Glyph
from draw.rect import draw_rect
from draw.loop import draw_loop
from draw.square_corner import draw_square_corner


class PoundSignGlyph(Glyph):
    name = "pound_sign"
    unicode = "0xA3"
    offset = 0
    width_ratio = 1.08
    mid_ratio = 0.33
    bar_height = 0.42
    bar_length = 0.80
    loop_ratio = 0.33
    overflow_ratio = 0.25

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="cap", width_ratio=self.width_ratio
        )
        sx, sy = dc.stroke_x, dc.stroke_y
        xmid = b.x1 + self.mid_ratio * b.width
        yl = b.y1 + (1 - self.loop_ratio) * b.height
        yb = b.y1 + self.bar_height * b.height
        bl = self.bar_length * b.width
        draw_rect(
            pen,
            b.x1,
            b.y1,
            b.x2,
            b.y1 + sy,
        )
        draw_rect(
            pen,
            b.x1,
            yb,
            b.x1 + bl,
            yb + sy,
        )
        draw_square_corner(
            pen, sx, sy, xmid, b.ymid, b.x1, b.y1, orientation="bottom-left"
        )
        draw_rect(
            pen,
            xmid - sx,
            b.ymid,
            xmid,
            yl,
        )
        draw_rect(
            pen,
            xmid - sx,
            b.ymid,
            xmid,
            yl,
        )
        draw_loop(
            pen,
            sx,
            sy,
            xmid - sx,
            yl - (b.y2 - yl),
            b.x2,
            b.y2,
            b.hx,
            b.hy * self.loop_ratio * 2,
            cut="bottom",
        )
