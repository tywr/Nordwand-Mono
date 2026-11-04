from draw.arch import draw_arch
from glyphs.lowercase import TailedLowercaseGlyph
from glyphs.lowercase.single_story import SingleStoryLowercaseGlyph


class LowercaseGGlyph(TailedLowercaseGlyph, SingleStoryLowercaseGlyph):
    name = "lowercase_g"
    unicode = "0x67"
    offset = -10

    def draw(self, pen, dc):
        b = dc.body_bounds(
            width_ratio=self.width_ratio,
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
        y1 = b.y1 + self.y1_offset * b.height

        # Bowl (open on the right, mirrored from b)
        dx = bsx - dc.stroke_x
        draw_arch(
            pen,
            bsx,
            bsy,
            b.x1,
            y1,
            b.x2 + dx,
            b.y2,
            hx * (b.x2 + dx - b.x1) / b.width,
            hy * (b.y2 - y1) / b.height,
            taper=dc.taper * self.taper,
            side="right",
        )

        self.draw_tail(pen, dc, b)
