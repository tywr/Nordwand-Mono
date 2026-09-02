from draw.parallelogramm import draw_parallelogramm
from glyphs.numbers.zero import ZeroGlyph


class ZeroSlashedGlyph(ZeroGlyph):
    name = "zero_slashed"
    font_feature = {"cv01": 1}
    slash_stroke_ratio = 0.65
    slash_vertical_inset = 0.16

    def draw_mark(self, pen, dc, b):
        x_inset = dc.stroke_x * 0.5
        y_inset = self.slash_vertical_inset * b.height
        draw_parallelogramm(
            pen,
            dc.stroke_x * self.slash_stroke_ratio,
            dc.stroke_y * self.slash_stroke_ratio,
            b.x1 + x_inset,
            b.y1 + y_inset,
            b.x2 - x_inset,
            b.y2 - y_inset,
        )
