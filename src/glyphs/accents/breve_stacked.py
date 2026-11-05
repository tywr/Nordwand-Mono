from glyphs.accents import StackedAccent
from glyphs.accents.breve import Breve
from glyphs.accents.acute import Acute
from glyphs.accents.grave import Grave
from glyphs.accents.hook_above import HookAbove
from glyphs.accents.tilde import Tilde
from glyphs.accents.dot_below import DotBelow


class BreveAcute(StackedAccent):
    """Acute on top of the breve."""

    name = "breve_acute"
    first = Breve
    second = Acute
    second_dy = 0.18


class BreveGrave(StackedAccent):
    """Grave on top of the breve."""

    name = "breve_grave"
    first = Breve
    second = Grave
    second_dy = 0.18


class BreveHookAbove(StackedAccent):
    """Hook above on top of the breve."""

    name = "breve_hookabove"
    first = Breve
    second = HookAbove
    second_dy = 0.18


class BreveTilde(StackedAccent):
    """Tilde on top of the breve."""

    name = "breve_tilde"
    first = Breve
    second = Tilde
    second_dy = 0.28


class BreveDotBelow(StackedAccent):
    """Breve above and a dot below the baseline."""

    name = "breve_dotbelow"
    first = Breve
    second = DotBelow
    second_y = 0
