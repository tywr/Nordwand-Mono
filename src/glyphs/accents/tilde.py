from glyphs.accents import Accent
from glyphs.special.tilde import TildeGlyph


class Tilde(Accent):
    """The tilde glyph's shape, scaled down by `rescale`, drawn with the
    breve's stroke (`stroke_alt`) so that it stays light in bold."""

    name = "accent_tilde"
    unicode = "0x2DC"
    rescale = 0.7
    stroke_ratio = 1.0  # Relative to stroke_alt

    def draw_at(self, pen, dc, x, y):
        tilde = TildeGlyph()
        b = dc.body_bounds(
            offset=tilde.offset, height="x_height", width_ratio=tilde.width_ratio
        )
        s = dc.stroke_alt * self.stroke_ratio
        tilde.draw_shape(pen, dc, b, x, y, s, s, scale=self.rescale)
