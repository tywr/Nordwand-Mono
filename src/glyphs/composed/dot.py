"""Composed glyphs with the dot above."""

from config import FontConfig as fc
from glyphs.composed import ComposedGlyph
from glyphs.lowercase.round.e import LowercaseEGlyph
from glyphs.lowercase.round.c import LowercaseCGlyph
from glyphs.lowercase.single_story.g import LowercaseGGlyph
from glyphs.lowercase.z import LowercaseZGlyph
from glyphs.uppercase.e import UppercaseEGlyph
from glyphs.uppercase.i import UppercaseIGlyph
from glyphs.uppercase.round.c import UppercaseCGlyph
from glyphs.uppercase.round.g import UppercaseGGlyph
from glyphs.uppercase.z import UppercaseZGlyph
from glyphs.accents.dot import DotAbove
from glyphs.lowercase.square.n import LowercaseNGlyph
from glyphs.lowercase.single_story.p import LowercasePGlyph
from glyphs.uppercase.stem_diagonal.n import UppercaseNGlyph
from glyphs.uppercase.bowl.p import UppercasePGlyph

_lc_accent = fc.accent
_uc_accent = fc.accent_cap


class UppercaseIDotGlyph(ComposedGlyph):
    name = "uppercase_idotaccent"
    unicode = "0x130"
    base_glyph_class = UppercaseIGlyph
    accent_class = DotAbove
    accent_y = _uc_accent


class LowercaseZDotGlyph(ComposedGlyph):
    name = "lowercase_zdotaccent"
    unicode = "0x17C"
    base_glyph_class = LowercaseZGlyph
    accent_class = DotAbove
    accent_y = _lc_accent


class UppercaseZDotGlyph(ComposedGlyph):
    name = "uppercase_zdotaccent"
    unicode = "0x17B"
    base_glyph_class = UppercaseZGlyph
    accent_class = DotAbove
    accent_y = _uc_accent


class LowercaseCDotGlyph(ComposedGlyph):
    name = "lowercase_cdotaccent"
    unicode = "0x10B"
    base_glyph_class = LowercaseCGlyph
    accent_class = DotAbove
    accent_y = _lc_accent


class UppercaseCDotGlyph(ComposedGlyph):
    name = "uppercase_cdotaccent"
    unicode = "0x10A"
    base_glyph_class = UppercaseCGlyph
    accent_class = DotAbove
    accent_y = _uc_accent


class LowercaseGDotGlyph(ComposedGlyph):
    name = "lowercase_gdotaccent"
    unicode = "0x121"
    base_glyph_class = LowercaseGGlyph
    accent_class = DotAbove
    accent_y = _lc_accent


class UppercaseGDotGlyph(ComposedGlyph):
    name = "uppercase_gdotaccent"
    unicode = "0x120"
    base_glyph_class = UppercaseGGlyph
    accent_class = DotAbove
    accent_y = _uc_accent


class LowercaseEDotGlyph(ComposedGlyph):
    name = "lowercase_edotaccent"
    unicode = "0x117"
    base_glyph_class = LowercaseEGlyph
    accent_class = DotAbove
    accent_y = _lc_accent


class UppercaseEDotGlyph(ComposedGlyph):
    name = "uppercase_edotaccent"
    unicode = "0x116"
    base_glyph_class = UppercaseEGlyph
    accent_class = DotAbove
    accent_y = _uc_accent


class LowercaseNDotGlyph(ComposedGlyph):
    name = "lowercase_ndotaccent"
    unicode = "0x1E45"
    base_glyph_class = LowercaseNGlyph
    accent_class = DotAbove
    accent_y = _lc_accent


class LowercasePDotGlyph(ComposedGlyph):
    name = "lowercase_pdotaccent"
    unicode = "0x1E57"
    base_glyph_class = LowercasePGlyph
    accent_class = DotAbove
    accent_y = _lc_accent


class UppercaseNDotGlyph(ComposedGlyph):
    name = "uppercase_ndotaccent"
    unicode = "0x1E44"
    base_glyph_class = UppercaseNGlyph
    accent_class = DotAbove
    accent_y = _uc_accent


class UppercasePDotGlyph(ComposedGlyph):
    name = "uppercase_pdotaccent"
    unicode = "0x1E56"
    base_glyph_class = UppercasePGlyph
    accent_class = DotAbove
    accent_y = _uc_accent
