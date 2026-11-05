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
    second_width = 0.55
    second_dy = 0.15
    second_height = 0.25


class CircumflexGrave(StackedAccent):
    """Grave at the top-right of the circumflex."""

    name = "circumflex_grave"
    first = Circumflex
    second = Grave
    second_dx = 0.55
    second_width = 0.55
    second_dy = 0.15
    second_height = 0.25


class CircumflexHookAbove(StackedAccent):
    """Hook above at the top-right of the circumflex."""

    name = "circumflex_hookabove"
    first = Circumflex
    second = HookAbove
    second_dx = 0.55
    second_dy = 0.12
    second_height = 0.3


class CircumflexTilde(StackedAccent):
    """Tilde on top of the circumflex."""

    name = "circumflex_tilde"
    first = Circumflex
    second = Tilde
    first_height = 0.25
    first_width = 0.9
    first_dy = -0.08
    first_stroke_ratio = 0.8
    second_dy = 0.2
    second_height = 0.22
    second_dy = 0.18
    second_width = 1.0


class CircumflexDotBelow(StackedAccent):
    """Circumflex above and a dot below the baseline."""

    name = "circumflex_dotbelow"
    first = Circumflex
    second = DotBelow
    second_y = 0
    first_stroke_ratio = 1
