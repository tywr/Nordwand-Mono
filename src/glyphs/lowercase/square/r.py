import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph

from draw.rect import draw_rect
from glyphs.lowercase.square.n import LowercaseNGlyph


class LowercaseRGlyph(LowercaseNGlyph):
    """The n with its right stem cut, the cut ending the terminal."""

    name = "lowercase_r"
    unicode = "0x72"
    offset = 21
    width_ratio = 0.99
    tail_cut_ratio = 0.44

    def draw(self, pen, dc):
        b = self.body(dc)

        n_glyph = ufoLib2.objects.Glyph()
        super().draw(n_glyph.getPen(), dc)

        # Cut the right stem horizontally
        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            b.xmid,
            -10,
            b.x2 + 10,
            b.y2 - self.tail_cut_ratio * b.height,
        )
        result = BooleanGlyph(n_glyph).difference(BooleanGlyph(cut_glyph))
        result.draw(pen)
