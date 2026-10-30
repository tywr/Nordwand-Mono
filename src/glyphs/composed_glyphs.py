"""Accented / composed glyphs.

Each class pairs a base glyph with an accent mark. The accent_y controls
the vertical anchor. For lowercase letters with ascenders or dots (i, j),
draw_base is called to omit the dot.
"""

from config import FontConfig as fc
from glyphs.composed import ComposedGlyph

from glyphs.lowercase.a import LowercaseAGlyph
from glyphs.lowercase.round.e import LowercaseEGlyph
from glyphs.lowercase.round.o import LowercaseOGlyph
from glyphs.lowercase.round.c import LowercaseCGlyph
from glyphs.lowercase.square.u import LowercaseUGlyph
from glyphs.lowercase.square.n import LowercaseNGlyph
from glyphs.lowercase.dotted.i import LowercaseIGlyph
from glyphs.lowercase.dotted.i_2 import LowercaseI2Glyph
from glyphs.lowercase.y import LowercaseYGlyph
from glyphs.lowercase.w import LowercaseWGlyph
from glyphs.lowercase.s import LowercaseSGlyph
from glyphs.lowercase.single_story.g import LowercaseGGlyph
from glyphs.lowercase.l import LowercaseLGlyph
from glyphs.lowercase.z import LowercaseZGlyph
from glyphs.lowercase.t import LowercaseTGlyph
from glyphs.lowercase.k import LowercaseKGlyph
from glyphs.lowercase.r import LowercaseRGlyph

from glyphs.uppercase.a import UppercaseAGlyph
from glyphs.uppercase.e import UppercaseEGlyph
from glyphs.uppercase.i import UppercaseIGlyph
from glyphs.uppercase.o import UppercaseOGlyph
from glyphs.uppercase.u import UppercaseUGlyph
from glyphs.uppercase.n import UppercaseNGlyph
from glyphs.uppercase.c import UppercaseCGlyph
from glyphs.uppercase.y import UppercaseYGlyph
from glyphs.uppercase.w import UppercaseWGlyph
from glyphs.uppercase.s import UppercaseSGlyph
from glyphs.uppercase.g import UppercaseGGlyph
from glyphs.uppercase.l import UppercaseLGlyph
from glyphs.uppercase.z import UppercaseZGlyph
from glyphs.uppercase.t import UppercaseTGlyph
from glyphs.uppercase.k import UppercaseKGlyph
from glyphs.uppercase.r import UppercaseRGlyph
from glyphs.uppercase.h import UppercaseHGlyph
from glyphs.lowercase.square.h import LowercaseHGlyph
from glyphs.uppercase.d import UppercaseDGlyph
from glyphs.lowercase.single_story.d import LowercaseDGlyph
from glyphs.latin.uppercase.eth import UppercaseEthGlyph
from glyphs.lowercase.dotted.j import LowercaseJGlyph
from glyphs.uppercase.j import UppercaseJGlyph

from glyphs.accents.acute import Acute
from glyphs.accents.grave import Grave
from glyphs.accents.circumflex import Circumflex
from glyphs.accents.dieresis import Dieresis
from glyphs.accents.tilde import Tilde
from glyphs.accents.caron import Caron
from glyphs.accents.caron_vertical import CaronVertical
from glyphs.accents.double_acute import DoubleAcute
from glyphs.accents.ring import Ring
from glyphs.accents.cedilla import Cedilla
from glyphs.accents.macron import Macron
from glyphs.accents.breve import Breve
from glyphs.accents.dot import DotAbove
from glyphs.accents.ogonek import Ogonek
from glyphs.accents.stroke import Stroke, UppercaseStroke
from glyphs.accents.comma_below import CommaBelow
import pathops
from draw.rect import draw_rect
from draw.square_corner import draw_square_corner

# Heights for accent positioning
_lc_accent = fc.accent
_uc_accent = fc.accent_cap
_cedilla_y = 0


# ── Lowercase with acute ─────────────────────────────────────────────


class LowercaseAAcuteGlyph(ComposedGlyph):
    name = "lowercase_aacute"
    unicode = "0xE1"
    base_glyph_class = LowercaseAGlyph
    accent_class = Acute
    accent_y = _lc_accent


class LowercaseEAcuteGlyph(ComposedGlyph):
    name = "lowercase_eacute"
    unicode = "0xE9"
    base_glyph_class = LowercaseEGlyph
    accent_class = Acute
    accent_y = _lc_accent


class LowercaseIAcuteGlyph(ComposedGlyph):
    name = "lowercase_iacute"
    unicode = "0xED"
    base_glyph_class = LowercaseIGlyph
    accent_class = Acute
    accent_y = _lc_accent


class LowercaseOAcuteGlyph(ComposedGlyph):
    name = "lowercase_oacute"
    unicode = "0xF3"
    base_glyph_class = LowercaseOGlyph
    accent_class = Acute
    accent_y = _lc_accent


class LowercaseUAcuteGlyph(ComposedGlyph):
    name = "lowercase_uacute"
    unicode = "0xFA"
    base_glyph_class = LowercaseUGlyph
    accent_class = Acute
    accent_y = _lc_accent


class LowercaseYAcuteGlyph(ComposedGlyph):
    name = "lowercase_yacute"
    unicode = "0xFD"
    base_glyph_class = LowercaseYGlyph
    accent_class = Acute
    accent_y = _lc_accent


# ── Lowercase with grave ─────────────────────────────────────────────


class LowercaseAGraveGlyph(ComposedGlyph):
    name = "lowercase_agrave"
    unicode = "0xE0"
    base_glyph_class = LowercaseAGlyph
    accent_class = Grave
    accent_y = _lc_accent


class LowercaseEGraveGlyph(ComposedGlyph):
    name = "lowercase_egrave"
    unicode = "0xE8"
    base_glyph_class = LowercaseEGlyph
    accent_class = Grave
    accent_y = _lc_accent


class LowercaseIGraveGlyph(ComposedGlyph):
    name = "lowercase_igrave"
    unicode = "0xEC"
    base_glyph_class = LowercaseIGlyph
    accent_class = Grave
    accent_y = _lc_accent


class LowercaseOGraveGlyph(ComposedGlyph):
    name = "lowercase_ograve"
    unicode = "0xF2"
    base_glyph_class = LowercaseOGlyph
    accent_class = Grave
    accent_y = _lc_accent


class LowercaseUGraveGlyph(ComposedGlyph):
    name = "lowercase_ugrave"
    unicode = "0xF9"
    base_glyph_class = LowercaseUGlyph
    accent_class = Grave
    accent_y = _lc_accent


# ── Lowercase with circumflex ────────────────────────────────────────


class LowercaseACircumflexGlyph(ComposedGlyph):
    name = "lowercase_acircumflex"
    unicode = "0xE2"
    base_glyph_class = LowercaseAGlyph
    accent_class = Circumflex
    accent_y = _lc_accent


class LowercaseECircumflexGlyph(ComposedGlyph):
    name = "lowercase_ecircumflex"
    unicode = "0xEA"
    base_glyph_class = LowercaseEGlyph
    accent_class = Circumflex
    accent_y = _lc_accent


class LowercaseICircumflexGlyph(ComposedGlyph):
    name = "lowercase_icircumflex"
    unicode = "0xEE"
    base_glyph_class = LowercaseIGlyph
    accent_class = Circumflex
    accent_y = _lc_accent


class LowercaseOCircumflexGlyph(ComposedGlyph):
    name = "lowercase_ocircumflex"
    unicode = "0xF4"
    base_glyph_class = LowercaseOGlyph
    accent_class = Circumflex
    accent_y = _lc_accent


class LowercaseUCircumflexGlyph(ComposedGlyph):
    name = "lowercase_ucircumflex"
    unicode = "0xFB"
    base_glyph_class = LowercaseUGlyph
    accent_class = Circumflex
    accent_y = _lc_accent


# ── Lowercase with dieresis ──────────────────────────────────────────


class LowercaseADieresisGlyph(ComposedGlyph):
    name = "lowercase_adieresis"
    unicode = "0xE4"
    base_glyph_class = LowercaseAGlyph
    accent_class = Dieresis
    accent_y = _lc_accent


class LowercaseEDieresisGlyph(ComposedGlyph):
    name = "lowercase_edieresis"
    unicode = "0xEB"
    base_glyph_class = LowercaseEGlyph
    accent_class = Dieresis
    accent_y = _lc_accent


class LowercaseIDieresisGlyph(ComposedGlyph):
    name = "lowercase_idieresis"
    unicode = "0xEF"
    base_glyph_class = LowercaseIGlyph
    accent_class = Dieresis
    accent_y = _lc_accent


class LowercaseODieresisGlyph(ComposedGlyph):
    name = "lowercase_odieresis"
    unicode = "0xF6"
    base_glyph_class = LowercaseOGlyph
    accent_class = Dieresis
    accent_y = _lc_accent


class LowercaseUDieresisGlyph(ComposedGlyph):
    name = "lowercase_udieresis"
    unicode = "0xFC"
    base_glyph_class = LowercaseUGlyph
    accent_class = Dieresis
    accent_y = _lc_accent


class LowercaseYDieresisGlyph(ComposedGlyph):
    name = "lowercase_ydieresis"
    unicode = "0xFF"
    base_glyph_class = LowercaseYGlyph
    accent_class = Dieresis
    accent_y = _lc_accent


# ── Lowercase with macron (romaji long vowels) ───────────────────────


class LowercaseAMacronGlyph(ComposedGlyph):
    name = "lowercase_amacron"
    unicode = "0x101"
    base_glyph_class = LowercaseAGlyph
    accent_class = Macron
    accent_y = _lc_accent


class LowercaseEMacronGlyph(ComposedGlyph):
    name = "lowercase_emacron"
    unicode = "0x113"
    base_glyph_class = LowercaseEGlyph
    accent_class = Macron
    accent_y = _lc_accent


class LowercaseIMacronGlyph(ComposedGlyph):
    name = "lowercase_imacron"
    unicode = "0x12B"
    base_glyph_class = LowercaseIGlyph
    accent_class = Macron
    accent_y = _lc_accent


class LowercaseOMacronGlyph(ComposedGlyph):
    name = "lowercase_omacron"
    unicode = "0x14D"
    base_glyph_class = LowercaseOGlyph
    accent_class = Macron
    accent_y = _lc_accent


class LowercaseUMacronGlyph(ComposedGlyph):
    name = "lowercase_umacron"
    unicode = "0x16B"
    base_glyph_class = LowercaseUGlyph
    accent_class = Macron
    accent_y = _lc_accent


# ── Lowercase with tilde ─────────────────────────────────────────────


class LowercaseATildeGlyph(ComposedGlyph):
    name = "lowercase_atilde"
    unicode = "0xE3"
    base_glyph_class = LowercaseAGlyph
    accent_class = Tilde
    accent_y = _lc_accent


class LowercaseNTildeGlyph(ComposedGlyph):
    name = "lowercase_ntilde"
    unicode = "0xF1"
    base_glyph_class = LowercaseNGlyph
    accent_class = Tilde
    accent_y = _lc_accent


class LowercaseOTildeGlyph(ComposedGlyph):
    name = "lowercase_otilde"
    unicode = "0xF5"
    base_glyph_class = LowercaseOGlyph
    accent_class = Tilde
    accent_y = _lc_accent


# ── Lowercase with ring ──────────────────────────────────────────────


class LowercaseARingGlyph(ComposedGlyph):
    name = "lowercase_aring"
    unicode = "0xE5"
    base_glyph_class = LowercaseAGlyph
    accent_class = Ring
    accent_y = _lc_accent


# ── Lowercase with cedilla ───────────────────────────────────────────


class LowercaseCCedillaGlyph(ComposedGlyph):
    name = "lowercase_ccedilla"
    unicode = "0xE7"
    base_glyph_class = LowercaseCGlyph
    accent_class = Cedilla
    accent_y = _cedilla_y


class LowercaseSCedillaGlyph(ComposedGlyph):
    name = "lowercase_scedilla"
    unicode = "0x15F"
    base_glyph_class = LowercaseSGlyph
    accent_class = Cedilla
    accent_y = _cedilla_y


# ── Lowercase with caron ─────────────────────────────────────────────


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


# ── Lowercase with breve ─────────────────────────────────────────────


class LowercaseGBreveGlyph(ComposedGlyph):
    name = "lowercase_gbreve"
    unicode = "0x11F"
    base_glyph_class = LowercaseGGlyph
    accent_class = Breve
    accent_y = _lc_accent


# ── Dotless i ────────────────────────────────────────────────────────


class LowercaseDotlessIGlyph(LowercaseIGlyph):
    name = "lowercase_dotlessi"
    unicode = "0x131"

    def draw(self, pen, dc):
        self.draw_base(pen, dc)


class LowercaseDotlessI2Glyph(LowercaseI2Glyph):
    name = "lowercase_dotlessi_2"
    unicode = "0x131"

    def draw(self, pen, dc):
        self.draw_base(pen, dc)


# ── L with middle dot (Catalan) ──────────────────────────────────────


def _draw_l_dot(pen, dc, x, y):
    """Middle dot centered between the stem of an L and its right edge."""
    s = 1.4 * dc.stroke_x
    draw_rect(pen, x - s, y - s / 2, x, y + s / 2)


class LowercaseLDotGlyph(LowercaseLGlyph):
    name = "lowercase_ldot"
    unicode = "0x140"

    def draw(self, pen, dc):
        super().draw(pen, dc)
        b = dc.body_bounds(
            offset=self.offset, height="ascent", width_ratio=self.width_ratio
        )
        _draw_l_dot(pen, dc, b.x2, dc.cap / 2)


class UppercaseLDotGlyph(UppercaseLGlyph):
    name = "uppercase_ldot"
    unicode = "0x13F"

    def draw(self, pen, dc):
        super().draw(pen, dc)
        b = dc.body_bounds(
            offset=self.offset, height="cap", width_ratio=self.width_ratio
        )
        _draw_l_dot(pen, dc, b.x2, dc.cap / 2)


# ── Uppercase with acute ─────────────────────────────────────────────


class UppercaseAAcuteGlyph(ComposedGlyph):
    name = "uppercase_aacute"
    unicode = "0xC1"
    base_glyph_class = UppercaseAGlyph
    accent_class = Acute
    accent_y = _uc_accent


class UppercaseEAcuteGlyph(ComposedGlyph):
    name = "uppercase_eacute"
    unicode = "0xC9"
    base_glyph_class = UppercaseEGlyph
    accent_class = Acute
    accent_y = _uc_accent


class UppercaseIAcuteGlyph(ComposedGlyph):
    name = "uppercase_iacute"
    unicode = "0xCD"
    base_glyph_class = UppercaseIGlyph
    accent_class = Acute
    accent_y = _uc_accent


class UppercaseOAcuteGlyph(ComposedGlyph):
    name = "uppercase_oacute"
    unicode = "0xD3"
    base_glyph_class = UppercaseOGlyph
    accent_class = Acute
    accent_y = _uc_accent


class UppercaseUAcuteGlyph(ComposedGlyph):
    name = "uppercase_uacute"
    unicode = "0xDA"
    base_glyph_class = UppercaseUGlyph
    accent_class = Acute
    accent_y = _uc_accent


class UppercaseYAcuteGlyph(ComposedGlyph):
    name = "uppercase_yacute"
    unicode = "0xDD"
    base_glyph_class = UppercaseYGlyph
    accent_class = Acute
    accent_y = _uc_accent


# ── Uppercase with grave ─────────────────────────────────────────────


class UppercaseAGraveGlyph(ComposedGlyph):
    name = "uppercase_agrave"
    unicode = "0xC0"
    base_glyph_class = UppercaseAGlyph
    accent_class = Grave
    accent_y = _uc_accent


class UppercaseEGraveGlyph(ComposedGlyph):
    name = "uppercase_egrave"
    unicode = "0xC8"
    base_glyph_class = UppercaseEGlyph
    accent_class = Grave
    accent_y = _uc_accent


class UppercaseIGraveGlyph(ComposedGlyph):
    name = "uppercase_igrave"
    unicode = "0xCC"
    base_glyph_class = UppercaseIGlyph
    accent_class = Grave
    accent_y = _uc_accent


class UppercaseOGraveGlyph(ComposedGlyph):
    name = "uppercase_ograve"
    unicode = "0xD2"
    base_glyph_class = UppercaseOGlyph
    accent_class = Grave
    accent_y = _uc_accent


class UppercaseUGraveGlyph(ComposedGlyph):
    name = "uppercase_ugrave"
    unicode = "0xD9"
    base_glyph_class = UppercaseUGlyph
    accent_class = Grave
    accent_y = _uc_accent


# ── Uppercase with circumflex ────────────────────────────────────────


class UppercaseACircumflexGlyph(ComposedGlyph):
    name = "uppercase_acircumflex"
    unicode = "0xC2"
    base_glyph_class = UppercaseAGlyph
    accent_class = Circumflex
    accent_y = _uc_accent


class UppercaseECircumflexGlyph(ComposedGlyph):
    name = "uppercase_ecircumflex"
    unicode = "0xCA"
    base_glyph_class = UppercaseEGlyph
    accent_class = Circumflex
    accent_y = _uc_accent


class UppercaseICircumflexGlyph(ComposedGlyph):
    name = "uppercase_icircumflex"
    unicode = "0xCE"
    base_glyph_class = UppercaseIGlyph
    accent_class = Circumflex
    accent_y = _uc_accent


class UppercaseOCircumflexGlyph(ComposedGlyph):
    name = "uppercase_ocircumflex"
    unicode = "0xD4"
    base_glyph_class = UppercaseOGlyph
    accent_class = Circumflex
    accent_y = _uc_accent


class UppercaseUCircumflexGlyph(ComposedGlyph):
    name = "uppercase_ucircumflex"
    unicode = "0xDB"
    base_glyph_class = UppercaseUGlyph
    accent_class = Circumflex
    accent_y = _uc_accent


# ── Uppercase with dieresis ──────────────────────────────────────────


class UppercaseADieresisGlyph(ComposedGlyph):
    name = "uppercase_adieresis"
    unicode = "0xC4"
    base_glyph_class = UppercaseAGlyph
    accent_class = Dieresis
    accent_y = _uc_accent


class UppercaseEDieresisGlyph(ComposedGlyph):
    name = "uppercase_edieresis"
    unicode = "0xCB"
    base_glyph_class = UppercaseEGlyph
    accent_class = Dieresis
    accent_y = _uc_accent


class UppercaseIDieresisGlyph(ComposedGlyph):
    name = "uppercase_idieresis"
    unicode = "0xCF"
    base_glyph_class = UppercaseIGlyph
    accent_class = Dieresis
    accent_y = _uc_accent


class UppercaseODieresisGlyph(ComposedGlyph):
    name = "uppercase_odieresis"
    unicode = "0xD6"
    base_glyph_class = UppercaseOGlyph
    accent_class = Dieresis
    accent_y = _uc_accent


class UppercaseUDieresisGlyph(ComposedGlyph):
    name = "uppercase_udieresis"
    unicode = "0xDC"
    base_glyph_class = UppercaseUGlyph
    accent_class = Dieresis
    accent_y = _uc_accent


class UppercaseYDieresisGlyph(ComposedGlyph):
    name = "uppercase_ydieresis"
    unicode = "0x178"
    base_glyph_class = UppercaseYGlyph
    accent_class = Dieresis
    accent_y = _uc_accent


# ── W and Y with circumflex, grave, acute, dieresis (Welsh) ──────────


class LowercaseWCircumflexGlyph(ComposedGlyph):
    name = "lowercase_wcircumflex"
    unicode = "0x175"
    base_glyph_class = LowercaseWGlyph
    accent_class = Circumflex
    accent_y = _lc_accent


class UppercaseWCircumflexGlyph(ComposedGlyph):
    name = "uppercase_wcircumflex"
    unicode = "0x174"
    base_glyph_class = UppercaseWGlyph
    accent_class = Circumflex
    accent_y = _uc_accent


class LowercaseYCircumflexGlyph(ComposedGlyph):
    name = "lowercase_ycircumflex"
    unicode = "0x177"
    base_glyph_class = LowercaseYGlyph
    accent_class = Circumflex
    accent_y = _lc_accent


class UppercaseYCircumflexGlyph(ComposedGlyph):
    name = "uppercase_ycircumflex"
    unicode = "0x176"
    base_glyph_class = UppercaseYGlyph
    accent_class = Circumflex
    accent_y = _uc_accent


class LowercaseWGraveGlyph(ComposedGlyph):
    name = "lowercase_wgrave"
    unicode = "0x1E81"
    base_glyph_class = LowercaseWGlyph
    accent_class = Grave
    accent_y = _lc_accent


class UppercaseWGraveGlyph(ComposedGlyph):
    name = "uppercase_wgrave"
    unicode = "0x1E80"
    base_glyph_class = UppercaseWGlyph
    accent_class = Grave
    accent_y = _uc_accent


class LowercaseWAcuteGlyph(ComposedGlyph):
    name = "lowercase_wacute"
    unicode = "0x1E83"
    base_glyph_class = LowercaseWGlyph
    accent_class = Acute
    accent_y = _lc_accent


class UppercaseWAcuteGlyph(ComposedGlyph):
    name = "uppercase_wacute"
    unicode = "0x1E82"
    base_glyph_class = UppercaseWGlyph
    accent_class = Acute
    accent_y = _uc_accent


class LowercaseWDieresisGlyph(ComposedGlyph):
    name = "lowercase_wdieresis"
    unicode = "0x1E85"
    base_glyph_class = LowercaseWGlyph
    accent_class = Dieresis
    accent_y = _lc_accent


class UppercaseWDieresisGlyph(ComposedGlyph):
    name = "uppercase_wdieresis"
    unicode = "0x1E84"
    base_glyph_class = UppercaseWGlyph
    accent_class = Dieresis
    accent_y = _uc_accent


class LowercaseYGraveGlyph(ComposedGlyph):
    name = "lowercase_ygrave"
    unicode = "0x1EF3"
    base_glyph_class = LowercaseYGlyph
    accent_class = Grave
    accent_y = _lc_accent


class UppercaseYGraveGlyph(ComposedGlyph):
    name = "uppercase_ygrave"
    unicode = "0x1EF2"
    base_glyph_class = UppercaseYGlyph
    accent_class = Grave
    accent_y = _uc_accent


# ── Uppercase with tilde ─────────────────────────────────────────────


class UppercaseATildeGlyph(ComposedGlyph):
    name = "uppercase_atilde"
    unicode = "0xC3"
    base_glyph_class = UppercaseAGlyph
    accent_class = Tilde
    accent_y = _uc_accent


class UppercaseNTildeGlyph(ComposedGlyph):
    name = "uppercase_ntilde"
    unicode = "0xD1"
    base_glyph_class = UppercaseNGlyph
    accent_class = Tilde
    accent_y = _uc_accent


class UppercaseOTildeGlyph(ComposedGlyph):
    name = "uppercase_otilde"
    unicode = "0xD5"
    base_glyph_class = UppercaseOGlyph
    accent_class = Tilde
    accent_y = _uc_accent


# ── Uppercase with ring ──────────────────────────────────────────────


class UppercaseARingGlyph(ComposedGlyph):
    name = "uppercase_aring"
    unicode = "0xC5"
    base_glyph_class = UppercaseAGlyph
    accent_class = Ring
    accent_y = _uc_accent


# ── Uppercase with cedilla ───────────────────────────────────────────


class UppercaseCCedillaGlyph(ComposedGlyph):
    name = "uppercase_ccedilla"
    unicode = "0xC7"
    base_glyph_class = UppercaseCGlyph
    accent_class = Cedilla
    accent_y = _cedilla_y


class UppercaseSCedillaGlyph(ComposedGlyph):
    name = "uppercase_scedilla"
    unicode = "0x15E"
    base_glyph_class = UppercaseSGlyph
    accent_class = Cedilla
    accent_y = _cedilla_y


# ── Uppercase with caron ─────────────────────────────────────────────


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


# ── Uppercase with breve ─────────────────────────────────────────────


class UppercaseGBreveGlyph(ComposedGlyph):
    name = "uppercase_gbreve"
    unicode = "0x11E"
    base_glyph_class = UppercaseGGlyph
    accent_class = Breve
    accent_y = _uc_accent


# ── Uppercase with dot above ─────────────────────────────────────────


class UppercaseIDotGlyph(ComposedGlyph):
    name = "uppercase_idotaccent"
    unicode = "0x130"
    base_glyph_class = UppercaseIGlyph
    accent_class = DotAbove
    accent_y = _uc_accent


# ── Uppercase with macron (romaji long vowels) ───────────────────────


class UppercaseAMacronGlyph(ComposedGlyph):
    name = "uppercase_amacron"
    unicode = "0x100"
    base_glyph_class = UppercaseAGlyph
    accent_class = Macron
    accent_y = _uc_accent


class UppercaseEMacronGlyph(ComposedGlyph):
    name = "uppercase_emacron"
    unicode = "0x112"
    base_glyph_class = UppercaseEGlyph
    accent_class = Macron
    accent_y = _uc_accent


class UppercaseIMacronGlyph(ComposedGlyph):
    name = "uppercase_imacron"
    unicode = "0x12A"
    base_glyph_class = UppercaseIGlyph
    accent_class = Macron
    accent_y = _uc_accent


class UppercaseOMacronGlyph(ComposedGlyph):
    name = "uppercase_omacron"
    unicode = "0x14C"
    base_glyph_class = UppercaseOGlyph
    accent_class = Macron
    accent_y = _uc_accent


class UppercaseUMacronGlyph(ComposedGlyph):
    name = "uppercase_umacron"
    unicode = "0x16A"
    base_glyph_class = UppercaseUGlyph
    accent_class = Macron
    accent_y = _uc_accent


# ── Polish: acute ────────────────────────────────────────────────────


class LowercaseCAcuteGlyph(ComposedGlyph):
    name = "lowercase_cacute"
    unicode = "0x107"
    base_glyph_class = LowercaseCGlyph
    accent_class = Acute
    accent_y = _lc_accent


class LowercaseNAcuteGlyph(ComposedGlyph):
    name = "lowercase_nacute"
    unicode = "0x144"
    base_glyph_class = LowercaseNGlyph
    accent_class = Acute
    accent_y = _lc_accent


class LowercaseSAcuteGlyph(ComposedGlyph):
    name = "lowercase_sacute"
    unicode = "0x15B"
    base_glyph_class = LowercaseSGlyph
    accent_class = Acute
    accent_y = _lc_accent


class LowercaseZAcuteGlyph(ComposedGlyph):
    name = "lowercase_zacute"
    unicode = "0x17A"
    base_glyph_class = LowercaseZGlyph
    accent_class = Acute
    accent_y = _lc_accent


class UppercaseCAcuteGlyph(ComposedGlyph):
    name = "uppercase_cacute"
    unicode = "0x106"
    base_glyph_class = UppercaseCGlyph
    accent_class = Acute
    accent_y = _uc_accent


class UppercaseNAcuteGlyph(ComposedGlyph):
    name = "uppercase_nacute"
    unicode = "0x143"
    base_glyph_class = UppercaseNGlyph
    accent_class = Acute
    accent_y = _uc_accent


class UppercaseSAcuteGlyph(ComposedGlyph):
    name = "uppercase_sacute"
    unicode = "0x15A"
    base_glyph_class = UppercaseSGlyph
    accent_class = Acute
    accent_y = _uc_accent


class UppercaseZAcuteGlyph(ComposedGlyph):
    name = "uppercase_zacute"
    unicode = "0x179"
    base_glyph_class = UppercaseZGlyph
    accent_class = Acute
    accent_y = _uc_accent


# ── Polish: dot above ────────────────────────────────────────────────


class LowercaseZDotGlyph(ComposedGlyph):
    name = "lowercase_zdotaccent"
    unicode = "0x17C"
    base_glyph_class = LowercaseZGlyph
    accent_class = DotAbove
    accent_y = _lc_accent


class UppercaseZDotGlyph(ComposedGlyph):
    name = "uppercase_zdotaccent"
    unicode = "0x17B"
    base_glyph_class = UppercaseZGlyph
    accent_class = DotAbove
    accent_y = _uc_accent


# ── Maltese: dot above and H with stroke ─────────────────────────────


class LowercaseCDotGlyph(ComposedGlyph):
    name = "lowercase_cdotaccent"
    unicode = "0x10B"
    base_glyph_class = LowercaseCGlyph
    accent_class = DotAbove
    accent_y = _lc_accent


class UppercaseCDotGlyph(ComposedGlyph):
    name = "uppercase_cdotaccent"
    unicode = "0x10A"
    base_glyph_class = UppercaseCGlyph
    accent_class = DotAbove
    accent_y = _uc_accent


class LowercaseGDotGlyph(ComposedGlyph):
    name = "lowercase_gdotaccent"
    unicode = "0x121"
    base_glyph_class = LowercaseGGlyph
    accent_class = DotAbove
    accent_y = _lc_accent


class UppercaseGDotGlyph(ComposedGlyph):
    name = "uppercase_gdotaccent"
    unicode = "0x120"
    base_glyph_class = UppercaseGGlyph
    accent_class = DotAbove
    accent_y = _uc_accent


class LowercaseHStrokeGlyph(LowercaseHGlyph):
    name = "lowercase_hbar"
    unicode = "0x127"
    # Bar reach past the stem, as fractions of the body width
    bar_left = 0.15
    bar_right = 0.45

    def draw(self, pen, dc):
        super().draw(pen, dc)
        b = dc.body_bounds(width_ratio=self.width_ratio, offset=self.offset)
        y = (dc.x_height + dc.ascent) / 2
        draw_rect(
            pen,
            b.x1 - self.bar_left * b.width,
            y - dc.stroke_y / 2,
            b.x1 + dc.stroke_x + self.bar_right * b.width,
            y + dc.stroke_y / 2,
        )


class UppercaseHStrokeGlyph(UppercaseHGlyph):
    name = "uppercase_hbar"
    unicode = "0x126"
    bar_y = 0.78  # Relative to the cap height
    bar_overhang = 0.15  # Past each stem, relative to the body width

    def draw(self, pen, dc):
        super().draw(pen, dc)
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            width_ratio=self.width_ratio,
            uppercase=True,
        )
        sy = dc.stroke_y * self.stroke_y_ratio
        y = self.bar_y * b.height
        o = self.bar_overhang * b.width
        draw_rect(pen, b.x1 - o, y - sy / 2, b.x2 + o, y + sy / 2)


# ── Czech and Slovak: caron and ring ─────────────────────────────────


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


class LowercaseURingGlyph(ComposedGlyph):
    name = "lowercase_uring"
    unicode = "0x16F"
    base_glyph_class = LowercaseUGlyph
    accent_class = Ring
    accent_y = _lc_accent


class UppercaseURingGlyph(ComposedGlyph):
    name = "uppercase_uring"
    unicode = "0x16E"
    base_glyph_class = UppercaseUGlyph
    accent_class = Ring
    accent_y = _uc_accent


class LowercaseDCaronGlyph(ComposedGlyph):
    """d with the vertical caron beside its ascender.

    The d is narrowed if needed and shifted left so that it and the mark
    fit in the cell together, centered as a pair.
    """

    name = "lowercase_dcaron"
    unicode = "0x10F"
    base_glyph_class = LowercaseDGlyph
    accent_class = CaronVertical

    def draw(self, pen, dc):
        base = self._resolve_base_class(dc)()
        mark = self.accent_class()
        margin = 0
        mark_width = mark.gap_width(dc) + mark.top_width(dc)
        room = dc.window_width - 2 * margin - mark_width
        base.width_ratio = min(base.width_ratio, (room - dc.stroke_x) / dc.width)
        d_width = dc.width * base.width_ratio + dc.stroke_x
        x1 = (dc.window_width - d_width - mark_width) / 2
        base.offset = x1 - (dc.window_width - d_width) / 2
        base.draw(pen, dc)
        mark.draw_at(pen, dc, x=x1 + d_width + mark.gap_width(dc), y=dc.ascent)


class LowercaseRAcuteGlyph(ComposedGlyph):
    name = "lowercase_racute"
    unicode = "0x155"
    base_glyph_class = LowercaseRGlyph
    accent_class = Acute
    accent_y = _lc_accent


class UppercaseRAcuteGlyph(ComposedGlyph):
    name = "uppercase_racute"
    unicode = "0x154"
    base_glyph_class = UppercaseRGlyph
    accent_class = Acute
    accent_y = _uc_accent


class UppercaseLAcuteGlyph(ComposedGlyph):
    name = "uppercase_lacute"
    unicode = "0x139"
    base_glyph_class = UppercaseLGlyph
    accent_class = Acute
    accent_y = _uc_accent

    def accent_x(self, dc, base, b):
        return b.x1 + Acute.stroke_ratio * dc.stroke_x / 2


class LowercaseLAcuteGlyph(ComposedGlyph):
    """l with the acute above its ascender, centered on the stem."""

    name = "lowercase_lacute"
    unicode = "0x13A"
    base_glyph_class = LowercaseLGlyph
    accent_class = Acute
    # Above the ascent by most of the gap capitals leave below their accent
    accent_y = fc.ascent + 0.8 * (fc.accent_cap - fc.cap)

    def accent_x(self, dc, base, b):
        return base.stem_center(dc)


class UppercaseLCaronGlyph(ComposedGlyph):
    """L with the vertical caron beside the top of its stem."""

    name = "uppercase_lcaron"
    unicode = "0x13D"
    base_glyph_class = UppercaseLGlyph
    accent_class = CaronVertical

    def draw(self, pen, dc):
        base = self._resolve_base_class(dc)()
        base.draw(pen, dc)
        b = dc.body_bounds(
            offset=base.offset, height="cap", width_ratio=base.width_ratio
        )
        self.accent_class().draw_at(pen, dc, x=(b.x1 + b.x2) * 0.55, y=dc.cap)


class LowercaseLCaronGlyph(ComposedGlyph):
    """l with the vertical caron beside the top of its stem."""

    name = "lowercase_lcaron"
    unicode = "0x13E"
    base_glyph_class = LowercaseLGlyph
    accent_class = CaronVertical

    def draw(self, pen, dc):
        base = self._resolve_base_class(dc)()
        b = dc.body_bounds(
            offset=base.offset, height="cap", width_ratio=base.width_ratio
        )
        base.draw(pen, dc)
        mark = self.accent_class()
        mark.draw_at(pen, dc, x=(b.x2 + b.xmid) / 2, y=dc.ascent)


class LowercaseTCaronGlyph(ComposedGlyph):
    """t with the vertical caron beside the top of its stem."""

    name = "lowercase_tcaron"
    unicode = "0x165"
    base_glyph_class = LowercaseTGlyph
    accent_class = CaronVertical

    def draw(self, pen, dc):
        base = self._resolve_base_class(dc)()
        base.draw(pen, dc)
        b = dc.body_bounds(
            offset=base.offset, height="x_height", width_ratio=base.width_ratio
        )
        top = (1 + base.up_ratio) * dc.x_height
        accent = self.accent_class()
        accent.height = 0.3
        accent.draw_at(pen, dc, x=(b.xmid + b.x2) * 0.55, y=top)


# ── Croatian, Bosnian, Serbian: D with stroke ────────────────────────


class UppercaseDStrokeGlyph(UppercaseEthGlyph):
    """Drawn exactly like the Icelandic eth `Ð`."""

    name = "uppercase_dcroat"
    unicode = "0x110"


class LowercaseDStrokeGlyph(LowercaseDGlyph):
    """d with a bar across its ascender, at the height of the one on ħ."""

    name = "lowercase_dcroat"
    unicode = "0x111"
    # Bar reach past the stem, as fractions of the body width
    bar_left = 0.45
    bar_right = 0.15

    def draw(self, pen, dc):
        super().draw(pen, dc)
        b = dc.body_bounds(width_ratio=self.width_ratio, offset=self.offset)
        y = (dc.x_height + dc.ascent) / 2
        draw_rect(
            pen,
            b.x2 - dc.stroke_x - self.bar_left * b.width,
            y - dc.stroke_y / 2,
            b.x2 + self.bar_right * b.width,
            y + dc.stroke_y / 2,
        )


# ── Hungarian: double acute ──────────────────────────────────────────


class LowercaseODoubleAcuteGlyph(ComposedGlyph):
    name = "lowercase_ohungarumlaut"
    unicode = "0x151"
    base_glyph_class = LowercaseOGlyph
    accent_class = DoubleAcute
    accent_y = _lc_accent


class UppercaseODoubleAcuteGlyph(ComposedGlyph):
    name = "uppercase_ohungarumlaut"
    unicode = "0x150"
    base_glyph_class = UppercaseOGlyph
    accent_class = DoubleAcute
    accent_y = _uc_accent


class LowercaseUDoubleAcuteGlyph(ComposedGlyph):
    name = "lowercase_uhungarumlaut"
    unicode = "0x171"
    base_glyph_class = LowercaseUGlyph
    accent_class = DoubleAcute
    accent_y = _lc_accent


class UppercaseUDoubleAcuteGlyph(ComposedGlyph):
    name = "uppercase_uhungarumlaut"
    unicode = "0x170"
    base_glyph_class = UppercaseUGlyph
    accent_class = DoubleAcute
    accent_y = _uc_accent


# ── Polish: ogonek ───────────────────────────────────────────────────


class OgonekComposedGlyph(ComposedGlyph):
    """Hangs the ogonek from the base glyph's measured outline, so it follows
    the real shape of each base (including italic variants)."""

    accent_class = Ogonek
    accent_y = 0
    # Hang from the rightmost stem, spanning it from its inner to its outer
    # edge. Otherwise the hook is a stem wide and placed by `ogonek_inset`.
    from_stem = False
    # Hook center, measured from the base's right edge as a fraction of its
    # width (0 = flush with the right edge).
    ogonek_inset = 0.0
    ogonek_width = Ogonek.stem_ratio  # Start width, relative to stroke_x
    ogonek_start = 0.0
    stem_probe = 0.25  # Height where the stem is measured, relative to x-height
    keep_dot = False  # Draw the full base (e.g. the dot of į) instead of draw_base

    def _base_path(self, base, dc):
        path = pathops.Path()
        pen = pathops.PathPen(path)
        base.draw_base(pen, dc) if hasattr(base, "draw_base") else base.draw(pen, dc)
        return pathops.simplify(path)

    def _rightmost_stem(self, path, dc):
        """Horizontal span of the rightmost piece of the outline crossing a
        thin band just above the baseline."""
        y = self.stem_probe * dc.x_height
        band = pathops.Path()
        draw_rect(pathops.PathPen(band), -1000, y, 2000, y + 1)
        section = pathops.op(path, band, pathops.PathOp.INTERSECTION)
        pieces = []
        for contour in section.contours:
            xs = [x for _, points in contour for x, _ in points]
            pieces.append((min(xs), max(xs)))
        return max(pieces, key=lambda piece: piece[1])

    def draw(self, pen, dc):
        base_class = self._resolve_base_class(dc)
        base = base_class()
        if self.keep_dot or not hasattr(base, "draw_base"):
            base.draw(pen, dc)
        else:
            base.draw_base(pen, dc)

        path = self._base_path(base, dc)
        start = self.ogonek_start * dc.x_height
        if self.from_stem:
            x1, x2 = self._rightmost_stem(path, dc)
            Ogonek().draw_at(
                pen,
                dc,
                x=(x1 + x2) / 2,
                y=self.accent_y,
                width=x2 - x1,
                start=start,
            )
        else:
            x1, _, x2, _ = path.bounds
            width = self.ogonek_width * dc.stroke_x
            x = x2 - self.ogonek_inset * (x2 - x1) - width / 2
            Ogonek().draw_at(pen, dc, x=x, y=self.accent_y, width=width, start=start)


class LowercaseAOgonekGlyph(OgonekComposedGlyph):
    name = "lowercase_aogonek"
    unicode = "0x105"
    base_glyph_class = LowercaseAGlyph
    from_stem = True


class LowercaseEOgonekGlyph(OgonekComposedGlyph):
    name = "lowercase_eogonek"
    unicode = "0x119"
    base_glyph_class = LowercaseEGlyph
    ogonek_inset = 0.3


class UppercaseAOgonekGlyph(OgonekComposedGlyph):
    name = "uppercase_aogonek"
    unicode = "0x104"
    base_glyph_class = UppercaseAGlyph
    ogonek_width = 0.85
    ogonek_inset = 0.05


class UppercaseEOgonekGlyph(OgonekComposedGlyph):
    name = "uppercase_eogonek"
    unicode = "0x118"
    base_glyph_class = UppercaseEGlyph
    ogonek_inset = 0.2


# ── Polish: stroke ───────────────────────────────────────────────────


class LowercaseLStrokeGlyph(ComposedGlyph):
    name = "lowercase_lslash"
    unicode = "0x142"
    base_glyph_class = LowercaseLGlyph
    accent_class = Stroke
    accent_y = 0.55 * fc.ascent

    def accent_x(self, dc, base, b):
        return base.stem_center(dc)


class UppercaseLStrokeGlyph(ComposedGlyph):
    name = "uppercase_lslash"
    unicode = "0x141"
    base_glyph_class = UppercaseLGlyph
    accent_class = UppercaseStroke
    accent_y = 0.45 * fc.cap

    def accent_x(self, dc, base, b):
        return base.stem_center(dc)


# ── Romanian: breve ──────────────────────────────────────────────────


class LowercaseABreveGlyph(ComposedGlyph):
    name = "lowercase_abreve"
    unicode = "0x103"
    base_glyph_class = LowercaseAGlyph
    accent_class = Breve
    accent_y = _lc_accent


class UppercaseABreveGlyph(ComposedGlyph):
    name = "uppercase_abreve"
    unicode = "0x102"
    base_glyph_class = UppercaseAGlyph
    accent_class = Breve
    accent_y = _uc_accent


# ── Romanian: comma below ────────────────────────────────────────────


class LowercaseSCommaGlyph(ComposedGlyph):
    name = "lowercase_scommaaccent"
    unicode = "0x219"
    base_glyph_class = LowercaseSGlyph
    accent_class = CommaBelow
    accent_y = 0


class LowercaseTCommaGlyph(ComposedGlyph):
    name = "lowercase_tcommaaccent"
    unicode = "0x21B"
    base_glyph_class = LowercaseTGlyph
    accent_class = CommaBelow
    accent_y = 0


class UppercaseSCommaGlyph(ComposedGlyph):
    name = "uppercase_scommaaccent"
    unicode = "0x218"
    base_glyph_class = UppercaseSGlyph
    accent_class = CommaBelow
    accent_y = 0


class UppercaseTCommaGlyph(ComposedGlyph):
    name = "uppercase_tcommaaccent"
    unicode = "0x21A"
    base_glyph_class = UppercaseTGlyph
    accent_class = CommaBelow
    accent_y = 0


# ── Romanian (legacy): t with cedilla ────────────────────────────────


class LowercaseTCedillaGlyph(ComposedGlyph):
    name = "lowercase_tcedilla"
    unicode = "0x163"
    base_glyph_class = LowercaseTGlyph
    accent_class = Cedilla

    def accent_x(self, dc, base, b):
        """Horizontal anchor of the accent; centered on the body by default."""
        return b.xmid + 0.15 * b.width

    def draw(self, pen, dc):
        base_class = self._resolve_base_class(dc)
        base = base_class()
        base.draw_base(pen, dc) if hasattr(base, "draw_base") else base.draw(pen, dc)

        b = dc.body_bounds(offset=base_class.offset)
        accent_class = self.accent_class()
        accent_class.y_start = 10
        accent_class.draw_at(pen, dc, x=self.accent_x(dc, base, b), y=0)


class UppercaseTCedillaGlyph(ComposedGlyph):
    name = "uppercase_tcedilla"
    unicode = "0x162"
    base_glyph_class = UppercaseTGlyph
    accent_class = Cedilla
    accent_y = _cedilla_y


# ── Latvian: comma below (Unicode names them "cedilla") ──────────────


class LowercaseGCommaGlyph(ComposedGlyph):
    """The descender leaves no room below, so ģ takes its comma above."""

    name = "lowercase_gcommaaccent"
    unicode = "0x123"
    base_glyph_class = LowercaseGGlyph
    accent_class = Acute
    accent_y = _lc_accent


class LowercaseKCommaGlyph(ComposedGlyph):
    name = "lowercase_kcommaaccent"
    unicode = "0x137"
    base_glyph_class = LowercaseKGlyph
    accent_class = CommaBelow
    accent_y = 0


class LowercaseLCommaGlyph(ComposedGlyph):
    name = "lowercase_lcommaaccent"
    unicode = "0x13C"
    base_glyph_class = LowercaseLGlyph
    accent_class = CommaBelow
    accent_y = 0


class LowercaseNCommaGlyph(ComposedGlyph):
    name = "lowercase_ncommaaccent"
    unicode = "0x146"
    base_glyph_class = LowercaseNGlyph
    accent_class = CommaBelow
    accent_y = 0


class LowercaseRCommaGlyph(ComposedGlyph):
    name = "lowercase_rcommaaccent"
    unicode = "0x157"
    base_glyph_class = LowercaseRGlyph
    accent_class = CommaBelow
    accent_y = 0


class UppercaseGCommaGlyph(ComposedGlyph):
    name = "uppercase_gcommaaccent"
    unicode = "0x122"
    base_glyph_class = UppercaseGGlyph
    accent_class = CommaBelow
    accent_y = 0


class UppercaseKCommaGlyph(ComposedGlyph):
    name = "uppercase_kcommaaccent"
    unicode = "0x136"
    base_glyph_class = UppercaseKGlyph
    accent_class = CommaBelow
    accent_y = 0


class UppercaseLCommaGlyph(ComposedGlyph):
    name = "uppercase_lcommaaccent"
    unicode = "0x13B"
    base_glyph_class = UppercaseLGlyph
    accent_class = CommaBelow
    accent_y = 0


class UppercaseNCommaGlyph(ComposedGlyph):
    name = "uppercase_ncommaaccent"
    unicode = "0x145"
    base_glyph_class = UppercaseNGlyph
    accent_class = CommaBelow
    accent_y = 0


class UppercaseRCommaGlyph(ComposedGlyph):
    name = "uppercase_rcommaaccent"
    unicode = "0x156"
    base_glyph_class = UppercaseRGlyph
    accent_class = CommaBelow
    accent_y = 0


# ── Lithuanian: dot above and ogonek ─────────────────────────────────


class LowercaseEDotGlyph(ComposedGlyph):
    name = "lowercase_edotaccent"
    unicode = "0x117"
    base_glyph_class = LowercaseEGlyph
    accent_class = DotAbove
    accent_y = _lc_accent


class UppercaseEDotGlyph(ComposedGlyph):
    name = "uppercase_edotaccent"
    unicode = "0x116"
    base_glyph_class = UppercaseEGlyph
    accent_class = DotAbove
    accent_y = _uc_accent


class LowercaseIOgonekGlyph(OgonekComposedGlyph):
    name = "lowercase_iogonek"
    unicode = "0x12F"
    base_glyph_class = LowercaseIGlyph
    keep_dot = True
    from_stem = True


class UppercaseIOgonekGlyph(OgonekComposedGlyph):
    name = "uppercase_iogonek"
    unicode = "0x12E"
    base_glyph_class = UppercaseIGlyph
    from_stem = True


class LowercaseUOgonekGlyph(OgonekComposedGlyph):
    name = "lowercase_uogonek"
    unicode = "0x173"
    base_glyph_class = LowercaseUGlyph
    ogonek_inset = 0.32


class UppercaseUOgonekGlyph(OgonekComposedGlyph):
    name = "uppercase_uogonek"
    unicode = "0x172"
    base_glyph_class = UppercaseUGlyph
    ogonek_inset = 0.3


# ── Esperanto: circumflex and breve ──────────────────────────────────


class LowercaseCCircumflexGlyph(ComposedGlyph):
    name = "lowercase_ccircumflex"
    unicode = "0x109"
    base_glyph_class = LowercaseCGlyph
    accent_class = Circumflex
    accent_y = _lc_accent


class UppercaseCCircumflexGlyph(ComposedGlyph):
    name = "uppercase_ccircumflex"
    unicode = "0x108"
    base_glyph_class = UppercaseCGlyph
    accent_class = Circumflex
    accent_y = _uc_accent


class LowercaseGCircumflexGlyph(ComposedGlyph):
    name = "lowercase_gcircumflex"
    unicode = "0x11D"
    base_glyph_class = LowercaseGGlyph
    accent_class = Circumflex
    accent_y = _lc_accent


class UppercaseGCircumflexGlyph(ComposedGlyph):
    name = "uppercase_gcircumflex"
    unicode = "0x11C"
    base_glyph_class = UppercaseGGlyph
    accent_class = Circumflex
    accent_y = _uc_accent


class LowercaseHCircumflexGlyph(ComposedGlyph):
    """h with the circumflex above its ascender, centered on the left stem."""

    name = "lowercase_hcircumflex"
    unicode = "0x125"
    base_glyph_class = LowercaseHGlyph
    accent_class = Circumflex
    accent_y = LowercaseLAcuteGlyph.accent_y

    def accent_x(self, dc, base, b):
        b = dc.body_bounds(
            width_ratio=base.width_ratio, offset=base.offset, overshoot_top=True
        )
        return b.x1 + dc.stroke_x / 2


class UppercaseHCircumflexGlyph(ComposedGlyph):
    name = "uppercase_hcircumflex"
    unicode = "0x124"
    base_glyph_class = UppercaseHGlyph
    accent_class = Circumflex
    accent_y = _uc_accent


class LowercaseJCircumflexGlyph(ComposedGlyph):
    name = "lowercase_jcircumflex"
    unicode = "0x135"
    base_glyph_class = LowercaseJGlyph
    accent_class = Circumflex
    accent_y = _lc_accent

    def accent_x(self, dc, base, b):
        b = dc.body_bounds(
            width_ratio=base.width_ratio, offset=base.offset, overshoot_top=True
        )
        return b.xmid


class UppercaseJCircumflexGlyph(ComposedGlyph):
    name = "uppercase_jcircumflex"
    unicode = "0x134"
    base_glyph_class = UppercaseJGlyph
    accent_class = Circumflex
    accent_y = _uc_accent

    def accent_x(self, dc, base, b):
        b = dc.body_bounds(
            width_ratio=base.width_ratio, offset=base.offset, overshoot_top=True
        )
        return (b.x1 + b.x2) * 0.57


class LowercaseSCircumflexGlyph(ComposedGlyph):
    name = "lowercase_scircumflex"
    unicode = "0x15D"
    base_glyph_class = LowercaseSGlyph
    accent_class = Circumflex
    accent_y = _lc_accent


class UppercaseSCircumflexGlyph(ComposedGlyph):
    name = "uppercase_scircumflex"
    unicode = "0x15C"
    base_glyph_class = UppercaseSGlyph
    accent_class = Circumflex
    accent_y = _uc_accent


class LowercaseUBreveGlyph(ComposedGlyph):
    name = "lowercase_ubreve"
    unicode = "0x16D"
    base_glyph_class = LowercaseUGlyph
    accent_class = Breve
    accent_y = _lc_accent


class UppercaseUBreveGlyph(ComposedGlyph):
    name = "uppercase_ubreve"
    unicode = "0x16C"
    base_glyph_class = UppercaseUGlyph
    accent_class = Breve
    accent_y = _uc_accent


# ── Sámi: eng ────────────────────────────────────────────────────────


class EngComposedGlyph(ComposedGlyph):
    """n/N whose right stem continues into a hook curving left below the
    baseline."""

    hook_end = 0.35  # Where the hook ends, as a fraction of the body width

    def body(self, base, dc): ...

    def draw(self, pen, dc):
        base = self._resolve_base_class(dc)()
        base.draw(pen, dc)
        b, sx, sy = self.body(base, dc)
        draw_square_corner(
            pen,
            sx,
            sy,
            b.x2,
            0,
            b.x1 + self.hook_end * b.width,
            dc.descent,
            orientation="bottom-left",
        )


class LowercaseEngGlyph(EngComposedGlyph):
    name = "lowercase_eng"
    unicode = "0x14B"
    base_glyph_class = LowercaseNGlyph

    def body(self, base, dc):
        b = dc.body_bounds(
            offset=base.offset, overshoot_top=True, width_ratio=base.width_ratio
        )
        return b, dc.stroke_x, dc.stroke_y


class UppercaseEngGlyph(EngComposedGlyph):
    name = "uppercase_eng"
    unicode = "0x14A"
    base_glyph_class = UppercaseNGlyph

    def body(self, base, dc):
        b = dc.body_bounds(
            offset=base.offset,
            height="cap",
            width_ratio=base.width_ratio,
            uppercase=True,
            min_margin=dc.min_margin_uppercase,
        )
        return b, dc.stroke_x * base.stroke_x_ratio, dc.stroke_y * base.stroke_y_ratio


# ── Sámi: t with stroke ──────────────────────────────────────────────


class TStrokeComposedGlyph(ComposedGlyph):
    """t/T with a horizontal bar crossing the stem."""

    bar_y = 0.5  # Bar center, relative to the body height
    bar_half = 0.4  # Reach on each side of the stem center, relative to body width

    def body(self, base, dc): ...

    def draw(self, pen, dc):
        base = self._resolve_base_class(dc)()
        base.draw(pen, dc)
        b, sy = self.body(base, dc)
        y = self.bar_y * b.height
        h = self.bar_half * b.width
        draw_rect(pen, b.xmid - h, y - sy / 2, b.xmid + h, y + sy / 2)


class LowercaseTStrokeGlyph(TStrokeComposedGlyph):
    name = "lowercase_tbar"
    unicode = "0x167"
    base_glyph_class = LowercaseTGlyph
    # Between the bottom curve (which starts at mid x-height) and the crossbar
    bar_y = 0.56

    def body(self, base, dc):
        b = dc.body_bounds(
            offset=base.offset, height="x_height", width_ratio=base.width_ratio
        )
        return b, dc.stroke_y


class UppercaseTStrokeGlyph(TStrokeComposedGlyph):
    name = "uppercase_tbar"
    unicode = "0x166"
    base_glyph_class = UppercaseTGlyph

    def body(self, base, dc):
        b = dc.body_bounds(
            offset=base.offset,
            height="cap",
            width_ratio=base.width_ratio,
            min_margin=dc.min_margin_uppercase,
        )
        return b, dc.stroke_y * base.stroke_y_ratio


# ── Breve and tilde (Latin Extended-A) ───────────────────────────────


class LowercaseEBreveGlyph(ComposedGlyph):
    name = "lowercase_ebreve"
    unicode = "0x115"
    base_glyph_class = LowercaseEGlyph
    accent_class = Breve
    accent_y = _lc_accent


class UppercaseEBreveGlyph(ComposedGlyph):
    name = "uppercase_ebreve"
    unicode = "0x114"
    base_glyph_class = UppercaseEGlyph
    accent_class = Breve
    accent_y = _uc_accent


class LowercaseIBreveGlyph(ComposedGlyph):
    name = "lowercase_ibreve"
    unicode = "0x12D"
    base_glyph_class = LowercaseIGlyph
    accent_class = Breve
    accent_y = _lc_accent


class UppercaseIBreveGlyph(ComposedGlyph):
    name = "uppercase_ibreve"
    unicode = "0x12C"
    base_glyph_class = UppercaseIGlyph
    accent_class = Breve
    accent_y = _uc_accent


class LowercaseOBreveGlyph(ComposedGlyph):
    name = "lowercase_obreve"
    unicode = "0x14F"
    base_glyph_class = LowercaseOGlyph
    accent_class = Breve
    accent_y = _lc_accent


class UppercaseOBreveGlyph(ComposedGlyph):
    name = "uppercase_obreve"
    unicode = "0x14E"
    base_glyph_class = UppercaseOGlyph
    accent_class = Breve
    accent_y = _uc_accent


class LowercaseITildeGlyph(ComposedGlyph):
    name = "lowercase_itilde"
    unicode = "0x129"
    base_glyph_class = LowercaseIGlyph
    accent_class = Tilde
    accent_y = _lc_accent


class UppercaseITildeGlyph(ComposedGlyph):
    name = "uppercase_itilde"
    unicode = "0x128"
    base_glyph_class = UppercaseIGlyph
    accent_class = Tilde
    accent_y = _uc_accent


class LowercaseUTildeGlyph(ComposedGlyph):
    name = "lowercase_utilde"
    unicode = "0x169"
    base_glyph_class = LowercaseUGlyph
    accent_class = Tilde
    accent_y = _lc_accent


class UppercaseUTildeGlyph(ComposedGlyph):
    name = "uppercase_utilde"
    unicode = "0x168"
    base_glyph_class = UppercaseUGlyph
    accent_class = Tilde
    accent_y = _uc_accent
