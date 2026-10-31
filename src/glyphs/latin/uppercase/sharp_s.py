from glyphs import Glyph
from draw.arch import draw_arch
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm
from draw.corner import draw_corner


class CapitalSharpSGlyph(Glyph):
    name = "uppercase_sharp_s"
    unicode = "0x1e9e"
    offset = 12
    upper_ratio = 0.9  # Upper loop width as a fraction of the lower loop width
    mid_ratio = 0.52
    width_ratio = 1.06
    offset_lower_bar = 0.3
    reach_upper_bar = 0.9
    tail_reach = 0.0
    diag_stroke_ratio = 1.0
    stroke_x_ratio = 1.00
    stroke_y_ratio = 1.00

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            uppercase=True,
            width_ratio=self.width_ratio,
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        hx, hy = b.hx, b.hy
        ymid = b.y1 + self.mid_ratio * b.height
        xu = b.x1 + self.reach_upper_bar * b.width
        o = self.offset_lower_bar * b.width
        yt = -self.tail_reach * b.height

        lower_x1 = b.x1
        lower_x2 = b.x2
        lower_width = lower_x2 - lower_x1
        upper_width = self.upper_ratio * lower_width
        delta = lower_width - upper_width
        upper_x1 = lower_x1 + delta / 2
        upper_x2 = lower_x2 - delta / 2

        # Left stem
        draw_rect(pen, b.x1, yt, b.x1 + sx, (ymid - sy / 2 + b.y2) / 2)

        draw_corner(
            pen,
            sx,
            sy,
            b.x1,
            (ymid - sy / 2 + b.y2) / 2,
            (upper_x1 + upper_x2) / 2,
            b.y2,
            hx * (upper_x2 - upper_x1) / b.width,
            hy * (1 - self.mid_ratio),
            orientation="top-right",
        )

        # Upper loop
        draw_rect(
            pen,
            b.xmid,
            b.y2 - sy,
            xu,
            b.y2,
        )
        theta, delta = draw_parallelogramm(
            pen,
            self.diag_stroke_ratio * sx,
            xu,
            b.y2 - sy,
            b.x1 + o,
            ymid + sy * 0.75 - sy / 2,
            direction="bottom-left",
        )

        # Lower loop (full width)
        draw_arch(
            pen,
            sx,
            sy,
            lower_x1,
            0,
            lower_x2,
            ymid + sy / 2,
            hx,
            hy * self.mid_ratio,
            taper=0.75,
            cut="left",
            side="top",
        )

        # Middle part
        draw_rect(
            pen,
            b.x1 + o,
            ymid - sy / 2,
            max(b.x1 + o + delta, (lower_x1 + lower_x2) / 2),
            ymid + sy * 0.75 - sy / 2,
        )

        # Bottom extension
        draw_rect(
            pen,
            b.x1 + o,
            b.y1,
            (lower_x1 + lower_x2) / 2,
            b.y1 + sy,
        )
