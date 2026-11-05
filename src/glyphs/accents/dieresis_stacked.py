from glyphs.accents import StackedAccent
from glyphs.accents.dieresis import Dieresis
from glyphs.accents.acute import Acute
from glyphs.accents.grave import Grave
from glyphs.accents.caron import Caron
from glyphs.accents.macron import Macron


class DieresisStackedAccent(StackedAccent):
    first = Dieresis
    first_dy = -0.2
    first_stroke_ratio = 0.9
    second_dy = 0.05


class DieresisMacron(DieresisStackedAccent):
    """Macron on top of the dieresis."""

    name = "dieresis_macron"
    second = Macron
    second_stroke_ratio = 0.8
    second_width = 0.8


class DieresisAcute(DieresisStackedAccent):
    """Acute on top of the dieresis."""

    name = "dieresis_acute"
    second = Acute
    second_height = 0.22
    second_width = 0.5


class DieresisCaron(DieresisStackedAccent):
    """Caron on top of the dieresis."""

    name = "dieresis_caron"
    second = Caron
    second_height = 0.2
    second_width = 0.8


class DieresisGrave(DieresisStackedAccent):
    """Grave on top of the dieresis."""

    name = "dieresis_grave"
    second = Grave
    second_height = 0.22
    second_width = 0.5
