"""Composed glyphs with the circumflex below (Venda ḓ ḽ ṋ ṱ)."""

from glyphs.composed import ComposedGlyph
from glyphs.accents.circumflex import CircumflexBelow
from glyphs.lowercase.single_story.d import LowercaseDGlyph
from glyphs.uppercase.d import UppercaseDGlyph
from glyphs.lowercase.l import LowercaseLGlyph
from glyphs.uppercase.l import UppercaseLGlyph
from glyphs.lowercase.square.n import LowercaseNGlyph
from glyphs.uppercase.n import UppercaseNGlyph
from glyphs.lowercase.t import LowercaseTGlyph
from glyphs.uppercase.t import UppercaseTGlyph


class LowercaseDCircumflexBelowGlyph(ComposedGlyph):
    name = "lowercase_dcircumflexbelow"
    unicode = "0x1E13"
    base_glyph_class = LowercaseDGlyph
    accent_class = CircumflexBelow
    accent_y = 0


class UppercaseDCircumflexBelowGlyph(ComposedGlyph):
    name = "uppercase_dcircumflexbelow"
    unicode = "0x1E12"
    base_glyph_class = UppercaseDGlyph
    accent_class = CircumflexBelow
    accent_y = 0


class LowercaseLCircumflexBelowGlyph(ComposedGlyph):
    name = "lowercase_lcircumflexbelow"
    unicode = "0x1E3D"
    base_glyph_class = LowercaseLGlyph
    accent_class = CircumflexBelow
    accent_y = 0


class UppercaseLCircumflexBelowGlyph(ComposedGlyph):
    name = "uppercase_lcircumflexbelow"
    unicode = "0x1E3C"
    base_glyph_class = UppercaseLGlyph
    accent_class = CircumflexBelow
    accent_y = 0


class LowercaseNCircumflexBelowGlyph(ComposedGlyph):
    name = "lowercase_ncircumflexbelow"
    unicode = "0x1E4B"
    base_glyph_class = LowercaseNGlyph
    accent_class = CircumflexBelow
    accent_y = 0


class UppercaseNCircumflexBelowGlyph(ComposedGlyph):
    name = "uppercase_ncircumflexbelow"
    unicode = "0x1E4A"
    base_glyph_class = UppercaseNGlyph
    accent_class = CircumflexBelow
    accent_y = 0


class LowercaseTCircumflexBelowGlyph(ComposedGlyph):
    name = "lowercase_tcircumflexbelow"
    unicode = "0x1E71"
    base_glyph_class = LowercaseTGlyph
    accent_class = CircumflexBelow
    accent_y = 0


class UppercaseTCircumflexBelowGlyph(ComposedGlyph):
    name = "uppercase_tcircumflexbelow"
    unicode = "0x1E70"
    base_glyph_class = UppercaseTGlyph
    accent_class = CircumflexBelow
    accent_y = 0
