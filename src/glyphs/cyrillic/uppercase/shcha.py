from glyphs.cyrillic import RightDescenderGlyph
from glyphs.cyrillic.uppercase.sha import CyrillicUppercaseShaGlyph


class CyrillicUppercaseShchaGlyph(RightDescenderGlyph, CyrillicUppercaseShaGlyph):
    name = "cyrillic_uppercase_shcha"
    unicode = "0x0429"
    offset = 10
    width_ratio = 1.26
    damp_descender = True
