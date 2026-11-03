from glyphs.special.right_square_bracket import RightSquareBracketGlyph
from draw.rect import draw_rect


class LeftSquareBracketGlyph(RightSquareBracketGlyph):
    name = "left_square_bracket"
    unicode = "0x5B"
    offset = 0

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        ymid = dc.parenthesis

        draw_rect(
            pen,
            b.x1,
            ymid - dc.parenthesis_length / 2,
            b.x1 + dc.stroke_x,
            ymid + dc.parenthesis_length / 2,
        )
        draw_rect(
            pen,
            b.x1,
            ymid + dc.parenthesis_length / 2 - dc.stroke_y,
            b.x2,
            ymid + dc.parenthesis_length / 2,
        )
        draw_rect(
            pen,
            b.x1,
            ymid - dc.parenthesis_length / 2,
            b.x2,
            ymid - dc.parenthesis_length / 2 + dc.stroke_y,
        )
