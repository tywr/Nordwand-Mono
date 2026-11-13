"""Small capitals of the IPA: the capitals drawn at the x-height, with the
horizontal strokes of the lowercase."""

from glyphs.uppercase.bowl.b import UppercaseBGlyph
from glyphs.uppercase.round.g import UppercaseGGlyph
from glyphs.uppercase.h import UppercaseHGlyph
from glyphs.uppercase.i import UppercaseIGlyph
from glyphs.uppercase.l import UppercaseLGlyph
from glyphs.uppercase.stem_diagonal.n import UppercaseNGlyph
from glyphs.uppercase.bowl.r import UppercaseRGlyph
from glyphs.uppercase.diagonal.y import UppercaseYGlyph


class LatinSmallCapitalBGlyph(UppercaseBGlyph):
    name = "latin_small_capital_b"
    unicode = "0x299"
    height = "x_height"
    stroke_y_ratio = 1.00


class LatinSmallCapitalGGlyph(UppercaseGGlyph):
    name = "latin_small_capital_g"
    unicode = "0x262"
    height = "x_height"
    stroke_y_ratio = 1.00


class LatinSmallCapitalHGlyph(UppercaseHGlyph):
    name = "latin_small_capital_h"
    unicode = "0x29C"
    height = "x_height"
    stroke_y_ratio = 1.00


class LatinSmallCapitalIGlyph(UppercaseIGlyph):
    name = "latin_small_capital_i"
    unicode = "0x26A"
    height = "x_height"
    stroke_y_ratio = 1.00


class LatinSmallCapitalLGlyph(UppercaseLGlyph):
    name = "latin_small_capital_l"
    unicode = "0x29F"
    height = "x_height"
    stroke_y_ratio = 1.00


class LatinSmallCapitalNGlyph(UppercaseNGlyph):
    name = "latin_small_capital_n"
    unicode = "0x274"
    height = "x_height"
    stroke_y_ratio = 1.00


class LatinSmallCapitalRGlyph(UppercaseRGlyph):
    name = "latin_small_capital_r"
    unicode = "0x280"
    height = "x_height"
    stroke_y_ratio = 1.00


class LatinSmallCapitalYGlyph(UppercaseYGlyph):
    name = "latin_small_capital_y"
    unicode = "0x28F"
    height = "x_height"
    stroke_y_ratio = 1.00
