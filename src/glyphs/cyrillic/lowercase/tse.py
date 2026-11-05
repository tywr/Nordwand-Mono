from glyphs.cyrillic import RightDescenderGlyph
from glyphs.cyrillic.lowercase.dzhe import CyrillicLowercaseDzheGlyph


class CyrillicLowercaseTseGlyph(RightDescenderGlyph, CyrillicLowercaseDzheGlyph):
    """џ without its middle descender, with one on the right."""

    name = "cyrillic_lowercase_tse"
    unicode = "0x0446"
    offset = 10
    width_ratio = 1.12
    base_kwargs = {"draw_descender": False}
