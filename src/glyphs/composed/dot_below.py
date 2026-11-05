"""Composed glyphs with the dot below."""

import pathops

from draw.dot import dot_size
from draw.rect import draw_rect
from glyphs.composed import ComposedGlyph
from glyphs.lowercase.a import LowercaseAGlyph
from glyphs.accents.dot_below import DotBelow
from glyphs.lowercase.dotted.i import LowercaseIGlyph
from glyphs.lowercase.round.e import LowercaseEGlyph
from glyphs.lowercase.round.o import LowercaseOGlyph
from glyphs.lowercase.square.u import LowercaseUGlyph
from glyphs.lowercase.y import LowercaseYGlyph
from glyphs.uppercase.e import UppercaseEGlyph
from glyphs.uppercase.a import UppercaseAGlyph
from glyphs.uppercase.i import UppercaseIGlyph
from glyphs.uppercase.o import UppercaseOGlyph
from glyphs.uppercase.u import UppercaseUGlyph
from glyphs.uppercase.y import UppercaseYGlyph
from glyphs.lowercase.single_story.b import LowercaseBGlyph
from glyphs.lowercase.single_story.d import LowercaseDGlyph
from glyphs.lowercase.square.h import LowercaseHGlyph
from glyphs.lowercase.square.n import LowercaseNGlyph
from glyphs.lowercase.s import LowercaseSGlyph
from glyphs.lowercase.z import LowercaseZGlyph
from glyphs.uppercase.b import UppercaseBGlyph
from glyphs.uppercase.d import UppercaseDGlyph
from glyphs.uppercase.h import UppercaseHGlyph
from glyphs.uppercase.n import UppercaseNGlyph
from glyphs.uppercase.s import UppercaseSGlyph
from glyphs.uppercase.z import UppercaseZGlyph


class LowercaseADotBelowGlyph(ComposedGlyph):
    name = "lowercase_adotbelow"
    unicode = "0x1EA1"
    base_glyph_class = LowercaseAGlyph
    accent_class = DotBelow
    accent_y = 0


class LowercaseEDotBelowGlyph(ComposedGlyph):
    name = "lowercase_edotbelow"
    unicode = "0x1EB9"
    base_glyph_class = LowercaseEGlyph
    accent_class = DotBelow
    accent_y = 0


class LowercaseIDotBelowGlyph(ComposedGlyph):
    name = "lowercase_idotbelow"
    unicode = "0x1ECB"
    base_glyph_class = LowercaseIGlyph
    accent_class = DotBelow
    accent_y = 0
    keep_dot = True  # Vietnamese keeps the dot of the i


class LowercaseODotBelowGlyph(ComposedGlyph):
    name = "lowercase_odotbelow"
    unicode = "0x1ECD"
    base_glyph_class = LowercaseOGlyph
    accent_class = DotBelow
    accent_y = 0


class LowercaseUDotBelowGlyph(ComposedGlyph):
    name = "lowercase_udotbelow"
    unicode = "0x1EE5"
    base_glyph_class = LowercaseUGlyph
    accent_class = DotBelow
    accent_y = 0


class LowercaseYDotBelowGlyph(ComposedGlyph):
    """The descender fills the space below y: the dot sits right of the
    upright tail, and inside the italic hook, between it and the bowl."""

    name = "lowercase_ydotbelow"
    unicode = "0x1EF5"
    base_glyph_class = LowercaseYGlyph
    accent_class = DotBelow
    accent_y = 0
    gap = 0.5  # Space between the descender and the dot, relative to stroke_x

    def accent_x(self, dc, base, b):
        # Rightmost point of the descender, within the height of the dot
        dot = self.accent_class()
        w, h = dot_size(dc, dot.dot_ratio)
        top = -dot.gap * dc.x_height
        path = pathops.Path()
        base.draw(pathops.PathPen(path), dc)
        band = pathops.Path()
        draw_rect(pathops.PathPen(band), -1000, top - h, 2000, top)
        _, _, x2, _ = pathops.op(path, band, pathops.PathOp.INTERSECTION).bounds
        return x2 + self.gap * dc.stroke_x + w / 2

    def draw(self, pen, dc):
        base_class = self._resolve_base_class(dc)
        if base_class is self.base_glyph_class:
            super().draw(pen, dc)
            return

        # Italic y, whose hook runs under the whole bowl: center the dot
        # between the baseline and the inside of the hook
        base = base_class()
        base.draw(pen, dc)
        dot = self.accent_class()
        _, h = dot_size(dc, dot.dot_ratio)
        center = (dc.descent + dc.stroke_y) / 2
        b = dc.body_bounds(offset=base.offset)
        dot.draw_at(pen, dc, b.xmid, center + dot.gap * dc.x_height + h / 2)


class UppercaseEDotBelowGlyph(ComposedGlyph):
    name = "uppercase_edotbelow"
    unicode = "0x1EB8"
    base_glyph_class = UppercaseEGlyph
    accent_class = DotBelow
    accent_y = 0


class UppercaseADotBelowGlyph(ComposedGlyph):
    name = "uppercase_adotbelow"
    unicode = "0x1EA0"
    base_glyph_class = UppercaseAGlyph
    accent_class = DotBelow
    accent_y = 0


class UppercaseIDotBelowGlyph(ComposedGlyph):
    name = "uppercase_idotbelow"
    unicode = "0x1ECA"
    base_glyph_class = UppercaseIGlyph
    accent_class = DotBelow
    accent_y = 0


class UppercaseODotBelowGlyph(ComposedGlyph):
    name = "uppercase_odotbelow"
    unicode = "0x1ECC"
    base_glyph_class = UppercaseOGlyph
    accent_class = DotBelow
    accent_y = 0


class UppercaseUDotBelowGlyph(ComposedGlyph):
    name = "uppercase_udotbelow"
    unicode = "0x1EE4"
    base_glyph_class = UppercaseUGlyph
    accent_class = DotBelow
    accent_y = 0


class UppercaseYDotBelowGlyph(ComposedGlyph):
    name = "uppercase_ydotbelow"
    unicode = "0x1EF4"
    base_glyph_class = UppercaseYGlyph
    accent_class = DotBelow
    accent_y = 0


class LowercaseBDotBelowGlyph(ComposedGlyph):
    name = "lowercase_bdotbelow"
    unicode = "0x1E05"
    base_glyph_class = LowercaseBGlyph
    accent_class = DotBelow
    accent_y = 0


class LowercaseDDotBelowGlyph(ComposedGlyph):
    name = "lowercase_ddotbelow"
    unicode = "0x1E0D"
    base_glyph_class = LowercaseDGlyph
    accent_class = DotBelow
    accent_y = 0


class LowercaseHDotBelowGlyph(ComposedGlyph):
    name = "lowercase_hdotbelow"
    unicode = "0x1E25"
    base_glyph_class = LowercaseHGlyph
    accent_class = DotBelow
    accent_y = 0


class LowercaseNDotBelowGlyph(ComposedGlyph):
    name = "lowercase_ndotbelow"
    unicode = "0x1E47"
    base_glyph_class = LowercaseNGlyph
    accent_class = DotBelow
    accent_y = 0


class LowercaseSDotBelowGlyph(ComposedGlyph):
    name = "lowercase_sdotbelow"
    unicode = "0x1E63"
    base_glyph_class = LowercaseSGlyph
    accent_class = DotBelow
    accent_y = 0


class LowercaseZDotBelowGlyph(ComposedGlyph):
    name = "lowercase_zdotbelow"
    unicode = "0x1E93"
    base_glyph_class = LowercaseZGlyph
    accent_class = DotBelow
    accent_y = 0


class UppercaseBDotBelowGlyph(ComposedGlyph):
    name = "uppercase_bdotbelow"
    unicode = "0x1E04"
    base_glyph_class = UppercaseBGlyph
    accent_class = DotBelow
    accent_y = 0


class UppercaseDDotBelowGlyph(ComposedGlyph):
    name = "uppercase_ddotbelow"
    unicode = "0x1E0C"
    base_glyph_class = UppercaseDGlyph
    accent_class = DotBelow
    accent_y = 0


class UppercaseHDotBelowGlyph(ComposedGlyph):
    name = "uppercase_hdotbelow"
    unicode = "0x1E24"
    base_glyph_class = UppercaseHGlyph
    accent_class = DotBelow
    accent_y = 0


class UppercaseNDotBelowGlyph(ComposedGlyph):
    name = "uppercase_ndotbelow"
    unicode = "0x1E46"
    base_glyph_class = UppercaseNGlyph
    accent_class = DotBelow
    accent_y = 0


class UppercaseSDotBelowGlyph(ComposedGlyph):
    name = "uppercase_sdotbelow"
    unicode = "0x1E62"
    base_glyph_class = UppercaseSGlyph
    accent_class = DotBelow
    accent_y = 0


class UppercaseZDotBelowGlyph(ComposedGlyph):
    name = "uppercase_zdotbelow"
    unicode = "0x1E92"
    base_glyph_class = UppercaseZGlyph
    accent_class = DotBelow
    accent_y = 0
