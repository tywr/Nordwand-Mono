from abc import ABC
from nordwand_mono.glyphs.uppercase import UppercaseGlyph


class CyrillicUppercaseGlyph(UppercaseGlyph, ABC):
    """Define common class variables for all uppercase glyphs"""

    descent_ratio = 0.75
