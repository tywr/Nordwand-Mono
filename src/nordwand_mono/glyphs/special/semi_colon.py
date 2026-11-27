from nordwand_mono.glyphs import Glyph
from nordwand_mono.draw.dot import dot_size, draw_dot


class SemiColonGlyph(Glyph):
    name = "semi_colon"
    unicode = "0x3B"
    offset = 0
    width_ratio = 1
    dot_ratio = 1.5
    gap = 1

    def draw(self, pen, dc):
        from nordwand_mono.glyphs.special.comma import CommaGlyph

        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        _, h = dot_size(dc, self.dot_ratio)
        g = b.height * self.gap

        draw_dot(pen, dc, b.xmid, b.y1 + g - h / 2, self.dot_ratio)
        cg = CommaGlyph()
        cg.draw(pen, dc)


class GreekQuestionMarkGlyph(SemiColonGlyph):
    name = "greek_question_mark"
    unicode = "0x037E"
