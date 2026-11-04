from abc import ABC
from glyphs import Glyph


class SingleStoryLowercaseGlyph(Glyph, ABC):
    """Define common class variables for single-story lowercase glyphs"""

    taper = 0.8
    width_ratio = 1.01

    bowl_stroke_x_ratio = 1.01
    bowl_stroke_y_ratio = 1.00

    hx_ratio = 1
    hy_ratio = 1
