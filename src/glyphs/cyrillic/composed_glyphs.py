from config import FontConfig as fc
from glyphs.accents.acute import Acute
from glyphs.accents.breve import Breve
from glyphs.accents.dieresis import Dieresis
from glyphs.accents.grave import Grave
from glyphs import LigatureGlyph
from glyphs.composed import ComposedGlyph
from glyphs.cyrillic.lowercase.ghe import CyrillicLowercaseGheGlyph
from glyphs.cyrillic.lowercase.i import CyrillicLowercaseIGlyph
from glyphs.cyrillic.lowercase.ka import CyrillicLowercaseKaGlyph
from glyphs.cyrillic.lowercase.lookalikes import (
    CyrillicLowercaseAGlyph,
    CyrillicLowercaseByelorussianUkrainianIGlyph,
    CyrillicLowercaseEsGlyph,
    CyrillicLowercaseIeGlyph,
    CyrillicLowercaseUGlyph,
)
from glyphs.cyrillic.lowercase.ze import CyrillicLowercaseZeGlyph
from glyphs.cyrillic.lowercase.zhe import CyrillicLowercaseZheGlyph
from glyphs.cyrillic.uppercase.ghe import CyrillicUppercaseGheGlyph
from glyphs.cyrillic.uppercase.i import CyrillicUppercaseIGlyph
from glyphs.cyrillic.uppercase.lookalikes import (
    CyrillicUppercaseAGlyph,
    CyrillicUppercaseByelorussianUkrainianIGlyph,
    CyrillicUppercaseEsGlyph,
    CyrillicUppercaseIeGlyph,
    CyrillicUppercaseKaGlyph,
)
from glyphs.cyrillic.uppercase.u import CyrillicUppercaseUGlyph
from glyphs.cyrillic.uppercase.ze import CyrillicUppercaseZeGlyph
from glyphs.cyrillic.uppercase.zhe import CyrillicUppercaseZheGlyph


class CyrillicUppercaseIeGraveGlyph(ComposedGlyph):
    name = "cyrillic_uppercase_ie_grave"
    unicode = "0x0400"
    base_glyph_class = CyrillicUppercaseIeGlyph
    accent_class = Grave
    accent_y = fc.accent_cap


class CyrillicUppercaseIoGlyph(ComposedGlyph):
    name = "cyrillic_uppercase_io"
    unicode = "0x0401"
    base_glyph_class = CyrillicUppercaseIeGlyph
    accent_class = Dieresis
    accent_y = fc.accent_cap


class CyrillicUppercaseGjeGlyph(ComposedGlyph):
    name = "cyrillic_uppercase_gje"
    unicode = "0x0403"
    base_glyph_class = CyrillicUppercaseGheGlyph
    accent_class = Acute
    accent_y = fc.accent_cap


class CyrillicUppercaseYiGlyph(ComposedGlyph):
    name = "cyrillic_uppercase_yi"
    unicode = "0x0407"
    base_glyph_class = CyrillicUppercaseByelorussianUkrainianIGlyph
    accent_class = Dieresis
    accent_y = fc.accent_cap


class CyrillicUppercaseKjeGlyph(ComposedGlyph):
    name = "cyrillic_uppercase_kje"
    unicode = "0x040C"
    base_glyph_class = CyrillicUppercaseKaGlyph
    accent_class = Acute
    accent_y = fc.accent_cap


class CyrillicUppercaseIGraveGlyph(ComposedGlyph):
    name = "cyrillic_uppercase_i_grave"
    unicode = "0x040D"
    base_glyph_class = CyrillicUppercaseIGlyph
    accent_class = Grave
    accent_y = fc.accent_cap


class CyrillicLowercaseIeGraveGlyph(ComposedGlyph):
    name = "cyrillic_lowercase_ie_grave"
    unicode = "0x0450"
    base_glyph_class = CyrillicLowercaseIeGlyph
    accent_class = Grave
    accent_y = fc.accent


class CyrillicLowercaseIoGlyph(ComposedGlyph):
    name = "cyrillic_lowercase_io"
    unicode = "0x0451"
    base_glyph_class = CyrillicLowercaseIeGlyph
    accent_class = Dieresis
    accent_y = fc.accent


class CyrillicLowercaseGjeGlyph(ComposedGlyph):
    name = "cyrillic_lowercase_gje"
    unicode = "0x0453"
    base_glyph_class = CyrillicLowercaseGheGlyph
    accent_class = Acute
    accent_y = fc.accent


class CyrillicLowercaseYiGlyph(ComposedGlyph):
    name = "cyrillic_lowercase_yi"
    unicode = "0x0457"
    base_glyph_class = CyrillicLowercaseByelorussianUkrainianIGlyph
    accent_class = Dieresis
    accent_y = fc.accent


class CyrillicLowercaseKjeGlyph(ComposedGlyph):
    name = "cyrillic_lowercase_kje"
    unicode = "0x045C"
    base_glyph_class = CyrillicLowercaseKaGlyph
    accent_class = Acute
    accent_y = fc.accent


class CyrillicLowercaseIGraveGlyph(ComposedGlyph):
    name = "cyrillic_lowercase_i_grave"
    unicode = "0x045D"
    base_glyph_class = CyrillicLowercaseIGlyph
    accent_class = Grave
    accent_y = fc.accent


class CyrillicUppercaseShortUGlyph(ComposedGlyph):
    name = "cyrillic_uppercase_short_u"
    unicode = "0x040E"
    base_glyph_class = CyrillicUppercaseUGlyph
    accent_class = Breve
    accent_y = fc.accent_cap


class CyrillicUppercaseShortIGlyph(ComposedGlyph):
    name = "cyrillic_uppercase_short_i"
    unicode = "0x0419"
    base_glyph_class = CyrillicUppercaseIGlyph
    accent_class = Breve
    accent_y = fc.accent_cap


class CyrillicLowercaseShortIGlyph(ComposedGlyph):
    name = "cyrillic_lowercase_short_i"
    unicode = "0x0439"
    base_glyph_class = CyrillicLowercaseIGlyph
    accent_class = Breve
    accent_y = fc.accent


class CyrillicLowercaseShortUGlyph(ComposedGlyph):
    name = "cyrillic_lowercase_short_u"
    unicode = "0x045E"
    base_glyph_class = CyrillicLowercaseUGlyph
    accent_class = Breve
    accent_y = fc.accent


class CyrillicUppercaseZheBreveGlyph(ComposedGlyph):
    name = "cyrillic_uppercase_zhe_breve"
    unicode = "0x04C1"
    base_glyph_class = CyrillicUppercaseZheGlyph
    accent_class = Breve
    accent_y = fc.accent_cap


class CyrillicLowercaseZheBreveGlyph(ComposedGlyph):
    name = "cyrillic_lowercase_zhe_breve"
    unicode = "0x04C2"
    base_glyph_class = CyrillicLowercaseZheGlyph
    accent_class = Breve
    accent_y = fc.accent


class CyrillicUppercaseABreveGlyph(ComposedGlyph):
    name = "cyrillic_uppercase_a_breve"
    unicode = "0x04D0"
    base_glyph_class = CyrillicUppercaseAGlyph
    accent_class = Breve
    accent_y = fc.accent_cap


class CyrillicLowercaseABreveGlyph(ComposedGlyph):
    name = "cyrillic_lowercase_a_breve"
    unicode = "0x04D1"
    base_glyph_class = CyrillicLowercaseAGlyph
    accent_class = Breve
    accent_y = fc.accent


class CyrillicUppercaseIeBreveGlyph(ComposedGlyph):
    name = "cyrillic_uppercase_ie_breve"
    unicode = "0x04D6"
    base_glyph_class = CyrillicUppercaseIeGlyph
    accent_class = Breve
    accent_y = fc.accent_cap


class CyrillicLowercaseIeBreveGlyph(ComposedGlyph):
    name = "cyrillic_lowercase_ie_breve"
    unicode = "0x04D7"
    base_glyph_class = CyrillicLowercaseIeGlyph
    accent_class = Breve
    accent_y = fc.accent


class CyrillicUppercaseZeAcuteGlyph(ComposedGlyph, LigatureGlyph):
    name = "cyrillic_uppercase_ze_acute"
    unicode = None
    components = ["cyrillic_uppercase_ze", "combining_acute"]
    feature_tags = ("ccmp",)
    base_glyph_class = CyrillicUppercaseZeGlyph
    accent_class = Acute
    accent_y = fc.accent_cap


class CyrillicLowercaseZeAcuteGlyph(ComposedGlyph, LigatureGlyph):
    name = "cyrillic_lowercase_ze_acute"
    unicode = None
    components = ["cyrillic_lowercase_ze", "combining_acute"]
    feature_tags = ("ccmp",)
    base_glyph_class = CyrillicLowercaseZeGlyph
    accent_class = Acute
    accent_y = fc.accent


class CyrillicUppercaseEsAcuteGlyph(ComposedGlyph, LigatureGlyph):
    name = "cyrillic_uppercase_es_acute"
    unicode = None
    components = ["cyrillic_uppercase_es", "combining_acute"]
    feature_tags = ("ccmp",)
    base_glyph_class = CyrillicUppercaseEsGlyph
    accent_class = Acute
    accent_y = fc.accent_cap


class CyrillicLowercaseEsAcuteGlyph(ComposedGlyph, LigatureGlyph):
    name = "cyrillic_lowercase_es_acute"
    unicode = None
    components = ["cyrillic_lowercase_es", "combining_acute"]
    feature_tags = ("ccmp",)
    base_glyph_class = CyrillicLowercaseEsGlyph
    accent_class = Acute
    accent_y = fc.accent
