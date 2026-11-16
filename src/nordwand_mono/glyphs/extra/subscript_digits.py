from nordwand_mono.glyphs.extra.superscript_digits import SuperscriptDigitGlyph
from nordwand_mono.glyphs.numbers.zero import ZeroGlyph
from nordwand_mono.glyphs.numbers.one import OneGlyph
from nordwand_mono.glyphs.numbers.two import TwoGlyph
from nordwand_mono.glyphs.numbers.three import ThreeGlyph
from nordwand_mono.glyphs.numbers.four import FourGlyph
from nordwand_mono.glyphs.numbers.five import FiveGlyph
from nordwand_mono.glyphs.numbers.six import SixGlyph
from nordwand_mono.glyphs.numbers.seven import SevenGlyph
from nordwand_mono.glyphs.numbers.eight import EightGlyph
from nordwand_mono.glyphs.numbers.nine import NineGlyph


class SubscriptDigitGlyph(SuperscriptDigitGlyph):
    """The superscript digit lowered to dip slightly below the baseline."""

    top_ratio = 0.48


class SubscriptZeroGlyph(SubscriptDigitGlyph):
    name = "subscript_zero"
    unicode = "0x2080"
    source = ZeroGlyph


class SubscriptOneGlyph(SubscriptDigitGlyph):
    name = "subscript_one"
    unicode = "0x2081"
    source = OneGlyph


class SubscriptTwoGlyph(SubscriptDigitGlyph):
    name = "subscript_two"
    unicode = "0x2082"
    source = TwoGlyph


class SubscriptThreeGlyph(SubscriptDigitGlyph):
    name = "subscript_three"
    unicode = "0x2083"
    source = ThreeGlyph


class SubscriptFourGlyph(SubscriptDigitGlyph):
    name = "subscript_four"
    unicode = "0x2084"
    source = FourGlyph


class SubscriptFiveGlyph(SubscriptDigitGlyph):
    name = "subscript_five"
    unicode = "0x2085"
    source = FiveGlyph


class SubscriptSixGlyph(SubscriptDigitGlyph):
    name = "subscript_six"
    unicode = "0x2086"
    source = SixGlyph


class SubscriptSevenGlyph(SubscriptDigitGlyph):
    name = "subscript_seven"
    unicode = "0x2087"
    source = SevenGlyph


class SubscriptEightGlyph(SubscriptDigitGlyph):
    name = "subscript_eight"
    unicode = "0x2088"
    source = EightGlyph


class SubscriptNineGlyph(SubscriptDigitGlyph):
    name = "subscript_nine"
    unicode = "0x2089"
    source = NineGlyph
