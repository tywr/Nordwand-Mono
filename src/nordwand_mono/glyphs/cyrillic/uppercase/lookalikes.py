from nordwand_mono.glyphs.uppercase.diagonal.a import UppercaseAGlyph
from nordwand_mono.glyphs.uppercase.bowl.b import UppercaseBGlyph
from nordwand_mono.glyphs.uppercase.e import UppercaseEGlyph
from nordwand_mono.glyphs.uppercase.i import UppercaseIGlyph
from nordwand_mono.glyphs.uppercase.j import UppercaseJGlyph
from nordwand_mono.glyphs.uppercase.round.o import UppercaseOGlyph
from nordwand_mono.glyphs.uppercase.bowl.p import UppercasePGlyph
from nordwand_mono.glyphs.uppercase.s import UppercaseSGlyph
from nordwand_mono.glyphs.uppercase.t import UppercaseTGlyph
from nordwand_mono.glyphs.uppercase.diagonal.x import UppercaseXGlyph
from nordwand_mono.glyphs.uppercase.k import UppercaseKGlyph
from nordwand_mono.glyphs.uppercase.stem_diagonal.m import UppercaseMGlyph
from nordwand_mono.glyphs.uppercase.h import UppercaseHGlyph
from nordwand_mono.glyphs.uppercase.round.c import UppercaseCGlyph

from nordwand_mono.glyphs.latin.uppercase.schwa import UppercaseSchwaGlyph
from nordwand_mono.glyphs.uppercase.diagonal.y import UppercaseYGlyph

class CyrillicUppercaseAGlyph(UppercaseAGlyph):
    name = "cyrillic_uppercase_a"
    unicode = "0x0410"


class CyrillicUppercaseVeGlyph(UppercaseBGlyph):
    name = "cyrillic_uppercase_ve"
    unicode = "0x0412"

class CyrillicUppercaseEsGlyph(UppercaseCGlyph):
    name = "cyrillic_uppercase_es"
    unicode = "0x0421"


class CyrillicUppercaseIeGlyph(UppercaseEGlyph):
    name = "cyrillic_uppercase_ie"
    unicode = "0x0415"


class CyrillicUppercaseKaGlyph(UppercaseKGlyph):
    name = "cyrillic_uppercase_ka"
    unicode = "0x041A"


class CyrillicUppercaseEmGlyph(UppercaseMGlyph):
    name = "cyrillic_uppercase_em"
    unicode = "0x041C"


class CyrillicUppercaseEnGlyph(UppercaseHGlyph):
    name = "cyrillic_uppercase_en"
    unicode = "0x041D"


class CyrillicUppercaseOGlyph(UppercaseOGlyph):
    name = "cyrillic_uppercase_o"
    unicode = "0x041E"


class CyrillicUppercaseErGlyph(UppercasePGlyph):
    name = "cyrillic_uppercase_er"
    unicode = "0x0420"


class CyrillicUppercaseTeGlyph(UppercaseTGlyph):
    name = "cyrillic_uppercase_te"
    unicode = "0x0422"


class CyrillicUppercaseHaGlyph(UppercaseXGlyph):
    name = "cyrillic_uppercase_ha"
    unicode = "0x0425"


class CyrillicUppercaseJeGlyph(UppercaseJGlyph):
    name = "cyrillic_uppercase_je"
    unicode = "0x0408"


class CyrillicUppercaseByelorussianUkrainianIGlyph(UppercaseIGlyph):
    name = "cyrillic_uppercase_byelorussian_ukrainian_i"
    unicode = "0x0406"


class CyrillicUppercaseDzeGlyph(UppercaseSGlyph):
    name = "cyrillic_uppercase_dze"
    unicode = "0x0405"


class CyrillicUppercaseSchwaGlyph(UppercaseSchwaGlyph):
    name = "cyrillic_uppercase_schwa"
    unicode = "0x04D8"


class CyrillicUppercaseStraightUGlyph(UppercaseYGlyph):
    name = "cyrillic_uppercase_straight_u"
    unicode = "0x04AE"
