from abc import ABC
from glyphs import Glyph


class SquareLowercaseGlyph(Glyph, ABC):
    """Define common class variables for all squared lowercase glyphs"""

    taper = 0.65
    width_ratio = 0.99
    loop_ratio = 0.75
