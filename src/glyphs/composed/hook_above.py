"""Composed glyphs with the hook above."""

from config import FontConfig as fc
from glyphs.composed import ComposedGlyph
from glyphs.lowercase.a import LowercaseAGlyph
from glyphs.accents.hook_above import HookAbove
from glyphs.lowercase.dotted.i import LowercaseIGlyph
from glyphs.lowercase.round.e import LowercaseEGlyph
from glyphs.lowercase.round.o import LowercaseOGlyph
from glyphs.lowercase.square.u import LowercaseUGlyph
from glyphs.lowercase.y import LowercaseYGlyph
from glyphs.uppercase.e import UppercaseEGlyph
from glyphs.uppercase.a import UppercaseAGlyph
from glyphs.uppercase.i import UppercaseIGlyph
from glyphs.uppercase.o import UppercaseOGlyph
from glyphs.uppercase.u import UppercaseUGlyph
from glyphs.uppercase.y import UppercaseYGlyph

_lc_accent = fc.accent
_uc_accent = fc.accent_cap


class LowercaseAHookAboveGlyph(ComposedGlyph):
    name = "lowercase_ahookabove"
    unicode = "0x1EA3"
    base_glyph_class = LowercaseAGlyph
    accent_class = HookAbove
    accent_y = _lc_accent


class LowercaseEHookAboveGlyph(ComposedGlyph):
    name = "lowercase_ehookabove"
    unicode = "0x1EBB"
    base_glyph_class = LowercaseEGlyph
    accent_class = HookAbove
    accent_y = _lc_accent


class LowercaseIHookAboveGlyph(ComposedGlyph):
    name = "lowercase_ihookabove"
    unicode = "0x1EC9"
    base_glyph_class = LowercaseIGlyph
    accent_class = HookAbove
    accent_y = _lc_accent


class LowercaseOHookAboveGlyph(ComposedGlyph):
    name = "lowercase_ohookabove"
    unicode = "0x1ECF"
    base_glyph_class = LowercaseOGlyph
    accent_class = HookAbove
    accent_y = _lc_accent


class LowercaseUHookAboveGlyph(ComposedGlyph):
    name = "lowercase_uhookabove"
    unicode = "0x1EE7"
    base_glyph_class = LowercaseUGlyph
    accent_class = HookAbove
    accent_y = _lc_accent


class LowercaseYHookAboveGlyph(ComposedGlyph):
    name = "lowercase_yhookabove"
    unicode = "0x1EF7"
    base_glyph_class = LowercaseYGlyph
    accent_class = HookAbove
    accent_y = _lc_accent


class UppercaseEHookAboveGlyph(ComposedGlyph):
    name = "uppercase_ehookabove"
    unicode = "0x1EBA"
    base_glyph_class = UppercaseEGlyph
    accent_class = HookAbove
    accent_y = _uc_accent


class UppercaseAHookAboveGlyph(ComposedGlyph):
    name = "uppercase_ahookabove"
    unicode = "0x1EA2"
    base_glyph_class = UppercaseAGlyph
    accent_class = HookAbove
    accent_y = _uc_accent


class UppercaseIHookAboveGlyph(ComposedGlyph):
    name = "uppercase_ihookabove"
    unicode = "0x1EC8"
    base_glyph_class = UppercaseIGlyph
    accent_class = HookAbove
    accent_y = _uc_accent


class UppercaseOHookAboveGlyph(ComposedGlyph):
    name = "uppercase_ohookabove"
    unicode = "0x1ECE"
    base_glyph_class = UppercaseOGlyph
    accent_class = HookAbove
    accent_y = _uc_accent


class UppercaseUHookAboveGlyph(ComposedGlyph):
    name = "uppercase_uhookabove"
    unicode = "0x1EE6"
    base_glyph_class = UppercaseUGlyph
    accent_class = HookAbove
    accent_y = _uc_accent


class UppercaseYHookAboveGlyph(ComposedGlyph):
    name = "uppercase_yhookabove"
    unicode = "0x1EF6"
    base_glyph_class = UppercaseYGlyph
    accent_class = HookAbove
    accent_y = _uc_accent
