from glyphs.lowercase.a import LowercaseAGlyph
from glyphs.lowercase.single_story.a_2 import LowercaseA2Glyph
from glyphs.lowercase.dotted.i import LowercaseIGlyph
from glyphs.lowercase.dotted.i_2 import LowercaseI2Glyph
from glyphs.lowercase.dotted.j import LowercaseJGlyph
from glyphs.lowercase.round.e import LowercaseEGlyph
from glyphs.lowercase.round.e_2 import LowercaseE2Glyph
from glyphs.lowercase.round.o import LowercaseOGlyph
from glyphs.lowercase.s import LowercaseSGlyph
from glyphs.lowercase.single_story.p import LowercasePGlyph
from glyphs.lowercase.y import LowercaseYGlyph
from glyphs.lowercase.x import LowercaseXGlyph
from glyphs.lowercase.x_2 import LowercaseX2Glyph
from glyphs.lowercase.round.c import LowercaseCGlyph


class CyrillicLowercaseAGlyph(LowercaseAGlyph):
    name = "cyrillic_lowercase_a"
    unicode = "0x0430"


class CyrillicLowercaseAItalicGlyph(LowercaseA2Glyph):
    name = "cyrillic_lowercase_a_italic"
    unicode = "0x0430"


class CyrillicLowercaseIeGlyph(LowercaseEGlyph):
    name = "cyrillic_lowercase_ie"
    unicode = "0x0435"


class CyrillicLowercaseIeItalicGlyph(LowercaseE2Glyph):
    name = "cyrillic_lowercase_ie_italic"
    unicode = "0x0435"


class CyrillicLowercaseOGlyph(LowercaseOGlyph):
    name = "cyrillic_lowercase_o"
    unicode = "0x043E"


class CyrillicLowercaseErGlyph(LowercasePGlyph):
    name = "cyrillic_lowercase_er"
    unicode = "0x0440"


class CyrillicLowercaseEsGlyph(LowercaseCGlyph):
    name = "cyrillic_lowercase_es"
    unicode = "0x0441"


class CyrillicLowercaseHaGlyph(LowercaseXGlyph):
    name = "cyrillic_lowercase_ha"
    unicode = "0x0445"


class CyrillicLowercaseHaItalicGlyph(LowercaseX2Glyph):
    name = "cyrillic_lowercase_ha_italic"
    unicode = "0x0445"


class CyrillicLowercaseJeGlyph(LowercaseJGlyph):
    name = "cyrillic_lowercase_je"
    unicode = "0x0458"


class CyrillicLowercaseByelorussianUkrainianIGlyph(LowercaseIGlyph):
    name = "cyrillic_lowercase_byelorussian_ukrainian_i"
    unicode = "0x0456"


class CyrillicLowercaseByelorussianUkrainianIItalicGlyph(LowercaseI2Glyph):
    name = "cyrillic_lowercase_byelorussian_ukrainian_i_italic"
    unicode = "0x0456"


class CyrillicLowercaseDzeGlyph(LowercaseSGlyph):
    name = "cyrillic_lowercase_dze"
    unicode = "0x0455"


class CyrillicLowercaseUGlyph(LowercaseYGlyph):
    name = "cyrillic_lowercase_u"
    unicode = "0x0443"
