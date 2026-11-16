"""Composed glyphs with the macron."""

from nordwand_mono.config import FontConfig as fc
from nordwand_mono.glyphs.composed import ComposedGlyph
from nordwand_mono.glyphs.lowercase.a import LowercaseAGlyph
from nordwand_mono.glyphs.lowercase.round.e import LowercaseEGlyph
from nordwand_mono.glyphs.lowercase.round.o import LowercaseOGlyph
from nordwand_mono.glyphs.lowercase.square.u import LowercaseUGlyph
from nordwand_mono.glyphs.lowercase.dotted.i import LowercaseIGlyph
from nordwand_mono.glyphs.uppercase.diagonal.a import UppercaseAGlyph
from nordwand_mono.glyphs.uppercase.e import UppercaseEGlyph
from nordwand_mono.glyphs.uppercase.i import UppercaseIGlyph
from nordwand_mono.glyphs.uppercase.round.o import UppercaseOGlyph
from nordwand_mono.glyphs.uppercase.u import UppercaseUGlyph
from nordwand_mono.glyphs.accents.macron import Macron
from nordwand_mono.glyphs.lowercase.y import LowercaseYGlyph
from nordwand_mono.glyphs.uppercase.diagonal.y import UppercaseYGlyph
from nordwand_mono.glyphs.lowercase.single_story.g import LowercaseGGlyph
from nordwand_mono.glyphs.uppercase.round.g import UppercaseGGlyph

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


class LowercaseGMacronGlyph(ComposedGlyph):
    name = "lowercase_gmacron"
    unicode = "0x1E21"
    base_glyph_class = LowercaseGGlyph
    accent_class = Macron
    accent_y = _lc_accent


class UppercaseGMacronGlyph(ComposedGlyph):
    name = "uppercase_gmacron"
    unicode = "0x1E20"
    base_glyph_class = UppercaseGGlyph
    accent_class = Macron
    accent_y = _uc_accent
