from draw.arch import draw_arch
from draw.rect import draw_rect
from glyphs.lowercase.square import SquareLowercaseGlyph


class MicroSignGlyph(SquareLowercaseGlyph):
    """u-like bowl between a left stem reaching the descender and a right stem.

    The bowl is drawn as two quarter arches, each tapered where it joins its
    stem.
    """

    name = "micro_sign"
    unicode = "0xB5"
    offset = 0

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            overshoot_bottom=True,
            width_ratio=self.width_ratio,
        )
        yl = b.y1 + self.loop_ratio * b.height

        for side, cut in (("left", "top,right"), ("right", "top,left")):
            draw_arch(
                pen,
                dc.stroke_x,
                dc.stroke_y,
                b.x1,
                b.y1,
                b.x2,
                yl,
                b.hx,
                self.loop_ratio * b.hy,
                taper=self.taper * dc.taper,
                side=side,
                cut=cut,
            )

        # Left stem down to the descender, right stem from the baseline
        draw_rect(pen, b.x1, dc.descent, b.x1 + dc.stroke_x, dc.x_height)
        draw_rect(pen, b.x2 - dc.stroke_x, 0, b.x2, dc.x_height)
