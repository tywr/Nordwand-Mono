from glyphs import Glyph
from draw.rect import draw_rect
from draw.arch import draw_arch
from draw.square_corner import draw_square_corner


class GreekLowercaseOmegaGlyph(Glyph):
    name = "greek_lowercase_omega"
    unicode = "0x3C9"
    width_ratio = 1.2
    offset = 0
    tail_ratio = 0.2
    mid_ratio = 0.5
    mid_y_ratio = 0.66

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
            overshoot_bottom=True,
        )
        xmid = b.x1 + self.mid_ratio * b.width
        ymid = b.y1 + self.mid_y_ratio * b.height
        sy = dc.stroke_y
        sx = max(0, 0.8 * (dc.stroke_x - dc.default_stroke)) + min(dc.default_stroke, dc.stroke_x)
        xtr = b.x2 - self.tail_ratio * b.width - sx / 2
        xtl = b.x1 + self.tail_ratio * b.width + sx / 2

        draw_rect(
            pen,
            xmid - sx / 2,
            b.ymid,
            xmid + sx / 2,
            ymid,
        )
        draw_arch(
            pen,
            sx,
            sy,
            b.x1,
            b.y1,
            xmid + sx / 2,
            b.y2,
            # Handles rescaled to the arch's width
            b.hx * (xmid + sx / 2 - b.x1) / b.width,
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
            b.hx * (b.x2 - xmid + sx / 2) / b.width,
            b.hy,
            side="left",
            cut="top",
            taper=0.6,
        )
        draw_square_corner(
            pen, sx, sy, b.x1, b.ymid, xtl, b.y2, orientation="top-right"
        )
        draw_square_corner(pen, sx, sy, b.x2, b.ymid, xtr, b.y2, orientation="top-left")
