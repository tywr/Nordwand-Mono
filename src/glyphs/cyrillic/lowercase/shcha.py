from glyphs.cyrillic import RightDescenderGlyph
from glyphs.cyrillic.lowercase.sha import CyrillicLowercaseShaGlyph


class CyrillicLowercaseShchaGlyph(RightDescenderGlyph, CyrillicLowercaseShaGlyph):
    name = "cyrillic_lowercase_shcha"
    unicode = "0x0449"
    offset = 10
    width_ratio = 1.26
    damp_descender = True
