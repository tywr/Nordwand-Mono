from glyphs.accents import StackedAccent
from glyphs.accents.breve import Breve
from glyphs.accents.acute import Acute
from glyphs.accents.grave import Grave
from glyphs.accents.hook_above import HookAbove
from glyphs.accents.tilde import Tilde
from glyphs.accents.dot_below import DotBelow


class UppercaseBreveStackedAccent(StackedAccent):
    first_stroke_ratio = 0.8
    first_height = 0.2
    first_dy = -0.15
    second_stroke_ratio = 0.8
    second_height = 0.25
    second_dy = 0.075


class UppercaseBreveAcute(UppercaseBreveStackedAccent):
    """Acute on top of the breve."""

    name = "uppercase_breve_acute"
    first = Breve
    second = Acute


class UppercaseBreveGrave(UppercaseBreveStackedAccent):
    """Grave on top of the breve."""

    name = "uppercase_breve_grave"
    first = Breve
    second = Grave


class UppercaseBreveHookAbove(UppercaseBreveStackedAccent):
    """Hook above on top of the breve."""

    name = "uppercase_breve_hookabove"
    first = Breve
    second = HookAbove
    second_dx = -0.13


class UppercaseBreveTilde(UppercaseBreveStackedAccent):
    """Tilde on top of the breve."""

    name = "uppercase_breve_tilde"
    first = Breve
    second = Tilde
    second_height = 0.23
    second_width = 1
    second_dy = 0.085

class UppercaseBreveDotBelow(StackedAccent):
    """Breve above and a dot below the baseline."""

    name = "uppercase_breve_dotbelow"
    first = Breve
    second = DotBelow
    second_y = 0
    first_stroke_ratio = 1
    second_stroke_ratio = 1
