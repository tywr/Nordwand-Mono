"""Composed glyphs with the horn."""

import pathops

from glyphs.composed import ComposedGlyph
from glyphs.lowercase.round.o import LowercaseOGlyph
from glyphs.lowercase.square.u import LowercaseUGlyph
from glyphs.uppercase.o import UppercaseOGlyph
from glyphs.uppercase.u import UppercaseUGlyph
from glyphs.accents.horn import Horn
from config import FontConfig as fc
from glyphs.accents.acute import Acute
from glyphs.accents.dot_below import DotBelow
from glyphs.accents.grave import Grave
from glyphs.accents.hook_above import HookAbove
from glyphs.accents.tilde import Tilde

_lc_accent = fc.accent
_uc_accent = fc.accent_cap


class HornComposedGlyph(ComposedGlyph):
    """Grows the horn out of the base glyph's measured right edge, so it
    follows the real shape of each base (including italic variants)."""

    accent_class = Horn
    x_offset = 0
    y_offset = 0

    def draw(self, pen, dc):
        base = self._resolve_base_class(dc)()
        base.draw(pen, dc)

        path = pathops.Path()
        base.draw(pathops.PathPen(path), dc)
        x1, y1, x2, y2 = path.bounds
        w = x2 - x1
        h = y2 - y1

        # Same strokes as the base, so the horn matches it
        width = getattr(base, "width_ratio", 1) * dc.width

        horn = self.accent_class()
        horn.draw_at(
            pen,
            dc,
            x=x1 + w / 2 + self.x_offset * width,
            y=y2 + self.y_offset * h,
        )


class LowercaseOHornGlyph(HornComposedGlyph):
    name = "lowercase_ohorn"
    unicode = "0x1A1"
    base_glyph_class = LowercaseOGlyph
    x_offset = 0.4
    y_offset = -0.07


class UppercaseOHornGlyph(HornComposedGlyph):
    name = "uppercase_ohorn"
    unicode = "0x1A0"
    base_glyph_class = UppercaseOGlyph
    x_offset = 0.39
    y_offset = -0.07


class LowercaseUHornGlyph(HornComposedGlyph):
    name = "lowercase_uhorn"
    unicode = "0x1B0"
    base_glyph_class = LowercaseUGlyph
    x_offset = 0.47


class UppercaseUHornGlyph(HornComposedGlyph):
    name = "uppercase_uhorn"
    unicode = "0x1AF"
    base_glyph_class = UppercaseUGlyph
    x_offset = 0.47


class LowercaseOHornAcuteGlyph(ComposedGlyph):
    name = "lowercase_ohornacute"
    unicode = "0x1EDB"
    base_glyph_class = LowercaseOHornGlyph
    accent_class = Acute
    accent_y = _lc_accent


class LowercaseOHornGraveGlyph(ComposedGlyph):
    name = "lowercase_ohorngrave"
    unicode = "0x1EDD"
    base_glyph_class = LowercaseOHornGlyph
    accent_class = Grave
    accent_y = _lc_accent


class LowercaseOHornHookAboveGlyph(ComposedGlyph):
    name = "lowercase_ohornhookabove"
    unicode = "0x1EDF"
    base_glyph_class = LowercaseOHornGlyph
    accent_class = HookAbove
    accent_y = _lc_accent


class LowercaseOHornTildeGlyph(ComposedGlyph):
    name = "lowercase_ohorntilde"
    unicode = "0x1EE1"
    base_glyph_class = LowercaseOHornGlyph
    accent_class = Tilde
    accent_y = _lc_accent


class LowercaseOHornDotBelowGlyph(ComposedGlyph):
    name = "lowercase_ohorndotbelow"
    unicode = "0x1EE3"
    base_glyph_class = LowercaseOHornGlyph
    accent_class = DotBelow
    accent_y = 0


class LowercaseUHornAcuteGlyph(ComposedGlyph):
    name = "lowercase_uhornacute"
    unicode = "0x1EE9"
    base_glyph_class = LowercaseUHornGlyph
    accent_class = Acute
    accent_y = _lc_accent


class LowercaseUHornGraveGlyph(ComposedGlyph):
    name = "lowercase_uhorngrave"
    unicode = "0x1EEB"
    base_glyph_class = LowercaseUHornGlyph
    accent_class = Grave
    accent_y = _lc_accent


class LowercaseUHornHookAboveGlyph(ComposedGlyph):
    name = "lowercase_uhornhookabove"
    unicode = "0x1EED"
    base_glyph_class = LowercaseUHornGlyph
    accent_class = HookAbove
    accent_y = _lc_accent


class LowercaseUHornTildeGlyph(ComposedGlyph):
    name = "lowercase_uhorntilde"
    unicode = "0x1EEF"
    base_glyph_class = LowercaseUHornGlyph
    accent_class = Tilde
    accent_y = _lc_accent


class LowercaseUHornDotBelowGlyph(ComposedGlyph):
    name = "lowercase_uhorndotbelow"
    unicode = "0x1EF1"
    base_glyph_class = LowercaseUHornGlyph
    accent_class = DotBelow
    accent_y = 0


class UppercaseOHornAcuteGlyph(ComposedGlyph):
    name = "uppercase_ohornacute"
    unicode = "0x1EDA"
    base_glyph_class = UppercaseOHornGlyph
    accent_class = Acute
    accent_y = _uc_accent


class UppercaseOHornGraveGlyph(ComposedGlyph):
    name = "uppercase_ohorngrave"
    unicode = "0x1EDC"
    base_glyph_class = UppercaseOHornGlyph
    accent_class = Grave
    accent_y = _uc_accent


class UppercaseOHornHookAboveGlyph(ComposedGlyph):
    name = "uppercase_ohornhookabove"
    unicode = "0x1EDE"
    base_glyph_class = UppercaseOHornGlyph
    accent_class = HookAbove
    accent_y = _uc_accent


class UppercaseOHornTildeGlyph(ComposedGlyph):
    name = "uppercase_ohorntilde"
    unicode = "0x1EE0"
    base_glyph_class = UppercaseOHornGlyph
    accent_class = Tilde
    accent_y = _uc_accent


class UppercaseOHornDotBelowGlyph(ComposedGlyph):
    name = "uppercase_ohorndotbelow"
    unicode = "0x1EE2"
    base_glyph_class = UppercaseOHornGlyph
    accent_class = DotBelow
    accent_y = 0


class UppercaseUHornAcuteGlyph(ComposedGlyph):
    name = "uppercase_uhornacute"
    unicode = "0x1EE8"
    base_glyph_class = UppercaseUHornGlyph
    accent_class = Acute
    accent_y = _uc_accent


class UppercaseUHornGraveGlyph(ComposedGlyph):
    name = "uppercase_uhorngrave"
    unicode = "0x1EEA"
    base_glyph_class = UppercaseUHornGlyph
    accent_class = Grave
    accent_y = _uc_accent


class UppercaseUHornHookAboveGlyph(ComposedGlyph):
    name = "uppercase_uhornhookabove"
    unicode = "0x1EEC"
    base_glyph_class = UppercaseUHornGlyph
    accent_class = HookAbove
    accent_y = _uc_accent


class UppercaseUHornTildeGlyph(ComposedGlyph):
    name = "uppercase_uhorntilde"
    unicode = "0x1EEE"
    base_glyph_class = UppercaseUHornGlyph
    accent_class = Tilde
    accent_y = _uc_accent


class UppercaseUHornDotBelowGlyph(ComposedGlyph):
    name = "uppercase_uhorndotbelow"
    unicode = "0x1EF0"
    base_glyph_class = UppercaseUHornGlyph
    accent_class = DotBelow
    accent_y = 0
