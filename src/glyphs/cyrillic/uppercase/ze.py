from glyphs.cyrillic.uppercase import CyrillicUppercaseGlyph
from glyphs.latin.open_e import OpenEGlyph


class CyrillicUppercaseZeGlyph(CyrillicUppercaseGlyph, OpenEGlyph):
    """The number 3, with the handles of the capitals"""

    name = "cyrillic_uppercase_ze"
    unicode = "0x0417"
    mid_ratio = 0.52
    width_ratio = 1.08
    mid_length = 0.64
    opening1 = 0.29
    opening2 = 0.74
    cap = True
