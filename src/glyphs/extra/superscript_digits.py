from glyphs.extra.ordinal_indicator import OrdinalIndicatorGlyph
from glyphs.numbers.zero import ZeroGlyph
from glyphs.numbers.one import OneGlyph
from glyphs.numbers.two import TwoGlyph
from glyphs.numbers.three import ThreeGlyph
from glyphs.numbers.four import FourGlyph
from glyphs.numbers.five import FiveGlyph
from glyphs.numbers.six import SixGlyph
from glyphs.numbers.seven import SevenGlyph
from glyphs.numbers.eight import EightGlyph
from glyphs.numbers.nine import NineGlyph


class SuperscriptDigitGlyph(OrdinalIndicatorGlyph):
    """A digit scaled down with its top at the cap height."""

    scale = 0.72
    # Lighter than the ordinals: digits have tighter counters at this size
    stroke_ratio = 0.82
    top_ratio = 1.15


class SuperscriptZeroGlyph(SuperscriptDigitGlyph):
    name = "superscript_zero"
    unicode = "0x2070"
    source = ZeroGlyph


class SuperscriptOneGlyph(SuperscriptDigitGlyph):
    name = "superscript_one"
    unicode = "0xB9"
    source = OneGlyph


class SuperscriptTwoGlyph(SuperscriptDigitGlyph):
    name = "superscript_two"
    unicode = "0xB2"
    source = TwoGlyph


class SuperscriptThreeGlyph(SuperscriptDigitGlyph):
    name = "superscript_three"
    unicode = "0xB3"
    source = ThreeGlyph


class SuperscriptFourGlyph(SuperscriptDigitGlyph):
    name = "superscript_four"
    unicode = "0x2074"
    source = FourGlyph


class SuperscriptFiveGlyph(SuperscriptDigitGlyph):
    name = "superscript_five"
    unicode = "0x2075"
    source = FiveGlyph


class SuperscriptSixGlyph(SuperscriptDigitGlyph):
    name = "superscript_six"
    unicode = "0x2076"
    source = SixGlyph


class SuperscriptSevenGlyph(SuperscriptDigitGlyph):
    name = "superscript_seven"
    unicode = "0x2077"
    source = SevenGlyph


class SuperscriptEightGlyph(SuperscriptDigitGlyph):
    name = "superscript_eight"
    unicode = "0x2078"
    source = EightGlyph


class SuperscriptNineGlyph(SuperscriptDigitGlyph):
    name = "superscript_nine"
    unicode = "0x2079"
    source = NineGlyph
