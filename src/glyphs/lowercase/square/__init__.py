from abc import ABC
from glyphs import Glyph


class SquareLowercaseGlyph(Glyph, ABC):
    """Define common class variables for all squared lowercase glyphs"""

    hx_ratio = 1
    taper = 0.65
    width_ratio = 0.99
    ending_thickness = 0.8
    loop_ratio = 0.9
