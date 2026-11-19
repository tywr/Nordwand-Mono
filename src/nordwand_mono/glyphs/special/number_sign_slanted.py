from math import hypot

from nordwand_mono.draw.parallelogramm import draw_parallelogramm
from nordwand_mono.draw.rect import draw_rect
from nordwand_mono.glyphs.special.number_sign import NumberSignGlyph


class NumberSignSlantedGlyph(NumberSignGlyph):
    """Number sign whose vertical bars lean to the right. Its ligature forms
    keep the vertical bars of the default number sign."""

    name = "number_sign_slanted"
    font_feature = {"cv30": 1}
    alternative_character_comment = "Number sign with slanted bars"
    # Horizontal run of the slanted bars, ratio of the body width
    slant = 0.16
    stroke_ratio = 1

    def draw(self, pen, dc):
        b, xm1, xm2, _, _, y1, y2 = self._geometry(dc)
        s = self.stroke_ratio * dc.stroke_x
        d = self.slant * b.width
        # Horizontal width of a band of perpendicular thickness s
        delta = s * hypot(d, y2 - y1) / (y2 - y1)
        for xm in (xm1, xm2):
            x1 = xm - (d + delta) / 2
            draw_parallelogramm(pen, s, x1, y1, x1 + d + delta, y2)

        stroke = self.horizontal_bar_stroke(dc)
        x1, x2 = self.horizontal_bar_bounds(dc)
        for y in self.horizontal_bar_heights(dc):
            draw_rect(pen, x1, y - stroke / 2, x2, y + stroke / 2)
