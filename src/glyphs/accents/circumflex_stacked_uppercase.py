from glyphs.accents import StackedAccent
from glyphs.accents.circumflex import Circumflex
from glyphs.accents.acute import Acute
from glyphs.accents.grave import Grave
from glyphs.accents.hook_above import HookAbove
from glyphs.accents.tilde import Tilde
from glyphs.accents.dot_below import DotBelow


class UppercaseCicumflexStackedAccent(StackedAccent):
    first_stroke_ratio = 0.8
    first_height = 0.2
    first_width = 0.8
    first_dy = -0.16
    second_stroke_ratio = 0.8
    second_dy = 0.0
    second_dx = 0.5
    second_height = 0.25


class UppercaseCircumflexAcute(UppercaseCicumflexStackedAccent):
    """Acute at the top-right of the circumflex."""

    name = "uppercase_circumflex_acute"
    first = Circumflex
    second = Acute


class UppercaseCircumflexGrave(UppercaseCicumflexStackedAccent):
    """Grave at the top-right of the circumflex."""

    name = "uppercase_circumflex_grave"
    first = Circumflex
    second = Grave


class UppercaseCircumflexHookAbove(UppercaseCicumflexStackedAccent):
    """Hook above at the top-right of the circumflex."""

    name = "uppercase_circumflex_hookabove"
    first = Circumflex
    second = HookAbove
    second_height = 0.3

class UppercaseCircumflexTilde(UppercaseCicumflexStackedAccent):
    """Tilde on top of the circumflex."""

    name = "uppercase_circumflex_tilde"
    first = Circumflex
    second = Tilde
    second_height = 0.23
    second_dy = 0.085
    second_dx = 0


class UppercaseCircumflexDotBelow(UppercaseCicumflexStackedAccent):
    """Circumflex above and a dot below the baseline."""

    name = "uppercase_circumflex_dotbelow"
    first = Circumflex
    second = DotBelow
    second_y = 0
    first_stroke_ratio = 1
    second_stroke_ratio = 1
