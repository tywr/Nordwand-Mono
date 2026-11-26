from nordwand_mono.glyphs.numbers import NumberGlyph
from nordwand_mono.draw.rect import draw_rect
from nordwand_mono.draw.parallelogramm import draw_parallelogramm


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
    slant_offset_coef = 0.1
    vertical_offset_coef = 0.45

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="cap", width_ratio=self.width_ratio
        )
        sx, sy = self.get_strokes(dc)

        xo = 0.75 * (sx - dc.default_stroke)
        xvo = self.vertical_offset_coef * (sx - dc.default_stroke)
        xho = -0.25 * (sx - dc.default_stroke)
        xto = self.slant_offset_coef * (sx - dc.default_stroke)

        xmid = b.x1 + self.horizontal_ratio * b.width + xho
        xtop = b.x1 + self.slant_ratio * b.width + xto
        ymid = b.y1 + self.vertical_ratio * b.height + xvo
        ybar = b.y1 + self.mid_bar_ratio * b.height

        s = self.stroke_ratio * dc.stroke_x

        # Diagonal bar
        draw_parallelogramm(pen, s, b.x1, ymid, xtop - sx / 2 + xo, b.y2)

        # Horizontal line
        draw_rect(pen, b.x1, ymid - sy, b.x2, ymid)

        # Vertical line
        draw_rect(pen, xmid - sx / 2, b.y1, xmid + sx / 2, ybar)
