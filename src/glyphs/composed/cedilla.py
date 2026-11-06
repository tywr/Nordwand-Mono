"""Composed glyphs with the cedilla."""

from glyphs.composed import ComposedGlyph
from glyphs.lowercase.round.c import LowercaseCGlyph
from glyphs.lowercase.s import LowercaseSGlyph
from glyphs.lowercase.t import LowercaseTGlyph
from glyphs.uppercase.c import UppercaseCGlyph
from glyphs.uppercase.s import UppercaseSGlyph
from glyphs.uppercase.t import UppercaseTGlyph
from glyphs.accents.cedilla import Cedilla

_cedilla_y = 0


class LowercaseCCedillaGlyph(ComposedGlyph):
    name = "lowercase_ccedilla"
    unicode = "0xE7"
    base_glyph_class = LowercaseCGlyph
    accent_class = Cedilla
    accent_y = _cedilla_y


class LowercaseSCedillaGlyph(ComposedGlyph):
    name = "lowercase_scedilla"
    unicode = "0x15F"
    base_glyph_class = LowercaseSGlyph
    accent_class = Cedilla
    accent_y = _cedilla_y


class UppercaseCCedillaGlyph(ComposedGlyph):
    name = "uppercase_ccedilla"
    unicode = "0xC7"
    base_glyph_class = UppercaseCGlyph
    accent_class = Cedilla
    accent_y = _cedilla_y


class UppercaseSCedillaGlyph(ComposedGlyph):
    name = "uppercase_scedilla"
    unicode = "0x15E"
    base_glyph_class = UppercaseSGlyph
    accent_class = Cedilla
    accent_y = _cedilla_y


class LowercaseTCedillaGlyph(ComposedGlyph):
    name = "lowercase_tcedilla"
    unicode = "0x163"
    base_glyph_class = LowercaseTGlyph
    accent_class = Cedilla

    def accent_x(self, dc, base, b):
        """Horizontal anchor of the accent; centered on the body by default."""
        return b.xmid + 0.17 * b.width

    def draw(self, pen, dc):
        base_class = self._resolve_base_class(dc)
        base = base_class()
        base.draw_base(pen, dc) if hasattr(base, "draw_base") else base.draw(pen, dc)

        b = dc.body_bounds(offset=base_class.offset)
        accent_class = self.accent_class()
        accent_class.y_start = 10
        accent_class.draw_at(pen, dc, x=self.accent_x(dc, base, b), y=0)


class UppercaseTCedillaGlyph(ComposedGlyph):
    name = "uppercase_tcedilla"
    unicode = "0x162"
    base_glyph_class = UppercaseTGlyph
    accent_class = Cedilla
    accent_y = _cedilla_y

    def accent_x(self, dc, base, b):
        """Neck's top-right corner (x + sl/2) on the stem's right edge."""
        stem_right = b.xmid + base.stroke_x_ratio * dc.stroke_x / 2
        sl = (
            self.accent_class.slant_ratio
            * self.accent_class.stroke_ratio_x
            * dc.stroke_x
        )
        return stem_right - sl / 2 - self.accent_class.x_offset * dc.width
