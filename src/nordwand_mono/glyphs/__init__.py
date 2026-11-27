from abc import ABC, abstractmethod


class Glyph(ABC):
    accent_x_offset: int = 0

    @property
    @abstractmethod
    def name(self) -> str: ...

    @property
    @abstractmethod
    def unicode(self) -> str: ...

    @property
    @abstractmethod
    def offset(self) -> int: ...

    number_characters: int = 1
    font_feature: dict = None
    alternative_character_comment: str = None
    default_italic: bool = False
    italic_only: bool = False
    # Alternate left out of the italic, which keeps the default design
    regular_only: bool = False
    # Name of the alternate this one replaces when its feature is on, instead
    # of the default glyph: it then applies on top of that alternate's feature
    alternate_of: str = None
    italic_skew: bool = True
    # Strokes of the glyph relative to the weight's, see `get_strokes`
    stroke_x_ratio: float = 1
    stroke_y_ratio: float = 1
    # Share of the stroke growth past the regular weight that is kept
    stroke_x_dampening: float = 1
    stroke_y_dampening: float = 1
    # Extra cut ratio
    extra_cut_ratio = 0.66
    thinning = 1

    @abstractmethod
    def draw(self, pen, dc) -> None: ...

    def get_strokes(self, dc):
        """Strokes (sx, sy) of the glyph: the weight's, keeping only
        `dampening` of their growth past the regular weight, scaled by the
        ratios."""
        from nordwand_mono.config import FontConfig

        def damp(stroke, default, dampening):
            return max(0, dampening * (stroke - default)) + min(default, stroke)

        sx = self.stroke_x_ratio * damp(
            dc.stroke_x, dc.default_stroke, self.stroke_x_dampening
        )
        sy = self.stroke_y_ratio * damp(
            dc.stroke_y, FontConfig.stroke_y, self.stroke_y_dampening
        )
        return sx, sy

    def get_thinned_stroke(self, dc, coefficient=None, stroke=None):
        """Get the thinned stroke to apply on cut endings (eg. c, a, s etc.)"""

        def damp(stroke, default, dampening):
            return max(0, dampening * (stroke - default)) + min(default, stroke)

        if not stroke:
            s, _ = self.get_strokes(dc)
        else:
            s = stroke
        if coefficient is None:
            coefficient = self.thinning
        return damp(s, dc.default_stroke, coefficient)

    def extra_cut(self, dc) -> int:
        return min(
            self.extra_cut_ratio * max(0, dc.stroke_x - dc.default_stroke),
            dc.stroke_x / 4,
        )

    def diag_stroke_dampening(self, ratio, stroke, coef=0.25):
        from math import exp

        ds = max(stroke - 85, 0) / 85
        # If ds > 0, we add some dampening, other we let as is
        if ds <= 0:
            return ratio * stroke

        delta = exp(-ds * coef)
        sx = delta * stroke * ratio
        return sx


class InfiniteLigatureGlyph(Glyph):
    """Glyph whose horizontal bars can join across any number of cells."""

    @abstractmethod
    def horizontal_bar_heights(self, dc) -> tuple[float, ...]: ...

    @abstractmethod
    def horizontal_bar_stroke(self, dc) -> float: ...

    @abstractmethod
    def horizontal_bar_bounds(self, dc) -> tuple[float, float]: ...

    def draw_non_horizontal(self, pen, dc) -> None:
        pass

    def draw(self, pen, dc) -> None:
        self._draw_joined(pen, dc, join_left=False, join_right=False)

    def _draw_joined(self, pen, dc, join_left, join_right) -> None:
        from nordwand_mono.draw.rect import draw_rect

        stroke = self.horizontal_bar_stroke(dc)
        dent = stroke * dc.ligature_dent_stroke
        junction_width = stroke * dc.ligature_junction_width
        x1, x2 = self.horizontal_bar_bounds(dc)
        if join_left:
            x1 = junction_width / 2
        if join_right:
            x2 = dc.window_width - junction_width / 2

        self.draw_non_horizontal(pen, dc)
        for y in self.horizontal_bar_heights(dc):
            draw_rect(pen, x1, y - stroke / 2, x2, y + stroke / 2)
            if join_right:
                draw_rect(
                    pen,
                    dc.window_width - junction_width / 2,
                    y - dent / 2,
                    dc.window_width + junction_width / 2,
                    y + dent / 2,
                )

    def ligature_forms(self):
        return [
            InfiniteLigatureForm(self, "start", join_left=False, join_right=True),
            InfiniteLigatureForm(self, "middle", join_left=True, join_right=True),
            InfiniteLigatureForm(self, "end", join_left=True, join_right=False),
        ]


class InfiniteLigatureForm(Glyph):
    """One contextual joining form of an :class:`InfiniteLigatureGlyph`."""

    generated_only = True
    name = None
    unicode = None
    offset = 0
    number_characters = 1
    font_feature = None
    default_italic = False
    italic_only = False
    feature_tags = ("dlig",)

    def __init__(self, source, position, join_left, join_right):
        self.source = source
        self.source_name = source.name
        self.position = position
        self.join_left = join_left
        self.join_right = join_right
        self.name = f"{source.name}_liga_{position}"

    def draw(self, pen, dc):
        self.source._draw_joined(
            pen,
            dc,
            join_left=self.join_left,
            join_right=self.join_right,
        )


class LigatureGlyph(Glyph):
    """Base class for ligature glyphs.

    Subclasses must define `components` — a list of glyph names that
    this ligature replaces (e.g. ["low_line", "low_line"] for "__").
    Set `feature_tags` to one or more OpenType tags; enabling any listed
    feature activates the ligature.
    """

    unicode = None
    offset = 0
    feature_tags = ("liga",)
    # Whether the ligature can join a run of its first component on its left
    # (e.g. `--->` with dlig): it then gets a JoinedLigatureForm, drawn with
    # draw(pen, dc, join_left=True)
    joinable = False

    @property
    @abstractmethod
    def components(self) -> list[str]: ...

    def ligature_forms(self):
        return [JoinedLigatureForm(self)] if self.joinable else []


class JoinedLigatureForm(Glyph):
    """Form of a joinable :class:`LigatureGlyph` that follows a run of its
    first component, which is an :class:`InfiniteLigatureGlyph`."""

    generated_only = True
    name = None
    unicode = None
    offset = 0
    font_feature = None
    default_italic = False
    italic_only = False
    feature_tags = ("dlig",)

    def __init__(self, source):
        self.source = source
        self.source_name = source.name
        self.joins = source.components[0]
        self.name = f"{source.name}_joined"
        self.number_characters = source.number_characters

    def draw(self, pen, dc):
        self.source.draw(pen, dc, join_left=True)


class ContextualLigatureGlyph(LigatureGlyph):
    """Ligature that only fires when not adjacent to `forbidden_neighbors`.

    Useful for capped-length ligatures: e.g. `==` and `===` ligate, but
    `====` and longer stay unligated. Set `forbidden_neighbors` to the
    glyph names whose presence on either side disqualifies the match
    (typically the ligature's own component glyph).
    """

    forbidden_neighbors: list[str] = []
    feature_tags = ("calt",)
