"""Composed glyphs with the acute."""

from config import FontConfig as fc
from glyphs.composed import ComposedGlyph
from glyphs.lowercase.a import LowercaseAGlyph
from glyphs.lowercase.round.e import LowercaseEGlyph
from glyphs.lowercase.round.o import LowercaseOGlyph
from glyphs.lowercase.round.c import LowercaseCGlyph
from glyphs.lowercase.square.u import LowercaseUGlyph
from glyphs.lowercase.square.n import LowercaseNGlyph
from glyphs.lowercase.dotted.i import LowercaseIGlyph
from glyphs.lowercase.y import LowercaseYGlyph
from glyphs.lowercase.w import LowercaseWGlyph
from glyphs.lowercase.s import LowercaseSGlyph
from glyphs.lowercase.l import LowercaseLGlyph
from glyphs.lowercase.z import LowercaseZGlyph
from glyphs.lowercase.r import LowercaseRGlyph
from glyphs.uppercase.a import UppercaseAGlyph
from glyphs.uppercase.e import UppercaseEGlyph
from glyphs.uppercase.i import UppercaseIGlyph
from glyphs.uppercase.o import UppercaseOGlyph
from glyphs.uppercase.u import UppercaseUGlyph
from glyphs.uppercase.n import UppercaseNGlyph
from glyphs.uppercase.c import UppercaseCGlyph
from glyphs.uppercase.y import UppercaseYGlyph
from glyphs.uppercase.w import UppercaseWGlyph
from glyphs.uppercase.s import UppercaseSGlyph
from glyphs.uppercase.l import UppercaseLGlyph
from glyphs.uppercase.z import UppercaseZGlyph
from glyphs.uppercase.r import UppercaseRGlyph
from glyphs.accents.acute import Acute

_lc_accent = fc.accent
_uc_accent = fc.accent_cap


class LowercaseAAcuteGlyph(ComposedGlyph):
    name = "lowercase_aacute"
    unicode = "0xE1"
    base_glyph_class = LowercaseAGlyph
    accent_class = Acute
    accent_y = _lc_accent


class LowercaseEAcuteGlyph(ComposedGlyph):
    name = "lowercase_eacute"
    unicode = "0xE9"
    base_glyph_class = LowercaseEGlyph
    accent_class = Acute
    accent_y = _lc_accent


class LowercaseIAcuteGlyph(ComposedGlyph):
    name = "lowercase_iacute"
    unicode = "0xED"
    base_glyph_class = LowercaseIGlyph
    accent_class = Acute
    accent_y = _lc_accent


class LowercaseOAcuteGlyph(ComposedGlyph):
    name = "lowercase_oacute"
    unicode = "0xF3"
    base_glyph_class = LowercaseOGlyph
    accent_class = Acute
    accent_y = _lc_accent


class LowercaseUAcuteGlyph(ComposedGlyph):
    name = "lowercase_uacute"
    unicode = "0xFA"
    base_glyph_class = LowercaseUGlyph
    accent_class = Acute
    accent_y = _lc_accent


class LowercaseYAcuteGlyph(ComposedGlyph):
    name = "lowercase_yacute"
    unicode = "0xFD"
    base_glyph_class = LowercaseYGlyph
    accent_class = Acute
    accent_y = _lc_accent


class UppercaseAAcuteGlyph(ComposedGlyph):
    name = "uppercase_aacute"
    unicode = "0xC1"
    base_glyph_class = UppercaseAGlyph
    accent_class = Acute
    accent_y = _uc_accent


class UppercaseEAcuteGlyph(ComposedGlyph):
    name = "uppercase_eacute"
    unicode = "0xC9"
    base_glyph_class = UppercaseEGlyph
    accent_class = Acute
    accent_y = _uc_accent


class UppercaseIAcuteGlyph(ComposedGlyph):
    name = "uppercase_iacute"
    unicode = "0xCD"
    base_glyph_class = UppercaseIGlyph
    accent_class = Acute
    accent_y = _uc_accent


class UppercaseOAcuteGlyph(ComposedGlyph):
    name = "uppercase_oacute"
    unicode = "0xD3"
    base_glyph_class = UppercaseOGlyph
    accent_class = Acute
    accent_y = _uc_accent


class UppercaseUAcuteGlyph(ComposedGlyph):
    name = "uppercase_uacute"
    unicode = "0xDA"
    base_glyph_class = UppercaseUGlyph
    accent_class = Acute
    accent_y = _uc_accent


class UppercaseYAcuteGlyph(ComposedGlyph):
    name = "uppercase_yacute"
    unicode = "0xDD"
    base_glyph_class = UppercaseYGlyph
    accent_class = Acute
    accent_y = _uc_accent


class LowercaseWAcuteGlyph(ComposedGlyph):
    name = "lowercase_wacute"
    unicode = "0x1E83"
    base_glyph_class = LowercaseWGlyph
    accent_class = Acute
    accent_y = _lc_accent


class UppercaseWAcuteGlyph(ComposedGlyph):
    name = "uppercase_wacute"
    unicode = "0x1E82"
    base_glyph_class = UppercaseWGlyph
    accent_class = Acute
    accent_y = _uc_accent


class LowercaseCAcuteGlyph(ComposedGlyph):
    name = "lowercase_cacute"
    unicode = "0x107"
    base_glyph_class = LowercaseCGlyph
    accent_class = Acute
    accent_y = _lc_accent


class LowercaseNAcuteGlyph(ComposedGlyph):
    name = "lowercase_nacute"
    unicode = "0x144"
    base_glyph_class = LowercaseNGlyph
    accent_class = Acute
    accent_y = _lc_accent


class LowercaseSAcuteGlyph(ComposedGlyph):
    name = "lowercase_sacute"
    unicode = "0x15B"
    base_glyph_class = LowercaseSGlyph
    accent_class = Acute
    accent_y = _lc_accent


class LowercaseZAcuteGlyph(ComposedGlyph):
    name = "lowercase_zacute"
    unicode = "0x17A"
    base_glyph_class = LowercaseZGlyph
    accent_class = Acute
    accent_y = _lc_accent


class UppercaseCAcuteGlyph(ComposedGlyph):
    name = "uppercase_cacute"
    unicode = "0x106"
    base_glyph_class = UppercaseCGlyph
    accent_class = Acute
    accent_y = _uc_accent


class UppercaseNAcuteGlyph(ComposedGlyph):
    name = "uppercase_nacute"
    unicode = "0x143"
    base_glyph_class = UppercaseNGlyph
    accent_class = Acute
    accent_y = _uc_accent


class UppercaseSAcuteGlyph(ComposedGlyph):
    name = "uppercase_sacute"
    unicode = "0x15A"
    base_glyph_class = UppercaseSGlyph
    accent_class = Acute
    accent_y = _uc_accent


class UppercaseZAcuteGlyph(ComposedGlyph):
    name = "uppercase_zacute"
    unicode = "0x179"
    base_glyph_class = UppercaseZGlyph
    accent_class = Acute
    accent_y = _uc_accent


class LowercaseRAcuteGlyph(ComposedGlyph):
    name = "lowercase_racute"
    unicode = "0x155"
    base_glyph_class = LowercaseRGlyph
    accent_class = Acute
    accent_y = _lc_accent


class UppercaseRAcuteGlyph(ComposedGlyph):
    name = "uppercase_racute"
    unicode = "0x154"
    base_glyph_class = UppercaseRGlyph
    accent_class = Acute
    accent_y = _uc_accent


class UppercaseLAcuteGlyph(ComposedGlyph):
    name = "uppercase_lacute"
    unicode = "0x139"
    base_glyph_class = UppercaseLGlyph
    accent_class = Acute
    accent_y = _uc_accent

    def accent_x(self, dc, base, b):
        return b.x1 + Acute.stroke_ratio * dc.stroke_x / 2


class LowercaseLAcuteGlyph(ComposedGlyph):
    """l with the acute above its ascender, centered on the stem."""

    name = "lowercase_lacute"
    unicode = "0x13A"
    base_glyph_class = LowercaseLGlyph
    accent_class = Acute
    # Above the ascent by most of the gap capitals leave below their accent
    accent_y = fc.ascent + 1.0 * (fc.accent_cap - fc.cap)

    def accent_x(self, dc, base, b):
        return base.stem_center(dc)
