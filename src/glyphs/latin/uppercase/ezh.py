from glyphs.latin.lowercase.ezh import LatinLowercaseEzhGlyph


class LatinUppercaseEzhGlyph(LatinLowercaseEzhGlyph):
    """The ezh drawn at the cap height, sitting on the baseline (Ʒ)."""

    name = "latin_uppercase_ezh"
    unicode = "0x1B7"
    height = "cap"
    uppercase = True
    descender = False
    stroke_y_ratio = 1.03
