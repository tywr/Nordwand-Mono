from glyphs.accents import StackedAccent
from glyphs.accents.dieresis import Dieresis
from glyphs.accents.acute import Acute
from glyphs.accents.grave import Grave
from glyphs.accents.caron import Caron
from glyphs.accents.macron import Macron


class UppercaseDieresisStackedAccent(StackedAccent):
    first = Dieresis
    first_height = 0.2
    first_dy = -0.18
    first_stroke_ratio = 0.65
    second_stroke_ratio = 0.75
    second_height = 0.25
    second_dy = 0.075


class UppercaseDieresisMacron(UppercaseDieresisStackedAccent):
    """Macron on top of the dieresis."""

    name = "uppercase_dieresis_macron"
    second = Macron


class UppercaseDieresisAcute(UppercaseDieresisStackedAccent):
    """Acute on top of the dieresis."""

    name = "uppercase_dieresis_acute"
    second = Acute


class UppercaseDieresisCaron(UppercaseDieresisStackedAccent):
    """Caron on top of the dieresis."""

    name = "uppercase_dieresis_caron"
    second = Caron


class UppercaseDieresisGrave(UppercaseDieresisStackedAccent):
    """Grave on top of the dieresis."""

    name = "uppercase_dieresis_grave"
    second = Grave
