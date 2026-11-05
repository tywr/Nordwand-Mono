from glyphs.accents import StackedAccent
from glyphs.accents.circumflex import Circumflex
from glyphs.accents.acute import Acute
from glyphs.accents.grave import Grave
from glyphs.accents.hook_above import HookAbove
from glyphs.accents.tilde import Tilde
from glyphs.accents.dot_below import DotBelow


class CircumflexAcute(StackedAccent):
    """Acute at the top-right of the circumflex."""

    name = "circumflex_acute"
    first = Circumflex
    second = Acute
    second_dx = 0.5
    second_dy = 0.3


class CircumflexGrave(StackedAccent):
    """Grave at the top-right of the circumflex."""

    name = "circumflex_grave"
    first = Circumflex
    second = Grave
    second_dx = 0.5
    second_dy = 0.3


class CircumflexHookAbove(StackedAccent):
    """Hook above at the top-right of the circumflex."""

    name = "circumflex_hookabove"
    first = Circumflex
    second = HookAbove
    second_dx = 0.5
    second_dy = 0.3


class CircumflexTilde(StackedAccent):
    """Tilde on top of the circumflex."""

    name = "circumflex_tilde"
    first = Circumflex
    second = Tilde
    second_dy = 0.36
    # Smaller and thinner, to stay below the window ascent
    second_attrs = {"rescale": 0.55, "stroke_ratio": 0.75}


class CircumflexDotBelow(StackedAccent):
    """Circumflex above and a dot below the baseline."""

    name = "circumflex_dotbelow"
    first = Circumflex
    second = DotBelow
    second_y = 0
