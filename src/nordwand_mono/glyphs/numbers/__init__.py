from abc import ABC
from nordwand_mono.glyphs import Glyph


class NumberGlyph(Glyph, ABC):
    """Define common class variables for all number glyphs"""

    width_ratio = 1.06
    stroke_x_ratio = 0.98
    stroke_y_ratio = 0.98
    hx_ratio = 0.9
    hy_ratio = 0.9
