"""Composed glyphs with the ogonek."""

from glyphs.composed import ComposedGlyph
from glyphs.lowercase.a import LowercaseAGlyph
from glyphs.lowercase.round.e import LowercaseEGlyph
from glyphs.lowercase.square.u import LowercaseUGlyph
from glyphs.lowercase.dotted.i import LowercaseIGlyph
from glyphs.uppercase.a import UppercaseAGlyph
from glyphs.uppercase.e import UppercaseEGlyph
from glyphs.uppercase.i import UppercaseIGlyph
from glyphs.uppercase.u import UppercaseUGlyph
from glyphs.accents.ogonek import Ogonek
import pathops
from draw.rect import draw_rect


class OgonekComposedGlyph(ComposedGlyph):
    """Hangs the ogonek from the base glyph's measured outline, so it follows
    the real shape of each base (including italic variants)."""

    accent_class = Ogonek
    accent_y = 0
    # Hang from the rightmost stem, the hook's right edge flush with the
    # stem's. Otherwise the hook is placed by `ogonek_x`.
    from_stem = False
    # Hook apex between the base's left (0) and right (1) edges.
    ogonek_x = 0.0
    ogonek_xmid = False  # Center the hook in the cell, ignoring the above
    ogonek_width = Ogonek.stem_ratio  # Start width, relative to stroke_x
    ogonek_start = 0.0
    ogonek_x_offset = 0  # Manual horizontal nudge of the hook, in font units
    stem_probe = 0.25  # Height where the stem is measured, relative to x-height
    keep_dot = False  # Draw the full base (e.g. the dot of į) instead of draw_base
    cut_ogonek_top = True  # Cut the pivoted hook flat above sy / 2
    cut_ogonek_slant = False  # Cut the hook right of a 45° line through its apex
    vertical_overshoot = False  # Drop the hook by the base's vertical overshoot

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
        width = self.ogonek_width * dc.stroke_x
        if self.ogonek_xmid:
            x = dc.window_width / 2 + dc.stroke_x / 2
        elif self.from_stem:
            _, right = self._rightmost_stem(path, dc)
            x = right - width / 2
        else:
            x1, _, x2, _ = path.bounds
            x = x1 + self.ogonek_x * (x2 - x1)
        y = self.accent_y
        if self.vertical_overshoot:
            uppercase = self.name.startswith("uppercase")
            y -= dc.v_overshoot_cap if uppercase else dc.v_overshoot
        Ogonek().draw_at(
            pen,
            dc,
            x=x + self.ogonek_x_offset,
            y=y,
            width=width,
            start=start,
            cut_top=self.cut_ogonek_top,
            cut_slant=self.cut_ogonek_slant,
        )


class LowercaseAOgonekGlyph(OgonekComposedGlyph):
    name = "lowercase_aogonek"
    unicode = "0x105"
    base_glyph_class = LowercaseAGlyph
    cut_ogonek_top = False
    ogonek_x = 1


class LowercaseEOgonekGlyph(OgonekComposedGlyph):
    name = "lowercase_eogonek"
    unicode = "0x119"
    base_glyph_class = LowercaseEGlyph
    ogonek_x = 0.72


class UppercaseAOgonekGlyph(OgonekComposedGlyph):
    name = "uppercase_aogonek"
    unicode = "0x104"
    base_glyph_class = UppercaseAGlyph
    ogonek_x = 1
    cut_ogonek_top = False
    cut_ogonek_slant = True


class UppercaseEOgonekGlyph(OgonekComposedGlyph):
    name = "uppercase_eogonek"
    unicode = "0x118"
    base_glyph_class = UppercaseEGlyph
    ogonek_x = 1


class LowercaseIOgonekGlyph(OgonekComposedGlyph):
    name = "lowercase_iogonek"
    unicode = "0x12F"
    base_glyph_class = LowercaseIGlyph
    keep_dot = True
    ogonek_xmid = True


class UppercaseIOgonekGlyph(OgonekComposedGlyph):
    name = "uppercase_iogonek"
    unicode = "0x12E"
    base_glyph_class = UppercaseIGlyph
    ogonek_xmid = True


class LowercaseUOgonekGlyph(OgonekComposedGlyph):
    name = "lowercase_uogonek"
    unicode = "0x173"
    base_glyph_class = LowercaseUGlyph
    ogonek_x = 1
    cut_ogonek_top = False


class UppercaseUOgonekGlyph(OgonekComposedGlyph):
    name = "uppercase_uogonek"
    unicode = "0x172"
    base_glyph_class = UppercaseUGlyph
    ogonek_x = 0.75
    accent_y = 0
