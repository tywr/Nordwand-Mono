"""Composed glyphs with the horn."""

import pathops

from glyphs.composed import ComposedGlyph
from glyphs.lowercase.round.o import LowercaseOGlyph
from glyphs.lowercase.square.u import LowercaseUGlyph
from glyphs.uppercase.o import UppercaseOGlyph
from glyphs.uppercase.u import UppercaseUGlyph
from glyphs.accents.horn import Horn


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
