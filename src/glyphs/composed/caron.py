"""Composed glyphs with the caron."""

from config import FontConfig as fc
from glyphs.composed import ComposedGlyph
from glyphs.lowercase.round.e import LowercaseEGlyph
from glyphs.lowercase.round.c import LowercaseCGlyph
from glyphs.lowercase.square.n import LowercaseNGlyph
from glyphs.lowercase.s import LowercaseSGlyph
from glyphs.lowercase.z import LowercaseZGlyph
from glyphs.lowercase.square.r import LowercaseRGlyph
from glyphs.uppercase.e import UppercaseEGlyph
from glyphs.uppercase.n import UppercaseNGlyph
from glyphs.uppercase.c import UppercaseCGlyph
from glyphs.uppercase.s import UppercaseSGlyph
from glyphs.uppercase.z import UppercaseZGlyph
from glyphs.uppercase.t import UppercaseTGlyph
from glyphs.uppercase.r import UppercaseRGlyph
from glyphs.uppercase.d import UppercaseDGlyph
from glyphs.accents.caron import Caron
from glyphs.composed.circumflex import LowercaseHCircumflexGlyph
from glyphs.uppercase.h import UppercaseHGlyph
from glyphs.uppercase.a import UppercaseAGlyph
from glyphs.lowercase.a import LowercaseAGlyph
from glyphs.uppercase.g import UppercaseGGlyph
from glyphs.lowercase.single_story.g import LowercaseGGlyph
from glyphs.lowercase.dotted.i import LowercaseIGlyph
from glyphs.lowercase.round.o import LowercaseOGlyph
from glyphs.lowercase.square.u import LowercaseUGlyph
from glyphs.uppercase.i import UppercaseIGlyph
from glyphs.uppercase.o import UppercaseOGlyph
from glyphs.uppercase.u import UppercaseUGlyph

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
