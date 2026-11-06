"""Letters with a descender on the right of their base (Җ Қ Ң)."""

from glyphs.cyrillic import RightDescenderGlyph
from glyphs.cyrillic.lowercase.en import CyrillicLowercaseEnGlyph
from glyphs.cyrillic.lowercase.ka import CyrillicLowercaseKaGlyph
from glyphs.cyrillic.lowercase.zhe import CyrillicLowercaseZheGlyph
from glyphs.cyrillic.uppercase.lookalikes import (
    CyrillicUppercaseEnGlyph,
    CyrillicUppercaseKaGlyph,
)
from glyphs.cyrillic.uppercase.zhe import CyrillicUppercaseZheGlyph


class CyrillicUppercaseZheDescenderGlyph(RightDescenderGlyph, CyrillicUppercaseZheGlyph):
    name = "cyrillic_uppercase_zhe_descender"
    unicode = "0x0496"
    offset = 0
    width_ratio = 1.3
    right_offset = 0.1
    damp_descender = True


class CyrillicLowercaseZheDescenderGlyph(RightDescenderGlyph, CyrillicLowercaseZheGlyph):
    name = "cyrillic_lowercase_zhe_descender"
    unicode = "0x0497"
    offset = 0
    width_ratio = 1.3
    right_offset = 0.1
    damp_descender = True


class CyrillicUppercaseKaDescenderGlyph(RightDescenderGlyph, CyrillicUppercaseKaGlyph):
    name = "cyrillic_uppercase_ka_descender"
    unicode = "0x049A"
    offset = 30
    width_ratio = 1.12


class CyrillicLowercaseKaDescenderGlyph(RightDescenderGlyph, CyrillicLowercaseKaGlyph):
    name = "cyrillic_lowercase_ka_descender"
    unicode = "0x049B"
    offset = 20
    width_ratio = 1.1


class CyrillicUppercaseEnDescenderGlyph(RightDescenderGlyph, CyrillicUppercaseEnGlyph):
    name = "cyrillic_uppercase_en_descender"
    unicode = "0x04A2"
    offset = 10
    width_ratio = 1.12


class CyrillicLowercaseEnDescenderGlyph(RightDescenderGlyph, CyrillicLowercaseEnGlyph):
    name = "cyrillic_lowercase_en_descender"
    unicode = "0x04A3"
    offset = 10
    width_ratio = 1.12
