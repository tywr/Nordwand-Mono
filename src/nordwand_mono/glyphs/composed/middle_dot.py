"""Composed glyphs with the middle dot."""

from nordwand_mono.glyphs.composed import ComposedGlyph
from nordwand_mono.glyphs.lowercase.l import LowercaseLGlyph
from nordwand_mono.glyphs.uppercase.l import UppercaseLGlyph
from nordwand_mono.draw.dot import dot_size, draw_dot


def _draw_l_dot(pen, dc, x, y):
    """Middle dot centered between the stem of an L and its right edge."""
    w, _ = dot_size(dc, 1.4)
    draw_dot(pen, dc, x - w / 2, y, 1.4)


class LowercaseLDotGlyph(ComposedGlyph):
    """Composed so it follows the alternates of the l (cv03, ss01)."""

    name = "lowercase_ldot"
    unicode = "0x140"
    base_glyph_class = LowercaseLGlyph

    def draw(self, pen, dc):
        base = self._resolve_base_class(dc)()
        base.draw(pen, dc)
        b = dc.body_bounds(
            offset=base.offset, height="ascent", width_ratio=base.width_ratio
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
