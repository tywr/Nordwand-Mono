from glyphs.numbers import NumberGlyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm


class FourGlyph(NumberGlyph):
    name = "four"
    unicode = "0x34"
    offset = -7
    slant_ratio = 0.8
    horizontal_ratio = 0.735
    vertical_ratio = 0.34
    mid_bar_ratio = 0.61
    width_ratio = 1.16
    stroke_ratio = 1.00

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="cap", width_ratio=self.width_ratio
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio

        xmid = b.x1 + self.horizontal_ratio * b.width
        xtop = b.x1 + self.slant_ratio * b.width
        ymid = b.y1 + self.vertical_ratio * b.height
        ybar = b.y1 + self.mid_bar_ratio * b.height

        s = self.stroke_ratio * dc.stroke_x

        draw_parallelogramm(pen, s, b.x1, ymid, xtop - sx / 2, b.y2)

        # Horizontal line
        draw_rect(pen, b.x1, ymid - sy, b.x2, ymid)

        # Vertical line
        draw_rect(pen, xmid - sx / 2, b.y1, xmid + sx / 2, ybar)
