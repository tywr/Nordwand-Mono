from draw.rect import draw_rect
from glyphs.greek.lowercase import TailedGreekLowercaseGlyph


class GreekLowercaseZetaGlyph(TailedGreekLowercaseGlyph):
    name = "greek_lowercase_zeta"
    unicode = "0x3B6"
    offset = 0
    width_ratio = 0.99
    top_offset = 0.15
    diagonal_ratio = 1.2
    bow_height = 0.3
    bow_start = 0.15
    bow_end = 0.66

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            overshoot_left=True,
            width_ratio=self.width_ratio,
        )
        sx, sy = self.stroke_x_ratio * dc.stroke_x, self.stroke_y_ratio * dc.stroke_y
        ymid = self.tail_height_ratio * b.height

        # Top bar
        draw_rect(
            pen, b.x1 + self.top_offset * b.width, dc.ascent - sy, b.x2, dc.ascent
        )

        # Junction from the left side of the tail to the top bar: a bow
        # easing into a diagonal stroke, as for the ending of the 6 and the 9
        delta = self.diag_stroke_dampening(self.diagonal_ratio, dc.stroke_x, coef=0.15)
        yt = dc.ascent - sy
        # Where the outer and inner edges of the diagonal cross the sides
        yo = ymid + self.bow_height * (yt - ymid)
        slope = (yt - yo) / (b.x2 - delta - b.x1)
        yi = yt - (b.x2 - b.x1 - sx) * slope

        def along(x, y, xe, t):
            return x + t * (xe - x), y + t * (yt - y)

        outer = (b.x1, yo, b.x2 - delta)
        inner = (b.x1 + sx, yi, b.x2)
        pen.moveTo((b.x1 + sx, ymid))
        pen.curveTo(
            (b.x1 + sx, yi),
            along(*inner, self.bow_start),
            along(*inner, self.bow_end),
        )
        pen.lineTo((b.x2, yt))
        pen.lineTo((b.x2 - delta, yt))
        pen.lineTo(along(*outer, self.bow_end))
        pen.curveTo(along(*outer, self.bow_start), (b.x1, yo), (b.x1, ymid))
        pen.closePath()

        self.draw_tail(pen, dc, b, sx, sy)
