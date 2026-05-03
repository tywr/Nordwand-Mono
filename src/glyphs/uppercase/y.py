from glyphs.uppercase import UppercaseGlyph
from draw.parallelogramm import draw_parallelogramm
from draw.rect import draw_rect


class UppercaseYGlyph(UppercaseGlyph):
    name = "uppercase_y"
    unicode = "0x59"
    offset = 0
    width_ratio = 1.2
    junction_ratio = 0.4

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, width_ratio=self.width_ratio, height="cap"
        )
        sx = dc.stroke_x * self.stroke_x_ratio

        yj = b.x1 + self.junction_ratio * b.height

        draw_rect(pen, b.xmid - sx / 2, b.y1, b.xmid + sx / 2, yj)

        draw_parallelogramm(pen, sx, sx, b.xmid - sx / 2, yj, b.x2, b.y2, delta=sx)
        draw_parallelogramm(
            pen,
            sx,
            sx,
            b.xmid + sx / 2,
            yj,
            b.x1,
            b.y2,
            direction="top-left",
            delta=sx,
        )
