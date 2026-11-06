from glyphs.accents import StackedAccent
from glyphs.accents.dieresis import Dieresis
from glyphs.accents.acute import Acute
from glyphs.accents.grave import Grave
from glyphs.accents.caron import Caron
from glyphs.accents.macron import Macron


class LowercaseDieresisStackedAccent(StackedAccent):
    first = Dieresis
    first_dy = -0.1
    second_dy = 0.27
    second_height = 0.3


class LowercaseDieresisMacron(LowercaseDieresisStackedAccent):
    """Macron on top of the dieresis."""

    name = "lowercase_dieresis_macron"
    second = Macron


class LowercaseDieresisAcute(LowercaseDieresisStackedAccent):
    """Acute on top of the dieresis."""

    name = "lowercase_dieresis_acute"
    second = Acute


class LowercaseDieresisCaron(LowercaseDieresisStackedAccent):
    """Caron on top of the dieresis."""

    name = "lowercase_dieresis_caron"
    second = Caron


class LowercaseDieresisGrave(LowercaseDieresisStackedAccent):
    """Grave on top of the dieresis."""

    name = "lowercase_dieresis_grave"
    second = Grave
