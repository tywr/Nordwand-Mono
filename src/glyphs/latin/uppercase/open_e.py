from glyphs.uppercase import UppercaseGlyph
from glyphs.latin.open_e import OpenEGlyph


class UppercaseOpenEGlyph(UppercaseGlyph, OpenEGlyph):
    """The cyrillic uppercase ze mirrored horizontally, as a capital epsilon"""

    name = "uppercase_open_e"
    unicode = "0x190"
    mid_ratio = 0.52
    width_ratio = 1.08
    mid_length = 0.64
    opening1 = 0.29
    opening2 = 0.74
    cap = True
    mirrored = True
