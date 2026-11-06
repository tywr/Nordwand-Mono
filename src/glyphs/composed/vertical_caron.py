"""Composed glyphs with the vertical caron (ď ľ Ľ ť)."""

from glyphs.composed import ComposedGlyph
from glyphs.lowercase.l import LowercaseLGlyph
from glyphs.lowercase.t import LowercaseTGlyph
from glyphs.uppercase.l import UppercaseLGlyph
from glyphs.lowercase.single_story.d import LowercaseDGlyph
from glyphs.accents.caron_vertical import CaronVertical


class LowercaseDCaronGlyph(ComposedGlyph):
    """d with the vertical caron beside its ascender.

    The d is narrowed if needed and shifted left so that it and the mark
    fit in the cell together, centered as a pair.
    """

    name = "lowercase_dcaron"
    unicode = "0x10F"
    base_glyph_class = LowercaseDGlyph
    accent_class = CaronVertical
    margin = 0
    extra_gap = 0.08

    def draw(self, pen, dc):
        base = self._resolve_base_class(dc)()
        mark = self.accent_class()
        mark_width = mark.gap_width(dc) + mark.top_width(dc)
        gap = dc.window_width * self.extra_gap
        room = dc.window_width - 2 * self.margin - mark_width - gap
        base.width_ratio = min(base.width_ratio, (room - dc.stroke_x) / dc.width)
        d_width = dc.width * base.width_ratio + dc.stroke_x
        x1 = (dc.window_width - d_width - mark_width) / 2
        base.offset = x1 - (dc.window_width - d_width) / 2 - gap / 2
        base.draw(pen, dc)
        mark.draw_at(
            pen, dc, x=x1 + d_width + mark.gap_width(dc) + gap / 2, y=dc.ascent
        )


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


class LowercaseTCaronGlyph(ComposedGlyph):
    """t with the vertical caron beside the top of its stem."""

    name = "lowercase_tcaron"
    unicode = "0x165"
    base_glyph_class = LowercaseTGlyph
    accent_class = CaronVertical
    x_offset = 0.84
    height = 0.4
    up_ratio = 0.55

    def draw(self, pen, dc):
        base = self._resolve_base_class(dc)()
        base.draw(pen, dc)
        b = dc.body_bounds(
            offset=base.offset, height="x_height", width_ratio=base.width_ratio
        )
        top = (1 + self.up_ratio) * dc.x_height
        accent = self.accent_class()
        accent.height = self.height
        accent.draw_at(pen, dc, x=b.x1 + b.width * self.x_offset, y=top)


class LowercaseLCaronGlyph(LowercaseTCaronGlyph):
    """l with the vertical caron beside the top of its stem."""

    name = "lowercase_lcaron"
    unicode = "0x13E"
    base_glyph_class = LowercaseLGlyph
    accent_class = CaronVertical
    x_offset = 0.8
    up_ratio = 0.4
    height = 0.4
