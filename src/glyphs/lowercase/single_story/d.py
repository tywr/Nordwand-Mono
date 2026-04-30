from draw.arch import draw_arch
from draw.rect import draw_rect
from glyphs.lowercase.single_story import SingleStoryLowercaseGlyph


class LowercaseDGlyph(SingleStoryLowercaseGlyph):
    name = "lowercase_d"
    unicode = "0x64"
    offset = -10

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            overshoot_bottom=True,
            overshoot_top=True,
            overshoot_left=True,
        )
        hx, hy = self.hx_ratio * b.hx, self.hy_ratio * b.hy
        bsx, bsy = (
            self.bowl_stroke_x_ratio * dc.stroke_x,
            self.bowl_stroke_y_ratio * dc.stroke_y,
        )
        dx = bsx - dc.stroke_x
        arch_params = draw_arch(
            pen,
            bsx,
            bsy,
            b.x1,
            b.y1,
            b.x2 + dx,
            b.y2,
            hx,
            hy,
            taper=dc.taper * self.taper,
            side="right",
        )

        draw_rect(pen, b.x2 - dc.stroke_x, 0, b.x2, dc.ascent)
