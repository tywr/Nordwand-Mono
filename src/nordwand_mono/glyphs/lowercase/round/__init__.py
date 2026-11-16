from abc import ABC
from nordwand_mono.glyphs import Glyph


class RoundLowercaseGlyph(Glyph, ABC):
    """Define common class variables for round lowercase glyphs"""
    width_ratio = 1

    stroke_x_ratio = 1.01
    stroke_y_ratio = 1.00

    hy_ratio = 1
    hx_ratio = 1
