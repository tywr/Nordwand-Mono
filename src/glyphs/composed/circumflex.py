"""Composed glyphs with the circumflex."""

from config import FontConfig as fc
from glyphs.composed import ComposedGlyph
from glyphs.lowercase.a import LowercaseAGlyph
from glyphs.lowercase.round.e import LowercaseEGlyph
from glyphs.lowercase.round.o import LowercaseOGlyph
from glyphs.lowercase.round.c import LowercaseCGlyph
from glyphs.lowercase.square.u import LowercaseUGlyph
from glyphs.lowercase.dotted.i import LowercaseIGlyph
from glyphs.lowercase.y import LowercaseYGlyph
from glyphs.lowercase.w import LowercaseWGlyph
from glyphs.lowercase.s import LowercaseSGlyph
from glyphs.lowercase.single_story.g import LowercaseGGlyph
from glyphs.uppercase.diagonal.a import UppercaseAGlyph
from glyphs.uppercase.e import UppercaseEGlyph
from glyphs.uppercase.i import UppercaseIGlyph
from glyphs.uppercase.round.o import UppercaseOGlyph
from glyphs.uppercase.u import UppercaseUGlyph
from glyphs.uppercase.round.c import UppercaseCGlyph
from glyphs.uppercase.diagonal.y import UppercaseYGlyph
from glyphs.uppercase.diagonal.w import UppercaseWGlyph
from glyphs.uppercase.s import UppercaseSGlyph
from glyphs.uppercase.round.g import UppercaseGGlyph
from glyphs.uppercase.h import UppercaseHGlyph
from glyphs.lowercase.square.h import LowercaseHGlyph
from glyphs.lowercase.dotted.j import LowercaseJGlyph
from glyphs.uppercase.j import UppercaseJGlyph
from glyphs.accents.circumflex import Circumflex
from glyphs.composed.acute import LowercaseLAcuteGlyph

_lc_accent = fc.accent
_uc_accent = fc.accent_cap


class LowercaseACircumflexGlyph(ComposedGlyph):
    name = "lowercase_acircumflex"
    unicode = "0xE2"
    base_glyph_class = LowercaseAGlyph
    accent_class = Circumflex
    accent_y = _lc_accent


class LowercaseECircumflexGlyph(ComposedGlyph):
    name = "lowercase_ecircumflex"
    unicode = "0xEA"
    base_glyph_class = LowercaseEGlyph
    accent_class = Circumflex
    accent_y = _lc_accent


class LowercaseICircumflexGlyph(ComposedGlyph):
    name = "lowercase_icircumflex"
    unicode = "0xEE"
    base_glyph_class = LowercaseIGlyph
    accent_class = Circumflex
    accent_y = _lc_accent


class LowercaseOCircumflexGlyph(ComposedGlyph):
    name = "lowercase_ocircumflex"
    unicode = "0xF4"
    base_glyph_class = LowercaseOGlyph
    accent_class = Circumflex
    accent_y = _lc_accent


class LowercaseUCircumflexGlyph(ComposedGlyph):
    name = "lowercase_ucircumflex"
    unicode = "0xFB"
    base_glyph_class = LowercaseUGlyph
    accent_class = Circumflex
    accent_y = _lc_accent


class UppercaseACircumflexGlyph(ComposedGlyph):
    name = "uppercase_acircumflex"
    unicode = "0xC2"
    base_glyph_class = UppercaseAGlyph
    accent_class = Circumflex
    accent_y = _uc_accent


class UppercaseECircumflexGlyph(ComposedGlyph):
    name = "uppercase_ecircumflex"
    unicode = "0xCA"
    base_glyph_class = UppercaseEGlyph
    accent_class = Circumflex
    accent_y = _uc_accent


class UppercaseICircumflexGlyph(ComposedGlyph):
    name = "uppercase_icircumflex"
    unicode = "0xCE"
    base_glyph_class = UppercaseIGlyph
    accent_class = Circumflex
    accent_y = _uc_accent


class UppercaseOCircumflexGlyph(ComposedGlyph):
    name = "uppercase_ocircumflex"
    unicode = "0xD4"
    base_glyph_class = UppercaseOGlyph
    accent_class = Circumflex
    accent_y = _uc_accent


class UppercaseUCircumflexGlyph(ComposedGlyph):
    name = "uppercase_ucircumflex"
    unicode = "0xDB"
    base_glyph_class = UppercaseUGlyph
    accent_class = Circumflex
    accent_y = _uc_accent


class LowercaseWCircumflexGlyph(ComposedGlyph):
    name = "lowercase_wcircumflex"
    unicode = "0x175"
    base_glyph_class = LowercaseWGlyph
    accent_class = Circumflex
    accent_y = _lc_accent


class UppercaseWCircumflexGlyph(ComposedGlyph):
    name = "uppercase_wcircumflex"
    unicode = "0x174"
    base_glyph_class = UppercaseWGlyph
    accent_class = Circumflex
    accent_y = _uc_accent


class LowercaseYCircumflexGlyph(ComposedGlyph):
    name = "lowercase_ycircumflex"
    unicode = "0x177"
    base_glyph_class = LowercaseYGlyph
    accent_class = Circumflex
    accent_y = _lc_accent


class UppercaseYCircumflexGlyph(ComposedGlyph):
    name = "uppercase_ycircumflex"
    unicode = "0x176"
    base_glyph_class = UppercaseYGlyph
    accent_class = Circumflex
    accent_y = _uc_accent


class LowercaseCCircumflexGlyph(ComposedGlyph):
    name = "lowercase_ccircumflex"
    unicode = "0x109"
    base_glyph_class = LowercaseCGlyph
    accent_class = Circumflex
    accent_y = _lc_accent


class UppercaseCCircumflexGlyph(ComposedGlyph):
    name = "uppercase_ccircumflex"
    unicode = "0x108"
    base_glyph_class = UppercaseCGlyph
    accent_class = Circumflex
    accent_y = _uc_accent


class LowercaseGCircumflexGlyph(ComposedGlyph):
    name = "lowercase_gcircumflex"
    unicode = "0x11D"
    base_glyph_class = LowercaseGGlyph
    accent_class = Circumflex
    accent_y = _lc_accent


class UppercaseGCircumflexGlyph(ComposedGlyph):
    name = "uppercase_gcircumflex"
    unicode = "0x11C"
    base_glyph_class = UppercaseGGlyph
    accent_class = Circumflex
    accent_y = _uc_accent


class LowercaseHCircumflexGlyph(ComposedGlyph):
    """h with the circumflex above its ascender, centered on the left stem."""

    name = "lowercase_hcircumflex"
    unicode = "0x125"
    base_glyph_class = LowercaseHGlyph
    accent_class = Circumflex
    accent_y = LowercaseLAcuteGlyph.accent_y

    def accent_x(self, dc, base, b):
        b = dc.body_bounds(
            width_ratio=base.width_ratio, offset=base.offset, overshoot_top=True
        )
        return b.x1 + dc.stroke_x / 2


class UppercaseHCircumflexGlyph(ComposedGlyph):
    name = "uppercase_hcircumflex"
    unicode = "0x124"
    base_glyph_class = UppercaseHGlyph
    accent_class = Circumflex
    accent_y = _uc_accent


class LowercaseJCircumflexGlyph(ComposedGlyph):
    name = "lowercase_jcircumflex"
    unicode = "0x135"
    base_glyph_class = LowercaseJGlyph
    accent_class = Circumflex
    accent_y = _lc_accent

    def accent_x(self, dc, base, b):
        b = dc.body_bounds(
            width_ratio=base.width_ratio, offset=base.offset, overshoot_top=True
        )
        return b.xmid


class UppercaseJCircumflexGlyph(ComposedGlyph):
    name = "uppercase_jcircumflex"
    unicode = "0x134"
    base_glyph_class = UppercaseJGlyph
    accent_class = Circumflex
    accent_y = _uc_accent

    def accent_x(self, dc, base, b):
        b = dc.body_bounds(
            width_ratio=base.width_ratio, offset=base.offset, overshoot_top=True
        )
        return (b.x1 + b.x2) * 0.57


class LowercaseSCircumflexGlyph(ComposedGlyph):
    name = "lowercase_scircumflex"
    unicode = "0x15D"
    base_glyph_class = LowercaseSGlyph
    accent_class = Circumflex
    accent_y = _lc_accent


class UppercaseSCircumflexGlyph(ComposedGlyph):
    name = "uppercase_scircumflex"
    unicode = "0x15C"
    base_glyph_class = UppercaseSGlyph
    accent_class = Circumflex
    accent_y = _uc_accent
