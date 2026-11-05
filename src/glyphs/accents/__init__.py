from abc import ABC, abstractmethod
from glyphs import Glyph


class Accent(Glyph, ABC):
    """Base class for accent/diacritical marks.

    Accents are full glyphs (can be visualized standalone) and also
    provide draw_at(pen, dc, x, y) for positioning by ComposedGlyph.
    """

    offset = 0

    @abstractmethod
    def draw_at(self, pen, dc, x, y):
        """Draw the accent centered horizontally at x, vertically at y."""
        ...

    def draw(self, pen, dc):
        """Draw the accent at the default position (centered in the cell)."""
        b = dc.body_bounds(offset=self.offset)
        self.draw_at(pen, dc, x=b.xmid, y=dc.accent)


class StackedAccent(Accent):
    """Two accents merged into one mark (Vietnamese ấ, ặ): `first` drawn at
    the anchor, `second` shifted from it by (second_dx, second_dy), relative
    to the body width and the x-height. `second_y`, when set, pins the second
    accent at an absolute height instead, e.g. 0 for a dot below.
    `second_attrs` overrides attributes of the second accent, e.g. to make it
    smaller."""

    unicode = None
    generated_only = True  # Only used inside composed glyphs
    first = None
    second = None
    second_dx = 0
    second_dy = 0
    second_y = None
    second_attrs = {}

    def draw_at(self, pen, dc, x, y):
        self.first().draw_at(pen, dc, x, y)
        y2 = self.second_y
        if y2 is None:
            y2 = y + self.second_dy * dc.x_height
        second = self.second()
        for attr, value in self.second_attrs.items():
            setattr(second, attr, value)
        second.draw_at(pen, dc, x + self.second_dx * dc.width, y2)
