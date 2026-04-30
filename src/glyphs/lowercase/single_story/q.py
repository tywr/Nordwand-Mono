from draw.arch import draw_arch
from draw.rect import draw_rect
from draw.polygon import draw_polygon
from glyphs.lowercase.single_story import SingleStoryLowercaseGlyph


class LowercaseQGlyph(SingleStoryLowercaseGlyph):
    name = "lowercase_q"
    unicode = "0x71"
    offset = -10

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            overshoot_bottom=True,
            overshoot_top=True,
            overshoot_left=True,
        )
        bsx, bsy = (
            self.bowl_stroke_x_ratio * dc.stroke_x,
            self.bowl_stroke_y_ratio * dc.stroke_y,
        )
        dx = bsx - dc.stroke_x
        hx, hy = self.hx_ratio * b.hx, self.hy_ratio * b.hy

        # Bowl (open on the right, same as d)
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

        draw_rect(pen, b.x2 - dc.stroke_x, dc.descent, b.x2, dc.x_height)
