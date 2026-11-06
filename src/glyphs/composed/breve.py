"""Composed glyphs with the breve."""

from config import FontConfig as fc
from glyphs.composed import ComposedGlyph
from glyphs.lowercase.a import LowercaseAGlyph
from glyphs.lowercase.round.e import LowercaseEGlyph
from glyphs.lowercase.round.o import LowercaseOGlyph
from glyphs.lowercase.square.u import LowercaseUGlyph
from glyphs.lowercase.dotted.i import LowercaseIGlyph
from glyphs.lowercase.single_story.g import LowercaseGGlyph
from glyphs.uppercase.a import UppercaseAGlyph
from glyphs.uppercase.e import UppercaseEGlyph
from glyphs.uppercase.i import UppercaseIGlyph
from glyphs.uppercase.o import UppercaseOGlyph
from glyphs.uppercase.u import UppercaseUGlyph
from glyphs.uppercase.g import UppercaseGGlyph
from glyphs.accents.breve import Breve

_lc_accent = fc.accent
_uc_accent = fc.accent_cap


class LowercaseGBreveGlyph(ComposedGlyph):
    name = "lowercase_gbreve"
    unicode = "0x11F"
    base_glyph_class = LowercaseGGlyph
    accent_class = Breve
    accent_y = _lc_accent


class UppercaseGBreveGlyph(ComposedGlyph):
    name = "uppercase_gbreve"
    unicode = "0x11E"
    base_glyph_class = UppercaseGGlyph
    accent_class = Breve
    accent_y = _uc_accent


class LowercaseABreveGlyph(ComposedGlyph):
    name = "lowercase_abreve"
    unicode = "0x103"
    base_glyph_class = LowercaseAGlyph
    accent_class = Breve
    accent_y = _lc_accent


class UppercaseABreveGlyph(ComposedGlyph):
    name = "uppercase_abreve"
    unicode = "0x102"
    base_glyph_class = UppercaseAGlyph
    accent_class = Breve
    accent_y = _uc_accent


class LowercaseUBreveGlyph(ComposedGlyph):
    name = "lowercase_ubreve"
    unicode = "0x16D"
    base_glyph_class = LowercaseUGlyph
    accent_class = Breve
    accent_y = _lc_accent


class UppercaseUBreveGlyph(ComposedGlyph):
    name = "uppercase_ubreve"
    unicode = "0x16C"
    base_glyph_class = UppercaseUGlyph
    accent_class = Breve
    accent_y = _uc_accent


class LowercaseEBreveGlyph(ComposedGlyph):
    name = "lowercase_ebreve"
    unicode = "0x115"
    base_glyph_class = LowercaseEGlyph
    accent_class = Breve
    accent_y = _lc_accent


class UppercaseEBreveGlyph(ComposedGlyph):
    name = "uppercase_ebreve"
    unicode = "0x114"
    base_glyph_class = UppercaseEGlyph
    accent_class = Breve
    accent_y = _uc_accent


class LowercaseIBreveGlyph(ComposedGlyph):
    name = "lowercase_ibreve"
    unicode = "0x12D"
    base_glyph_class = LowercaseIGlyph
    accent_class = Breve
    accent_y = _lc_accent


class UppercaseIBreveGlyph(ComposedGlyph):
    name = "uppercase_ibreve"
    unicode = "0x12C"
    base_glyph_class = UppercaseIGlyph
    accent_class = Breve
    accent_y = _uc_accent


class LowercaseOBreveGlyph(ComposedGlyph):
    name = "lowercase_obreve"
    unicode = "0x14F"
    base_glyph_class = LowercaseOGlyph
    accent_class = Breve
    accent_y = _lc_accent


class UppercaseOBreveGlyph(ComposedGlyph):
    name = "uppercase_obreve"
    unicode = "0x14E"
    base_glyph_class = UppercaseOGlyph
    accent_class = Breve
    accent_y = _uc_accent
