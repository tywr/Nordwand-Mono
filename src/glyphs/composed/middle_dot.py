"""Composed glyphs with the middle dot."""

from glyphs.lowercase.l import LowercaseLGlyph
from glyphs.uppercase.l import UppercaseLGlyph
from draw.dot import dot_size, draw_dot


def _draw_l_dot(pen, dc, x, y):
    """Middle dot centered between the stem of an L and its right edge."""
    w, _ = dot_size(dc, 1.4)
    draw_dot(pen, dc, x - w / 2, y, 1.4)


class LowercaseLDotGlyph(LowercaseLGlyph):
    name = "lowercase_ldot"
    unicode = "0x140"

    def draw(self, pen, dc):
        super().draw(pen, dc)
        b = dc.body_bounds(
            offset=self.offset, height="ascent", width_ratio=self.width_ratio
        )
        _draw_l_dot(pen, dc, b.x2, dc.cap / 2)


class UppercaseLDotGlyph(UppercaseLGlyph):
    name = "uppercase_ldot"
    unicode = "0x13F"

    def draw(self, pen, dc):
        super().draw(pen, dc)
        b = dc.body_bounds(
            offset=self.offset, height="cap", width_ratio=self.width_ratio
        )
        _draw_l_dot(pen, dc, b.x2, dc.cap / 2)
