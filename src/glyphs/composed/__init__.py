import copy
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


def _alternates(base_class):
    """Return the cvXX/ssXX alternates of the Unicode of `base_class`."""
    if not base_class.unicode:
        return []
    code = int(base_class.unicode, 16)

    def walk(cls):
        for sub in cls.__subclasses__():
            if not inspect.isabstract(sub):
                yield sub
            yield from walk(sub)

    return [
        sub
        for sub in walk(Glyph)
        if sub is not base_class
        and sub.font_feature
        and sub.unicode
        and int(sub.unicode, 16) == code
    ]


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
        # An alternate base is drawn as is, it already went through the style
        # selection of its own Unicode
        if getattr(dc, "italic", False) and not self.base_glyph_class.font_feature:
            return _italic_base(self.base_glyph_class)
        return self.base_glyph_class

    def _alternate_name(self, alternate_name):
        base_name = self.base_glyph_class.name
        if alternate_name.startswith(base_name):
            return self.name + alternate_name[len(base_name) :]
        return f"{self.name}.{alternate_name}"

    def alternate_forms(self):
        """Copies of this glyph drawn on each cvXX/ssXX alternate of its base.

        They get the features and style flags of their base alternate, so
        the alternate also applies to the accented letters.
        """
        if not self.base_glyph_class:
            return []
        forms = []
        base_class = self.base_glyph_class
        has_italic_default = _italic_base(base_class) is not base_class
        for alternate in _alternates(base_class):
            form = copy.copy(self)
            form.name = self._alternate_name(alternate.name)
            form.base_glyph_class = alternate
            form.font_feature = alternate.font_feature
            form.italic_only = alternate.italic_only
            # Like the base: left out of the italic when the base letter has
            # an italic default, unless the alternate is italic only
            form.regular_only = alternate.regular_only or (
                has_italic_default and not alternate.italic_only
            )
            if alternate.alternate_of:
                form.alternate_of = self._alternate_name(alternate.alternate_of)
            forms.append(form)
        return forms

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
