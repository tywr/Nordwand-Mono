from glyphs.special.right_parenthesis import RightParenthesisGlyph
from draw.loop import draw_loop


class LeftParenthesisGlyph(RightParenthesisGlyph):
    name = "left_parenthesis"
    unicode = "0x28"
    offset = 0

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        sx, sy = self.stroke_x_ratio * dc.stroke_x, dc.stroke_y
        o = self.offset + b.width / 2 - sx
        ymid = dc.parenthesis
        draw_loop(
            pen,
            sx,
            sy,
            b.x1 + o,
            ymid - dc.parenthesis_length / 2,
            b.x2 + o,
            ymid + dc.parenthesis_length / 2,
            b.hx,
            b.hy * dc.parenthesis_length / b.height,
            cut="right",
        )
