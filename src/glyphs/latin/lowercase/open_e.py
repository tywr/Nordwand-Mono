from glyphs.latin.open_e import OpenEGlyph


class LowercaseOpenEGlyph(OpenEGlyph):
    """Drawn like the greek epsilon: the cyrillic ze mirrored horizontally"""

    name = "lowercase_open_e"
    unicode = "0x25B"
    mirrored = True
