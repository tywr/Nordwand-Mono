from glyphs import Glyph
from draw.rect import draw_rect
from draw.corner import draw_corner
from draw.square_corner import draw_square_corner
from utils.intersection import bezier_intersect


class RightCurlyBracketGlyph(Glyph):
    name = "right_curly_bracket"
    unicode = "0x7D"
    offset = 0
    width_ratio = 1
    peak_ratio = 0.35

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        pl = self.peak_ratio * b.width
        ymid = dc.parenthesis
        sx, sy = dc.stroke_x, dc.stroke_y
        y1, y2 = ymid - dc.parenthesis_length / 2, ymid + dc.parenthesis_length / 2
        x1, x2, xmid = b.x1, b.x2 - pl, (b.x1 - pl + b.x2) / 2
        l4 = dc.parenthesis_length / 4
        hx = (1 - self.peak_ratio) * b.hx
        hy = b.hy

        draw_square_corner(
            pen,
            sx,
            sy,
            xmid + sx / 2,
            y2 - l4,
            x1,
            y2,
            orientation="top-left",
        )
        draw_corner(
            pen,
            sx,
            0.75 * sx,
            xmid - sx / 2,
            y2 - l4,
            x2,
            ymid - 0.25 * sx,
            hx,
            hy,
            orientation="bottom-right",
        )

        draw_square_corner(
            pen,
            sx,
            sy,
            xmid + sx / 2,
            y1 + l4,
            x1,
            y1,
            orientation="bottom-left",
        )
        draw_corner(
            pen,
            sx,
            0.75 * sx,
            xmid - sx / 2,
            y1 + l4,
            x2,
            ymid + 0.25 * sx,
            hx,
            hy,
            orientation="top-right",
        )


        draw_rect(pen, b.xmid, ymid - sx / 2, b.x2, ymid + sx / 2)
