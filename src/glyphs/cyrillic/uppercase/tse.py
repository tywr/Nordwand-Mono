from glyphs.cyrillic import RightDescenderGlyph
from glyphs.cyrillic.uppercase.dzhe import CyrillicUppercaseDzheGlyph


class CyrillicUppercaseTseGlyph(RightDescenderGlyph, CyrillicUppercaseDzheGlyph):
    """Џ without its middle descender, with one on the right."""

    name = "cyrillic_uppercase_tse"
    unicode = "0x0426"
    offset = 10
    width_ratio = 1.12
    base_kwargs = {"draw_descender": False}
