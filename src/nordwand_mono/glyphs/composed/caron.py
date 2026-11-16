"""Composed glyphs with the caron."""

from nordwand_mono.config import FontConfig as fc
from nordwand_mono.glyphs.composed import ComposedGlyph
from nordwand_mono.glyphs.lowercase.round.e import LowercaseEGlyph
from nordwand_mono.glyphs.lowercase.round.c import LowercaseCGlyph
from nordwand_mono.glyphs.lowercase.square.n import LowercaseNGlyph
from nordwand_mono.glyphs.lowercase.s import LowercaseSGlyph
from nordwand_mono.glyphs.lowercase.z import LowercaseZGlyph
from nordwand_mono.glyphs.lowercase.square.r import LowercaseRGlyph
from nordwand_mono.glyphs.uppercase.e import UppercaseEGlyph
from nordwand_mono.glyphs.uppercase.stem_diagonal.n import UppercaseNGlyph
from nordwand_mono.glyphs.uppercase.round.c import UppercaseCGlyph
from nordwand_mono.glyphs.uppercase.s import UppercaseSGlyph
from nordwand_mono.glyphs.uppercase.z import UppercaseZGlyph
from nordwand_mono.glyphs.uppercase.t import UppercaseTGlyph
from nordwand_mono.glyphs.uppercase.bowl.r import UppercaseRGlyph
from nordwand_mono.glyphs.uppercase.bowl.d import UppercaseDGlyph
from nordwand_mono.glyphs.accents.caron import Caron
from nordwand_mono.glyphs.latin.lowercase.ezh import LatinLowercaseEzhGlyph
from nordwand_mono.glyphs.latin.uppercase.ezh import LatinUppercaseEzhGlyph
from nordwand_mono.glyphs.composed.circumflex import LowercaseHCircumflexGlyph
from nordwand_mono.glyphs.uppercase.h import UppercaseHGlyph
from nordwand_mono.glyphs.uppercase.diagonal.a import UppercaseAGlyph
from nordwand_mono.glyphs.lowercase.a import LowercaseAGlyph
from nordwand_mono.glyphs.uppercase.round.g import UppercaseGGlyph
from nordwand_mono.glyphs.lowercase.single_story.g import LowercaseGGlyph
from nordwand_mono.glyphs.lowercase.dotted.i import LowercaseIGlyph
from nordwand_mono.glyphs.lowercase.round.o import LowercaseOGlyph
from nordwand_mono.glyphs.lowercase.square.u import LowercaseUGlyph
from nordwand_mono.glyphs.uppercase.i import UppercaseIGlyph
from nordwand_mono.glyphs.uppercase.round.o import UppercaseOGlyph
from nordwand_mono.glyphs.uppercase.u import UppercaseUGlyph

_lc_accent = fc.accent
_uc_accent = fc.accent_cap


class LowercaseSCaronGlyph(ComposedGlyph):
    name = "lowercase_scaron"
    unicode = "0x161"
    base_glyph_class = LowercaseSGlyph
    accent_class = Caron
    accent_y = _lc_accent


class LowercaseZCaronGlyph(ComposedGlyph):
    name = "lowercase_zcaron"
    unicode = "0x17E"
    base_glyph_class = LowercaseZGlyph
    accent_class = Caron
    accent_y = _lc_accent


class UppercaseSCaronGlyph(ComposedGlyph):
    name = "uppercase_scaron"
    unicode = "0x160"
    base_glyph_class = UppercaseSGlyph
    accent_class = Caron
    accent_y = _uc_accent


class UppercaseZCaronGlyph(ComposedGlyph):
    name = "uppercase_zcaron"
    unicode = "0x17D"
    base_glyph_class = UppercaseZGlyph
    accent_class = Caron
    accent_y = _uc_accent


class LowercaseCCaronGlyph(ComposedGlyph):
    name = "lowercase_ccaron"
    unicode = "0x10D"
    base_glyph_class = LowercaseCGlyph
    accent_class = Caron
    accent_y = _lc_accent


class UppercaseCCaronGlyph(ComposedGlyph):
    name = "uppercase_ccaron"
    unicode = "0x10C"
    base_glyph_class = UppercaseCGlyph
    accent_class = Caron
    accent_y = _uc_accent


class UppercaseDCaronGlyph(ComposedGlyph):
    name = "uppercase_dcaron"
    unicode = "0x10E"
    base_glyph_class = UppercaseDGlyph
    accent_class = Caron
    accent_y = _uc_accent


class LowercaseECaronGlyph(ComposedGlyph):
    name = "lowercase_ecaron"
    unicode = "0x11B"
    base_glyph_class = LowercaseEGlyph
    accent_class = Caron
    accent_y = _lc_accent


class UppercaseECaronGlyph(ComposedGlyph):
    name = "uppercase_ecaron"
    unicode = "0x11A"
    base_glyph_class = UppercaseEGlyph
    accent_class = Caron
    accent_y = _uc_accent


class LowercaseNCaronGlyph(ComposedGlyph):
    name = "lowercase_ncaron"
    unicode = "0x148"
    base_glyph_class = LowercaseNGlyph
    accent_class = Caron
    accent_y = _lc_accent


class UppercaseNCaronGlyph(ComposedGlyph):
    name = "uppercase_ncaron"
    unicode = "0x147"
    base_glyph_class = UppercaseNGlyph
    accent_class = Caron
    accent_y = _uc_accent


class LowercaseRCaronGlyph(ComposedGlyph):
    name = "lowercase_rcaron"
    unicode = "0x159"
    base_glyph_class = LowercaseRGlyph
    accent_class = Caron
    accent_y = _lc_accent


class UppercaseRCaronGlyph(ComposedGlyph):
    name = "uppercase_rcaron"
    unicode = "0x158"
    base_glyph_class = UppercaseRGlyph
    accent_class = Caron
    accent_y = _uc_accent


class UppercaseTCaronGlyph(ComposedGlyph):
    name = "uppercase_tcaron"
    unicode = "0x164"
    base_glyph_class = UppercaseTGlyph
    accent_class = Caron
    accent_y = _uc_accent


class UppercaseACaronGlyph(ComposedGlyph):
    name = "uppercase_acaron"
    unicode = "0x1CD"
    base_glyph_class = UppercaseAGlyph
    accent_class = Caron
    accent_y = _uc_accent


class LowercaseACaronGlyph(ComposedGlyph):
    name = "lowercase_acaron"
    unicode = "0x1CE"
    base_glyph_class = LowercaseAGlyph
    accent_class = Caron
    accent_y = _lc_accent


class LowercaseGCaronGlyph(ComposedGlyph):
    name = "lowercase_gcaron"
    unicode = "0x1E7"
    base_glyph_class = LowercaseGGlyph
    accent_class = Caron
    accent_y = _lc_accent


class UppercaseGCaronGlyph(ComposedGlyph):
    name = "uppercase_gcaron"
    unicode = "0x1E6"
    base_glyph_class = UppercaseGGlyph
    accent_class = Caron
    accent_y = _uc_accent


class LowercaseICaronGlyph(ComposedGlyph):
    name = "lowercase_icaron"
    unicode = "0x1D0"
    base_glyph_class = LowercaseIGlyph
    accent_class = Caron
    accent_y = _lc_accent


class LowercaseOCaronGlyph(ComposedGlyph):
    name = "lowercase_ocaron"
    unicode = "0x1D2"
    base_glyph_class = LowercaseOGlyph
    accent_class = Caron
    accent_y = _lc_accent


class LowercaseUCaronGlyph(ComposedGlyph):
    name = "lowercase_ucaron"
    unicode = "0x1D4"
    base_glyph_class = LowercaseUGlyph
    accent_class = Caron
    accent_y = _lc_accent


class UppercaseICaronGlyph(ComposedGlyph):
    name = "uppercase_icaron"
    unicode = "0x1CF"
    base_glyph_class = UppercaseIGlyph
    accent_class = Caron
    accent_y = _uc_accent


class UppercaseOCaronGlyph(ComposedGlyph):
    name = "uppercase_ocaron"
    unicode = "0x1D1"
    base_glyph_class = UppercaseOGlyph
    accent_class = Caron
    accent_y = _uc_accent


class UppercaseUCaronGlyph(ComposedGlyph):
    name = "uppercase_ucaron"
    unicode = "0x1D3"
    base_glyph_class = UppercaseUGlyph
    accent_class = Caron
    accent_y = _uc_accent


class LowercaseHCaronGlyph(LowercaseHCircumflexGlyph):
    """h with the caron above its ascender, placed like the circumflex of ĥ."""

    name = "lowercase_hcaron"
    unicode = "0x21F"
    accent_class = Caron


class UppercaseHCaronGlyph(ComposedGlyph):
    name = "uppercase_hcaron"
    unicode = "0x21E"
    base_glyph_class = UppercaseHGlyph
    accent_class = Caron
    accent_y = _uc_accent


class LatinLowercaseEzhCaronGlyph(ComposedGlyph):
    name = "latin_lowercase_ezh_caron"
    unicode = "0x1EF"
    base_glyph_class = LatinLowercaseEzhGlyph
    accent_class = Caron
    accent_y = _lc_accent


class LatinUppercaseEzhCaronGlyph(ComposedGlyph):
    name = "latin_uppercase_ezh_caron"
    unicode = "0x1EE"
    base_glyph_class = LatinUppercaseEzhGlyph
    accent_class = Caron
    accent_y = _uc_accent
