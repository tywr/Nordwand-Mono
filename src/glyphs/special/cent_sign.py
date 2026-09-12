from glyphs import Glyph
from draw.rect import draw_rect


class CentSignGlyph(Glyph):
    name = "cent_sign"
    unicode = "0xA2"
    offset = 0
    width_ratio = 1
    overflow_ratio = 0.25

    def draw(self, pen, dc):
        from glyphs.lowercase.round.c import LowercaseCGlyph

        b = dc.body_bounds(offset=self.offset, width_ratio=self.width_ratio)
        sg = LowercaseCGlyph()
        sg.draw(pen, dc)

        dh = self.overflow_ratio * b.height
        draw_rect(
            pen,
            b.xmid - dc.stroke_x / 2,
            b.y2 - dc.stroke_y / 2,
            b.xmid + dc.stroke_x / 2,
            b.y2 + dh,
        )
        draw_rect(
            pen,
            b.xmid - dc.stroke_x / 2,
            b.y1 - dh,
            b.xmid + dc.stroke_x / 2,
            b.y1 + dc.stroke_y / 2,
        )
