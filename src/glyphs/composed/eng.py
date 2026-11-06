"""Composed glyphs with the eng."""

from glyphs.composed import ComposedGlyph
from glyphs.lowercase.square.n import LowercaseNGlyph
from glyphs.uppercase.n import UppercaseNGlyph
from draw.square_corner import draw_square_corner


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
