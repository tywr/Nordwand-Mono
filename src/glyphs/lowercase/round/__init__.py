from abc import ABC
from glyphs import Glyph


class RoundLowercaseGlyph(Glyph, ABC):
    """Define common class variables for round lowercase glyphs"""

    stroke_x_ratio = 1.01
    stroke_y_ratio = 1.00

    hy_ratio = 1
    hx_ratio = 1
