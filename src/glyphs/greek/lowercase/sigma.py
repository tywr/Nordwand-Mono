from glyphs import Glyph
from draw.rect import draw_rect
from draw.arch import draw_arch


class GreekLowercaseSigmaGlyph(Glyph):
    name = "greek_lowercase_sigma"
    unicode = "0x3C3"
    offset = 0
    stroke_x_ratio = 1.01
    right_offset = 0.075
    width_ratio = 1.02
    taper = 0.5

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            overshoot_top=True,
            overshoot_bottom=True,
            overshoot_left=True,
            overshoot_right=True,
            width_ratio=self.width_ratio,
        )
        sx, sy = dc.stroke_x, dc.stroke_y
        x2 = b.x2 - self.right_offset * b.width
        draw_arch(
            pen,
            sx * self.stroke_x_ratio,
            sy,
            b.x1,
            b.y1,
            x2,
            b.y2,
            b.hx * (x2 - b.x1) / b.width,
            b.hy,
            side="top",
            cut="left",
            taper=dc.taper * self.taper,
        )
        draw_arch(
            pen,
            sx * self.stroke_x_ratio,
            sy,
            b.x1,
            b.y1,
            x2,
            b.y2,
            b.hx * (x2 - b.x1) / b.width,
            b.hy,
            side="right",
            cut="right",
        )
        draw_rect(
            pen,
            (b.x1 + x2) / 2,
            b.y2 - sy,
            b.x2,
            b.y2,
        )
