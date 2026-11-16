from nordwand_mono.glyphs.accents import StackedAccent
from nordwand_mono.glyphs.accents.breve import Breve
from nordwand_mono.glyphs.accents.acute import Acute
from nordwand_mono.glyphs.accents.grave import Grave
from nordwand_mono.glyphs.accents.hook_above import HookAbove
from nordwand_mono.glyphs.accents.tilde import Tilde
from nordwand_mono.glyphs.accents.dot_below import DotBelow


class LowercaseBreveStackedAccent(StackedAccent):
    first_stroke_ratio = 1
    second_stroke_ratio = 1
    second_dy = 0.3


class LowercaseBreveAcute(LowercaseBreveStackedAccent):
    """Acute on top of the breve."""

    name = "lowercase_breve_acute"
    first = Breve
    second = Acute


class LowercaseBreveGrave(LowercaseBreveStackedAccent):
    """Grave on top of the breve."""

    name = "lowercase_breve_grave"
    first = Breve
    second = Grave


class LowercaseBreveHookAbove(LowercaseBreveStackedAccent):
    """Hook above on top of the breve."""

    name = "lowercase_breve_hookabove"
    first = Breve
    second = HookAbove


class LowercaseBreveTilde(LowercaseBreveStackedAccent):
    """Tilde on top of the breve."""

    name = "lowercase_breve_tilde"
    first = Breve
    second = Tilde
    second_dy = 0.4


class LowercaseBreveDotBelow(LowercaseBreveStackedAccent):
    """Breve above and a dot below the baseline."""

    name = "lowercase_breve_dotbelow"
    first = Breve
    second = DotBelow
    second_y = 0
