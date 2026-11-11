"""Composed glyphs with the comma below."""

from config import FontConfig as fc
from glyphs.composed import ComposedGlyph
from glyphs.lowercase.square.n import LowercaseNGlyph
from glyphs.lowercase.s import LowercaseSGlyph
from glyphs.lowercase.single_story.g import LowercaseGGlyph
from glyphs.lowercase.l import LowercaseLGlyph
from glyphs.lowercase.t import LowercaseTGlyph
from glyphs.lowercase.k import LowercaseKGlyph
from glyphs.lowercase.square.r import LowercaseRGlyph
from glyphs.uppercase.n import UppercaseNGlyph
from glyphs.uppercase.s import UppercaseSGlyph
from glyphs.uppercase.g import UppercaseGGlyph
from glyphs.uppercase.l import UppercaseLGlyph
from glyphs.uppercase.t import UppercaseTGlyph
from glyphs.uppercase.k import UppercaseKGlyph
from glyphs.uppercase.r import UppercaseRGlyph
from glyphs.accents.acute import Acute
from glyphs.accents.comma_below import CommaBelow

_lc_accent = fc.accent


class LowercaseSCommaGlyph(ComposedGlyph):
    name = "lowercase_scommaaccent"
    unicode = "0x219"
    base_glyph_class = LowercaseSGlyph
    accent_class = CommaBelow
    accent_y = 0


class LowercaseTCommaGlyph(ComposedGlyph):
    name = "lowercase_tcommaaccent"
    unicode = "0x21B"
    base_glyph_class = LowercaseTGlyph
    accent_class = CommaBelow
    accent_y = 0

    def accent_x(self, dc, base, b):
        """Horizontal anchor of the accent; centered on the body by default."""
        return b.xmid + 0.25 * b.width


class UppercaseSCommaGlyph(ComposedGlyph):
    name = "uppercase_scommaaccent"
    unicode = "0x218"
    base_glyph_class = UppercaseSGlyph
    accent_class = CommaBelow
    accent_y = 0


class UppercaseTCommaGlyph(ComposedGlyph):
    name = "uppercase_tcommaaccent"
    unicode = "0x21A"
    base_glyph_class = UppercaseTGlyph
    accent_class = CommaBelow
    accent_y = 0


class LowercaseGCommaGlyph(ComposedGlyph):
    """The descender leaves no room below, so ģ takes its comma above."""

    name = "lowercase_gcommaaccent"
    unicode = "0x123"
    base_glyph_class = LowercaseGGlyph
    accent_class = Acute
    accent_y = _lc_accent


class LowercaseKCommaGlyph(ComposedGlyph):
    name = "lowercase_kcommaaccent"
    unicode = "0x137"
    base_glyph_class = LowercaseKGlyph
    accent_class = CommaBelow
    accent_y = 0


class LowercaseLCommaGlyph(ComposedGlyph):
    name = "lowercase_lcommaaccent"
    unicode = "0x13C"
    base_glyph_class = LowercaseLGlyph
    accent_class = CommaBelow
    accent_y = 0


class LowercaseNCommaGlyph(ComposedGlyph):
    name = "lowercase_ncommaaccent"
    unicode = "0x146"
    base_glyph_class = LowercaseNGlyph
    accent_class = CommaBelow
    accent_y = 0


class LowercaseRCommaGlyph(ComposedGlyph):
    name = "lowercase_rcommaaccent"
    unicode = "0x157"
    base_glyph_class = LowercaseRGlyph
    accent_class = CommaBelow
    accent_y = 0

    def accent_x(self, dc, base, b):
        """Horizontal anchor of the accent; centered on the body by default."""
        return b.x1 + dc.stroke_x / 2


class UppercaseGCommaGlyph(ComposedGlyph):
    name = "uppercase_gcommaaccent"
    unicode = "0x122"
    base_glyph_class = UppercaseGGlyph
    accent_class = CommaBelow
    accent_y = 0


class UppercaseKCommaGlyph(ComposedGlyph):
    name = "uppercase_kcommaaccent"
    unicode = "0x136"
    base_glyph_class = UppercaseKGlyph
    accent_class = CommaBelow
    accent_y = 0


class UppercaseLCommaGlyph(ComposedGlyph):
    name = "uppercase_lcommaaccent"
    unicode = "0x13B"
    base_glyph_class = UppercaseLGlyph
    accent_class = CommaBelow
    accent_y = 0


class UppercaseNCommaGlyph(ComposedGlyph):
    name = "uppercase_ncommaaccent"
    unicode = "0x145"
    base_glyph_class = UppercaseNGlyph
    accent_class = CommaBelow
    accent_y = 0


class UppercaseRCommaGlyph(ComposedGlyph):
    name = "uppercase_rcommaaccent"
    unicode = "0x156"
    base_glyph_class = UppercaseRGlyph
    accent_class = CommaBelow
    accent_y = 0
