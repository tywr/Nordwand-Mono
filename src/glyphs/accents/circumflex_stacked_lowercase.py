from glyphs.accents import StackedAccent
from glyphs.accents.circumflex import Circumflex
from glyphs.accents.acute import Acute
from glyphs.accents.grave import Grave
from glyphs.accents.hook_above import HookAbove
from glyphs.accents.tilde import Tilde
from glyphs.accents.dot_below import DotBelow

class LowercaseCircumflexStackedAccent(StackedAccent):
    first_stroke_ratio = 1
    second_stroke_ratio = 1
    second_dy = 0.25
    second_dx = 0.5


class LowercaseCircumflexAcute(LowercaseCircumflexStackedAccent):
    """Acute at the top-right of the circumflex."""

    name = "lowercase_circumflex_acute"
    first = Circumflex
    second = Acute


class LowercaseCircumflexGrave(LowercaseCircumflexStackedAccent):
    """Grave at the top-right of the circumflex."""

    name = "lowercase_circumflex_grave"
    first = Circumflex
    second = Grave


class LowercaseCircumflexHookAbove(LowercaseCircumflexStackedAccent):
    """Hook above at the top-right of the circumflex."""

    name = "lowercase_circumflex_hookabove"
    first = Circumflex
    second = HookAbove


class LowercaseCircumflexTilde(LowercaseCircumflexStackedAccent):
    """Tilde on top of the circumflex."""

    name = "lowercase_circumflex_tilde"
    first = Circumflex
    second = Tilde
    second_dx = 0
    second_dy = 0.35


class LowercaseCircumflexDotBelow(LowercaseCircumflexStackedAccent):
    """Circumflex above and a dot below the baseline."""

    name = "lowercase_circumflex_dotbelow"
    first = Circumflex
    second = DotBelow
    second_y = 0
    second_dx = 0
