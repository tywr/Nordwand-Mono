from glyphs import Glyph
from draw.rect import draw_rect
from draw.arch import draw_arch


class GreekLowercaseRhoGlyph(Glyph):
    name = "greek_lowercase_rho"
    unicode = "0x3C1"
    offset = -10
    stroke_x_ratio = 1.01

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            overshoot_top=True,
            overshoot_bottom=True,
            overshoot_left=True,
            overshoot_right=True,
        )
        sx, sy = dc.stroke_x, dc.stroke_y
        draw_arch(
            pen,
            sx * self.stroke_x_ratio,
            sy,
            b.x1,
            b.y1,
            b.x2,
            b.y2,
            b.hx,
            b.hy,
            side="left",
            cut="top",
        )
        draw_arch(
            pen,
            sx * self.stroke_x_ratio,
            sy,
            b.x1,
            b.y1,
            b.x2,
            b.y2,
            b.hx,
            b.hy,
            side="bottom",
            cut="bottom",
        )
        draw_rect(
            pen,
            b.x1,
            dc.descent,
            b.x1 + sx,
            b.ymid,
        )
