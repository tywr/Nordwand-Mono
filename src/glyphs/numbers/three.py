from glyphs.numbers import NumberGlyph
from glyphs.latin.open_e import OpenEGlyph


class ThreeGlyph(NumberGlyph, OpenEGlyph):
    name = "three"
    unicode = "0x33"
    offset = -4
    loop_width_ratio = 0.92
    mid_ratio = 0.52
    taper = 1
    hx_ratio = 0.9
    hy_ratio = 0.9
    width_ratio = 1.08
    mid_length = 0.64
    opening1 = 0.29
    opening2 = 0.74
    number = True
