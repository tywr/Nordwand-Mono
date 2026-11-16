"""Composed glyphs with the hook above."""

from nordwand_mono.config import FontConfig as fc
from nordwand_mono.glyphs.composed import ComposedGlyph
from nordwand_mono.glyphs.lowercase.a import LowercaseAGlyph
from nordwand_mono.glyphs.accents.hook_above import HookAbove
from nordwand_mono.glyphs.lowercase.dotted.i import LowercaseIGlyph
from nordwand_mono.glyphs.lowercase.round.e import LowercaseEGlyph
from nordwand_mono.glyphs.lowercase.round.o import LowercaseOGlyph
from nordwand_mono.glyphs.lowercase.square.u import LowercaseUGlyph
from nordwand_mono.glyphs.lowercase.y import LowercaseYGlyph
from nordwand_mono.glyphs.uppercase.e import UppercaseEGlyph
from nordwand_mono.glyphs.uppercase.diagonal.a import UppercaseAGlyph
from nordwand_mono.glyphs.uppercase.i import UppercaseIGlyph
from nordwand_mono.glyphs.uppercase.round.o import UppercaseOGlyph
from nordwand_mono.glyphs.uppercase.u import UppercaseUGlyph
from nordwand_mono.glyphs.uppercase.diagonal.y import UppercaseYGlyph

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
