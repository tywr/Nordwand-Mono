from glyphs.uppercase import UppercaseGlyph
from draw.rect import draw_rect
from draw.loop import draw_loop


class GreekUppercaseThetaGlyph(UppercaseGlyph):
    name = "greek_uppercase_theta"
    unicode = "0x398"
    offset = 0
    stroke_x_ratio = UppercaseGlyph.stroke_x_ratio * 1.00
    stroke_y_ratio = UppercaseGlyph.stroke_y_ratio * 1.00
    width_ratio = 1.08
    bar_gap = 0.05

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            overshoot_bottom=True,
            overshoot_top=True,
            width_ratio=self.width_ratio,
            uppercase=True,
        )
        gap = self.bar_gap * b.width
        sx = dc.stroke_x * self.stroke_x_ratio
        sy = dc.stroke_y * self.stroke_y_ratio
        draw_loop(
            pen,
            sx,
            sy,
            b.x1,
            b.y1,
            b.x2,
            b.y2,
            b.hx,
            b.hy,
        )

        draw_rect(
            pen,
            b.x1 + sx + gap,
            b.ymid - sy / 2,
            b.x2 - sx - gap,
            b.ymid + sy / 2,
        )
