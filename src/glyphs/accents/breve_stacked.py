from glyphs.accents import StackedAccent
from glyphs.accents.breve import Breve
from glyphs.accents.acute import Acute
from glyphs.accents.grave import Grave
from glyphs.accents.hook_above import HookAbove
from glyphs.accents.tilde import Tilde
from glyphs.accents.dot_below import DotBelow


class BreveStackedAccent(StackedAccent):
    first_stroke_ratio = 0.85


class BreveAcute(BreveStackedAccent):
    """Acute on top of the breve."""

    name = "breve_acute"
    first = Breve
    second = Acute
    first_dy = -0.1
    second_dy = 0.15
    second_dx = -0.05
    second_height = 0.3
    second_width = 0.5


class BreveGrave(BreveStackedAccent):
    """Grave on top of the breve."""

    name = "breve_grave"
    first = Breve
    second = Grave
    first_dy = -0.1
    second_dy = 0.15
    second_dx = 0.05
    second_height = 0.3
    second_width = 0.5


class BreveHookAbove(BreveStackedAccent):
    """Hook above on top of the breve."""

    name = "breve_hookabove"
    first = Breve
    second = HookAbove
    first_dy = -0.1
    second_dy = 0.1
    second_dx = -0.1
    second_height = 0.3


class BreveTilde(BreveStackedAccent):
    """Tilde on top of the breve."""

    name = "breve_tilde"
    first = Breve
    second = Tilde
    first_height = 0.2
    first_dy = -0.12
    second_dy = 0.2
    second_height = 0.22
    second_dy = 0.18
    second_width = 1.0


class BreveDotBelow(StackedAccent):
    """Breve above and a dot below the baseline."""

    name = "breve_dotbelow"
    first = Breve
    second = DotBelow
    second_y = 0
    first_stroke_ratio = 1
