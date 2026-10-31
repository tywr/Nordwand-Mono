from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm


class GreekLowercaseLamdaGlyph(Glyph):
    """The y upside down: the legs stand on the baseline and the right one
    goes on up to the ascender"""

    name = "greek_lowercase_lamda"
    unicode = "0x3BB"
    offset = 0
    width_ratio = 1.15
    stroke_ratio = 0.895  # Perpendicular thickness of the legs and tail
    overlap = 0.536  # Former half of the 0.96 stroke, in the new stroke
    junction_ratio = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset, width_ratio=self.width_ratio)
        yj = dc.x_height
        s = self.stroke_ratio * dc.stroke_x
        ov = self.overlap * s

        draw_parallelogramm(
            pen, s, b.xmid + ov, yj, b.x1, 0, direction="bottom-left"
        )
        _, delta = draw_parallelogramm(
            pen, s, b.xmid - ov, yj, b.x2, 0, direction="bottom-right"
        )
        # Tail continuing the right leg up to the ascender, sharing its
        # section so the two join flush
        w2 = b.x2 - (b.xmid - ov)
        dx_tail = -(w2 - delta) * (dc.ascent - yj) / yj
        draw_parallelogramm(
            pen,
            s,
            b.xmid - ov + delta,
            yj,
            b.xmid - ov + dx_tail,
            dc.ascent,
            direction="top-left",
            overwrite_section=delta,
        )
