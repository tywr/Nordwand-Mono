"""Composed glyphs with the macron."""

from config import FontConfig as fc
from glyphs.composed import ComposedGlyph
from glyphs.lowercase.a import LowercaseAGlyph
from glyphs.lowercase.round.e import LowercaseEGlyph
from glyphs.lowercase.round.o import LowercaseOGlyph
from glyphs.lowercase.square.u import LowercaseUGlyph
from glyphs.lowercase.dotted.i import LowercaseIGlyph
from glyphs.uppercase.a import UppercaseAGlyph
from glyphs.uppercase.e import UppercaseEGlyph
from glyphs.uppercase.i import UppercaseIGlyph
from glyphs.uppercase.o import UppercaseOGlyph
from glyphs.uppercase.u import UppercaseUGlyph
from glyphs.accents.macron import Macron
from glyphs.lowercase.y import LowercaseYGlyph
from glyphs.uppercase.y import UppercaseYGlyph

_lc_accent = fc.accent
_uc_accent = fc.accent_cap


class LowercaseAMacronGlyph(ComposedGlyph):
    name = "lowercase_amacron"
    unicode = "0x101"
    base_glyph_class = LowercaseAGlyph
    accent_class = Macron
    accent_y = _lc_accent


class LowercaseEMacronGlyph(ComposedGlyph):
    name = "lowercase_emacron"
    unicode = "0x113"
    base_glyph_class = LowercaseEGlyph
    accent_class = Macron
    accent_y = _lc_accent


class LowercaseIMacronGlyph(ComposedGlyph):
    name = "lowercase_imacron"
    unicode = "0x12B"
    base_glyph_class = LowercaseIGlyph
    accent_class = Macron
    accent_y = _lc_accent


class LowercaseOMacronGlyph(ComposedGlyph):
    name = "lowercase_omacron"
    unicode = "0x14D"
    base_glyph_class = LowercaseOGlyph
    accent_class = Macron
    accent_y = _lc_accent


class LowercaseUMacronGlyph(ComposedGlyph):
    name = "lowercase_umacron"
    unicode = "0x16B"
    base_glyph_class = LowercaseUGlyph
    accent_class = Macron
    accent_y = _lc_accent


class UppercaseAMacronGlyph(ComposedGlyph):
    name = "uppercase_amacron"
    unicode = "0x100"
    base_glyph_class = UppercaseAGlyph
    accent_class = Macron
    accent_y = _uc_accent


class UppercaseEMacronGlyph(ComposedGlyph):
    name = "uppercase_emacron"
    unicode = "0x112"
    base_glyph_class = UppercaseEGlyph
    accent_class = Macron
    accent_y = _uc_accent


class UppercaseIMacronGlyph(ComposedGlyph):
    name = "uppercase_imacron"
    unicode = "0x12A"
    base_glyph_class = UppercaseIGlyph
    accent_class = Macron
    accent_y = _uc_accent


class UppercaseOMacronGlyph(ComposedGlyph):
    name = "uppercase_omacron"
    unicode = "0x14C"
    base_glyph_class = UppercaseOGlyph
    accent_class = Macron
    accent_y = _uc_accent


class UppercaseUMacronGlyph(ComposedGlyph):
    name = "uppercase_umacron"
    unicode = "0x16A"
    base_glyph_class = UppercaseUGlyph
    accent_class = Macron
    accent_y = _uc_accent


class UppercaseYMacronGlyph(ComposedGlyph):
    name = "uppercase_ymacron"
    unicode = "0x232"
    base_glyph_class = UppercaseYGlyph
    accent_class = Macron
    accent_y = _uc_accent


class LowercaseYMacronGlyph(ComposedGlyph):
    name = "lowercase_ymacron"
    unicode = "0x233"
    base_glyph_class = LowercaseYGlyph
    accent_class = Macron
    accent_y = _lc_accent
