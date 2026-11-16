from nordwand_mono.glyphs import Glyph
from nordwand_mono.glyphs.special.equals_sign import EqualsSignGlyph
from nordwand_mono.draw.rect import draw_rect


class NotSignGlyph(Glyph):
    """A bar with a drop at its right end, spanning the two bars of `=`."""

    name = "not_sign"
    unicode = "0xAC"
    offset = 0

    def draw(self, pen, dc):
        eq = EqualsSignGlyph()
        x1, x2 = eq.horizontal_bar_bounds(dc)
        y_top, y_bottom = eq.horizontal_bar_heights(dc)
        s = eq.horizontal_bar_stroke(dc)

        draw_rect(pen, x1, y_top - s / 2, x2, y_top + s / 2)
        draw_rect(pen, x2 - s, y_bottom - s / 2, x2, y_top)
