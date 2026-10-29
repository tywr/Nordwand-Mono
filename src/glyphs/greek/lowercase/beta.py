from draw.arch import draw_arch
from draw.rect import draw_rect
from glyphs.lowercase.single_story import SingleStoryLowercaseGlyph


class GreekLowercaseBetaGlyph(SingleStoryLowercaseGlyph):
    name = "greek_lowercase_beta"
    unicode = "0x3B2"
    offset = 12
    upper_ratio = 0.88
    mid_ratio = 0.515
    width_ratio = 1.06
    offset_lower_bar = 0.3
    reach_upper_bar = 0.9
    stroke_x_ratio = 1.00
    stroke_y_ratio = 1.00
    taper = 0.75

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            uppercase=True,
            overshoot_top=True,
            overshoot_bottom=True,
            width_ratio=self.width_ratio,
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        hx, hy = b.hx, b.hy
        ymid = b.y1 + self.mid_ratio * b.height
        o = self.offset_lower_bar * b.width
        yt = dc.descent

        lower_x1 = b.x1
        lower_x2 = b.x2
        lower_width = lower_x2 - lower_x1
        upper_width = self.upper_ratio * lower_width
        delta = lower_width - upper_width
        upper_x1 = lower_x1 + delta / 2
        upper_x2 = lower_x2 - delta / 2

        # Left stem
        draw_rect(pen, b.x1, yt, b.x1 + sx, (ymid - sy / 2 + b.y2) / 2)

        draw_arch(
            pen,
            sx,
            sy,
            b.x1,
            ymid - sy / 2,
            upper_x2,
            b.y2,
            hx * (upper_x2 - upper_x1) / b.width,
            hy * (1 - self.mid_ratio),
            taper=0.75,
            side="bottom",
            cut="left",
        )
        draw_arch(
            pen,
            sx,
            sy,
            b.x1,
            ymid - sy / 2,
            upper_x2,
            b.y2,
            hx * (upper_x2 - upper_x1) / b.width,
            hy * (1 - self.mid_ratio),
            taper=0.75,
            side="bottom",
            cut="bottom",
        )

        # Lower loop (full width)
        draw_arch(
            pen,
            sx,
            sy,
            lower_x1,
            b.y1,
            lower_x2,
            ymid + sy / 2,
            hx,
            hy * self.mid_ratio,
            taper=0.75,
            cut="left",
            side="top",
        )
        draw_arch(
            pen,
            sx,
            sy,
            lower_x1,
            b.y1,
            lower_x2,
            ymid + sy / 2,
            hx,
            hy * self.mid_ratio,
            taper=dc.taper * self.taper,
            cut="right,top",
            side="left",
        )

        draw_rect(
            pen,
            b.x1 + o,
            ymid - sy / 2,
            b.xmid,
            ymid + sy / 2,
        )
