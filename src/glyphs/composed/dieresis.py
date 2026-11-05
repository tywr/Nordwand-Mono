"""Composed glyphs with the dieresis."""

from config import FontConfig as fc
from glyphs.composed import ComposedGlyph
from glyphs.lowercase.a import LowercaseAGlyph
from glyphs.lowercase.round.e import LowercaseEGlyph
from glyphs.lowercase.round.o import LowercaseOGlyph
from glyphs.lowercase.square.u import LowercaseUGlyph
from glyphs.lowercase.dotted.i import LowercaseIGlyph
from glyphs.lowercase.y import LowercaseYGlyph
from glyphs.lowercase.w import LowercaseWGlyph
from glyphs.uppercase.a import UppercaseAGlyph
from glyphs.uppercase.e import UppercaseEGlyph
from glyphs.uppercase.i import UppercaseIGlyph
from glyphs.uppercase.o import UppercaseOGlyph
from glyphs.uppercase.u import UppercaseUGlyph
from glyphs.uppercase.y import UppercaseYGlyph
from glyphs.uppercase.w import UppercaseWGlyph
from glyphs.accents.dieresis import Dieresis

_lc_accent = fc.accent
_uc_accent = fc.accent_cap


class LowercaseADieresisGlyph(ComposedGlyph):
    name = "lowercase_adieresis"
    unicode = "0xE4"
    base_glyph_class = LowercaseAGlyph
    accent_class = Dieresis
    accent_y = _lc_accent


class LowercaseEDieresisGlyph(ComposedGlyph):
    name = "lowercase_edieresis"
    unicode = "0xEB"
    base_glyph_class = LowercaseEGlyph
    accent_class = Dieresis
    accent_y = _lc_accent


class LowercaseIDieresisGlyph(ComposedGlyph):
    name = "lowercase_idieresis"
    unicode = "0xEF"
    base_glyph_class = LowercaseIGlyph
    accent_class = Dieresis
    accent_y = _lc_accent


class LowercaseODieresisGlyph(ComposedGlyph):
    name = "lowercase_odieresis"
    unicode = "0xF6"
    base_glyph_class = LowercaseOGlyph
    accent_class = Dieresis
    accent_y = _lc_accent


class LowercaseUDieresisGlyph(ComposedGlyph):
    name = "lowercase_udieresis"
    unicode = "0xFC"
    base_glyph_class = LowercaseUGlyph
    accent_class = Dieresis
    accent_y = _lc_accent


class LowercaseYDieresisGlyph(ComposedGlyph):
    name = "lowercase_ydieresis"
    unicode = "0xFF"
    base_glyph_class = LowercaseYGlyph
    accent_class = Dieresis
    accent_y = _lc_accent


class UppercaseADieresisGlyph(ComposedGlyph):
    name = "uppercase_adieresis"
    unicode = "0xC4"
    base_glyph_class = UppercaseAGlyph
    accent_class = Dieresis
    accent_y = _uc_accent


class UppercaseEDieresisGlyph(ComposedGlyph):
    name = "uppercase_edieresis"
    unicode = "0xCB"
    base_glyph_class = UppercaseEGlyph
    accent_class = Dieresis
    accent_y = _uc_accent


class UppercaseIDieresisGlyph(ComposedGlyph):
    name = "uppercase_idieresis"
    unicode = "0xCF"
    base_glyph_class = UppercaseIGlyph
    accent_class = Dieresis
    accent_y = _uc_accent


class UppercaseODieresisGlyph(ComposedGlyph):
    name = "uppercase_odieresis"
    unicode = "0xD6"
    base_glyph_class = UppercaseOGlyph
    accent_class = Dieresis
    accent_y = _uc_accent


class UppercaseUDieresisGlyph(ComposedGlyph):
    name = "uppercase_udieresis"
    unicode = "0xDC"
    base_glyph_class = UppercaseUGlyph
    accent_class = Dieresis
    accent_y = _uc_accent


class UppercaseYDieresisGlyph(ComposedGlyph):
    name = "uppercase_ydieresis"
    unicode = "0x178"
    base_glyph_class = UppercaseYGlyph
    accent_class = Dieresis
    accent_y = _uc_accent


class LowercaseWDieresisGlyph(ComposedGlyph):
    name = "lowercase_wdieresis"
    unicode = "0x1E85"
    base_glyph_class = LowercaseWGlyph
    accent_class = Dieresis
    accent_y = _lc_accent


class UppercaseWDieresisGlyph(ComposedGlyph):
    name = "uppercase_wdieresis"
    unicode = "0x1E84"
    base_glyph_class = UppercaseWGlyph
    accent_class = Dieresis
    accent_y = _uc_accent
