from nordwand_mono.glyphs.accents import StackedAccent
from nordwand_mono.glyphs.accents.dieresis import Dieresis
from nordwand_mono.glyphs.accents.acute import Acute
from nordwand_mono.glyphs.accents.grave import Grave
from nordwand_mono.glyphs.accents.caron import Caron
from nordwand_mono.glyphs.accents.macron import Macron


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
