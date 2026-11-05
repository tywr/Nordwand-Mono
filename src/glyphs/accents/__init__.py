from abc import ABC, abstractmethod

from glyphs import Glyph


class Accent(Glyph, ABC):
    """Base class for accent/diacritical marks.

    Accents are full glyphs (can be visualized standalone) and also
    provide draw_at(pen, dc, x, y) for positioning by ComposedGlyph.
    """

    offset = 0
    # Relative to the x-height. Shared by the circumflex, caron, breve and
    # tilde, so that they read at the same scale
    height = 0.3

    @abstractmethod
    def draw_at(self, pen, dc, x, y):
        """Draw the accent centered horizontally at x, vertically at y."""
        ...

    def draw(self, pen, dc):
        """Draw the accent at the default position (centered in the cell)."""
        b = dc.body_bounds(offset=self.offset)
        self.draw_at(pen, dc, x=b.xmid, y=dc.accent)


class StackedAccent(Accent):
    """Two accents merged into one mark (Vietnamese ấ, ặ): `first` shifted
    from the anchor by (first_dx, first_dy), and `second` by (second_dx,
    second_dy), both relative to the body width and the x-height. `second_y`,
    when set, pins the second accent at an absolute height instead, e.g. 0
    for a dot below. `first_width`, `first_height`, `second_width` and
    `second_height`, when set, override the sizes of the accents,
    `first_stroke_ratio` and `second_stroke_ratio` scale their strokes, and
    `second_attrs` overrides any other attribute of the second one."""

    unicode = None
    generated_only = True  # Only used inside composed glyphs
    first = None
    first_dx = 0
    first_dy = 0
    first_width = None  # Relative to the body width
    first_height = None  # Relative to the x-height
    first_stroke_ratio = 0.8
    second_stroke_ratio = 0.7
    second = None
    second_dx = 0
    second_dy = 0
    second_y = None
    second_width = None  # Relative to the body width
    second_height = None  # Relative to the x-height
    second_attrs = {}

    def draw_at(self, pen, dc, x, y):
        first = self.first()
        if self.first_width is not None:
            first.width = self.first_width
        if self.first_height is not None:
            first.height = self.first_height
        _scale_stroke(first, self.first_stroke_ratio)
        first.draw_at(
            pen, dc, x + self.first_dx * dc.width, y + self.first_dy * dc.x_height
        )

        second = self.second()
        for attr, value in self.second_attrs.items():
            setattr(second, attr, value)
        if self.second_width is not None:
            second.width = self.second_width
        if self.second_height is not None:
            second.height = self.second_height
        _scale_stroke(second, self.second_stroke_ratio)
        y2 = self.second_y
        if y2 is None:
            y2 = y + self.second_dy * dc.x_height
        second.draw_at(pen, dc, x + self.second_dx * dc.width, y2)


def _scale_stroke(accent, ratio):
    """Scale the strokes of `accent`, or the size of a dot, which has none."""
    if hasattr(accent, "stroke_ratio"):
        accent.stroke_ratio *= ratio
    elif hasattr(accent, "dot_ratio"):
        accent.dot_ratio *= ratio
