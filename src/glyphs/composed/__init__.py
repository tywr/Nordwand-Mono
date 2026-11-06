import inspect
from abc import ABC
from glyphs import Glyph


def _italic_base(base_class):
    """Return the italic-default sibling of `base_class`, or `base_class` itself.

    Scans all Glyph subclasses for one sharing the same Unicode with
    `default_italic=True`. Required so accented glyphs pick the italic-shape
    base when the italic font is being built.
    """
    if not base_class.unicode:
        return base_class
    code = int(base_class.unicode, 16)

    def walk(cls):
        for sub in cls.__subclasses__():
            if not inspect.isabstract(sub):
                yield sub
            yield from walk(sub)

    for sub in walk(Glyph):
        if (
            sub is not base_class
            and getattr(sub, "default_italic", False)
            and sub.unicode
            and int(sub.unicode, 16) == code
        ):
            return sub
    return base_class


class ComposedGlyph(Glyph, ABC):
    """A glyph composed of a base glyph and an accent mark.

    Subclasses declare base_glyph_class, accent_class, and positioning.
    The accent is drawn centered on the base glyph's body bounds at accent_y.
    """

    base_glyph_class = None
    accent_class = None
    accent_y = None  # vertical position for the accent anchor
    accent_x_offset = 0  # horizontal adjustment if needed
    keep_dot = False  # Draw the full base (e.g. the dot of ị) instead of draw_base
    accent_attrs = {}  # Overrides attributes of the accent, e.g. second_dy

    def _resolve_base_class(self, dc):
        if getattr(dc, "italic", False):
            return _italic_base(self.base_glyph_class)
        return self.base_glyph_class

    @property
    def offset(self):
        return self.base_glyph_class.offset

    def accent_x(self, dc, base, b):
        """Horizontal anchor of the accent; centered on the body by default."""
        return b.xmid + base.accent_x_offset

    def draw(self, pen, dc):
        base_class = self._resolve_base_class(dc)
        base = base_class()
        if self.keep_dot or not hasattr(base, "draw_base"):
            base.draw(pen, dc)
        else:
            base.draw_base(pen, dc)

        b = dc.body_bounds(offset=base.offset)
        accent_y = self.accent_y if self.accent_y is not None else dc.accent
        accent = self.accent_class()
        for attr, value in self.accent_attrs.items():
            setattr(accent, attr, value)
        accent.draw_at(pen, dc, x=self.accent_x(dc, base, b), y=accent_y)
